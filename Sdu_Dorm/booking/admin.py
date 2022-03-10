from django.contrib import admin
from .models import Users, Block, Floor, Room
# Register your models here.

admin.site.register(Users)
admin.site.register(Block)
admin.site.register(Floor)
admin.site.register(Room)
