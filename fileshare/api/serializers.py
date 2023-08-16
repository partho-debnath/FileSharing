from rest_framework import serializers

from fileshare.models import File


class FileSerializer(serializers.ModelSerializer):
    # override the id field as read_only = True or use Meta class read_only_fields = ['id'] 
    # id = serializers.IntegerField(read_only=True) 

    class Meta:
        model = File
        fields = ['file', 'id']
        read_only_fields = ['id', ] 
    
