from django import forms
from durationwidget.widgets import TimeDurationWidget

from lesson_5.models import Client


# class MyForm(forms.Form):
#     name = forms.CharField(label='User name', disabled=False)
#     email = forms.EmailField(error_messages={'required': 'Please enter your'
#                                              ' available email'})
#     password = forms.CharField(max_length=20, min_length=10, widget=forms.PasswordInput())
#     age = forms.IntegerField(required=False,
#                              help_text='Enter your current age')
#     agreement = forms.BooleanField(required=False)
#     average_score = forms.FloatField(initial=10.1)
#     birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2022)))
#     work_experience = forms.DurationField(widget=TimeDurationWidget(show_seconds=False,
#                                                                     show_minutes=False,
#                                                                     show_hours=False))
#     gender = forms.ChoiceField(choices=[('1', 'male'), ('2', 'female')])


class MyForm(forms.Form):
    name = forms.CharField(label="User name", initial="User name",
                           error_messages={'required': 'Please enter your'
                                                       ' available email'})
    profile_picture = forms.ImageField(widget=forms.FileInput)
    additional_file = forms.FileField(widget=forms.FileInput)
    email = forms.EmailField(initial="admin@admin.com", error_messages={
        'required': 'Please enter your available email'})
    password = forms.CharField(max_length=20, min_length=10,
                               required=False,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, initial="45",
                             help_text="Enter your current age")
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)
    birthday = forms.DateField(widget=forms.SelectDateWidget,
                               required=False)
    work_experience = forms.DurationField(required=False,
                                          widget=TimeDurationWidget(
                                              show_days=False))
    gender = forms.ChoiceField(required=False,
                               choices=[("1", "man"), ("2", "woman")])


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ['user', 'second_email']
