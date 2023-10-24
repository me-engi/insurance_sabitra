from rest_framework import generics, permissions
from .models import InsurancePerson, InsuredFamilyMember
from .serializers import InsurancePersonSerializer, InsuredFamilyMemberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Q

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class InsurancePersonListCreate(generics.ListCreateAPIView):
    queryset = InsurancePerson.objects.all()
    serializer_class = InsurancePersonSerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return InsurancePerson.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(insured_family_members__name__icontains=query) |  # Search in family member names
            Q(insured_family_members__relationship__icontains=query)  # Search in family member relationships
        ).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class InsurancePersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsurancePerson.objects.all()
    serializer_class = InsurancePersonSerializer

class InsuredFamilyMemberListCreate(generics.ListCreateAPIView):
    queryset = InsuredFamilyMember.objects.all()
    serializer_class = InsuredFamilyMemberSerializer

class InsuredFamilyMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsuredFamilyMember.objects.all()
    serializer_class = InsuredFamilyMemberSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def your_api_view(request):
    if request.method == 'GET':
        try:
            # Example: Retrieve data from the database
            retrieved_data = InsurancePerson.objects.all()

            # Serialize the retrieved data
            serializer = InsurancePersonSerializer(retrieved_data, many=True)

            data = {
                "message": "GET request is working",
                "retrieved_data": serializer.data,
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred while retrieving data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)