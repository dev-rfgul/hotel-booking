from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField() 
    Image = models.ImageField(upload_to='items/')
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)  

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Ratings = models.IntegerField()
    Image = models.ImageField(upload_to='items/', blank=True)

    def __str__(self):
        return self.User_name

class BookTable(models.Model):
    Name = models.CharField(max_length=15)   
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_data = models.DateField()

    def __str__(self):
        return self.Name
    
class SignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name    