from django.contrib import admin
from .models import Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model  = OrderItem
    extra  = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'price', 'stock_quantity', 'created_at')
    search_fields = ('name',)
    list_filter   = ('created_at',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter  = ('status',)
    inlines      = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price')