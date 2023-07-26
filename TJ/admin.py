from django.contrib import admin
from .models import User, Journal, Entry

# Register your models here.
admin.site.register(User)
admin.site.register(Journal)
admin.site.register(Entry)