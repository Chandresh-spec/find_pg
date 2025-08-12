from django.db import models
from django.utils import timezone
# Create your models here.
class PG_Owner(models.Model):
   
    owner_name=models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email=models.EmailField(max_length=150)

    def __str__(self):
        return f"{self.owner_name}"


class PG(models.Model):
    owner_name=models.ForeignKey(PG_Owner,on_delete=models.CASCADE,related_name='pgs')
    pg_name = models.CharField(max_length=100)
    address = models.TextField()
    landmarks=models.TextField(max_length=600)
    rooms_available = models.IntegerField()
    


    def __str__(self):
  
     return f"{self.pg_name}"
class AboutPg(models.Model):
    GENDER_CHOICES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('Unisex', 'Unisex'),
    ]
    OCCUPANCY_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
    ]

    food_choice=[
    ('veg','veg'),
    ('Non-veg','Non-veg'),
    ('both','both'),
    ('Wifi','Wifi'),
    ]
    
    


    pg=models.OneToOneField(PG,on_delete=models.CASCADE,related_name='about')
    occupancy=models.CharField(max_length=10,choices= OCCUPANCY_CHOICES )
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    food=models.CharField(choices=food_choice,default='Not availabel')
    AC=models.BooleanField(default=False)
    Power_Backup=models.BooleanField(default=False)
    Wifi=models.BooleanField(default=False)
    Attached_Washroom=models.BooleanField(default=False)
    Room_Cleaning=models.BooleanField(default=False)
    Laundry=models.BooleanField(default=False)
    warden=models.BooleanField(default=False)
    fridge=models.BooleanField(default=False)
    tv=models.BooleanField(default=False)
    food_charges=models.CharField(default='No charges')
    



    def __str__(self):
       return f"{self.pg}"


class PG_Image(models.Model):
    owner_name=models.ForeignKey(PG,on_delete=models.CASCADE,related_name='imgs')
    imgs=models.ImageField(upload_to='media/',null=True)



    def __str__(self):
       return f"{self.owner_name}"


class DeatilPage(models.Model):
   pg=models.OneToOneField(PG,on_delete=models.CASCADE,related_name='deatils')
   deposit_amount=models.DecimalField(max_digits=10,decimal_places=2)
   notice_period=models.IntegerField(default=0)
   parking=models.BooleanField(default=False)
   operating_since=models.IntegerField()
   def __str__(self):
      return f"{self.pg}"
 

class PGRules(models.Model):
   pg=models.OneToOneField(PG,on_delete=models.CASCADE,related_name='rules')
   visitor_entry=models.BooleanField(default=True)
   smoking=models.BooleanField(default=False)
   drinking=models.BooleanField(default=False)
   party=models.BooleanField(default=False)
   def __str__(self):
       return f"{self.pg}"
   


 


