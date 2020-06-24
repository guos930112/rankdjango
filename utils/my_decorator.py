# -*- coding: utf-8 -*-
"""
@Time   ： 2020/6/24 9:11 上午
@Author ： guos
@File   ：my_decorator.py
@IDE    ：PyCharm

"""
import functools
from django.http import JsonResponse


def need_login(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user:
            return JsonResponse({'msg': 'need login'})
        return func(request, *args, **kwargs)

    return wrapper
