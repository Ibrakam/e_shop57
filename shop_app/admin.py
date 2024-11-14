from django.contrib import admin
from shop_app.models import CategoryProduct, Product, UserCart


# Register your models here.
@admin.register(CategoryProduct)
class CategoryAdminModel(admin.ModelAdmin):
    search_fields = ["category_name", "id", "created_at"]
    list_filter = ["created_at"]
    list_display = ["id", "category_name", "created_at"]
    ordering = ["-id"]


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    search_fields = ["product_name", "id"]
    list_filter = ["created_at"]
    list_display = ["id", "product_name", "product_cost"]
    ordering = ["-id"]



