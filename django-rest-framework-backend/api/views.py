from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from serializers import (
    PersonSerializer,
    PreferenceSerializer,
)

class SnippetList(APIView):
    def post(self, request, format=None):
        server_data = {'user': request.user.id, 'date_created': datetime.now(), 'date_updated': datetime.now()}
        person_data = request.data

        person_serializer = PersonSerializer(data = { **server_data, **person_data})
        if person_serializer.is_valid():
            person_serializer.save()

            preference_data = request.data
            preference_serializer = PreferenceSerializer(data = { **server_data, **preference_data})
            preference_serializer.save()
            result = ""
            return Response(result, status=status.HTTP_201_CREATED)
        
        error = ""
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
