from order.models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.shortcuts import HttpResponse

######################################

class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Area
		fields='__all__'

@api_view(['GET'])
def area(request):
	if request.method=='GET':
		areaInfo=Area.objects.order_by('-id')
		serializer=AreaSerializer(areaInfo,many=True)
		return Response(serializer.data)


######################################

class OrgSerializer(serializers.ModelSerializer):
	class Meta:
		model=Org
		fields='__all__'

@api_view(['GET'])
def org(request):
	if request.method=='GET':
		orgInfo=Org.objects.order_by('-id')
		serializer=OrgSerializer(orgInfo,many=True)
		return Response(serializer.data)


######################################

class PurchaseCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=PurchaseCategory
		fields='__all__'

@api_view(['GET'])
def purchasecategory(request):
	if request.method=='GET':
		purcateInfo=PurchaseCategory.objects.order_by('-id')
		serializer=PurchaseCategorySerializer(purcateInfo,many=True)
		return Response(serializer.data)


######################################

class OrgCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=OrgCategory
		fields='__all__'

@api_view(['GET'])
def orgcategory(request):
	if request.method=='GET':
		orgcateInfo=OrgCategory.objects.order_by('AliasName')
		serializer=OrgCategorySerializer(orgcateInfo,many=True)
		return Response(serializer.data)

######################################

class OrderDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=OrderDetail
		fields='__all__'

@api_view(['GET'])
def orderdetail(request):
	if request.method=='GET':
		orderdetailInfo=OrderDetail.objects.order_by('-id')
		serializer=OrderDetailSerializer(orderdetailInfo,many=True)
		return Response(serializer.data)


######################################

class BonusPointsSerializer(serializers.ModelSerializer):
	class Meta:
		model=BonusPoints
		fields='__all__'

@api_view(['GET'])
def bonuspoints(request):
	if request.method=='GET':
		bonuspointsInfo=BonusPoints.objects.order_by('-id')
		serializer=BonusPointsSerializer(bonuspointsInfo,many=True)
		return Response(serializer.data)


######################################

class OrgUserSerializer(serializers.ModelSerializer):
	class Meta:
		model=OrgUser
		fields='__all__'

@api_view(['GET'])
def orguser(request):
	if request.method=='GET':
		orguserInfo=OrgUser.objects.order_by('-id')
		serializer=OrgUserSerializer(orguserInfo,many=True)
		return Response(serializer.data)


######################################

class BiddingInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=BiddingInfo
		fields='__all__'

@api_view(['GET'])
def biddinginfo(request):
	if request.method=='GET':
		bidinfo=BiddingInfo.objects.order_by('-id')
		serializer=BiddingInfoSerializer(bidinfo,many=True)
		return Response(serializer.data)


######################################

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields='__all__'

@api_view(['GET'])
def userprofile(request):
	if request.method=='GET':
		userinfo=UserProfile.objects.order_by('-id')
		serializer=UserProfileSerializer(userinfo,many=True)
		return Response(serializer.data)


######################################

class FootPrintSerializer(serializers.ModelSerializer):
	class Meta:
		model=FootPrint
		# fields='__all__'

@api_view(['GET'])		
def footprint(request):
	if request.method=='GET':
		footprintinfo=FootPrint.objects.order_by('-id')
		serializer=FootPrintSerializer(footprintinfo,many=True)
		return Response(serializer.data)


######################################


