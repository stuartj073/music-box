from django.contrib import admin
from .models import Topic, Blog, Comments

# Register your models here.


admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(Comments)
