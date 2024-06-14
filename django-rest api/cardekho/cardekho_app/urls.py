from django.urls import path, include
from . import views
urlpatterns=[
    path('list',views.car_list_view,name='list'),
    path('<int:pk>',views.car_detail_view,name='car_detail'),
    path('showroom',views.showroom_view.as_view(), name='showroom'),
    path('showroom/<int:pk>',views.showroom_details.as_view(),name='showroomdet')

]