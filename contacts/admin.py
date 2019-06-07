from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    listing_display = ('id', 'name', 'listing', 'email', 'contact_date')
    listing_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)