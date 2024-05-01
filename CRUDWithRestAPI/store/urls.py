from django.urls import path
from store.views import ProductDetailView, ProductList, CreateProduct, UpdateProduct, DeleteProduct

app_name = 'store'

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='get_product'),
    path('create-product/', CreateProduct.as_view(), name='create_product'),
    path('update-product/<int:product_id>/', UpdateProduct.as_view(), name='update_product'),
    path('delete/<int:product_id>', DeleteProduct.as_view(), name='delete_product'),
]