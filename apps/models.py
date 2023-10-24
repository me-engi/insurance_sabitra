from django.db import models
from datetime import datetime


class InsurancePerson(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    address = models.TextField()
    citizenship_image = models.ImageField(upload_to='citizenship/')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    insured_person_image = models.ImageField(upload_to='insured_person/', blank=True, null=True)
    date_of_insurance = models.DateField(default="2023-10-20")
    date_of_birth = models.DateField(null=True)  # Add date of birth field
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    
    


    

    def __str__(self):
        # Construct a full name from the first_name, middle_name, and last_name fields
        full_name = self.first_name
        if self.middle_name:
            full_name += ' ' + self.middle_name
        full_name += ' ' + self.last_name
        return full_name

class InsuredFamilyMember(models.Model):
    insurance_person = models.ForeignKey(InsurancePerson, on_delete=models.CASCADE, related_name='insured_family_members')
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    family_member_image = models.ImageField(upload_to='insured_family_member/', blank=True, null=True)
    date_of_birth = models.DateField(default=datetime.now)  # Add date of birth field
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])


    def __str__(self):
        return self.name
