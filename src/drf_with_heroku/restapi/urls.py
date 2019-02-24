from django.urls import path
from restapi.views import *
urlpatterns = [
    path('getwithifsc/', bdDetails.as_view()),
    path('getwithid/', BankDetailsListView.as_view())
]
