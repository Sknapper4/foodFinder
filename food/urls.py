from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('snack_list/', views.snack_list, name='snack_list'),
    path('store_list/', views.store_list, name='store_list'),
    path('snack/<int:snack_id>/', views.snack_details, name='snack_details'),
    path('store/<int:store_id>/', views.store_detail, name='store_details'),
    path('snack/create_snack/', views.create_snack, name='create_snack'),
    path('store/create_store/', views.create_store, name='create_store'),
]
