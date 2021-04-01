from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Button, Field
from crispy_forms.bootstrap import FormActions

# Create your forms here.


class ContactForm(forms.Form):
    First_Name = forms.CharField(required=True)
    Surname = forms.CharField(required=True)
    Email_Adress = forms.EmailField(required=True)
    Description = forms.CharField(widget=forms.Textarea, required=True)

    Type = forms.ChoiceField(
        choices=(
            ('option_one', "Draping"),
            ('option_two', "Landscaping")
        ),
        widget=forms.RadioSelect,
        initial='option_one',
    )

    Work_Required = forms.MultipleChoiceField(
        choices=(
            ('option_one', "Garden Decking"),
            ('option_two', 'Garden Fencing'),
            ('option_three', 'Garden Furniture'),
            ('option_four', 'Event Draping'),
            ('option_five', 'Draping'),
            ('option_six', 'Special'),
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong>Chose all that apply, if not listed write in your comments below",
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('First_Name'),
        Field('Surname'),
        Field('Email_Adress', css_class='input-xlarge'),
        'Type',
        Field('Work_Required', style="background: #FAFAFA; padding: 10px;"),
        Field('Description', rows="3", css_class='input-xlarge mb-3'),
        HTML('<div class="g-recaptcha" data-sitekey="6Lee148aAAAAAIXAn7tovPfLMs_Xl91NZD87hESh"></div>'),
        FormActions(
            Submit('save_changes', 'Submit', css_class="btn-primary mb-3 mt-3"),
        )
    )
