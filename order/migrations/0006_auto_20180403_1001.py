# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-03 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0005_auto_20180327_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRead', models.BooleanField()),
                ('isMailSend', models.BooleanField()),
                ('isFavor', models.BooleanField()),
                ('isWeiXinSend', models.BooleanField()),
            ],
            options={
                'verbose_name': 'UserBidding',
                'verbose_name_plural': 'UserBidding',
            },
        ),
        migrations.CreateModel(
            name='UserSubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ScribeName', models.BooleanField()),
                ('SeqNo', models.CharField(max_length=100)),
                ('UpdateTime', models.TimeField(auto_now=True)),
                ('KeyWord', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'UserSubscribe',
                'verbose_name_plural': 'UserSubscribe',
            },
        ),
        migrations.AddField(
            model_name='orgcategory',
            name='ParentId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentid', to='order.OrgCategory'),
        ),
        migrations.AlterField(
            model_name='biddinginfo',
            name='PurchseArea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchsearea_id', to='order.Area'),
        ),
        migrations.AddField(
            model_name='usersubscribe',
            name='OrgCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orgcategory', to='order.OrgCategory'),
        ),
        migrations.AddField(
            model_name='usersubscribe',
            name='PurchaseCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasecategory', to='order.PurchaseCategory'),
        ),
        migrations.AddField(
            model_name='usersubscribe',
            name='PurchseArea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchsearea_id', to='order.Area'),
        ),
        migrations.AddField(
            model_name='usersubscribe',
            name='UserId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orderuserid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userbidding',
            name='UserBiddingId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biddinginfo', to='order.BiddingInfo'),
        ),
        migrations.AddField(
            model_name='userbidding',
            name='UserId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orderuserid', to=settings.AUTH_USER_MODEL),
        ),
    ]