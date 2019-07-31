from django.db import models

# Create your models here.


class HomePage(models.Model):
    odd1 = models.CharField(max_length=4, help_text='Home odd')
    odd2 = models.CharField(max_length=4, help_text='Draw odd')
    odd3 = models.CharField(max_length=4, help_text='Away odd')

    class Meta:
        db_table = 'odds'
