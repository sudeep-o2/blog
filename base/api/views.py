
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Blog
from . serializers import BlogSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/detail/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getDetail(request):
    blogs=Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getout(request,pk):
    blogs=Blog.objects.filter(host=pk)
    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)

