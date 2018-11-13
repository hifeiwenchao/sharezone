from rest_framework import serializers
from api.models import User, UserInfo, Share, Category, Demand, DepositPool, OrderInfo, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'email', 'is_email_verified', 'robot', 'status', 'created_at')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'
        # exclude = ('geotable_id',)



