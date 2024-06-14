from django.urls import path, include
from . import views
urlpatterns=[
    path('list',views.car_list_view,name='list'),
    path('<int:pk>',views.car_detail_view,name='car_detail'),
    path('showtoom',views.)

]