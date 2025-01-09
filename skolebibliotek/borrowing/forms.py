from django import forms
from .models import BorrowingModel

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = BorrowingModel
        fields = ['borrowing_title', 'borrowing_desc', 'borrowing_image']

