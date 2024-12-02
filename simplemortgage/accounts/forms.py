from django import forms
from .models import CustomUser, UserFile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "phone_number",
            "gross_income",
            "dob",
            "ssn",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "ssn": forms.PasswordInput(render_value=True),
        }


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "phone_number",
            "gross_income",
            "dob",
            "ssn",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "ssn": forms.PasswordInput(render_value=True),
        }


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ["file", "label"]
