from django.contrib import admin

from .models import User, UsersFinancials


class UsersFinancialsInline(admin.StackedInline):
    model = UsersFinancials
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User

    inlines = [UsersFinancialsInline]

