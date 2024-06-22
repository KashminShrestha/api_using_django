from django.contrib import admin
from .models import Cart, CartItem, Category, Customer, Order, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'qty', 'category']
    list_filter = ['category']
    search_fields = ['name', 'category']
    autocomplete_fields = ['category']
    list_per_page = 20


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name',
                    'last_name', 'contact', 'address']
    list_per_page = 20


class CartItemInline(admin.TabularInline):
    list_per_page = 20

    model = CartItem
    extra = 2


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer',]
    list_per_page = 20

    inlines = (CartItemInline,)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'address',
                    'payment_status', 'payment_mode', 'status']
    list_editable = ['status']
    list_filter = ['status', 'payment_mode', 'payment_status']
    list_per_page = 20
