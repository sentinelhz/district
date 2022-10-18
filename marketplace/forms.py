from django import forms

from .models import *


class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "category", "price", "stock", "imageUrl")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProductUploadForm, self).__init__(*args, **kwargs)

    def clean_user(self):
        return self.user


# class FavoriteForm(forms.ModelForm):
#     class Meta:
#         model = Favorite
#         fields = ("song",)
#
#     def clean_song(self):
#         pass

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
