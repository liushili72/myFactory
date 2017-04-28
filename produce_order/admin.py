# coding: utf-8
from django.contrib import admin

# Register your models here.
from .models import ProductSize, Customer, ProduceOrder


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('kind', 'value')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ProduceOrder)
class ProduceOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'style',
                    'customer_name', 'display_size',
                    'box_number', 'pay_time', 'create_time')
    list_select_related = ('customer', 'length', 'width', 'height')
    fieldsets = (
        (None, {
            'fields': ('order_number', 'name', 'style')
        }),
        (u'产品尺寸', {
            'fields': ('length', 'width', 'height')
        }),
        (u'订单交付', {
            'fields': ('customer', 'box_number', 'pay_time')
        })
    )

    def customer_name(self, obj):
        return obj.customer.name

    def display_size(self, obj):
        return '长: (%s)  宽: (%s)  高: (%s)' % (obj.length.value, obj.width.value, obj.height.value)

    customer_name.short_description = u'客户名称'
    display_size.short_description = u'产品尺寸'

