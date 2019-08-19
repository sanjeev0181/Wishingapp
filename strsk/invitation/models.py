from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    king = models.CharField(max_length=50,default="King")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image1 = models.ImageField(default='default.jpg', upload_to='profile1_pics')
    queen = models.CharField(max_length=50,default="Queen")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)
        img1 = Image.open(self.image1.path)
        if((img.height and img1.height ) > (300 or img.width and img1.width > 300)):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img1.thumbnail(output_size)
            img.save(self.image.path)
            img1.save(self.image1.path)


class Birthday(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    queen = models.CharField(max_length=50,default="Queen")
    image = models.ImageField(default='default.jpg', upload_to='birth_profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Birthday,self).save(*args,**kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

   