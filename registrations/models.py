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
    father_unit_name = models.CharField(max_length=90, null=True)
    mother_unit_name = models.CharField(max_length=90, null=True)
    
    
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
    family_Name = models.CharField(max_length=500)
    child_First_Name = models.CharField(max_length=200)
    child_Middle_Name = models.CharField(max_length=200, null=True, blank=True)
    child_Last_Name = models.CharField(max_length=200)
    father_Band_Name = models.CharField(max_length=20, choices=MALE_BAND_CHOICES, default='SM')
    mother_Band_Name = models.CharField(max_length=20, choices=FEMALE_BAND_CHOICES, default='RH')
    father_unit_name = models.CharField(max_length=90, null=True)
    mother_unit_name = models.CharField(max_length=90, null=True)
    
    
    def __str__(self):
        return f"{self.child_First_Name} {self.child_Last_Name}"
    
    
class ChildDedication(models.Model):
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
    family_Name = models.CharField(max_length=500)
    child_First_Name = models.CharField(max_length=200)
    child_Middle_Name = models.CharField(max_length=200, null=True, blank=True)
    child_Last_Name = models.CharField(max_length=200)
    father_Band_Name = models.CharField(max_length=20, choices=MALE_BAND_CHOICES, default='SM')
    mother_Band_Name = models.CharField(max_length=20, choices=FEMALE_BAND_CHOICES, default='RH')
    father_unit_name = models.CharField(max_length=90, null=True)
    mother_unit_name = models.CharField(max_length=90, null=True)
    def __str__(self):
        return f"{self.child_First_Name} {self.child_Last_Name}"
