from django import forms
from .models import Article
from django_summernote.widgets import SummernoteWidget
from djangocodemirror.fields import CodeMirrorWidget
# from codemirror.widgets import CodeMirror

# For ModelForm
class ArticleForm(forms.ModelForm):
    title=forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content=forms.CharField(
        label='내용',
        widget=SummernoteWidget(),
		error_messages={
            'required': 'Please enter your content',
        },
    )
    
    code=forms.CharField(
        label='코드',
        widget=CodeMirrorWidget(config_name='python'),
        # widget=SummernoteWidget(),
    )
    
    class Meta:
        model = Article
        fields = '__all__'
#        widgets = {
#            'content': SummernoteWidget(),
#        }
