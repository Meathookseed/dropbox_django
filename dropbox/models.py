from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import FileExtensionValidator
# from dropbox.validators import image_validation,file_size_validator


class Profile(User):
    image = models.ImageField(upload_to='image/%Y/%m/%d/',
                              blank=True,
                              )
    profile_site = models.CharField(max_length=100,
                                    blank=True)
    about_profile = models.TextField(blank=True)



class Vault(models.Model):
    owner = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='vault')
    title = models.CharField(max_length=50,
                             unique=True)
    description = models.TextField()
    volume = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class File(models.Model):
    vault = models.ForeignKey(to=Vault,
                              on_delete=models.CASCADE,
                              related_name='file')
    description = models.TextField()
    document = models.FileField(upload_to='documents/%Y/%m/%d/',blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.document.name.split('/')[-1])


