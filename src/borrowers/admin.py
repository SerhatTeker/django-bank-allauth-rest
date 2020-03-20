from django.contrib import admin

from .models import Borrower, Invoice


admin.site.register(Borrower)
admin.site.register(Invoice)
