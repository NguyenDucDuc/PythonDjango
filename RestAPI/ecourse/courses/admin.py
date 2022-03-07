from django.contrib import admin
from django.utils.html import mark_safe
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','subject','created_date','image']
    readonly_fields = ['image_view']

    def image_view(self, courses):
        if courses:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=courses.image.name)
            )


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject','content']
    readonly_fields = ['image_lesson']
    form = LessonForm

    def image_lesson(self, lesson):
        if lesson:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=lesson.image.name)
            )




admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)