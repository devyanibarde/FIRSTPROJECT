from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.first_name

class Contact(models.Model):
    pid = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=100)
    email_id = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.pid

class Address(models.Model):
    pid = models.ForeignKey(Person, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.pid