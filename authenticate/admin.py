from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from .forms import GroupAdminForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'phone', 'categoria', 'genero', 'is_active',)
    list_filter = ('email', 'is_staff', 'categoria', 'genero', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'categoria', 'genero', 'password',
                           'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1',
                       'password2', 'categoria', 'genero', 'phone', 'is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions']
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, CustomUserAdmin)
