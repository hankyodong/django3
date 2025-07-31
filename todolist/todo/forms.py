# todo / forms.py

from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "start_date", "end_date"]

# todo / forms.py

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message',]
        labels = {
            'message': '내용',
        }
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3, 'cols': 40, 'class': 'form-control', 'placeholder': '댓글 내용을 입력해주세요.'
            }),
        }
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "start_date", "end_date", "is_completed"]