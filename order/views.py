from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets, filters
from .forms import BiddingInfoFilter
from .models import BiddingInfo,Area,PurchaseCategory
from .api import BiddingInfoSerializer,AreaSerializer,PurchaseCategorySerializer
from .serializers import UsersubscribeSerializer
from .scribe_model.subscribe import UserSubscribe

# Create your views here.


class DefaultsMixin(object):
	"""Default settings for view authentication, permissions, filtering
	 and pagination."""

	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100
	filter_backends = (
		filters.SearchFilter,
	)


class BiddingInfoViewSet(DefaultsMixin, viewsets.ModelViewSet):
	"""API endpoint for listing and creating sprints."""
	queryset = BiddingInfo.objects.order_by('Title')
	serializer_class = BiddingInfoSerializer
	search_fields = ('Title')
	ordering_fields = ('PublishTime',)


class UserSubscribeViewSet(DefaultsMixin, viewsets.ModelViewSet):
	"""API endpoint for listing and creating sprints."""

	queryset = UserSubscribe.objects.order_by('SeqNo')
	serializer_class = UsersubscribeSerializer
	search_fields = ('ScribeName',)
	ordering_fields = ('SeqNo',)

class AreaViewSet(DefaultsMixin,viewsets.ModelViewSet):
	"""Area API"""
	queryset=Area.objects.order_by('Code')
	serializer_class=AreaSerializer
	search_fields=('Code',)
	ordering_fields=('Code',)


class PurchaseCategoryViewSet(DefaultsMixin,viewsets.ModelViewSet):
	"""PurchaseCategory API"""
	queryset=PurchaseCategory.objects.order_by('Name')
	serializer_class=PurchaseCategorySerializer
	search_fields=('Name',)
	ordering_fields=('Name',)

