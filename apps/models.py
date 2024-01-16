from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE
from django_resized import ResizedImageField


class User(AbstractUser):
    image = ResizedImageField(size=[90, 90], crop=['middle', 'center'], upload_to='users/images',
                              default='users/default.png')


class CategoryView(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class UserView(Model):
    name = CharField(max_length=255)
    category = ForeignKey('apps.CategoryView', CASCADE)
    description = CharField(max_length=255)
    image = ImageField(upload_to='users/images/')
