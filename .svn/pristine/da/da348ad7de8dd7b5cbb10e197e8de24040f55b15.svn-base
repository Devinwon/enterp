from django.contrib import admin
from order.models import *
# Register your models here.
@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
	list_display=('Name','Latitude','Longitude','Type','Representative')
	list_per_page=20
	ordering=('Name',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	list_display=('Code','Name','ParentId')
	list_per_page = 20
	ordering = ('Name',)
	

@admin.register(PurchaseCategory)
class PurchaseCategory(admin.ModelAdmin):
	list_display=('Name','ParentId')
	list_per_page=20
	ordering=('Name',)


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
	list_display=('UserId','ProductName','AmountBeforePayment','Receipts','TotalAmount')
	list_per_page = 20
	ordering = ('UserId',)

@admin.register(BonusPoints)
class bonuspointsAdmin(admin.ModelAdmin):
	list_display=('ProductPrice','RatiofReceiptsAndBonuspoint','RatiofBonuspointReward','RefundDeadline')
	list_per_page=20
	ordering=('ProductPrice',)

"""
@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
	list_display=('areaId','bidInfoId','favoriteTag','orgId','purchseCateId','userId')
	list_per_page = 20
	ordering = ('areaId',)


"""