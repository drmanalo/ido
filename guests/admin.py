from django.contrib import admin
from .models import Guest, Party

class GuestInline(admin.TabularInline):
    model = Guest
    fields = ('first_name', 'last_name', 'email', 'is_attending', 'meal', 'is_child')
    readonly_fields = ('first_name', 'last_name', 'email')

class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'party', 'email', 'is_attending', 'is_child', 'meal')
    list_filter = ('is_attending', 'is_child', 'meal', 'party__is_invited')

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'save_the_date_sent', 'invitation_sent', 'invitation_opened', 'is_invited', 'is_attending')
    list_filter = ('category', 'is_invited', 'is_attending', 'invitation_opened')
    inlines = [GuestInline]

admin.site.register(Guest, GuestAdmin)
admin.site.register(Party, PartyAdmin)