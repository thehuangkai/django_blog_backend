from django.shortcuts import render
from .models import Portfolio
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PortfolioSerializer

@api_view(['GET'])
def portfolio_collection(request):
    if request.method == 'GET':
        portfolio = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolio, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def portfolio_detail(request, portfolio_slug):
    try:
        post = Portfolio.objects.get(intro=portfolio_slug)
    except Portfolio.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PortfolioSerializer(post)
        return Response(serializer.data)

class PortfolioCreate(generics.CreateAPIView):
    queryset = Portfolio.objects.all(),
    serializer_class = PortfolioSerializer