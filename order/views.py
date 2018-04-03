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
	search_fields=('Name',)
	ordering_fields=('Code',)


class PurchaseCategoryViewSet(DefaultsMixin,viewsets.ModelViewSet):
	"""PurchaseCategory API"""
	queryset=PurchaseCategory.objects.order_by('Name')
	serializer_class=PurchaseCategorySerializer
	search_fields=('Name',)
	ordering_fields=('Name',)


##############################
from django.contrib.auth.models import User
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from django.views.decorators.http import require_http_methods
# from utils.SmsSender import getcode, send_smscode
# from utils.sendemail import send_email,send_email_code
# from utils.random_code import generate_verification_code
# from utils.get_hash import get_hash
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 检验用户名是否存在
def verify_user(request):
    email = request.POST.get('email')
    try:
        obj = User.objects.get(email=email)
        if obj and obj.is_atcive:
            # 用户名已经存在 返回res:1
            return JsonResponse({'res': 1})
    except:
        # 返回异常则表示用户名不存在 返回res:0
        return JsonResponse({'res': 0})


# # 发送验证码接口
# def send_code(request):
#     # 获取用户邮箱
#     email = request.POST.get('email')
#     # email = '287082003@qq.com'
#     # 随机生成6位验证码
#     code = generate_verification_code()
#     # 把生成的验证码保存在session中
#     request.session['code'] = code
#     print(request.session.get('code'))
#     # session_key = request.session.session_key
#     # 把验证码发送到邮箱
#     try:
#         send_email_code(email=email, code=code)
#         return JsonResponse({'res': 1})
#     except:
#         return JsonResponse({'res': 0})

# 发送短信验证码接口
def send_code(request):
    """Conf"""
    appid = 1400076660
    appkey = "79219a01f7f44ff69b2e9d3420e91af1"
    template_id =98106
    expired_time=5  #5 minutes
    params=[]
    phone_numbers=[]
    phone = request.POST.get('phone')
    phone_numbers.append(phone)
    smscode = getcode()         # 随机生成5位验证码
    params.insert(0,smscode)
    params.append(expired_time)
    request.session['smscode'] = smscode+phone  # 把生成的验证码保存在session中
    # print(request.session.get('smscode'))
    # session_key = request.session.session_key
    ssender = SmsSingleSender(appid, appkey)
    try:
        result = ssender.send_with_param(86, phone_numbers[0],template_id, params)
        return JsonResponse({'res': 1})
        # send_smscode(phone=phone, code=smscode)
    except:
        return JsonResponse({'res': 0})

# 注册
# @csrf_exempt
def register_check(request):
    # 获取验证码参数
    sms_code = request.POST.get('YZM')
    #sms_code = '0'
    # 获取用户名和密码
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    # 获取保存的生存验证 码
    ser_code = request.session.get('smscode')
    print(ser_code)
    # 判断输入的验证码数否一致 成功返回res1 失败res0
    try:
        obj = User.objects.get(username=phone)
        # 用户名已经存在 返回res:0
        return JsonResponse({'res': 0})
    except:
        pass
    if sms_code+phone == ser_code:
        # 成功的话把数据存入数据库中
        User.objects.add_one_passport(username=phone, password=password, phone=phone)
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


# 登录校验
# @csrf_exempt
def login_check(request):
    """进行登录校验"""
    # 1.接收用户名和密码
    username = request.POST.get('phone')
    password = request.POST.get('password')
    # 2.根据用户名和密码查找账户信息
    passport = User.objects.get_one_passport(username=username, password=password)
    # 3.如果查到，返回json {'res':1} 如果查不到，返回 {'res':0}
    if passport:
        # 用户名密码正确
        jres = {'res': 1}
        # 记录用户登录状态
        request.session['islogin'] = True
        request.session['username'] = username
        # 记录登录账户id
        request.session['Passport_id'] = passport.id
        return HttpResponse(json.dumps(jres), content_type='application/json')
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0})


#修改密码
def update_pwd(request):
    username = request.POST.get('phone')
    password = request.POST.get('password')
    #根据用户名获取用户数据
    passport = User.objects.get_passpory(username=username)
    User.objects.filter(id=passport.id).update(password=password)


#验证手机号
def getCode(request):
    phone = request.POST.get('phone')
    #phone='18607232032'
    # 获取验证码参数
    sms_code = request.POST.get('YZM')
    #sms_code='39695'
    ser_code = request.session.get('smscode')
    if sms_code+phone == ser_code:
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

#
def Information_setting(request):
    username = request.POST.get('phone')
    #username='1'
    company_name = request.POST.get('company_name')
    #company_name='opo'
    credit = request.POST.get('credit')
    #credit='lol'
    email = request.POST.get('email')
    #email='122wwzz.com'
    passport = User.objects.get_passpory(username=username)
    if passport:
        User.objects.filter(id=passport.id).update(company_name=company_name,credit=credit,email=email)
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})





