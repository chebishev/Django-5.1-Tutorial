from django.contrib import admin
from django.utils import timezone
import datetime

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date information", {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter  = ["pub_date"]
    search_fields = ["question_text"]
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self, obj):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
