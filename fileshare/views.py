from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

import io
import qrcode
from qrcode.image.svg import SvgImage


from . models import  File, UserIPAddress

# Create your views here.


def index(request):
    if request.method == 'GET':
        userip = request.META.get('REMOTE_ADDR')
        try:
            UserIPAddress.objects.get(ipaddress=userip)
        except UserIPAddress.DoesNotExist:
            UserIPAddress.objects.create(ipaddress=userip)
            
        return render(request, 'index.html')
        
    else:
        uploadedfile = request.FILES.get('files')
        file = File.objects.create(file=uploadedfile)

        root_url = 'http://127.0.0.1:8000'
        qr_url = root_url + reverse('fileshare:recive') + f'?fileid={file.pk}/'
        print(qr_url)
        
        img = qrcode.make(qr_url, image_factory=SvgImage, box_size=15, border=2)
        stream = io.BytesIO()  
        img.save(stream)    # Convert to byte array and store in stream

        context = {'fileid': file.id, 'qrcode': stream.getvalue().decode()}
        return render(request, 'index.html', context)


def recive(request):
    if request.method == 'GET':
        fileid = str(request.GET['fileid'])

        try:
            fileid = fileid[:-1] if fileid.endswith('/') else fileid
            file = get_object_or_404(File, pk=int(fileid))
        except Exception as e:
            messages.warning(request, 'Key is Not Found or Expired!')
            return render(request, 'index.html')
                        
        context = {'userfile': file}
        file.delete()
        return render(request, 'index.html', context)