from django.contrib import admin
from dropbox.models import Profile,Vault,File
# Register your models here.
admin.site.register([Profile, Vault, File])