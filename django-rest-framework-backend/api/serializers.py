from rest_framework import serializers
from main.models import (
    Person,
    Preference,
)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'created_date']

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ['person_id', 'sel_variety']