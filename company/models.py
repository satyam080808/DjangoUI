from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class CompanyVarity(models.Model):
    COMPANY_TYPE_CHOICE = [
        ('EC', 'ECOMMERCE'),
        ('SU', 'STARTUP'),
        ('HW', 'HARDWARE'),
        ('SW', 'SOFTWARE'),

    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'company/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=COMPANY_TYPE_CHOICE)
    description = models.TextField(default='')



    def __str__(self):
        return self.name


# One to Many

class CompanyReview(models.Model):
    company = models.ForeignKey(CompanyVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.company.name}'

# Many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company_varieties = models.ManyToManyField(CompanyVarity, related_name='stores')

    def __str__(self):
        return self.name

class CompanyCertificate(models.Model):
    company = models.OneToOneField(CompanyVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.company}'
    