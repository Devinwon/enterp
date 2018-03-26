from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


###############################################
'''
地区表
'''
class Area(models.Model):
	Code=models.IntegerField()
	Name=models.CharField(null=True,blank=True,max_length=100)
	ParentId=models.ForeignKey('self',null=True,blank=True,default=None,related_name='area') 	#自关联
	
	class Meta:
		verbose_name='Area'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.Name


###############################################
'''
组织表
'''
class Org(models.Model):
	Name=models.CharField(max_length=200)
	Latitude=models.CharField(max_length=200)
	Longitude=models.CharField(max_length=200)
	Type=models.CharField(max_length=200)
	Representative=models.CharField(max_length=200)					#法人代表

	class Meta:
		verbose_name='Org'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.Name



###############################################
'''
采购目录
'''
class PurchaseCategory(models.Model):
	Name=models.CharField(max_length=100)
	ParentId=models.ForeignKey('self',related_name='parentid')

	class Meta:
		verbose_name='PurchaseCategory'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.Name


###############################################
'''
订单明细表
'''
class OrderDetail(models.Model):
	UserId=models.OneToOneField(to=User,related_name='userid')
	ProductName=models.CharField(max_length=100)
	Price=models.DecimalField(decimal_places=2,max_digits=10)
	OrderDate=models.DateField(auto_now=True)
	WayToPay=models.CharField(max_length=300)
	PaymentTime=models.DateTimeField(auto_now=True)
	Receipts=models.DecimalField(decimal_places=2,max_digits=10)
	Quality=models.IntegerField()
	RefundOperator=models.CharField(max_length=100)
	RefundAmount=models.DecimalField(decimal_places=2,max_digits=10)
	RefundFrom=models.CharField(max_length=200)
	RefundTime=models.DateTimeField(auto_now=True)
	AmountBeforePayment=models.DecimalField(decimal_places=2,max_digits=10)
	Discount=models.DecimalField(decimal_places=2,max_digits=10)
	TotalAmount=models.DecimalField(decimal_places=2,max_digits=10)

	class Meta:
		verbose_name='OrderDetail'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.ProductName


###############################################
'''
积分相关表
'''
class BonusPoints(models.Model):
	ProductPrice=models.DecimalField(max_digits=10,decimal_places=2)
	Second=models.DecimalField(max_digits=10,decimal_places=2)
	Third=models.DecimalField(max_digits=10,decimal_places=2)
	Fourth=models.DecimalField(max_digits=10,decimal_places=2)
	Fifth=models.DecimalField(max_digits=10,decimal_places=2)
	Sixth=models.DecimalField(max_digits=10,decimal_places=2)
	Seventh=models.DecimalField(max_digits=10,decimal_places=2)
	FirstRecommended=models.DecimalField(max_digits=10,decimal_places=2)
	RatiofReceiptsAndBonuspoint=models.DecimalField(max_digits=10,decimal_places=2) #付款金额与积分比率
	RatiofBonuspointReward=models.DecimalField(max_digits=10,decimal_places=2)
	PayerHasBonuspoint=models.BooleanField(default=False)
	RefundDeadline=models.DateTimeField(auto_now=False)

	class Meta:
		verbose_name='BonusPoints'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.ProductPrice

"""
###############################################
'''
用户组织关联表
'''
class OrgUser(models.Model):
	UserId=models.OneToOneField(to=User,related_name='userid')
	OrgId=models.OneToOneField(to=Org,related_name='orgid')
	
	class Meta:
		verbose_name='OrgUser'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.OrgId


###############################################
'''
投标信息
'''
class BiddingInfo(models.Model):
	TagName=models.CharField(max_length=100)
	Url=models.URLField()
	Title=models.CharField(max_length=200)
	LabelTime=models.DateTimeField(auto_now=True)	#标注时间
	PurchaseDept=models.CharField(max_length=200)	#采购单位
	OrgCategory=models.CharField(max_length=100)	#采购单位性质

	PurchseArea=models.ForeignKey(to=Area,related_name='purchsearea')	#采购地区
	PurchaseCategory=models.ForeignKey(to=PurchaseCategory,related_name='purchasecategory')	#采购目录
	GetViews=models.IntegerField()									#查看次数
	PublishTime=models.DateTimeField(auto_now=True)	#发布时间
	DeadLine=models.DateTimeField(auto_now=False)		#截止时间
	TimestoFavo=models.IntegerField()
	LabelByWhom=models.CharField(max_length=100)	#手工标注人
	BiddingType=models.IntegerField()								#招标类型
	BiddingStatus=models.IntegerField()					
	BiddingSubject=models.CharField(max_length=200) #主提

	class Meta:
		verbose_name='BiddingInfo'
		verbose_name_plural=verbose_name
	def __str__(self):
		return self.Title


###############################################
'''
用户拓展信息
'''
class Userprofile(models.Model):
	Belongto=models.OneToOneField(to=User)
	Mobile=models.IntegerField(max_length=11)
	PromoteCode=models.CharField(max_length=100)
	WeixinId=models.IntegerField()


###############################################
'''
浏览足迹记录表
'''
class Footprint(models.Model):
	AreaId=models.ForeignKey(to=Area,null=True,blank=True,related_name='areaid')
	BidInfoId=models.ForeignKey(to=BiddingInfo,null=True,blank=True,related_name='bidinfoid')
	FavoTag=models.CharField(null=True,blank=True,max_length=100)
	OrgId=models.OneToOneField(to=Org,related_name='orgid')
	PurchaseCateId=models.ForeignKey(to=PurchaseCategory,related_name='purchasecateid')
	userId=models.OneToOneField(to=User)

	class Meta:
		verbose_name='Footprint'
		verbose_name_plural=verbose_name
	def __str__(self):
		return self.areaId
"""


