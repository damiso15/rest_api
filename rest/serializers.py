from rest_framework import serializers
from .models import Employees


class EmployeesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employees
        # fields = ('first_name', 'last_name')
        fields = '__all__'
