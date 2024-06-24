from django.contrib import admin
from shop.models.Slider import Slider
from django.utils.html import format_html
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.Image import Image
from shop.models.Setting import Setting
from shop.models.Social import Social
from shop.models.Page import Page
from django.db import models
from ckeditor.widgets import CKEditorWidget
from shop.models.Navcollection import Navcollection
from shop.models.Carrier import Carrier

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
        return format_html(f'<img src="{ obj.image.url }" heigth="80" width="90" />')
    
    display_image.short_description = 'image'

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" heigth="80" width="90" />')
    
    display_image.short_description = 'image'

class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'display_image', 'price',)
    list_display_links = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" heigth="80" width="90" />')
    
    display_image.short_description = 'image'



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mega',)
    list_display_links = ('name',)
    list_editable = ('is_mega', )
    
    #def display_image(self, obj):
        #return format_html(f'<img src="{ obj.image.url }" heigth="80" width="90" />')
    
    #display_image.short_description = 'image'
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
        return format_html(f'<img src="{ first_image.image.url }" heigth="80" width="90" />')
    
    exclude = ('slug',)
    display_image.short_description = 'image'


admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Navcollection, NavcollectionAdmin)
admin.site.register(Carrier, CarrierAdmin)