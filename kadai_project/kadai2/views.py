from django.shortcuts import render


def createView(request):
    return render(request, 'create.html')


def listView(request):
    return render(request, 'list.html')
