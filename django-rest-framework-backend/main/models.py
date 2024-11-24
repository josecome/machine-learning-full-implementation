from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)
    
    class Meta:  
        db_table = "persons"


class Preference(models.Model):
    id = models.AutoField(primary_key=True)
    sepal_length = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sepal_width	= models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    petal_length = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    petal_width = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sel_variety = models.CharField(max_length=20, null=True)
    pred_variety = models.CharField(max_length=20, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_created = models.DateField(null=True)
    date_updated = models.DateField(null=True)

    class Meta:  
        db_table = "preferences"
