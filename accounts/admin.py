from django.contrib import admin
from  .models import Account

from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display =  ('email','first_name','last_name','username','last_login',
                     'date_joined','is_active')
    list_display_links = ('email','first_name','last_name') # to make clickable
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)


    filter_horizontal = () # since we are using custom user also for hashing password in admin.
    list_filter = ()        # since we are using custom user also for hashing password in admin.
    fieldsets = ()      # since we are using custom user  also for hashing password in admin.


admin.site.register(Account,AccountAdmin)