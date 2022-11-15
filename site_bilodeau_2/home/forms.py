from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

# iterable 
CHOICES =( 
    ("Investissements", "Investissements"), 
    ("Assurances", "Assurances"), 
    ("Hypotheque", "Hypothèque"), 
    ("Fiscalite", "Fiscalité"), 
    ("Un peu de tout / Je ne sais pas", "Un peu de tout / Je ne sais pas"), 
) 


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Nom complet :")
    from_email = forms.EmailField(required=True, label="Email :")
    phone = forms.IntegerField(required=False, label="Numéro de téléphone (optionnel):", max_value=9999999999)
    choices = forms.ChoiceField(required=True, choices = CHOICES, label="Je souhaite discuter de :")
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), required=False, label="Message (optionnel):")
    captcha = ReCaptchaField(required=True, widget=ReCaptchaV2Invisible(attrs={'data-badge':'inline'}), label="")
    
