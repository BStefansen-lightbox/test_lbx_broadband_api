from django.http import HttpResponse


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. <br><br>{request.META}")