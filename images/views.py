from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # formulario es enviado
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # datos del formulario son validos
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # asignamos el usuario actual al item
            new_image.user = request.user
            new_image.save()
            messages.success(request,
                             'Imagen se agregó con éxito')
            # redireccionamos a la vista del item recientemente creado
            return redirect(new_image.get_absolute_url())
        
    else:
        # construir formulario con data obtenida del bookmarklet
        # via GET
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})
