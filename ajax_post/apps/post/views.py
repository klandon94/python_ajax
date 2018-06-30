from django.shortcuts import render,redirect

def index(request):
    return redirect('/postpage')

def postpage(request):
    return render(request, 'post/index.html')

def makepost(request):
    context = {
        'newnote':request.POST['note']
    }
    return render(request, 'post/newpost.html', context)

