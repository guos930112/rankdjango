import _md5
import base64

from django.shortcuts import render
from django.views import View
from users.models import UserProfile
from django.core import serializers
from django.http import JsonResponse
import json
from config.redis_config import cache_redis

# Create your views here.


def user_score_update(request):
    if request.method == 'GET':
        all_users = UserProfile.objects.all()
        pass


def user_score_rank():
    pass


class UserScoreUpdate(View):
    def post(self, request):
        # 表单 请求的话 第一需要把中间件的 csrf 注释 第二 获取数据方式 request.POST.get('uid', None)
        # uid = request.POST.get('uid', None)
        # post json格式传参 获取方法：request.body, 且需要 把 bytes类型 转为 str 再转为 dict
        data_dict = json.loads(request.body.decode())
        uid = data_dict.get('uid', None)
        score = data_dict.get('score', None)
        if not uid:
            return JsonResponse({'msg': 'uid is null'}, safe=False)
        users = UserProfile.objects.filter(id=int(uid))
        print(len(users), users)
        if not users:
            user = UserProfile()
            user.name = 'test%s' % uid
            user.username = 'test_%s' % uid
        else:
            user = users[0]
        user.score = int(score)
        user.save()
        mapping = {str(uid): int(score)}
        cache_redis.zadd('score_rank', mapping)
        return JsonResponse({'msg': 'update is ok'}, safe=False)


class UserScoreRank(View):
    def get(self, request):
        all_users = UserProfile.objects.all()  # queryset 列表
        data_str = serializers.serialize('json', all_users)  # 通过 serializers 把数据序列化为 字符串
        # 实现带分数 以及用户名 降序排序 取前10名 且带登陆的当前用户的名次
        cache_data = cache_redis.zrange('score_rank', 0, 2, desc=True, withscores=True)
        all_data = []
        for d in cache_data:
            cache_dict = {
                'user_name': d[0].decode(),
                'score': d[1]
            }
            all_data.append(cache_dict)
        return JsonResponse(all_data, safe=False)
