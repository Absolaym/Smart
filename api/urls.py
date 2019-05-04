from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('store/all', views.get_stores_all, name='allStores'),
    path('me/points',views.getAllFidelityPoints, name='getAllFidelityPoints'),
    path('me/points/<int:store_id>',views.getFidelityPoints, name='getFidelityPoints'),
    path('products/<int:storeId>', views.get_store_products, name='getStoreProducts'),
    path('me/products/add', views.add_product_to_store, name='addProductToStore'),
    path('me/products/update', views.update_product, name='updateProduct'),
    path('me/products/remove', views.remove_product_from_store, name='removeProductFromStore'),
]
