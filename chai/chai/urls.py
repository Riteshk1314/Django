from django.urls import path, include
from chai import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chai/', include('chaicode.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]


