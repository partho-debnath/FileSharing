from django.shortcuts import render, get_object_or_404

from . models import  File

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        info = request.FILES.get('files')
        file = File.objects.create(file=info)
        context = {'fileid':file.id}
        print(context)
        return render(request, 'index.html', context)


def recive(request):
    if request.method == 'GET':
        fileid = request.GET['fileid']
        file = get_object_or_404(File, pk=int(fileid))
        print(f'\n{file}\n')
        context = {'userfile': file}
        return render(request, 'index.html', context)