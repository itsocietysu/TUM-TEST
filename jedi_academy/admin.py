# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Planet, Jedi, Question

admin.site.register(Planet)
admin.site.register(Jedi)
admin.site.register(Question)
