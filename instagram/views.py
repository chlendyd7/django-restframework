from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.decorators import api_view, action


# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         queryset = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def public_post_list(request):
#     queryset = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data)


class PostListAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
       return Post.objects.all()


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    def get_serializer_class(self):
        return PostSerializer
    
    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True) #자동으로 serializer 찾아 만들어줌
        return Response(serializer.data)
    
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance) #자동으로 serializer 찾아 만들어줌
        return Response(serializer.data)

#     def dispatch(self, request, *args, **kwargs): #실제 요청이 올 떄 마다 호출되는 함수
#         print('request.body:', request.body) # print 비추천, logger 추천
#         print('request.POST:', request.POST) # print 비추천, logger 추천
#         return super().dispatch(request, *args, **kwargs)
