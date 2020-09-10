from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class TypePageList(APIView):
    def get(self, request):
        type = TypePage.objects.all()
        serializer = TypePageListSerializer(type, many=True)
        return Response(serializer.data)


class PageDetail(APIView):
    def get(self, request, pk):
        page = Page.objects.get(id=pk)
        serializer = PageDetailSerializer(page)
        return Response(serializer.data)


class PageList(APIView):
    def get(self, request):
        pageList = Page.objects.all()
        serializer = PageListSerializer(pageList, many=True)
        return Response(serializer.data)