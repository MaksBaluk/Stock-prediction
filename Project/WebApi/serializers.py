from rest_framework import serializers

from .models import Company, FinancialInfo


class FinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInfo
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    financial_info = FinancialInfoSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Переміщуємо financial_info в кінець словника
        if 'financial_info' in data:
            financial_info = data.pop('financial_info')
            data['financial_info'] = financial_info
        return data
