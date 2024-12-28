from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul' : 'IKASDA | BLOG',
        'subJudul' : 'Ini adalah halaman blog Ikatan Alumni SMAN 2 Lembang',
        'kontributor' : 'myus kasep',
        'nav': [
            ['/','Home'],
            ['/blog/cerita','Cerita'],
            ['/blog/news','News'],
        ],
        'banner': 'blog/img/blog.png',
        'app_css':'blog/css/style.css'
    }
    return render(request,'index.html', context)

def news(request):
    context = {
        'judul' : 'news',
        'kontributor' : 'teman myuss'
    }
    return render(request,'blog/index.html', context)

def cerita(request):
    context = {
        'judul' : 'cerita',
        'kontributor' : 'calon myus'
    }
    return render(request,'blog/index.html', context)

def recent(request):
    return HttpResponse(' <h1> Mugen Tsukuyomi terjadi di jepang</h1>')