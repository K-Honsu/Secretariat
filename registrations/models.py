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
    Parents_Name = models.CharField(max_length=500)
    home_address = models.CharField(max_length=500, null=True)
    contact_number = models.CharField(max_length=90, null=True)
    delivery_date = models.CharField(max_length=150, null=True)
    date_of_naming_ceremony = models.CharField(max_length=250, null=True)
    place_of_naming_ceremony = models.CharField(max_length=450, null=True)
    father_Band_Name = models.CharField(max_length=20, choices=MALE_BAND_CHOICES, default='SM')
    mother_Band_Name = models.CharField(max_length=20, choices=FEMALE_BAND_CHOICES, default='RH')
    father_unit_name = models.CharField(max_length=90, null=True)
    mother_unit_name = models.CharField(max_length=90, null=True)
    
    
    def __str__(self):
        return f"{self.Parents_Name} Birth Notification"
    
    
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
    Parent_Name = models.CharField(max_length=500)
    child_First_Name = models.CharField(max_length=200)
    father_Band_Name = models.CharField(max_length=20, choices=MALE_BAND_CHOICES, default='SM')
    mother_Band_Name = models.CharField(max_length=20, choices=FEMALE_BAND_CHOICES, default='RH')
    father_unit_name = models.CharField(max_length=90, null=True)
    mother_unit_name = models.CharField(max_length=90, null=True)
    # date_of_dedication = models.CharField(auto_created=True ,max_length=100, null=True)
    
    
    def __str__(self):
        return f"{self.child_First_Name} Child Dedication"
