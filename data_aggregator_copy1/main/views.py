from django.shortcuts import render
import requests
import yfinance as yf
from django.http import JsonResponse

from datetime import datetime
import time

# Create your views here.

def home(request):
    data = yf.download("AAPL", period="1d", interval="1m", progress=False)
    latest_time = data.index[-1]
    context = {"latest_time":latest_time}
    return render(request, "main/home.html", context)

def show_time(request):
    now = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    return JsonResponse({'time':now})

def show_price(request):
    data = yf.download("AAPL", period="1d", interval="1m", progress=False)
    latest_price = float(data['Close'].iloc[-1].item())
    return JsonResponse({'price':latest_price})

def latest_time(request):
    data = yf.download("AAPL", period="1d", interval="1m", progress=False)
    latest_time = data.index[-1]
    latest_time = latest_time.strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse({'latest_time':latest_time})
