from django.contrib import admin

from .models import Question, Choice, Player, Personality, Compatibility

admin.site.register(Player)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Personality)
admin.site.register(Compatibility)
