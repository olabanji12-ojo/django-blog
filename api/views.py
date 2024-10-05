from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializers import PersonSerializer, MessageSerializer
from appblog.models import Person, Message
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def first_api(request):
    if request.method == 'GET':
        task = Person.objects.all()
    
        serializer = PersonSerializer(task, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        task = Person.objects.create(
            name = request.data['name'],
            description = request.data['description'],
            email = request.data['email']
            
        )
        serializer = PersonSerializer(task, many=False)
        return Response(serializer.data)
        

@api_view(['GET', 'PUT', 'DELETE'])
def index_api(request, id):
    task = Person.objects.get(id=id)
    if request.method == 'GET':
        # task = Person.objects.get(id=id)
        serializer = PersonSerializer(task, many=False)
        
        return Response(serializer.data)
    if request.method == 'PUT':
        task.name = request.data['name']
        task.description = request.data['description']
        task.email = request.data['email']
        
        task.save()
        serializer = PersonSerializer(task, many=False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        task.delete()
        serializer = PersonSerializer(task, many=False)
        return HttpResponse('user was deleted')
        
        
        
        