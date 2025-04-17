from django.shortcuts import render
import requests
import yfinance as yf
from django.http import JsonResponse
from twisted.python.rebuild import latestClass

from .forms import Show_stock, Stocks
from datetime import datetime
import time

# Create your views here
def home(request):
    stock_symbol = "BTC"
    if request.method == 'POST':
        form = Show_stock(request.POST)
        if form.is_valid():
            stock_symbol = form.cleaned_data['stock']
            # store data in session for other views to have access
            request.session['stock_symbol'] = stock_symbol
    else:
        form = Show_stock()

        if 'stock_symbol' in request.session:
            stock_symbol = request.session['stock_symbol']
    try:
        data = yf.download(stock_symbol, period="1d", interval="1m", progress=False)
        if not data.empty and len(data.index) > 0:

            latest_time = data.index[-1]
        else:
            latest_time = None
    except Exception:
        latest_time = None
    context = {
        "latest_time":latest_time,
               'form':form,
        "stock":stock_symbol,
    }
    return render(request, "main/home.html", context)

def show_time(request):
    now = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    return JsonResponse({'time':now})

def show_price(request):
    stock_symbol = request.session.get('stock_symbol', 'BTC')
    try:
        data = yf.download(stock_symbol, period="1d", interval="1m", progress=False)
        if not data.empty and len(data.index) > 0:
            latest_price = float(data['Close'].iloc[-1].item())
            return JsonResponse({"price": latest_price, "symbol":stock_symbol})
        else:
            return JsonResponse({"error":'No data available for '+ stock_symbol},status=404)
    except Exception as e:
        return JsonResponse({"error":str(e)}, status=404)

def latest_time(request):
    data = yf.download("AAPL", period="1d", interval="1m", progress=False)
    if not data.empty and len(data.index) > 0:
        latest_time = data.index[-1]
        latest_time = latest_time.strftime('%Y-%m-%d %H:%M:%S')
        return JsonResponse({'latest_time':latest_time})
    else:
        return JsonResponse({"error":"No stock data available at the moment"}, status=503)
