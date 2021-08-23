from django.contrib.auth.forms import UserCreationForm

class FormUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)