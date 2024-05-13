from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
import yfinance as yf
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


# Create your views here.


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserStocksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            df = yf.download(request.user.financials.companies, period='1y')
            df.index = df.index.strftime('%Y-%m-%d %H:%M:%S%z')  # Convert index to string format
            data_dict = df.to_dict(orient='index')

            # Convert keys from tuples to strings if necessary
            for date_key, value in data_dict.items():
                data_dict[date_key] = {str(k) if isinstance(k, tuple) else k: v for k, v in value.items()}

            return Response(data_dict, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
