#!/usr/bin/env python
# encoding:utf-8
# Created by Andy @ 2020/8/24

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UserProfile
from api.sers.user import UserSerializer


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            user = UserProfile.objects.filter(pk=pk).first()
            ser = UserSerializer(instance=user, many=False)
            return Response(status=status.HTTP_200_OK, data=ser.data)

        queryset = UserProfile.objects.all()
        ser = UserSerializer(instance=queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=ser.data)

    def post(self, request, *args, **kwargs):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_200_OK, data=ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=ser.errors)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserProfile.objects.filter(pk=pk).first()
        ser = UserSerializer(instance=user, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_200_OK, data=ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=ser.errors)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserProfile.objects.filter(pk=pk).first()
        ser = UserSerializer(instance=user, data=request.data, partial=True)  # 如果不指定partial 会验证所有字段
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_200_OK, data=ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=ser.errors)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserProfile.objects.filter(pk=pk).first()
        user.status = '0'
        user.save()
        return Response(status=status.HTTP_200_OK, data={})
