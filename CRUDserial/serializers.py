from .models import Student,School
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields="__all__"