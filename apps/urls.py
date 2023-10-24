from django.urls import path
from .views import InsurancePersonListCreate, InsurancePersonDetail, \
    InsuredFamilyMemberListCreate, InsuredFamilyMemberDetail

urlpatterns = [
    path('insurance-person/', InsurancePersonListCreate.as_view(), name='insurance-person-list'),
    path('insurance-person/<int:pk>/', InsurancePersonDetail.as_view(), name='insurance-person-detail'),
    path('insured-family-member/', InsuredFamilyMemberListCreate.as_view(), name='insured-family-list'),
    path('insured-family-member/<int:pk>/', InsuredFamilyMemberDetail.as_view(), name='insured-family-detail'),
]

