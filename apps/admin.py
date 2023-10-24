from django.contrib import admin
from .models import InsurancePerson, InsuredFamilyMember

@admin.register(InsurancePerson)
class InsurancePersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_no', 'amount_paid')
    list_filter = ('amount_paid',)  # Add any additional fields you want to filter by
    search_fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone_no')  # Include fields from InsurancePerson
    list_per_page = 20  # Adjust the number of items per page as needed

@admin.register(InsuredFamilyMember)
class InsuredFamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationship', 'insurance_person')
    list_filter = ('relationship',)  # Add any additional fields you want to filter by
    search_fields = ('name', 'relationship', 'insurance_person__first_name', 'insurance_person__middle_name', 'insurance_person__last_name')  # Include fields from InsurancePerson
