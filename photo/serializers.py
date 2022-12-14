from rest_framework import serializers
from photo.models import *


class NameSerializer(serializers.ModelSerializer):
    """Вывод информации об имени"""
    class Meta:
        model = Names
        fields = ['name']


class PhotoSerializer(serializers.ModelSerializer):
    """Вывод информации о фотографии"""
    image_url = serializers.ImageField(required=False, max_length=None, use_url=True)
    people = NameSerializer(many=True, required=False)
    
    class Meta:
        model = Photo    
        fields = '__all__'

    def create(self, validated_data):
        peole_data = validated_data.pop('people', [])
        photo = Photo.objects.create(**validated_data)

        for people in peole_data:
            new_people, createrd = Names.objects.get_or_create(**people)
            photo.people.add(new_people)
        
        return photo
        

class PhotoListSerializer(serializers.ModelSerializer):
    """Вывод списка фотографий"""
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Photo
        fields = ['id', 'image_url']

