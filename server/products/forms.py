from django import forms

from products.models import ProductCategory, Product

from images.models import Image


class CategoryForm(forms.Form):

    name = forms.CharField(
        label='title',
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    description = forms.CharField(
        label='snippet',
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control'}
        )
    )


class ProductForm(forms.Form):

    name = forms.CharField(
        label='title',
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all()
    )

    image = forms.ModelChoiceField(
        queryset=Image.objects.all()
    )

    snippet = forms.CharField(
        label='snippet',
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control'}
        )
    )

    cost = forms.DecimalField(
        label='cost',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control'}
        )
    )


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'snippet']

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
