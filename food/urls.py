from django.urls import path
from django.contrib import admin
from django.urls import path, include  # new

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('snack_list/', views.snack_list, name='snack_list'),
    path('store_list/', views.store_list, name='store_list'),
    path('snack/<int:snack_id>/', views.snack_details, name='snack_details'),
    path('store/<int:store_id>/', views.store_detail, name='store_details'),
    path('snack/create_snack/', views.create_snack, name='create_snack'),
    path('snack/snack_search/', views.snack_search, name='snack_search'),
    path('store/create_store/', views.create_store, name='create_store'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('my_snacks/', views.user_snacks, name='my_snacks'),
    path('cities/', views.cities, name='cities'),
    path('store/city/<int:store_id>/', views.city_details, name='city_details'),
]
