from django import forms
from app.models import *
class ModelTopicForm(forms.ModelForm):
    class Meta:
        model=Topic 
        fields='__all__'
class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=('url')
        #labels={'topic_name':'tn'}
        #help_texts={'name':'this is topic name'}
        #widgets={'name':forms.PasswordInput}
class ModelAccessRecordsForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
    