from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        usrname = request.POST['usrname']
        passwd = request.POST['passwd']
        if usrname == passwd:
            return render(request, 'login/login.html',{'status':'Success'})
        else:
            return render(request, 'login/login.html', {'status': 'Fail'})
    else:
        return render(request,'login/login.html')

def userregistration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            pass
        else:
            return render(request, 'login/register.html',{'errmsg': 'Passwords you entered  do not match...!'})
    return render(request, 'login/register.html')
