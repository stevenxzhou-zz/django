from django.contrib import admin
from dealmoon.models import MainProductCategory
from dealmoon.models import SubProductCategory
from dealmoon.models import Products
from dealmoon.models import User
from dealmoon.models import Stores
from dealmoon.models import Favorites

admin.site.register(MainProductCategory)
admin.site.register(SubProductCategory)
admin.site.register(Products)
admin.site.register(User)
admin.site.register(Stores)
admin.site.register(Favorites)

class MainProductCategoryAdmin(admin.ModelAdmin):
    list_display=('MainCategoryName')

# Register your models here.

