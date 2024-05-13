from rest_framework import serializers

from .models import User, UsersFinancials


class UserFinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersFinancials
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    financials = UserFinancialSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'financials' in data:
            financials = data.pop('financials')
            data['financials'] = financials
        return data
