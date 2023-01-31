from django.db import models
from django.contrib.auth.models import User

#class Profile(models.Model) :
    # profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    #Picture_Picture = models.ImageField(upload_to='Images/profile', null=True)
    #contact_num = models.CharField(max_length=200, blank=True, null=True)
    #address = models.CharField(max_length=200, blank=True, null=True)

    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.user.username
    
class Profile(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    Picture_Picture = models.ImageField(upload_to='Images/profile',blank=True,null=True)
    Phone = models.IntegerField(null=True,blank=True)


    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username