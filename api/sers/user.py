#!/usr/bin/env python
# encoding:utf-8
# Created by Andy @ 2020/8/24


from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import UserProfile


class UserSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    avatar = serializers.ImageField(required=False)
    gender = serializers.CharField(source="get_gender_display")
    phone = serializers.CharField(required=False)
    status = serializers.CharField(source="get_status_display")

    def to_internal_value(self, data):
        # 对传进来的数据进行处理，比如如果状态传入的是中文，在这里转化成1或者0存入数据库
        user = data.get('user')
        user_obj = User.objects.filter(username=user).first()
        data['user'] = user_obj
        if not data.get('avatar'):
            data['avatar'] = "/media/avatar/default_male_avatar.png"
        return data

    def to_representation(self, instance):
        # 对允许为空的字段进行处理

        if not instance.avatar:
            instance.avatar = ""

        if not instance.phone:
            instance.phone = "未绑定"

        return super().to_representation(instance)

    def create(self, validated_data):
        user_name = validated_data.get('user')
        user = User.objects.filter(username=user_name).first()
        avatar = validated_data.get('avatar')
        gender = validated_data.get('gender')
        phone = validated_data.get('phone')
        status = validated_data.get('status')
        return UserProfile.objects.create(
            user=user,
            avatar=avatar,
            gender=gender,
            phone=phone,
            status=status
        )

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
