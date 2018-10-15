from django.contrib import admin

# Register your models here.
from api.models import IdentityCode, UserInfo, User

admin.site.register((IdentityCode, UserInfo, User))
