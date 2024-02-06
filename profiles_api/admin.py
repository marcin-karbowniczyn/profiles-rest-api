from django.contrib import admin
from . import models

# By default, the Django Admin is enabled ion all new project,
# however we need to register any newly created models with the Django admin, so it knows that I want to display that model in the admin UI.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
