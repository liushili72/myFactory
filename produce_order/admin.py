# coding: utf-8
from django.contrib import admin

# Register your models here.
from .models import ProductSize, Company, ProduceOrder, Product


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


@admin.register(ProduceOrder)
class ProduceOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'company_name', 'pay_time', 'create_time')
    list_select_related = ('company',)

    def company_name(self, obj):
        return obj.company.name

    company_name.short_description = u'客户名称'

