# from django.contrib import admin
# from .models import Choice, Question


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,                 {'fields' : ['question_text']}),
#         ('Data informatiomn',  {'fields': ['pub_date'], 'classes':['collapse']}),
#     ]
#     # avakin  element dar har majmue chandtaii fieldset, hamun onvane un fieldset hast.

#     inlines = [ChoiceInline]
    
#     # For good measure, let’s also include the was_published_recently() method
#     list_display = ('question_text', 'pub_date')
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']


# admin.site.register(Question, QuestionAdmin)
        


from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    llist_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)





