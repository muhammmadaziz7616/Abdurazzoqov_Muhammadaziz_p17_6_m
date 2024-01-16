from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from apps.models import CategoryView, UserView, User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('custom_image', "name", "category", "description")

    fieldsets = (
        (None, {"fields": ("description")}),
        (_("Personal info"), {"fields": ("name", "category", 'image')}),
        (
            _("Permissions"),
            {
                'fields': (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def custom_image(self, obj: User):
        return mark_safe('<img src="{}"/>'.format(obj.image.url))

    custom_image.short_description = "Image"


@admin.register(CategoryView)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserView)
class UserAdmin(admin.ModelAdmin):
    pass
