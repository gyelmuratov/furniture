from django import forms

from users.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
    def clean_message(self):
        message = self.cleaned_data['message']
        return message