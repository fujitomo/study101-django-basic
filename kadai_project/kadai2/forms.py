from django import forms
from .models import KimetsuCharactorModel, SexModel


class KimetsuCharactorForm(forms.ModelForm):
    """鬼滅の刃キャラクターForm用"""
    name = forms.CharField(
        label='名前', max_length=30
    )

    sex_id = forms.ModelChoiceField(
        SexModel.objects, label='性別'
    )

    characteristic = forms.CharField(
        label='特徴', max_length=300, widget=forms.Textarea
    )

    class Meta:
        model = KimetsuCharactorModel
        # TODO : このコードがないとエラーが発生する
        fields = ('name', 'sex_id', 'characteristic')
