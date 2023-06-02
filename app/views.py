from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework import status
class ProductCrud(APIView):
    def get(self,request,pid):
        PQS=Product.objects.filter(product_id=pid)
        #PQS=Product.objects.all()
        PSO=ProductSerializer(PQS,many=True)
        return Response(PSO.data)
    def post(self,request,pid):
        PSO=ProductSerializer(data=request.data)
        if PSO.is_valid():
            PS=PSO.save()
            return Response({'success':'product "{}" is created.'.format(PS.product_name)})
        return Response({'failure':'Not Done'})
    def put(self,request,pid):
        PQO=Product.objects.get(product_id=pid)
        PSO=ProductSerializer(PQO,data=request.data)
        if PSO.is_valid():
            PS=PSO.save()
            return Response({'success':'product "{}" is Updated.'.format(PS.product_name)})
        return Response({'failure':'Not Done'})
    def patch(self,request,pid):
        data=request.data
        PQO=Product.objects.get(product_id=pid)
        PQO.product_name=data.get('product_name')
        PQO.save()
        return Response({'Success':'Partial Update is Done'})
    def delete(self,request,pid):
        PQO=Product.objects.filter(product_id=pid).delete()
        return Response(status=status.HTTP_200_OK)
    
    
    

