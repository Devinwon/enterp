from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from ..models import *


###############################################
'''
订单明细表
'''
class UserSubscribe(models.Model):
	UserId=models.OneToOneField(to=User, related_name='orderuserid')
	ScribeName=models.BooleanField()
	OrgCategory = models.ForeignKey(to=OrgCategory, related_name='orgcategory', null=True)  # 采购单位性质
	SeqNo = models.CharField(max_length=100)
	PurchseArea = models.ForeignKey(to=Area, related_name='purchsearea_id', null=True)  # 采购地区
	UpdateTime=models.TimeField(auto_now=True)
	PurchaseCategory = models.ForeignKey(to=PurchaseCategory, related_name='purchasecategory', null=True)  # 采购目录
	KeyWord=models.CharField(max_length=500)

	class Meta:
		verbose_name='UserSubscribe'
		verbose_name_plural=verbose_name

	def __str__(self):
		return self.ScribeName


###############################################
'''
订单明细表
'''
class UserBidding(models.Model):

	UserId=models.OneToOneField(to=User, related_name='orderuserid')
	UserBiddingId = models.ForeignKey(to=BiddingInfo ,related_name='biddinginfo' ,null=True ) # 匹配后的招标信息
	isRead = models.BooleanField() #
	isMailSend = models.BooleanField()  #
	isFavor = models.BooleanField() #
	isWeiXinSend = models.BooleanField() #

	class Meta:
		verbose_name='UserBidding'
		verbose_name_plural=verbose_name