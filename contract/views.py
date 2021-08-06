# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contract
from .serializers import ContractSerializer
import random
# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomContract(request, id):
    totalContracts = Contract.objects.all()
    randomContracts = random.sample(list(totalContracts), id)
    serializer = ContractSerializer(randomContracts, many = True) #many = True옵션을 넣으면 다수의 데이터에 대해서도 직렬화가 진행
    return Response(serializer.data)