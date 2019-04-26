from django import forms

class Planner_Form(forms.Form):
    select_attrs = {
        'class': 'form-control',
    }

    checkbox_attrs = {
        'class': 'form-check',
    }

    calories_choices = (
        ('Diet', 'Diet'),
        ('Normal', 'Normal'),
        ('High Calories', 'High Calories'),
    )

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

    ''' <div class="form-check">
        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
        <label class="form-check-label" for="defaultCheck1">
            Default checkbox
        </label>
    </div> '''

    calories = forms.ChoiceField(label = 'Calories', required=True, choices=calories_choices, widget = forms.Select(attrs=select_attrs))
    meals_per_day = forms.ChoiceField(label = 'Number of Meals per Day',required=True, choices=meals_num_choices, widget=forms.Select(attrs=select_attrs))
    # contains_pork = forms.CharField(label = 'Do you consume pork?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_pork = forms.BooleanField(label= 'Include pork', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_alcohol = forms.CharField(label = 'Do you consume alcohol?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_alcohol = forms.BooleanField(label= 'Include alcohol', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_gluten = forms.CharField(label = 'Do you consume gluten?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_gluten = forms.BooleanField(label= 'Include gluten', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_lactose = forms.CharField(label = 'Do you consume lactose?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_lactose = forms.BooleanField(label= 'Include lactose', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_egg = forms.CharField(label = 'Do you consume eggs?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_egg = forms.BooleanField(label= 'Include eggs', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_meat = forms.CharField(label = 'Do you consume meat?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_meat = forms.BooleanField(label= 'Include meat', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # is_vegan = forms.CharField(label = 'Are you a vegan?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    is_vegan = forms.BooleanField(label= 'Are you a vegan', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_milk = forms.CharField(label = 'Do you consume milk?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_milk = forms.BooleanField(label= 'Include milk', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    # contains_milk_substitute = forms.CharField(label = 'Do you consume milk substitutes?', widget=forms.Select(choices=boolean_choices, attrs=select_attrs))
    contains_milk_substitute = forms.BooleanField(label= 'Include milk substitute', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    

