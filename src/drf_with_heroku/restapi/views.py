from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

from django.http import Http404

from .models import Bank_Details
from .serializers import Bank_Details_serializer


# Create your views here.
class bdDetails(generics.ListAPIView):
    serializer_class = Bank_Details_serializer

    def get_queryset(self):
        queryset = Bank_Details.objects.all()
        Ifsc = self.request.query_params.get('ifsc','')

        if Ifsc:
            return queryset.filter(ifsc=Ifsc)
        return queryset


class BankDetailsFilter(filters.FilterSet):
    city = filters.CharFilter('city')
    bank_name = filters.CharFilter('bankname')
    class Meta:
        model = Bank_Details
        fields =('city','bank_name')

class BankDetailsListView(generics.ListAPIView):
    serializer_class = Bank_Details_serializer
    queryset = Bank_Details.objects.all()

    filter_backends =(DjangoFilterBackend,SearchFilter)
    filter_class = BankDetailsFilter
    search_fields=('city','bank_name')
