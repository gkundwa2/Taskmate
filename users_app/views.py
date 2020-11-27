from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages


#user authentification .
def register(request):

    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New family has been added. Login to Enter their visits to the pantry"))
            return redirect('todolist')
    
    else: 
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
    
