from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    context = {
        'judul' : 'IKASDA',
        'subJudul' : 'Selamat Datang',
        'subsubJudul' : 'Di Website Ikatan Alumni SMAN 2 Lembang',
        'kontributor':'mustofa',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ],
        'banner': 'img/home.png'
    }
    return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')