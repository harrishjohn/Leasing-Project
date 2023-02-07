from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login

def registerpage(request):
    if request.method =='POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        username = request.POST.get('username')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        users = register()
        users.Name = name
        users.Phone_number = phone_number
        users.Country = country
        users.Email_id = email_id
        users.Username = username
        users.Password = password
        users.save()
        return redirect(userlogin)
    return render(request,'lesseeregister.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin@123':
            return render(request,"adminpage.html")
        else:
            return HttpResponse('Invalid person')
    return render(request,'admin.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            register.objects.get(Username=username, Password=password)
            user = username
            data = upload.objects.filter(Status=False)
            return render(request, 'useraccount.html', {'value': data,'username':user})
        except:
            return HttpResponse('Wrong username or password.Check your username or password.Or else create an user account')
    return render(request, 'lesseelogin.html')

def logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout successfully")
        return redirect('/')

def businesspage(request):
    return render(request,'businessaccount.html')

def userpage(request):
    data = upload.objects.filter(Status=False)
    return render(request, 'useraccount.html', {'value': data})

def pending(request):
     details = register.objects.filter(Status=False)
     return render(request,'pendingdetails.html',{'value':details})

def approved(request):
    details = register.objects.filter(Status=True)
    return render(request,'approvedetails.html',{'value':details})


def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')

def home(request):
    pass
    return render(request,'home.html')

def lessorregister(request):
    if request.method =='POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        company_name = request.POST.get('company_name')
        country = request.POST.get('country')
        username = request.POST.get('username')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        users = lessor()
        users.Name = name
        users.Phone_number = phone_number
        users.Company_name = company_name
        users.Country = country
        users.Email_id = email_id
        users.Username = username
        users.Password = password
        users.save()
        return redirect(lessorlogin)
    return render(request,'lessorregister.html')

def lessorlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            lessor.objects.get(Username=username,Password=password)
            user = username
            data = upload.objects.filter(Owner=username)
            return render(request, 'businessaccount.html', {'value': data,'username':user})
        except:
            return HttpResponse('Wrong username or password.Check your username or password.Or else create an business account')
    return render(request,'lessorlogin.html')

def uploadfile(request,username):
    if request.method == 'POST':
        name = request.POST.get('name')
        container_id = request.POST.get('container_id')
        rate = request.POST.get('rate')
        container_type = request.POST.get('container_type')
        container_length = request.POST.get('container_length')
        container_material = request.POST.get('container_material')
        container_condition = request.POST.get('container_condition')
        location = request.POST.get('location')
        description = request.POST.get('description')
        picture = request.FILES['picture']
        owner = request.POST.get('owner')
        file = upload()
        file.Name = name
        file.Container_id = container_id
        file.Rate = rate
        file.Container_type = container_type
        file.Container_length = container_length
        file.Container_material = container_material
        file.Container_condition = container_condition
        file.Location = location
        file.Description = description
        file.Picture = picture
        file.Owner = owner
        file.save()
        return redirect(businesspage)
    data = username
    data_dict = {'username': data}
    return render(request, 'uploadfile.html', context=data_dict)

def viewimage(request,username):
    user = username
    data = upload.objects.filter(Status=False)
    return render(request,'viewimage.html',{'value': data,'username':user})

def myupload(request,username):
    data = upload.objects.filter(Owner=username)
    return render(request, 'myupload.html', {'value': data})

def order(request,username):
    details = book.objects.filter(Owner=username)
    return render(request,'pendingdetails.html',{'value':details})

def container(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        shipping_location = request.POST.get('shipping_location')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        owner = request.POST.get('owner')
        container_id = request.POST.get('container_id')
        details = book()
        details.Name = name
        details.Company_name = company_name
        details.Company_address = company_address
        details.Shipping_location = shipping_location
        details.Phone_no = phone_no
        details.Email = email
        details.Owner = owner
        details.Container_id = container_id
        details.save()
        return redirect(home)
    data = upload.objects.filter(id=id)
    return render(request,'buycontainer.html',{'value':data})

def containerview(request):
    data = upload.objects.filter(Status=False)
    return render(request,'container.html',{'value':data})

def about(request):
    return render(request,'about.html')

