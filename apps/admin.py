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

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "admin/change_list.html"
    list_display = ['id', 'title']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            next(reader)
            result = []
            for row in reader:
                result.append(Product(
                    pk=int(row[0]),
                    title=row[1],
                    image=row[2],
                    description=row[3],
                    quantity=row[4],
                    price=row[5]
                ))

            Product.objects.bulk_create(result)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "csv_form.html", payload)
@admin.register(CategoryView)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserView)
class UserAdmin(admin.ModelAdmin):
    pass
