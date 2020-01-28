from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email',  'balance', 'email', 'currency', 'password',)
    list_filter = ('email', 'email', 'currency',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'who', 'whom', 'how')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Transaction, TransactionAdmin)
