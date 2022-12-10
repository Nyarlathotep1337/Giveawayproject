from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)


class Institution(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    TYPE = [
        ('fundacja', 'fundacja'),
        ('organizacja pozarzádowa', 'organizacja pozarzádowa'),
        ('zbiórka lokalna', 'zbiórka lokalna'),
    ]
    type = models.CharField(max_length=40, choices=TYPE, null=True, blank=True, help_text='What type of organization?',
                            default='fundacja')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.type}'

    # def __unicode__(self):
    #     return u'%s' % self.name % self.description % self.type


class Donation(models.Model):
    quantity = models.IntegerField(null=True)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.TimeField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bags = models.IntegerField(default=0)
    current = models.BooleanField(default=True)
