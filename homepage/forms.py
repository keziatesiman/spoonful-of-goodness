from django import forms

class Planner_Form(forms.Form):
    
    error_messages = {
        'required': 'Please fill this input',
    }
    
    name_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter name of activity'
    }

    cat_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter category of activity'
    }

    loc_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter location of activity'
    }

    date_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter date of activity',
        'type': 'date'
    }

    time_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter time of activity',
        'type': 'time'
    }

    calories_attrs = {
        'class': 'form-control form-group',
        'placeholder': 'Enter calories needed',
    }

    name = forms.CharField(label='Activity Name', required=True, max_length=80, widget=forms.TextInput(attrs=name_attrs))
    category = forms.CharField(label='Category', required=True,max_length=50, widget=forms.TextInput(attrs=cat_attrs))
    location = forms.CharField(label='Location', required=False,max_length=100, widget=forms.TextInput(attrs=loc_attrs))
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs=date_attrs))
    time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput(attrs=time_attrs))
    calories = forms.IntegerField(label = 'Calories', required=True, widget = forms.NumberInput(attrs=calories_attrs))