from django import forms
from display.models import Comment

class CommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your comment here...'
            })
        }