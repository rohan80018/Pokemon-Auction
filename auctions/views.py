from tkinter import Y
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Category, Comment, Bid


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def index(request):
    return render(request, "auctions/index.html", {
        "listing": Listing.objects.exclude(is_active=False).all()
    })

def closedListings(request):
    return render(request, "auctions/closed_listing.html", {
        "listing": Listing.objects.exclude(is_active=True).all()
    })


def new_listing(request):
    
    if request.method == "POST":
        value = request.POST
        # bid_save=Bid(bid=int(value["price"]), user=request.user)
        # bid_save.save()
        data = Listing(
            title = value["title"],
            description = value["des"],
            price = value["price"],
            # category= Category.objects.get(pk = int(value["category"])),
            category = Category.objects.get(category_name=(value["category"])),
            imageUrl = value["image"],
            owner = request.user
        )
        data.save()
        return HttpResponseRedirect(reverse("index"))
        
    categories = Category.objects.all()
    print(categories)
    return render(request, "auctions/new_listing.html", {
        "categories": categories
    })

def addBid(request, id):
    if request.method == "POST":
        
        item = Listing.objects.get(id=id)
        
        data = Bid(
            bid = request.POST["bid"],
            item = item,
            user = request.user
            )
        data.save()
        return HttpResponseRedirect(reverse('item', args=(id,)))

def add_category(request, pk):
    
    if request.method == "POST":
        value = request.POST
        data = Category(
            category_name = value["cat"],
            imgUrl = value["image"]
        )
        data.save()
        if pk == "list":
            return HttpResponseRedirect(reverse("new_listing"))
        else :
            return HttpResponseRedirect(reverse("categories"))

    return render(request, 'auctions/new_cat.html', {"pk":pk})


def category(request):
    
    return render(request, "auctions/category.html", {
        "category": Category.objects.all()
    })
 

def view_cats(request, pk):
    print(pk)
    id = Category.objects.only('id').get(category_name=pk).id
    print(id)
    # type_list = Category.objects.get(category_name=pk)
    # print(type_list)
    
    # print(Listing.objects.filter(category=int(Category.objects.get(pk.category))))
    d=Listing.objects.filter(category=id)
    print(d)
    return render(request, 'auctions/category.html', {
        "list_cat": pk,
        "lists" : d
    })

def item(request, id):
    item = Listing.objects.get(id=id)
    in_watchlist = request.user in item.watchlist.all()
    comment = Comment.objects.filter(item=item)
    if Bid.objects.filter(item=item).last() == None:
        bid_user = None
        bid = 0
    else:
        bid= Bid.objects.only('bid').filter(item=item).last().bid
        bid_user = Bid.objects.only('user').filter(item=item).last().user
    print(bid)
    price = Listing.objects.only('price').get(id=id).price
    if price > bid:
        mini = price + 1
    else:
        mini = bid + 1

    print(mini)
    
    
    return render(request, "auctions/item.html", {
        "pokemon" : item,
        "in_watchlist": in_watchlist,
        "comments": comment,
        "bid": bid,
        "mini": int(mini),
        "bid_user": bid_user
    })


def remove_watchlist(request, id):
    current_user = request.user
    listingdata = Listing.objects.get(pk=id)
    listingdata.watchlist.remove(current_user)
    return HttpResponseRedirect(reverse('item', args=(id,)))


def add_watchlist(request, id):
    current_user = request.user
    listingdata = Listing.objects.get(pk=id)
    listingdata.watchlist.add(current_user)
    return HttpResponseRedirect(reverse('item', args=(id,)))

def showWatchlist(request):
    print(Category.objects.only('id').get(category_name='Fire').id,'Hello')
    watchlist_item = request.user.watch_list.all()
    
    return render(request, 'auctions/watchlist.html', {"watchlist": watchlist_item})


def userComment(request, id):
    getComment= request.POST["comment"]
    item = Listing.objects.get(id=id)
    comment= Comment(author=request.user, item=item, message=getComment)
    comment.save()
    return HttpResponseRedirect(reverse('item', args=(id,)))


def closeBid(request, id):
    item = Listing.objects.get(id=id)

    item.is_active = False
    item.save()
    return HttpResponseRedirect(reverse('item', args=(id,)))

# def startBid(request, id):
#     item = Listing.objects.get(id=id)

#     item.is_active = True
#     item.save()
#     return HttpResponseRedirect(reverse('item', args=(id,)))



    # <form action="{% url 'start' id=pokemon.id %}" method="POST">
    #                 {%csrf_token%}
    #                     <button type="submit" class="btn btn-success">Start Bid</button>
    #                 </form>
            