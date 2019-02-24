from rest_framework import serializers
from .models import Bank_Details

class Bank_Details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Details
        fields = ('ifsc','bank_id','branch','address','city','district','state','bank_name')
