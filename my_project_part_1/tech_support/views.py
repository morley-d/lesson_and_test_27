# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    # TODO напишите view-функцию которая возвращает всю статистику
    #  обращений в тех-поддержку (задание tech_support)
    appeals = Statistic.objects.all()
    response = []
    for appeal in appeals:
        response.append({
            "id": appeal.id,
            "author": appeal.author,
            "day": appeal.day,
            "store": appeal.store,
            "reason": appeal.reason,
            "status": appeal.status,
            "timestamp": appeal.timestamp,
        })
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
