from django import forms

class Planner_Form(forms.Form):
    calories_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter calories needed',
    }

    select_attrs = {
        'class': 'form-control form-group',
    }

    meals_num_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )

    boolean_choices = (
        (True, 'Yes'),
        (False, 'No'),
    )

    calories = forms.IntegerField(label = 'Calories', required=True, widget = forms.NumberInput(attrs=calories_attrs))
    meals_per_day = forms.CharField(label = 'Number of Meals per Day',required=True, widget=forms.Select(choices=meals_num_choices, attrs=select_attrs))
    contains_pork = forms.CharField(label = 'Do you consume pork?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_alcohol = forms.CharField(label = 'Do you consume alcohol?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_gluten = forms.CharField(label = 'Do you consume gluten?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_lactose = forms.CharField(label = 'Do you consume lactose?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_egg = forms.CharField(label = 'Do you consume eggs?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_meat = forms.CharField(label = 'Do you consume meat?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    is_vegan = forms.CharField(label = 'Are you a vegan?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_milk = forms.CharField(label = 'Do you consume milk?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_milk_substitute = forms.CharField(label = 'Do you consume milk substitutes?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    

