from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=100)
    content = forms.CharField(label='内容', widget=forms.Textarea)