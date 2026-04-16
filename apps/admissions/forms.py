from django import forms
from .models import AdmissionInquiry

class AdmissionInquiryForm(forms.ModelForm):
    class Meta:
        model = AdmissionInquiry
        fields = [
            'parent_name', 'email', 'phone', 
            'child_name', 'child_age', 'class_applied_for', 
            'message'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
