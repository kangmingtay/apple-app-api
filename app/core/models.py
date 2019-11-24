from django.db import models

class Pdu(models.Model):
    BRAND_CHOICES = [
        ('apc', 'APC'),
        ('cyberpower', 'Cyberpower'),
        ('hp', 'HP'),
        ('tripp_lite', 'Tripp Lite'),
    ]
    capacity = models.IntegerField()
    num_outlets = models.IntegerField()
    brand = models.CharField(default='test', max_length=30, choices=BRAND_CHOICES)

    def __str__(self):
        return self.brand

class Rack(models.Model):
    LOCATION_CHOICES = [
        ('N', 'North'),
        ('S', 'South'),
        ('W', 'West'),
        ('E', 'East'),
    ]
    HEIGHT_CHOICES = [
        (1, '1.0m'),
        (2, '2.0m'),
        (3, '3.0m'),
        (4, '4.0m'),
        (5, '5.0m'),
    ]

    height = models.PositiveIntegerField(null=False, choices=HEIGHT_CHOICES)
    location = models.CharField(max_length=200, null=False, choices=LOCATION_CHOICES)
    color = models.CharField(max_length=60)
    pdus = models.ForeignKey(
        Pdu,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.location + str(self.id)