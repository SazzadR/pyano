from django import forms


class ComposeForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type your message',
                'rows': 2
            }
        )
    )
