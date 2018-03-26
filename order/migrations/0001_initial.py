# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-26 09:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.IntegerField()),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('ParentId', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='order.Area')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Area',
            },
        ),
        migrations.CreateModel(
            name='BiddingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TagName', models.CharField(max_length=100)),
                ('Url', models.URLField()),
                ('Title', models.CharField(max_length=200)),
                ('LabelTime', models.DateTimeField(auto_now=True)),
                ('PurchaseDept', models.CharField(max_length=200)),
                ('OrgCategory', models.CharField(max_length=100)),
                ('GetViews', models.IntegerField()),
                ('PublishTime', models.DateTimeField(auto_now=True)),
                ('DeadLine', models.DateTimeField()),
                ('TimestoFavo', models.IntegerField()),
                ('LabelByWhom', models.CharField(max_length=100)),
                ('BiddingType', models.IntegerField()),
                ('BiddingStatus', models.IntegerField()),
                ('BiddingSubject', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'BiddingInfo',
                'verbose_name_plural': 'BiddingInfo',
            },
        ),
        migrations.CreateModel(
            name='BonusPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Second', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Third', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Fourth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Fifth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Sixth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Seventh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('FirstRecommended', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RatiofReceiptsAndBonuspoint', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RatiofBonuspointReward', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PayerHasBonuspoint', models.BooleanField(default=False)),
                ('RefundDeadline', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'BonusPoints',
                'verbose_name_plural': 'BonusPoints',
            },
        ),
        migrations.CreateModel(
            name='FootPrint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FavoTag', models.CharField(blank=True, max_length=100, null=True)),
                ('AreaId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footareaid', to='order.Area')),
                ('BidInfoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footbidinfoid', to='order.BiddingInfo')),
            ],
            options={
                'verbose_name': 'FootPrint',
                'verbose_name_plural': 'FootPrint',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OrderDate', models.DateField(auto_now=True)),
                ('WayToPay', models.CharField(max_length=300)),
                ('PaymentTime', models.DateTimeField(auto_now=True)),
                ('Receipts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Quality', models.IntegerField()),
                ('RefundOperator', models.CharField(max_length=100)),
                ('RefundAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RefundFrom', models.CharField(max_length=200)),
                ('RefundTime', models.DateTimeField(auto_now=True)),
                ('AmountBeforePayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TotalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('UserId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orderuserid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OrderDetail',
                'verbose_name_plural': 'OrderDetail',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Latitude', models.CharField(max_length=200)),
                ('Longitude', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=200)),
                ('Representative', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Org',
                'verbose_name_plural': 'Org',
            },
        ),
        migrations.CreateModel(
            name='OrgUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrgId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orgid', to='order.Org')),
                ('UserId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orguserid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OrgUser',
                'verbose_name_plural': 'OrgUser',
            },
        ),
        migrations.CreateModel(
            name='PurchaseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('ParentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentid', to='order.PurchaseCategory')),
            ],
            options={
                'verbose_name': 'PurchaseCategory',
                'verbose_name_plural': 'PurchaseCategory',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile', models.IntegerField()),
                ('PromoteCode', models.CharField(max_length=100)),
                ('WeixinId', models.IntegerField()),
                ('Belongto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='footprint',
            name='OrgId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='footorgid', to='order.Org'),
        ),
        migrations.AddField(
            model_name='footprint',
            name='PurchaseCateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasecateid', to='order.PurchaseCategory'),
        ),
        migrations.AddField(
            model_name='footprint',
            name='UserId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='biddinginfo',
            name='PurchaseCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasecategory', to='order.PurchaseCategory'),
        ),
        migrations.AddField(
            model_name='biddinginfo',
            name='PurchseArea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchsearea', to='order.Area'),
        ),
    ]