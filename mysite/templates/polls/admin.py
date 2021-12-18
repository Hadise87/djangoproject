

from django.contrib import admin

from .models import Question, Choice

# admin.site.site_header = "Polls Admin"
# admin.site.site_title = "Polls Admin area"
# admin.site.index_title = "welcome to the Polls admin"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    llist_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)





