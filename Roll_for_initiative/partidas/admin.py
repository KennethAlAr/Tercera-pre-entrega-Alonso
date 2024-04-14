from django.contrib import admin

from .models import Sistema, Juego, Reserva

# Register your models here.

admin.site.register(Sistema)
admin.site.register(Juego)
admin.site.register(Reserva)
