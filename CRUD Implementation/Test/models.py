from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s'%(self.name, self.email, self.gender)
