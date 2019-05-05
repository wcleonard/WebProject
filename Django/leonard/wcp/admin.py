from django.contrib import admin

from . import models
import datetime

from django.utils import timezone


class ChoiceInline(admin.StackedInline):
    model = models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'publish_date', 'was_published_recently')
    list_filter = ['publish_date']
    search_fields = ['question_text']

    def was_published_recently(self):
        pass

    was_published_recently.admin_order_field = 'publish_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


admin.site.register(models.Question, QuestionAdmin)

