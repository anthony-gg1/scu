from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create your views here.
def RegisterUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'Users/Register.html', {'form': form})

def Sucess(request):
    return render(request, 'Users/Sucess.html')

def ListRegisters(request):
    users = User.objects.all()
    return render(request, 'Users/list.html', {'users': users})

def DeleteUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('list_registers')

def UpdateUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_registers')
    else:
        form = UserForm(instance=user)
    return render(request, 'Users/Update.html', {'form': form})