from django.db import models

# Create youfrom django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True) 
    

    def __str__(self):
        return self.name
