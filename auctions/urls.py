from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed", views.closedListings, name="closed"),
    path("new_category/<str:pk>", views.add_category, name="new_cat"),
    path("categories", views.category, name="categories"),
    path("categories/<str:pk>", views.view_cats, name='view_cat'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("listing/<int:id>", views.item, name="item"),
    path("remove_Watchlist/<int:id>", views.remove_watchlist, name='remove_watchlist'),
    path("add_Watchlist/<int:id>", views.add_watchlist, name='add_watchlist'),
    path("watchlist", views.showWatchlist, name="showWatchlist"),
    path("itemComment/<int:id>", views.userComment, name="userComment"),
    path("addBid/<int:id>", views.addBid, name="addBid"),
    path("close/<int:id>", views.closeBid, name="close"),
    # path("start/<int:id>", views.startBid, name="start"),

]
