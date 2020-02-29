from django import forms
from .models import ArticlePost

#Article's forms
class ArticlePostForm(forms.ModelForm):
    class Meta:
        #指明数据模型来源
        model = ArticlePost
        #define fields
        fields = ('title', 'body')