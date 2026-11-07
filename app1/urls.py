from django.contrib import admin
from django.urls import path
# agregar las ulrs de app1
from . import views

urlpatterns = [
    #path("saludar/<str:nombre>/<int:edad>/", views.saludar),
    path("info/", views.info, name='info'),
    path("", views.home, name='home'),
    path("stores/", views.stores_view, name='stores'),
    path("products/", views.products_view, name='products'),
    path("create_store/", views.create_stores, name='create_store'),
    path("create_product/", views.create_product, name='create_product'),
    path('details/<int:id>',views.details,name='details'),
    path('contact',views.contact,name='contact'),
]