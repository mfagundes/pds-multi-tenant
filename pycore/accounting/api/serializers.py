from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from accounting.models import Vendor

class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'cnpj', 'corporate_name']
