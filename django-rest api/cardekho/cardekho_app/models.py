from django.db import models


def alphanumeric(value):
    if not str(value).isalnum:
        raise serializers.ValidationError('only alphanumeric characters are allowed ')


class showroomlist(models.Model)
class carlist(models.Model):
    name= models.CharField(max_length=50)
    active= models.BooleanField(default=False)
    description= models.CharField( max_length=50, blank=True, null=True)
    price=models.DecimalField(max_digits=9, decimal_places=2, default=1000)
    chasisnum=models.CharField( max_length= 50  ,blank=True,validators=[alphanumeric])
    