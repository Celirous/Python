print('\n') 

from django.db import models


# Create your models here.


class Topic(models.Model):
    """A Topic the user is leanring about."""
    text = models.CharField(max_length=200) #CharField means character field, "text box". We are setting 200 because these are titles, not body of info
    date_added = models.DateTimeField(auto_now_add=True) #auto_now_add means that we are adding this NOW when we make this, it will store the data till we use it, the data it is storing is DateimeField

    def __str__(self):
        """Return a String representation of the model."""
        return self.text 
    
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #ForeignKey is a reference to another record in the database. on_delete=models.CASCADE tells Django when i delete something, it should delete all info related to it
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta: #this class will be holding extra information for us
        verbose_name_plural = 'entries'


    def __str__(self): #the __str__ here tells Django which info i needs to show when refering to individual entries
        """Retrun a simple string prepresenting the entry you make"""
        return f"{self.text[:50]}..."
    