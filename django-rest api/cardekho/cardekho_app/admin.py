from django.contrib import admin
from .models import carlist,showroomlist, review
# Register your models here.
admin.site.register(carlist)
admin.site.register(showroomlist)
admin.site.register(review)