from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from tinymce.widgets import TinyMCE

from .models import Comment

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "username",
            "email",
            "homepage",
            "text",
            "image",
            "file",
            "captcha",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3"}),
            "homepage": forms.URLInput(attrs={"class": "form-control mb-3"}),
            "text": TinyMCE(attrs={"cols": 80, "rows": 30, "class": "mb-3"}),
            "image": forms.FileInput(attrs={"class": "form-control mb-3"}),
            "file": forms.FileInput(attrs={"class": "form-control mb-3"}),
        }

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "parent_comment",
            "username",
            "email",
            "homepage",
            "text",
            "image",
            "file",
            "captcha",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3"}),
            "homepage": forms.URLInput(attrs={"class": "form-control mb-3"}),
            "text": TinyMCE(attrs={"cols": 80, "rows": 30, "class": "mb-3"}),
            "image": forms.FileInput(attrs={"class": "form-control mb-3"}),
            "file": forms.FileInput(attrs={"class": "form-control mb-3"}),
            "parent_comment": forms.Select(
                attrs={"class": "form-control mb-3", "disabled": True}
            ),
        }

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
