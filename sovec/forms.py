# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    register_username = forms.CharField(max_length=15, min_length=4)
    register_name = forms.CharField(max_length=25, required=False)
    register_last_name = forms.CharField(max_length=25, required=False)
    register_email = forms.EmailField(required=False)
    register_password = forms.CharField(max_length=25, min_length=8,
                        widget=forms.TextInput(attrs={'autocomplete':'off'}))
    re_register_password = forms.CharField(max_length=25, min_length=8,
                             widget=forms.TextInput(attrs={'autocomplete':'off'}))

    def clean(self):
    	super(forms.Form,self).clean()
    	# Checking if username is available
    	if 'register_username' in self.cleaned_data:
    		if User.objects.filter(username=self.cleaned_data['register_username']).exists():
    			self.errors['register_username'] = [u'Nombre de usuario ya existe']
    	# Checking if password an re-password are the same
    	if 'register_password' in self.cleaned_data and 're_register_password' in self.cleaned_data:
    		if self.cleaned_data['register_password'] != self.cleaned_data['re_register_password']:
    			self._errors['re_register_password'] = [u'Contraseñas no coinciden']
    			return self.cleaned_data