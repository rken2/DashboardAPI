from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
@api_view(['GET'])
def getEmployees(request):
    data = {}
    try:
        instance = Employee.objects.all()
    except:
        data["error"] = "Employees not found"
        return Response(data)

    if instance:
        # Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
        # that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
        # allowing parsed data to be converted back into complex types, after first validating the incoming data.
        data = EmployeeSerializer(instance, many=True).data

    # Response takes a Python data type and converts it to a byte string JSON response or whatever response type you need
    return Response(data)

@api_view(['GET'])
def getEmployee(request, pk):
    data = {}
    try:
        instance = Employee.objects.get(id=pk)
    except:
        data["error"] = "Employee not found"
        return Response(data)

    if instance:
        data = EmployeeSerializer(instance).data

    return Response(data)

@swagger_auto_schema(method='post', request_body=EmployeeSerializer)
@api_view(['POST'])
def createEmployee(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=EmployeeSerializer)
@api_view(['PUT'])
def updateEmployee(request, pk):
    body = request.data
    data = []

    try:
        instance = Employee.objects.get(id=pk)
    except:
        data["error"] = "Employee not found"
        return Response(data)
    
    serializer = EmployeeSerializer(instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteEmployee(request, pk):
    data = {}

    try:
        instance = Employee.objects.get(id=pk)
    except:
        data["error"] = "Employee not found"
        return Response(data)

    if instance:
        instance.delete()
        data["success"] = "Employee deleted"

    return Response(data)