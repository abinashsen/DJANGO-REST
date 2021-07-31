from .models import StudentsModel
from rest_framework import serializers
# from .validator import ApiValidations


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = '__all__'

    # custom_api_validation = ApiValidations(request.data)
