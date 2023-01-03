from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


import io
import base64
import qrcode
from qrcode.image.svg import SvgImage

from fileshare.models import File
from .serializers import FileSerializer

# send file to the server api
# Post request API call url 'http://127.0.0.1:8000/file-share-bd-api/'
# required field name "file"
'''
1. ID and qr-image serve format
{
    "id": 228414,
    "qrImage": "data:image/svg+xml;utf8;base64,PDH......................IC8+PC9zdmc+"
}
'''


class FileReceiveView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        img = qrcode.make(serializer.data['id'], image_factory=SvgImage, box_size=15, border=2)
        stream = io.BytesIO()  
        img.save(stream)    # Convert to byte array and store in stream
        base64_image = base64.b64encode(stream.getvalue()).decode()

        context = dict()
        context['id'] = serializer.data.get('id')
        context['qrImage'] = 'data:image/svg+xml;utf8;base64,' + base64_image

        return Response(context, status=status.HTTP_202_ACCEPTED)


# serve file to the user api call
# Post request API call url 'http://127.0.0.1:8000/file-share-bd-api/serve-file/'
# required field name "id"

'''
1. File Not Found Error Format
{
    "detail": "Not found."
}

2. File Serve Format
{
    "id": "546789",
    "file": "media/file/user.pdf"
}

3. Invalid Key Error Format
{
    "error": "Please Enter Valid ID."
}

'''

class FileServeView(APIView):

    def post(self, request, *args, **kwargs):
        id = request.data.get('id', None)

        if id != None and len(str(id)) == 6:
            file = get_object_or_404(File, id=id)
            serializer = FileSerializer(file, many=False)

            return Response(serializer.data, status=status.HTTP_302_FOUND)

        else:
            return Response({'error': 'Please Enter Valid ID.'}, status=status.HTTP_400_BAD_REQUEST)
