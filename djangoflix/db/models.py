from time import time
from weakref import proxy
from django.db.models.signals import pre_save
from django.db import models



class PublishStateOptions(models.TextChoices):
        # CONSTANT = DB_VALUE , USER_DISPLAY_VALUE
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
