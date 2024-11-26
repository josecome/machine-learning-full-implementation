from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime
import requests
from .serializers import (
    PersonSerializer,
    PreferenceSerializer,
)

class ML():
    def predictedValue(preference_data):
        sepal_length = preference_data['sepal_length']
        sepal_width = preference_data['sepal_width']
        petal_length = preference_data['petal_length']
        petal_width = preference_data['petal_width']
        url = 'http://127.0.0.1:5000/api/ml_predict/'
        data = {'v1': sepal_length, 'v2': sepal_width, 'v3': petal_length, 'v4': petal_width}

        resp = requests.post(url, json = data)
        r = resp.content.decode("utf-8")
        return r

class ProcessRequest(APIView):
    def post(self, request, format=None):
        
        server_data = {'user': request.user.id, 'date_created': date.today(), 'date_updated': date.today()}
        data = request.data
        first_name, *last_name = data['full_name']
        person_data = dict()
        person_data['first_name'] = first_name
        person_data['last_name'] = " ".join(last_name)

        person_serializer = PersonSerializer(data = { **server_data, **person_data})
        if person_serializer.is_valid():
            person = person_serializer.save()
            preference_data = dict()
            preference_data['sepal_length'] = data['sepal_length']
            preference_data['sepal_width'] = data['sepal_width']
            preference_data['petal_length'] = data['petal_length']
            preference_data['petal_width'] = data['petal_width']
            
            
            result = ML.predictedValue(preference_data) # To see where is the error
            print('===Person id====')
            print(person.id)
            preference_data = dict()
            preference_data['person_id'] = person.id
            preference_data['sel_variety'] = data['sel_variety']
            preference_data['pred_variety'] = result
            preference_serializer = PreferenceSerializer(data = {'person_id': 64, 'sel_variety': 'Test'})
            #preference_serializer = PreferenceSerializer(data = { **preference_data, **server_data })
            if preference_serializer.is_valid():
                #if(1 == 1): return Response("Test6" + str(preference_serializer), status=status.HTTP_201_CREATED)
                preference_serializer.save()
            
                return Response(result, status=status.HTTP_201_CREATED)
        
        error = "Error..."
        return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
