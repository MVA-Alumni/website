from django import forms
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError
from directory.models import Alumnus, Domain, Year

class ModelChoiceFieldLabelPk(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.pk)

class ModelChoiceFieldLabelName(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.name)

class FormAdd(forms.Form):
    first_name = forms.CharField(label="First name ", max_length=30, widget=forms.TextInput(attrs={'autofocus' : 'autofocus'}))
    last_name = forms.CharField(label="Last name ", max_length=30)
    gender = forms.ChoiceField(label="Gender ", choices=Alumnus.Gender)
    email = forms.EmailField(label="Email ", max_length=50)
    year = ModelChoiceFieldLabelPk(queryset=Year.objects.all(), label="First year of attendance ")

class FormLogin(forms.Form):
    first_name = forms.CharField(label="First name ", max_length=30, widget=forms.TextInput(attrs={'autofocus' : 'autofocus'}))
    last_name = forms.CharField(label="Last name ", max_length=30)
    year = ModelChoiceFieldLabelPk(queryset=Year.objects.all(), label="First year of attendance ")


class FormIdentity(forms.Form):
    def clean_photo(self):
        photo = self.cleaned_data.get('photo',False)
        if photo:
            if photo._size > 512*1024:
                  raise ValidationError("Please upload a picture of size inferior to 512kB.")
            return photo
        else:
            raise ValidationError("Couldn't read the uploaded picture.")

    photo = forms.ImageField(label="Picture ", required=False)

class FormContact(forms.Form):
    email = forms.EmailField(label="Email ", max_length=50)
    phone1 = forms.CharField(label="Phone number ", max_length=20, required=False)
    phone2 = forms.CharField(label="Phone number (2) ", max_length=20, required=False)
    postal = forms.CharField(label="Postal address ", max_length=160, required=False)
    website = forms.URLField(label="Webpage ", required=False)

class FormAbout(forms.Form):
    def clean_cv(self):
        print self.cleaned_data
        cv = self.cleaned_data.get('cv',False)
        if cv:
            if cv._size > 512*1024:
                  raise ValidationError("Please upload a CV of size inferior to 512kB.")
            return cv
        else:
            return None
            #raise ValidationError("Couldn't read the uploaded CV.")
    presentation = forms.CharField(widget=forms.Textarea, label="Presentation ", required=False)
    diploma = forms.CharField(label="Diplomas ", max_length=80, required=False)
    company = forms.CharField(label="Current company ", max_length=160, required=False)
    job = forms.CharField(label="Current position ", max_length=160, required=False)
    keywords = forms.CharField(label="Keywords ", max_length=1000, required=False, help_text='enter comma-separated keywords, eg "start-up, big data, bioinformatics, cancer"')
    #domain = ModelChoiceFieldLabelName(queryset=Domain.objects.all(), label="Domain ", required=False)
    cv = forms.FileField(label="CV ", required=False)


