from django.contrib import admin
from .models import Post, imgPost, Question, QAnswer

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author",)

class imgPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author",)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "author")

class QAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer", "author")



admin.site.register(Post, PostAdmin)
admin.site.register(imgPost, imgPostAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QAnswer, QAnswerAdmin)