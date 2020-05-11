from django.shortcuts               import render, redirect
from django.views.decorators.csrf   import csrf_protect
from django.contrib.auth            import authenticate, login, logout
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required
from .models                        import Pet

# Create your views here.
@login_required(login_url='/login/')

def list_all_pets(req):
    pet = Pet.objects.filter(active = True)
    return render(req, 'list.html', {'pet':pet})

def list_user_pets(req):
    pet = Pet.objects.filter(active = True, user=req.user)
    return render(req, 'list.html', {'pet':pet})

def pat_datail(req, id):
    pet = Pet.objects.get(active = True, id = id)
    return render(req, 'pet.html', {'pet':pet})

def login_user(req):
    return render(req, 'login.html')
    
@csrf_protect
def submit_login(req):
    if req.POST:
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            #if user.is_activate:
            login(req, user)
            return redirect('/')
            #else:
                #messages.error(req, 'Seu usuário está desativado!')
        else:
            messages.error(req, 'Usuário e senha inválodo. Favor tentar novamente')
    return redirect('/login')

def logout_user(req):
    logout(req)
    return redirect('/login/')