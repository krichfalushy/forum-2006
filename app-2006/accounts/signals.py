from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Comment


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'accounts':
        author_group, created = Group.objects.get_or_create(name='Author')
        moderator_group, created = Group.objects.get_or_create(name='Moderator')

        try:
            comment_ct = ContentType.objects.get_for_model(Comment)

            # Дозволи на додавання, зміну та видалення коментарів
            add_comment = Permission.objects.get(codename='add_comment', content_type=comment_ct)
            change_comment = Permission.objects.get(codename='change_comment', content_type=comment_ct)
            delete_comment = Permission.objects.get(codename='delete_comment', content_type=comment_ct)

            # Автор може додавати коментарі (редагування/видалення своїх — регулюється у views.py)
            author_group.permissions.add(add_comment, change_comment, delete_comment)

            # Модератор має ті ж права + видалення (регулюється у views.py)
            moderator_group.permissions.add(add_comment, change_comment, delete_comment)
        except Exception as e:
            print(f"Could not assign permissions yet (might be first run): {e}")
