from django import forms
from .models import MarchentModel,ProductModel
class Marchentform(forms.ModelForm):
    class Meta:
        model=MarchentModel
        fields=['mrt_name','contactNo','Email_id']


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'