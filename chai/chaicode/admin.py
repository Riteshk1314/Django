from django.contrib import admin
from .models import ChaiVariety,ChaiReview, store, certificate



class ChaiReviewInLine(admin.TabularInline):
    model=ChaiReview
    extra=2
    
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[ChaiReviewInLine]
    
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varieties',)
    
class certificateAdmin(admin.ModelAdmin):
    list_display=('date',)
    
    
admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(certificate,certificateAdmin)