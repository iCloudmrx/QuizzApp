from django.contrib import admin
from .models import Test, Question, Category, CheckQuestion, CheckTest

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class QuestionInlines(admin.TabularInline):
    model = Question


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInlines,]
    list_display = ['title', 'max_attemps', 'start_date']
    list_filter = ['title', 'max_attemps', 'start_date']
    search_fields = ['title', 'max_attemps']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'true_answer']
    list_filter = ['question', 'true_answer']
    search_fields = ['question']


admin.site.register([CheckTest, CheckQuestion])
