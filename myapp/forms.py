from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

# Create your forms here.

class CreateNewList(forms.Form):
    nom = forms.CharField(label="Name", max_length=200)
    firstname = forms.CharField(label="First Name", max_length=200)
    check = forms.BooleanField(required=False)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

''' Le formatage d'un formulaire se fait dans le template ! '''
class SaisieForm(forms.Form):
    name2 = forms.CharField(label='Entrez votre name', max_length=100)
    firstname2 = forms.CharField(label="votre prenom", max_length=200)

class CheckRecForm(forms.Form):
    mavar1 = forms.CharField(label="mavar1", max_length=200)
    chkrec = forms.BooleanField(required=False)

'''
<form method="post" action="index.html">
    <p>
        <label for="pseudo">Votre pseudo :</label>
        <input type="text" name="pseudo" id="pseudo" placeholder="Ex : Zozor" size="30" maxlength="10" />
        <input type="submit" value="Envoyer" />
    </p>
</form>
'''