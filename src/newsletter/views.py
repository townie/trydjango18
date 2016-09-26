from django.shortcuts import render

# Create your views here.


def home(request):
    title = "welcome"
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        title = "Welcome senior %s" % (request.user)

    context = {
        'title': title
    }
    return render(request, "home.html", context)
