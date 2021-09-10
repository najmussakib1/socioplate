from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import userlist, userpost
import math
from django.contrib.auth.models import User
from django.http import JsonResponse
'''user = get_user_model()
user.objects.all()'''
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def likepost(request,post_id):
    if request.user.is_authenticated:
        if request.method =='GET':
            a = int(post_id)
            dpost = userpost.objects.filter(sno=a).first()
            if dpost.lovers.filter(username=request.user.username).exists():
                a = dpost.likes
                a -= 1
                dpost.likes =a
                dpost.lovers.remove(request.user)
                dpost.save()
                a = dpost.lovers.count()
                return JsonResponse({'status':'unliked','nooflikes':a})
            else:
                a = dpost.likes
                a += 1
                dpost.likes= a
                dpost.lovers.add(request.user)
                dpost.save()
                a = dpost.lovers.count()
                return JsonResponse({'status': 'liked', 'nooflikes': a})

        else:
            return redirect('')
    else:
        return redirect('')
def blankpath(req):
    if req.user.is_authenticated:

        if req.method=='GET':
            un = req.user.username
            a = req.GET.get('pgno')
            if a is None or a==0:
                a =1
            else:
                a= int(a)

            allposts_oo = userpost.objects.exclude(user=req.user)
            allposts= allposts_oo.exclude(lovers=req.user)
            if allposts:
                n = len(allposts)
            else:
                n =0
            p = n/10
            if p%1 ==0:
                p = int(p)
            else:
                p = math.ceil(p)
            if p == 0:
                p = 1
            if a>p:
                a = p
            elif a<1:
                a =1

            posts_tobe = allposts[int((a-1)*10):int((a*10)-1)]
            if len(allposts)>a*10:
                next_available=True
            else:
                next_available = False
            if int((a-1)*10) >=10:
                prev_available =True
            else:
                prev_available = False
            params={'username':req.user,'poststoshow':posts_tobe,'nomber':len(posts_tobe),'thispg':a,'next':next_available,'prev':prev_available}
            if next_available:
                params['pn']=a+1
            if prev_available:
                params['pp']=a-1
            return render(req,'home.html',params)
        else:
            return redirect('')
    else:
        return redirect('signin')
def search(request):
    if request.user.is_authenticated:
        if request.method=='GET':
            key = request.GET.get('search')
            a = User.objects.filter(username__contains=key)
            result = {'users':a,'searched':key}
            if len(a)==0:
                result['exists']=False
            else:
                result['exists']=True
            return render(request,'search.html',result)
        else:
            return redirect('')
    else:
        return redirect('signin')
def developer(request):
    return render('dev.html')
def signin(req):
    if req.user.is_authenticated:
        return redirect('')
    else:
        if req.method=='GET':
            return render(req,'login.html')
        else:
            #make user and redirect him a success page or alert
            username = req.POST.get("uname")
            pw =req.POST.get('pw')
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(req, user)
                return redirect('')
            else:
                message = 'incorrect username or password! please try again!'
                return render(req,'login.html',{'message':message,'sent':True})
            return redirect('')
def create(req):
    if req.user.is_authenticated:
        return redirect('')
    else:
        if req.method=='GET':
            return render(req,'create-account.html')
        elif req.method=='POST':
            #make user and redirect him a success page or alert
            username = req.POST.get("uname")
            pw =req.POST.get('pw')
            fn = req.POST.get('fn')
            ln = req.POST.get('ln')
            mail = req.POST.get('mail')
            if len(username.split())>1:
                message = 'Cannot create account.'
                return render(req,'create-account.html',{'message':message,'sent':True})
            elif User.objects.filter(username=username).exists():
                message = 'Cannot create account. The username you entered exists.'
                return render(req,'create-account.html',{'message':message,'sent':True})
            else:
                user = User.objects.create_user(username,email=mail,password=pw)
                user.save()
                user.first_name =  fn
                user.last_name = ln
                user.save()
                ul = userlist(username=username)
                ul.save()
                return render(req,'success.html')
            return redirect('')
        return redirect('')


def handle_logout(request):
    logout(request)
    return redirect('')
def developer(request):
    params ={}
    if request.user.is_authenticated:
        params['loggedin']=1
    else:
        params['loggedin']=0
    return render(request,'developer.html',params)
def myprof(request):

    if request.user.is_authenticated:

        if request.method == 'GET':

            un = request.user.username
            a = request.GET.get('pgno')
            if a is None or a == 0:
                a = 1
            else:
                a = int(a)

            allposts = userpost.objects.filter(user=request.user)
            if allposts:
                n = len(allposts)
            else:
                n = 0
            p = n / 10
            if p % 1 == 0:
                p = int(p)
            else:
                p = math.ceil(p)
            if p == 0:
                p = 1
            if a > p:
                a = p
            elif a < 1:
                a = 1

            osts_tobe = allposts[int((a - 1) * 10):int((a * 10) - 1)]
            if len(allposts) > a * 10:
                next_available = True
            else:
                next_available = False
            if int((a - 1) * 10) >= 10:
                prev_available = True
            else:
                prev_available = False
            un = request.user.username
            fn = request.user.first_name
            ln = request.user.last_name
            mail = request.user.email
            params = {'username': request.user, 'firstname':fn,'lastname':ln,'email':mail,'poststoshow': osts_tobe, 'nomber': len(osts_tobe), 'thispg': a,
                          'next': next_available, 'prev': prev_available}
            if next_available:
                params['pn'] = a + 1
            if prev_available:
                params['pp'] = a - 1


            return render(request,'myprof.html',params)
        else:
            return redirect('')
    else:
        return redirect('')

def anotheruser(request,user):
    if request.user.is_authenticated:

        if request.method == 'GET':
            userobj = get_user_model()
            duer= userobj.objects.filter(username=user).first()
            if request.user==duer:
                return redirect('myprof')
            a = request.GET.get('pgno')
            if a is None or a == 0:
                a = 1
            else:
                a = int(a)

            allposts = userpost.objects.filter(user=duer)
            if allposts:
                n = len(allposts)
            else:
                n = 0
            p = n / 10
            if p % 1 == 0:
                p = int(p)
            else:
                p = math.ceil(p)
            if p == 0:
                p = 1
            if a > p:
                a = p
            elif a < 1:
                a = 1

            osts_tobe = allposts[int((a - 1) * 10):int((a * 10) - 1)]
            if len(allposts) > a * 10:
                next_available = True
            else:
                next_available = False
            if int((a - 1) * 10) >= 10:
                prev_available = True
            else:
                prev_available = False
            un = duer.username
            fn = duer.first_name
            ln = duer.last_name
            mail = duer.email
            params = {'username': un, 'firstname': fn, 'lastname': ln, 'email': mail,
                      'poststoshow': osts_tobe, 'nomber': len(osts_tobe), 'thispg': a,
                      'next': next_available, 'prev': prev_available}
            if next_available:
                params['pn'] = a + 1
            if prev_available:
                params['pp'] = a - 1

            return render(request, 'anouser.html', params)
        else:
            return redirect('')
    else:
        return redirect('')


def createpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            content = request.POST.get('contentarea')
            ul = userpost(content=content,user=request.user)
            ul.save()
            return redirect('')
        else:
            return redirect('')
    else:
        return redirect('')
def dummypath(req):
    if req.user.is_authenticated:
        return HttpResponse('looged in')
    else:
        return HttpResponse('not logged in')