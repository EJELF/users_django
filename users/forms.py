from django import forms
from users import models


class AddUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "username",
            "email",
        ]


class DeleteUserForm(forms.ModelForm):

    class Meta:
        model = models.User

        fields = [
            "username",
        ]
