from django.db import models

# Create your models here.
class Bank_Details(models.Model):
    """ this is an model for bank Bank_Details """
    ifsc = models.CharField(max_length=255)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)

    def get_ifsc(self):
        return self.ifsc
