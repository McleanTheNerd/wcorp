from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = ((1,'Male'),(2,'Female'))
CONTRACT = ((1,'pending'),(2,'active'))

class WCORP(AbstractUser):
    user_type_data = ((1,'cms'),(2,'admin'),(3,'client'))
    user_type = models.CharField(default=1,choices=user_type_data, max_length=50)

# Create your models here.
class SuperUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin = models.OneToOneField(WCORP, on_delete = models.CASCADE)
    cell = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "superuser"
        verbose_name_plural = "superusers"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("superuser_detail", kwargs={"pk": self.pk})




class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin = models.OneToOneField(WCORP, on_delete = models.CASCADE)
    cell = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    objects = models.Manager()
    
    class Meta:
        verbose_name = "admin"
        verbose_name_plural = "admin"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("admin_detail", kwargs={"pk": self.pk})

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin = models.OneToOneField(WCORP, on_delete = models.CASCADE)
    cell = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    objects = models.Manager()  

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})

#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in WCORP model

@receiver(post_save, sender=WCORP)
# Now Creating a Function which will automatically insert data in CMS, admin or client
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            SuperUser.objects.create(admin=instance,cell="")
        if instance.user_type == 2:
            Admin.objects.create(admin=instance, cell="")
        if instance.user_type == 3:
            Client.objects.create(admin=instance, cell="")
    

@receiver(post_save, sender=WCORP)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.superuser.save()
    if instance.user_type == 2:
        instance.admin.save()
    if instance.user_type == 3:
        instance.client.save()
