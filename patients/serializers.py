from rest_framework import serializers
from .models import Patient
class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = ('id', 'first_name', 'last_name', 'sex_at_birth', 'birth_date', 'email', 'notes')