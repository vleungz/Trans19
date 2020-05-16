from django.db import models


class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_id = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_case_confirmed = models.DateField()
    case_number = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.patient_name


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    DISTRICT_CHOICES = [
        ('Hong Kong Island', (
            ('Central and Western', 'Central and Western'),
            ('Eastern', 'Eastern'),
            ('Southern', 'Southern'),
            ('Wan Chai', 'Wan Chai'),
        )
         ),
        ('Kowloon', (
            ('Sham Shui Po', 'Sham Shui Po'),
            ('Kowloon City', 'Kowloon City'),
            ('Kwun Tong', 'Kwun Tong'),
            ('Wong Tai Sin', 'Wong Tai Sin'),
            ('Yau Tsim Mong', 'Yau Tsim Mong'),
        )
         ),
        ('New Teritories', (
            ('Islands', 'Islands'),
            ('Kwai Tsing', 'Kwai Tsing'),
            ('North', 'North'),
            ('Sai Kung', 'Sai Kung'),
            ('Sha Tin', 'Sha Tin'),
            ('Tai Po', 'Tai Po'),
            ('Tsuen Wan', 'Tsuen Wan'),
            ('Tuen Mun', 'Tuen Mun'),
            ('Yuen Long', 'Yuen Long'),
        )
         ),
    ]
    district = models.CharField(max_length=200, choices=DISTRICT_CHOICES)
    address = models.CharField(max_length=200)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()

    def __str__(self):
        return self.location_name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    detail = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.location.location_name
