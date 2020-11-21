from django import forms
from .models import KimetsuCharactorModel


class KimetsuCharactorForm(forms.ModelForm):
    """鬼滅の刃キャラクターForm用"""
    class Meta:
        model = KimetsuCharactorModel
        fields = ("name", "sex_id", "characteristic")
        widgets = {
            'characteristic': forms.Textarea

        }
