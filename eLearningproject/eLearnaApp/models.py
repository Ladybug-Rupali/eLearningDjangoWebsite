from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    subject = models.CharField(max_length=100,null=False,blank=False)
    message = models.CharField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return self.name
    
    



class EmailInput(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email