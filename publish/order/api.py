from order.models import Area,Org,PurchaseCategory,OrderDetail,BonusPoints
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import HttpResponse

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
		serializer=OrgSerializer(purcateInfo,many=True)
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



