from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'registrations/register.html', context)
