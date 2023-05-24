from django.http import HttpResponse

from .models import Submissions


def index(request):
    return HttpResponse("hello")


def submissions(request):
    latest_submission_list = Submissions.objects.order_by("id")[:5]
    output = "<br><br>".join([f"{s.__dict__}" for s in latest_submission_list])
    response = HttpResponse(output)
    response.headers["foobar"] = 120
    return response

