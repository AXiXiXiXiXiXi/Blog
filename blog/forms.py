from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "autocomplete": "username",
                "placeholder": "你的用户名",
            }
        ),
    )
    password = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "placeholder": "你的密码"}
        ),
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "用户名"}
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "autofocus": True,
                    "autocomplete": "username",
                    "placeholder": "给自己取一个名字",
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "密码"
        self.fields["password1"].widget.attrs["placeholder"] = "设置密码"
        self.fields["password1"].widget.attrs["autocomplete"] = "new-password"
        self.fields["password2"].label = "确认密码"
        self.fields["password2"].widget.attrs["placeholder"] = "再次输入密码"
        self.fields["password2"].widget.attrs["autocomplete"] = "new-password"


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="标题",
        widget=forms.TextInput(
            attrs={"autocomplete": "off", "placeholder": "给这篇文章一个标题"}
        ),
    )
    category = forms.CharField(
        max_length=100,
        label="分类",
        widget=forms.TextInput(
            attrs={"placeholder": "例如：日常、技术、随笔", "list": "category-list"}
        ),
        help_text="选择已有分类或输入新分类，新分类会自动创建。",
    )
    body = forms.CharField(
        label="正文",
        widget=forms.Textarea(
            attrs={
                "rows": 16,
                "autocomplete": "off",
                "placeholder": "写下此刻想记录的内容……",
            }
        ),
    )
