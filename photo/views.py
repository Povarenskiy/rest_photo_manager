from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend

from photo.serializers import *
from photo.models import *


class PhotoViewSet(viewsets.ModelViewSet):
    """Представление фотографий"""
    queryset = Photo.objects.all().order_by('-date')
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('date', 'people__name', 'country', 'city')
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    permission_classes = (permissions.IsAuthenticated,)
    

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        return self.serializer_class



class NameViewSet(viewsets.ModelViewSet):
    """Представление имен"""
    queryset = Names.objects.all()
    serializer_class = NameSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('^name',)


