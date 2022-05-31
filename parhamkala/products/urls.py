from django.urls import path
from . import views


urlpatterns = [
    path('', views.index2, name='products'),
    path('cate/<str:ism>/', views.product_dastebandi, name="product_dastebandi"),
    path('admins/', views.index, name='products_admin'),
    path('add/', views.add, name="add_product"),
    path('add_cart/', views.add_cart, name="products_add_cart"),
    path('delete/<int:id_p>', views.delete, name="delete_product"),
    path('delete_pro', views.delete_pro, name="delete_pro"),
    path('edit/<int:id_pro>', views.edit, name="edit_product"),
    path('product/<int:id_pro>', views.edit, name="product_details"),
]