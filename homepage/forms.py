from django import forms

class Planner_Form(forms.Form):
    select_attrs = {
        'class': 'form-control',
        'style': 'margin-bottom: 1rem;',
    }

    checkbox_attrs = {
        'class': 'form-check',
        'style': 'margin-bottom: 1rem;',
    }

    vegan_checkbox_attrs = {
        'class': 'form-check',
        'style': 'margin-bottom: 1rem;',
        'onclick': "uncheckAntiVegan()",
    }

    antivegan_checkbox_attrs = {
        'class': 'form-check',
        'style': 'margin-bottom: 1rem;',
        'onclick': "uncheckVegan()",
    }

    milk_checkbox_attrs = {
        'class': 'form-check',
        'style': 'margin-bottom: 1rem;',
        'onclick': "milkIsChecked()",
    }

    milk_substitute_checkbox_attrs = {
        'class': 'form-check',
        'style': 'margin-bottom: 1rem;',
        'onclick': "uncheckMilk()",
    }

    calories_choices = (
        ('Diet', 'Diet'),
        ('Normal', 'Normal'),
        ('High Calories', 'High Calories'),
    )

    meals_num_choices = (
        (2, 2),
        (3, 3),
        (4, 4),
    )

    milk_choices = (
        ('Milk', 'Milk'),
        ('Milk substitute', 'Milk substitute'),
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
    milk = forms.ChoiceField(label= 'Which milk to include', required=True, choices=milk_choices, widget=forms.Select(attrs=select_attrs))
    contains_alcohol = forms.BooleanField(label= 'Include alcohol', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    contains_gluten = forms.BooleanField(label= 'Include gluten', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    contains_lactose = forms.BooleanField(label= 'Include lactose', required=False, widget=forms.CheckboxInput(attrs=checkbox_attrs))
    is_vegan = forms.BooleanField(label= 'Are you a vegan', required=False, widget=forms.CheckboxInput(attrs=vegan_checkbox_attrs))
    contains_egg = forms.BooleanField(label= 'Include eggs', required=False, widget=forms.CheckboxInput(attrs=antivegan_checkbox_attrs))
    contains_meat = forms.BooleanField(label= 'Include meat', required=False, widget=forms.CheckboxInput(attrs=antivegan_checkbox_attrs))
    contains_pork = forms.BooleanField(label= 'Include pork', required=False, widget=forms.CheckboxInput(attrs=antivegan_checkbox_attrs))
    contains_fish = forms.BooleanField(label= 'Include fish', required=False, widget=forms.CheckboxInput(attrs=antivegan_checkbox_attrs))
    

