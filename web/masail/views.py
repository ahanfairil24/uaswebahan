from django.shortcuts import render, redirect
from .models import masail
from .forms import masailform

# Create your views here.

def masailview(request):
    masail_form = masailform(request.POST or None)
    if request.method == 'POST':
        if masail_form.is_valid:
            simpan_data = masail.objects.create(
                asilah = masail_form.cleaned_data.get('asilah'),
                jawaban = masail_form.cleaned_data.get('jawaban'),
                iktirod = masail_form.cleaned_data.get('iktirod'),
                keputusan = masail_form.cleaned_data.get('keputusan'),
            )
            return redirect('masail:masailList')
    context = {
        'form':masail_form
    }
    return render(request, 'masail.html', context)



