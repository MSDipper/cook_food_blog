from django import forms

from food.models import Comment

class CommentForm(forms.ModelForm):
    ''' Форма комментариев '''
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']