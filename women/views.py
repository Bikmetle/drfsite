from django.shortcuts import render
from rest_framework import generics
from .models import Women
from women.serializer import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all()
        return Response({'posts': WomenSerializer(lst, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_post = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': WomenSerializer(new_post).data})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
