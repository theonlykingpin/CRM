from django.contrib import admin
from .models import User,UserProfile , Agent, Lead, Category

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Agent)
admin.site.register(Lead)
