from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("user_id", "title", "description")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("user_id", "queid_id", "answer")
