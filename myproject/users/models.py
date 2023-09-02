from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     # Add any additional fields or methods as needed

# class CustomUserGroup(Group):
#     class Meta:
#         proxy = True
#         auto_created = True
#         app_label = 'auth'
#         verbose_name = 'group'

#     def __str__(self):
#         return self.name

# class CustomUserPermission(Permission):
#     class Meta:
#         proxy = True
#         auto_created = True
#         app_label = 'auth'
#         verbose_name = 'permission'

#     def __str__(self):
#         return self.name


