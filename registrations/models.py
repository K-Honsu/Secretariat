from django.db import models

# Create your models here.
class MarriageThanksgiving(models.Model):
    MALE_BAND_CHOICES = [
        ('NIL', 'NIL'),
        ('J', 'JOSEPH'),
        ('JE', 'JEREMIAH'),
        ('EP', 'EPHRAIM'),
        ('SM', 'ST.MARK'),
        ('SJ', 'ST.JOHN'),
        ('JA', 'JAMES'),
    ]
    FEMALE_BAND_CHOICES = [
        ('NIL', 'NIL'),
        ('RH', 'RHODA'),
        ('HZ', 'HEPZIBAH'),
        ('FT', 'FAITH'),
        ('SU', 'SUSANNAH'),
        ('JO', 'JOANA'),
        ('TD', 'TRUTH DIVINE'),
    ]
    family_name = models.CharField(max_length=1000)
    band_of_husband = models.CharField(max_length=350, choices=MALE_BAND_CHOICES, default='J')
    band_of_wife = models.CharField(max_length=350, choices=FEMALE_BAND_CHOICES, default='RH')
    date_of_marriage = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.family_name
    
    
class BirthNotification(models.Model):
    MALE_BAND_CHOICES = [
        ('NIL', 'NIL'),
        ('J', 'JOSEPH'),
        ('JE', 'JEREMIAH'),
        ('EP', 'EPHRAIM'),
        ('SM', 'ST.MARK'),
        ('SJ', 'ST.JOHN'),
        ('JA', 'JAMES'),
    ]
    FEMALE_BAND_CHOICES = [
        ('NIL', 'NIL'),
        ('RH', 'RHODA'),
        ('HZ', 'HEPZIBAH'),
        ('FT', 'FAITH'),
        ('SU', 'SUSANNAH'),
        ('JO', 'JOANA'),
        ('TD', 'TRUTH DIVINE'),
    ]
    family_name = models.CharField(max_length=500)
    child_first_name = models.CharField(max_length=200)
    child_middle_name = models.CharField(max_length=200, null=True, blank=True)
    child_last_name = models.CharField(max_length=200, null=True, blank=True)
    father_band_name = models.CharField(max_length=20, choices=MALE_BAND_CHOICES, default='SM')
    mother_band_name = models.CharField(max_length=20, choices=FEMALE_BAND_CHOICES, default='RH')
