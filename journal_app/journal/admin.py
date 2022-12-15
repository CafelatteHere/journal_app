from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.header = "Journal app"
admin.site.site_title = "Journal app"
admin.site.index_title = "Manage Journal app"

admin.site.register(Post)
