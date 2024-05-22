from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productsPage, name="products-page"),
    path('my-products/', views.userProductsPage, name="user-products-page"),
    path('add-product/', views.addProduct, name="add-product"),
    path('update-product/<str:pk>', views.updateProduct, name="update-product"),
    path('delete-product/<str:pk>', views.deleteProduct, name="delete-product"),
    path('product/<str:pk>', views.singleProduct, name="single-product"),
]