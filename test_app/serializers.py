from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['img_code', 'description']
    
    def to_representation(self, instance: Post):
        return {
        "id": instance.id,
        "img_code": instance.img_code,
        "description": instance.description
    }
    