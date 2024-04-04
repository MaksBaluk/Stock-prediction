import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import yfinance as yf
import datetime
from .stocks import Stock


@api_view(['GET'])
def get_stocks_info(request, symbol):
    try:
        stock_info = yf.Ticker(symbol.upper()).info
        if stock_info['trailingPegRatio'] is None:
            return Response({'error': 'Stock symbol not found'}, status=400)
        else:
            return Response(stock_info, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['Get'])
def get_stocks_price_now(request, symbol):
    try:
        stock_info = yf.Ticker(symbol.upper()).info
        if stock_info['trailingPegRatio'] is None:
            return Response({'error': 'Stock symbol not found'}, status=400)
        else:
            return Response(stock_info['currentPrice'], status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def get_stocks_price(request, symbol):
    try:
        interval_mapping = {
            '': {'period': '1y', 'interval': '1d'},
            '1d': {'period': '1d', 'interval': '5m'},
            '5d': {'period': '5d', 'interval': '30m'},
            '1mo': {'period': '1mo', 'interval': '1d'},
            '1y': {'period': '1y', 'interval': '1d'},
            '5y': {'period': '5y', 'interval': '1wk'},
            'max': {'period': 'max', 'interval': '1wk'},
        }

        interval = request.query_params.get('interval', '1y')
        interval_params = interval_mapping.get(interval)

        if not interval_params:
            return Response({'error': 'Invalid interval provided'}, status=400)

        df = yf.download(symbol.upper(), period=interval_params['period'], interval=interval_params['interval'])
        df.index = df.index.strftime('%Y-%m-%d %H:%M:%S%z')
        data_dict = df.to_dict(orient='index')
        return Response(data_dict, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
