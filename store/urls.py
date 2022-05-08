from django.urls import path
from store import views


urlpatterns = [
    path('',views.home,name='home'),
    # path('clothes/',views.clothes.as_view(),name='clothes'), 
    path('clothes/',views.clothes,name='clothes'), 
    path('product_detail/<int:id>',views.product_detail,name='product_detail'), 
    # path('clothes/<slug:data>',views.clothes.as_view(),name='clothes'),
    path('clothes/<slug:data>',views.clothes,name='clothes'),
    path('mobiles/',views.mobiles,name='mobiles'),
    path('mobiles/<slug:data>',views.mobiles,name='mobiles'),
    path('vegetable/',views.vegetable,name='vegetable'), 
    path('check_out',views.check_out.as_view(),name='check_out'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin.as_view(),name='signin'),
    path('cart',views.cart,name="cart"), 
    path('signout',views.signout,name="signout"), 
] 