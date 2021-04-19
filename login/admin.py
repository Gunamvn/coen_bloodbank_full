from django.contrib import admin
from .models import bbank
from .models import donarreg

# Create Request Model Admin Rights
class Bbank_Admin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(bbank, Bbank_Admin)

# Donar Registration Model Admin Rights
class Dreg_Admin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(donarreg, Dreg_Admin)
