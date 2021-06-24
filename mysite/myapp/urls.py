'''router = DefaultRouter()
router.register('', plist, basename='post')
urlpatterns=router.urls'''

from . import views
from django.urls import path
from .views import ProductList as plist, SellerList as slist, CategoryList as clist
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products-list/', plist.showAll, name='products-list'),
    path('products-detail/<int:pk>/', plist.viewProduct, name='products-detail'),
    path('products-create/', plist.createProduct, name='products-create'),
    path('products-update/<int:pk>/', plist.updateProduct, name='products-update'),
    path('products-delete/<int:pk>/', plist.deleteProduct, name='products-delete'),

    path('categories-list/', clist.showAll, name='categories-list'),
    path('categories-detail/<int:pk>/', clist.viewCategory, name='categories-detail'),
    path('categories-create/', clist.createCategory, name='categories-create'),
    path('categories-update/<int:pk>/', clist.updateCategory, name='categories-update'),
    path('categories-delete/<int:pk>/', clist.deleteCategory, name='categories-delete'),

    path('sellers-list/', slist.showAll, name='sellers-list'),
    path('sellers-detail/<int:pk>/', slist.viewSeller, name='sellers-detail'),
    path('sellers-create/', slist.createSeller, name='sellers-create'),
    path('sellers-update/<int:pk>/', slist.updateSeller, name='sellers-update'),
    path('sellers-delete/<int:pk>/', slist.deleteSeller, name='sellers-delete'),
]


