from django.shortcuts import get_object_or_404

from courses.models import Course
from django.http import JsonResponse


def courses(request):
    courses_list = Course.objects.all()
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


def new_courses(request):
    # TODO напишите здесь view-функцию (задание new_courses)
    courses_list = Course.objects.filter(status="new")
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


def get_course(request, slug):
    # TODO напишите здесь view-функцию (задание find_by_name)
    course = get_object_or_404(Course, slug=slug)

    return JsonResponse(
        {
            "id": course.id,
            "slug": course.slug,
            "author": course.author,
            "description": course.description,
            "start_day": course.start_day,
            "status": course.status,
            "created": course.created,
        },
        json_dumps_params={"ensure_ascii": False}
    )


def search(request):
    # TODO напишите здесь view-функцию (задание who's author)
    courses = Course.objects.all()
    search_text = request.GET.get("author", None)
    if search_text:
        courses = courses.filter(author=search_text)

    response = []
    for course in courses:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
