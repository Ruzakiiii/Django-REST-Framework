from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import Womenserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

class WomenAPI(APIView):
    def get(self, request):
        lst = Women.objects.all().values()

        return Response({'posts': list(lst)})

    def post(self, request):
        pos_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': model_to_dict(pos_new)})


# class WomenAPI(generics.ListAPIView):
#     queryset = Women.objects.all()
#
#     serializer_class = Womenserializer
