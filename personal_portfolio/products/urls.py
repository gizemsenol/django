from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home_page, name="home_page"),
    path("products/", views.product_index, name="product_index"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/<int:pk>/payment",views.product_payment, name="product_payment"),

]