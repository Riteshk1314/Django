from django.urls import path, include
from chai import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('chai/', include('chaicode.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


