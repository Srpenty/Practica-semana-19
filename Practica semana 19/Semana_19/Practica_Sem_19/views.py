from django.shortcuts import render,redirect
from .Formularios.registerform import NewUserForm
from .Formularios.loginform import LoginForm
from .Formularios import add_Productos,add_Proveedor
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def reg_user(request):
    #comprobamos el metodo de envio de datos
    if request.method == 'POST':
        #creamos el objeto de tipo usuario y comprobamos si es valido, en tal caso, lo guardamos
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/')
    else:
        #se carga el formulario y es renderizado
        formulario = NewUserForm()
        return render(request,'Reg_user.html',{'form':formulario})

#creamos una funcion que diga que debes estar registrado para entrar
@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff

    if es_estudiante or es_admin:
        return render(request,'index.html',{'user':request.user,'es_estudiante':es_estudiante,'es_admin':es_admin})
    else:
        return render(request,'index.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def cerrar_session(request):
    #cargamos la funcion para cerrar sesion
    logout(request)

    #redirigimos a la pagina de login
    return redirect('login')

@login_required(login_url='login')
def vProductos(request):
    es_admin = request.user.is_staff
    #recuperamos los productos
    productos = Productos.objects.all()
    #renderizamos la template y le enviamos los productos
    return render(request,'Productos.html',{'productos':productos,'admin':es_admin})

@login_required(login_url='login')
def vProveedores(request):
    es_admin = request.user.is_staff
    #recuperamos la lista de proveedores
    proveedores = Proveedores.objects.all()
    #renderizamos la pagina
    return render(request,'Proveedores.html',{'proveedores':proveedores,'admin':es_admin})

@login_required(login_url='login')
def vAddProductos(request):
    es_admin = request.user.is_staff
    #recuperamos los proveedores para el formulario
    proveedores = Proveedores.objects.all()
    #comprobamos el metodo de envio de informacion
    if request.method == 'POST':
        #llamamos al formulario
        formulario = add_Productos.addProducto(request.POST)
        #comprobamos la integridad del formulario
        if formulario.is_valid():
            #creamos y guardamos el registro
            nuevoreg = Productos()
            nuevoreg.nombre = formulario.data['nombre']
            nuevoreg.stock = formulario.data['stock']
            proveedor = Proveedores.objects.get(id=request.POST['Proveedores'])
            nuevoreg.fk_prov = proveedor
            nuevoreg.save()
            #redirigimos a la lista de productos
            return HttpResponseRedirect('/listProductos')
    else:
        #cargamos por default el formulario y lo renderizamos
        formulario = add_Productos.addProducto()
        return render(request,'add_Productos.html',{'form':formulario,'Proveedores':proveedores,'admin':es_admin})

@login_required(login_url='login')
def vAddProveedores(request):
    es_admin = request.user.is_staff
    #comprobamos la forma de envio de datos
    if request.method == 'POST':
        #creamos el objeto formulario
        formulario = add_Proveedor.addProveedor(request.POST)
        if formulario.is_valid():
            #creamos y rellenamos un objeto de la base de datos con los datos del formulario
            nuevoreg = Proveedores()
            nuevoreg.nombre = formulario.data['nombre']
            nuevoreg.telefono = formulario.data['telefono']
            nuevoreg.save()
            #redirigimos a la pagina con la lista de proveedores
            return HttpResponseRedirect('/listProveedores')
    else:
        #cargamos el formulario por defecto y lo renderizamos
        formulario = add_Proveedor.addProveedor()
        return render(request,'add_Proveedores.html',{'form':formulario,'admin':es_admin})