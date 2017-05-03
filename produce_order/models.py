# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

PRODUCT_SIZE_KIND_CHOICES = (
    ('L', u'长'),
    ('W', u'宽'),
    ('H', u'高'),
)


class ProductSize(models.Model):
    kind = models.CharField(u'适用类型', choices=PRODUCT_SIZE_KIND_CHOICES, max_length=25)
    value = models.FloatField(u'尺寸')

    def __unicode__(self):
        return '%s' % self.value

    class Meta:
        db_table = 'product_size'
        verbose_name = u'基础尺寸'


class Company(models.Model):
    name = models.CharField(u'公司名称', max_length=255)
    address = models.CharField(u'公司地址', max_length=255)
    person = models.CharField(u'联系人', max_length=25)
    phone = models.CharField(u'联系电话', max_length=25)
    fax = models.CharField(u'传真号', max_length=25)
    kind = models.CharField(u'公司类型', max_length=255)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'company'
        verbose_name = u'公司'


class Product(models.Model):
    name = models.CharField(u'产品名称', max_length=255)
    style = models.CharField(u'款式', max_length=255)
    company = models.ForeignKey(Company, verbose_name=u'客户')
    length = models.ForeignKey(ProductSize,
                               related_name='po_by_length',
                               verbose_name=u'长度',
                               limit_choices_to={'kind': PRODUCT_SIZE_KIND_CHOICES[0][0]})
    width = models.ForeignKey(ProductSize,
                              related_name='po_by_width',
                              verbose_name=u'宽度',
                              limit_choices_to={'kind': PRODUCT_SIZE_KIND_CHOICES[1][0]})
    height = models.ForeignKey(ProductSize,
                               related_name='po_by_height',
                               verbose_name=u'高度',
                               limit_choices_to={'kind': PRODUCT_SIZE_KIND_CHOICES[2][0]})

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'product'
        verbose_name = u'产品'


class ProduceOrder(models.Model):
    order_number = models.CharField(u'生产单编号', max_length=255)
    company = models.ForeignKey(Company, verbose_name=u'客户')
    products = models.ManyToManyField(Product,
                                      through='OrderProductShip',
                                      through_fields=('order', 'product'),
                                      verbose_name=u'产品')

    pay_time = models.DateTimeField(u'交货时间')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = 'produce_order'
        verbose_name = u'生产单'


class OrderProductShip(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(ProduceOrder, on_delete=models.CASCADE)
    box_number = models.IntegerField(u'纸箱数量')
