from django.db import models
from django.db.models import Q

from djangounchained import settings


class ThreadManager(models.Manager):
    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        return self.get_queryset().filter(qlookup).distinct()

    def get_or_new(self, user, other_username):
        username = user.username
        if username == other_username:
            return None
        qlookup1 = Q(first__username=username) & Q(second__username=other_username)
        qlookup2 = Q(first__username=other_username) & Q(second__username=username)
        thread_search_query = self.get_queryset().filter(qlookup1 | qlookup2)
        if thread_search_query.count() == 0:
            user2 = user.__class__.objects.filter(username=other_username)
            if user2.count() == 0:
                return None
            thread = self.model(
                first=user,
                second=user2.first()
            )
            thread.save()
            return thread
        return thread_search_query.first()


class Thread(models.Model):
    first = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_first')
    second = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_second')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    object = ThreadManager()

    def __str__(self):
        return f"{self.first}'s Thread"


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='sender', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
