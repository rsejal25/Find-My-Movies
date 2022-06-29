from django.contrib import admin
from .models import Logging_User,Play_List,Movies,PlayList_Movie
# Register your models here.

admin.site.register(Logging_User)
admin.site.register(Play_List)
admin.site.register(Movies)
admin.site.register(PlayList_Movie)
