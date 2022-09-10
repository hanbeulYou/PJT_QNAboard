from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article

# Apply summernote to all TextField in model.
class ArticleAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Article, ArticleAdmin)