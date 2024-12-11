from django.contrib import admin
from premium.models import PremiumCode

class PremiumCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'expiry_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('code',)

admin.site.register(PremiumCode, PremiumCodeAdmin)
