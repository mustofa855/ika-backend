from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'IKASDA | ABOUT',
        'subJudul':'Tentang Ikatan Alumni SMAN 2 LEMBANG',
        'banner': 'about/img/about.jpg',
        'kontributor':'asep saepudin',
        'app_css':'about/css/style.css'
    }
    return render(request, 'index.html', context)