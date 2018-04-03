from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'bidding_infos', views.BiddingInfoViewSet )
router.register(r'user_scribes', views.UserSubscribeViewSet )
router.register(r'area_infos', views.AreaViewSet )
router.register(r'purcate_infos', views.PurchaseCategoryViewSet )