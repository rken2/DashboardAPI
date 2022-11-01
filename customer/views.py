from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
@api_view(['GET'])
def getCustomers(request):
    data = {}
    try:
        instance = Customer.objects.all()
    except:
        data["error"] = "Customers not found"
        return Response(data)

    if instance:
        # Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
        # that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
        # allowing parsed data to be converted back into complex types, after first validating the incoming data.
        data = CustomerSerializer(instance, many=True).data

    # Response takes a Python data type and converts it to a byte string JSON response or whatever response type you need
    return Response(data)

@api_view(['GET'])
def getCustomer(request, pk):
    data = {}
    try:
        instance = Customer.objects.get(id=pk)
    except:
        data["error"] = "Customer not found"
        return Response(data)

    if instance:
        data = CustomerSerializer(instance).data

    return Response(data)

@swagger_auto_schema(method='post', request_body=CustomerSerializer)
@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=CustomerSerializer)
@api_view(['PUT'])
def updateCustomer(request, pk):
    body = request.data
    data = []

    try:
        instance = Customer.objects.get(id=pk)
    except:
        data["error"] = "Customer not found"
        return Response(data)
    
    serializer = CustomerSerializer(instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteCustomer(request, pk):
    data = {}

    try:
        instance = Customer.objects.get(id=pk)
    except:
        data["error"] = "Customer not found"
        return Response(data)

    if instance:
        instance.delete()
        data["success"] = "Customer deleted"

    return Response(data)