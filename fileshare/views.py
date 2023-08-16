import zipfile
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

import os
import io
import qrcode
from qrcode.image.svg import SvgPathImage

from . utils import getFileNameAsTime, getTemporaryFilePath, get_media_storage_name
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
        
    elif request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')

        oneMB = 1048437.79264214   # 1MB = 1048437.79264214 bytes
        totalSize = 0.0
        for file in uploaded_files:
            totalSize += file.size
            if int(totalSize) > 104843779:
                messages.warning(
                    request,
                    'File size should not exceed 100.000 MB. But your file size is %.3fMB' %(totalSize/oneMB)
                )
                return HttpResponseRedirect(reverse('fileshare:index'))
        
        file_path = getFileNameAsTime('.zip')

        with zipfile.ZipFile(file_path, 'w') as zip_file:
            for uploaded_file in uploaded_files:
                
                file_name = uploaded_file.name
                # print('name:', file_name)
                # print('size:', uploaded_file.size)
                # print('Type: ', uploaded_file.content_type)
                
                '''
                read the entire uploaded data from the file. Be careful with 
                the method 'read()', if the uploaded file is huge it can overwhelm the 
                system if you try to read it into memory. You’ll probably want 
                to use 'chunks()' instead.
                 
                Using read(), see below. then chunks().
                '''
                file_data = uploaded_file.read()
                zip_file.writestr(zinfo_or_arcname= file_name, data=file_data)
                

                '''
                Using chunks() 
                '''
                # temporary_file = getTemporaryFilePath(file_name)
                # with open(temporary_file, 'wb') as destination:
                #     for chunk in uploaded_file.chunks():
                #         destination.write(chunk)
                # zip_file.write(temporary_file) # write each uploaded file in a zip file.
                # os.remove(temporary_file)   # remove the temporary file


        file_name = os.path.join(get_media_storage_name(), str(file_path).split('/')[-1])
        file = File.objects.create(file=file_name)
        print(file.file.url)
        domain = 'http://127.0.0.1:8000'
        qr_url = f"{domain}{reverse('fileshare:receive')}?fileid={file.pk}/"

        qr = qrcode.QRCode(
            version=1,
            image_factory=SvgPathImage,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)
        img = qr.make_image(back_color=(241, 246, 247), fill_color=(243, 30, 30))
        # img.save("C:/Users/parth/Downloads/Video/qr_web.svg")

        stream = io.BytesIO()  
        img.save(stream)    # Convert to byte array and store in stream

        context = {
            'fileid': file.id, 
            'qrcode': stream.getvalue().decode(),
            'key_expired_message': 'This key will expire after 7 days.'
        }
        return render(request, 'index.html', context)


def receive(request):
    if request.method == 'GET':
        fileid = str(request.GET['fileid'])
        
        if len(fileid) != 6 or fileid.isnumeric() == False:
            messages.warning(request, 'Please Enter Valid Key.')
            return render(request, 'index.html')
        try:
            fileid = fileid[:-1] if fileid.endswith('/') else fileid
            file = get_object_or_404(File, pk=int(fileid))
            print(file);
        except Exception as e:
            messages.warning(request, 'Key is Not Found or Expired!')
            return render(request, 'index.html')
    
        context = {'userfile': file}
        return render(request, 'index.html', context)