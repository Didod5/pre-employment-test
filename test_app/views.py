from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post


@api_view(['POST'])
def add_image(request):
    try:
        post = PostSerializer(data=request.data)
        post.is_valid(raise_exception=True)
        post.save()
        return Response('Success. Post id: ' + str(post.instance.id))
    except Exception as e:
        print(f"Error: {e}")
        return Response({str(e)}, status=400)
    
@api_view(['GET'])
def list_images(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def delete_image(request):
    try:
        id = request.data['id']
        post = Post.objects.get(id=id)
        post.delete()
        return Response('Successful deleting')
    except Exception as e:
        return Response({str(e)}, status=400)

def ui(request):
    return render(request, 'main.html')
