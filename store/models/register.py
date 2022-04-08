import email
from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    @staticmethod

    def isExists(email_id):
        if email_id:
            return Register.objects.filter(email = email_id)
        return False

    def get_email_by_id(email_id):
        try:
            return Register.objects.get(email = email_id)
        except:
            return False