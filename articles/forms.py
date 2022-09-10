from django import forms
from .models import Article
from django_summernote.widgets import SummernoteWidget

# For ModelForm
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }
