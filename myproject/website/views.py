from django.shortcuts import render

def index(request):
    datas = {

    }
    return render(request, 'index.html', datas)


def about(request):
    datas = {

    }
    return render(request, 'about.html', datas)




def contact(request):
    datas = {

    }
    return render(request, 'contact.html', datas)