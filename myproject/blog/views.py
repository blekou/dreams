from django.shortcuts import render

def blog(request):
    datas = {

    }
    return render(request, 'blog.html', datas)

def single(request):
    datas = {

    }
    return render(request, 'single-blog.html', datas)
