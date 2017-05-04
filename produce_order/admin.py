# coding: utf-8
from django.contrib import admin

# Register your models here.
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import ProductSize, Company, ProduceOrder, Product, OrderItem


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('kind', 'value')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'person', 'phone', 'fax', 'kind')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'style', 'company_name', 'length', 'width', 'height')

    def company_name(self, obj):
        return obj.company.name

    def display_size(self, obj):
        return '长: (%s)  宽: (%s)  高: (%s)' % (obj.length.value, obj.width.value, obj.height.value)

    company_name.short_description = u'客户名称'
    display_size.short_description = u'产品尺寸'


class OrderItemInline(admin.TabularInline):
    extra = 1
    model = OrderItem


@admin.register(ProduceOrder)
class ProduceOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'company_name', 'pay_time', 'create_time', 'items')
    inlines = [OrderItemInline,]
    list_select_related = ('company',)

    def company_name(self, obj):
        return obj.company.name

    def items(self, obj):
        print obj.order_item.all().values_list('product', flat=True), 123
        return format_html_join(mark_safe('</br>'),
                                '品名[{}] -- 长：{} 宽：{} 高：{} -- 纸箱数量:[{}]',
                                obj.order_item.all().values_list('product__name', 'product__length',
                                                                 'product__width', 'product__height', 'box_number'))
    company_name.short_description = u'客户名称'
    items.short_description = u'订单明细'

