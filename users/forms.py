from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'username')


class CustomAuthenticationForm(forms.Form):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    identifier = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)

    def clean(self):
        identifier = self.cleaned_data.get('identifier')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(Q(username=identifier) | Q(email=identifier))
        except User.DoesNotExist:
            raise forms.ValidationError("User not found, please check your credentials")

        credentials = {'email': user.email, 'password': password}

        user_in = authenticate(self.request, **credentials)
        if user_in is None:
            raise forms.ValidationError("User not found, please check your credentials")

        self.cleaned_data['user'] = user_in
        return self.cleaned_data