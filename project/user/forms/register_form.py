from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django import forms


from django.contrib.auth.password_validation import validate_password

class CustomUserCreationForm(UserCreationForm):
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        error_added = False

        # Check minimum length
        if len(password2) < 8:
            self.add_error('password2', "This password is too short. It must contain at least 8 characters.")
            error_added = True
        else:
            # Validate password
            try:
                validate_password(password2, self.instance)
            except ValidationError as validation_error:
                self.add_error('password2', validation_error)
                error_added = True

        if not error_added and password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        return password2

