from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ChildSerializers, BirthNotificationSerializers, MarriageThanksGivingSerializers
from registrations.models import ChildDedication, BirthNotification, MarriageThanksgiving


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects/'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        {'POST': '/api/user/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getChildRegistrations(request):
    childs = ChildDedication.objects.all()
    serializer = ChildSerializers(childs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getChildRegistration(request, pk):
    child = ChildDedication.objects.get(id=pk)
    serializer = ChildSerializers(child, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getBirthNotifications(request):
    birth = BirthNotification.objects.all()
    serializer = BirthNotificationSerializers(birth, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBirthNotification(request, pk):
    birth = BirthNotification.objects.get(id=pk)
    serializer = BirthNotificationSerializers(birth, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getMarriageThanksgivings(request):
    marriage = MarriageThanksgiving.objects.all()
    serializer = MarriageThanksGivingSerializers(marriage, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMarriageThanksgiving(request, pk):
    marriage = MarriageThanksgiving.objects.get(id=pk)
    serializer = MarriageThanksGivingSerializers(marriage, many=False)
    return Response(serializer.data)
    