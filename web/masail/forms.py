from django import forms

class masailform(forms.Form):
    Deskripsi = forms.CharField(max_length=50)
    Jawaban = forms.CharField(max_length=40)
    Tanggapan = forms.CharField(widget=forms.Textarea)
    Keputusan = forms.BooleanField()

#ModelForm
