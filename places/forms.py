from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(label="Назва")
    description = forms.CharField(label="Опис", widget=forms.Textarea)
    type = forms.CharField(label="Тип місця")
    location = forms.CharField(label="Локація", required=False)
    rating = forms.IntegerField(label="Рейтинг", min_value=1, max_value=5)
