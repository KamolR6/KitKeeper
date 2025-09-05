from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import User
def index(request):
    newest_user_list = User.objects.order_by("username")
    template = loader.get_template("KitKeeperMain/index.html")
    context = {"newest_user_list": newest_user_list}
    return render(request, "KitKeeperMain/index.html", context)
    #return HttpResponse(template.render(context, request))

def detail(request, username):
    return HttpResponse("Your name %s." % username)