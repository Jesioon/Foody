from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude =['owner']
        labels = {
            'recipe_name': 'Nazwa przepisu',
            'time_need': 'Potrzebny czas (min)',
            'portions': 'Liczba porcji',
            'day_key': 'Pora dnia',
            'country_key': 'Kuchnia',
            'level': 'Poziom trudności',
            'ingredients': 'Składniki',
            'recipe': 'Przepis',
            'image': 'Zdjęcie'
        }

