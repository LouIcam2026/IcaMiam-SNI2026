from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from ckeditor.widgets import CKEditorWidget

from shop.models import (
    Slider, Collection, Product, Category, Image, Setting, Social, Page,
    Navcollection, Carrier, Order, OrderItem
)

class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'link',)
    list_display_links = ('name',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_head', 'is_foot', 'is_checkout',)
    list_display_links = ('name',)
    list_editable = ('is_head', 'is_foot', 'is_checkout')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    exclude = ('slug',)

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'display_logo', 'currency', 'street', 'city',)
    list_display_links = ('name',)
    
    def display_logo(self, obj):
        return format_html(f'<img src="{ obj.logo.url }" width="100" />')
    
    display_logo.short_description = 'logo'

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'

class NavcollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" height="80" width="90" />')
    
    display_image.short_description = 'image'

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" height="80" width="90" />')
    
    display_image.short_description = 'image'

class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'display_image', 'price',)
    list_display_links = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" height="80" width="90" />')
    
    display_image.short_description = 'image'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mega',)
    list_display_links = ('name',)
    list_editable = ('is_mega', )
    exclude = ('slug',)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name', 'stock' ,'price', 'is_available', 'is_best_seller', 'display_image',)
    list_display_links = ('name',)
    list_editable = ('is_best_seller', 'is_available',)
    list_per_page = 5
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    
    def display_image(self, obj):
        first_image = obj.images.first()
        if not first_image:
            return ''
        return format_html(f'<img src="{ first_image.image.url }" height="80" width="90" />')
    
    display_image.short_description = 'image'
    exclude = ('slug',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nom', 'prenom', 'classe', 'email', 'time_slot', 'total', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Navcollection, NavcollectionAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Order, OrderAdmin)
