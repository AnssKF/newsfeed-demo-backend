from django.db.models import fields
import django_filters

from .models import *


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = "__all__"