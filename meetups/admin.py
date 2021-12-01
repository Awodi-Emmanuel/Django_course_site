from django.contrib import admin

from .models import  Location, Meetups, Participant

# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', 'location',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetups, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
