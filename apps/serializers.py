from rest_framework import serializers
from .models import InsurancePerson, InsuredFamilyMember
from django.http import JsonResponse


class InsurancePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePerson
        fields = '__all__'

class InsuredFamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredFamilyMember
        fields = '__all__'

class InsurancePersonSerializer(serializers.ModelSerializer):
    family_members = InsuredFamilyMemberSerializer(many=True, read_only=True)

    class Meta:
        model = InsurancePerson
        fields = '__all__'