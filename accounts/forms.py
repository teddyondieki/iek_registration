from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomAccountCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('category', 'first_name', 'last_name', 'email', 'username', )


class CustomAccountChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'category')
