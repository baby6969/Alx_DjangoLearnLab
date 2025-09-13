from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'bookshelf':
        Book = apps.get_model('bookshelf', 'Book')
        perms = Permission.objects.filter(content_type__app_label='bookshelf', content_type__model='book')
        
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        editors.permissions.set(perms.filter(codename__in=['can_create', 'can_edit', 'can_view']))
        viewers.permissions.set(perms.filter(codename__in=['can_view']))
        admins.permissions.set(perms)  # all permissions
