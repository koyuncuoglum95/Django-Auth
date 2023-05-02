from django.shortcuts import render
from fourth_app.forms import UserForm, UserProfileInfo


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "fourth_app/index.html")


@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')    


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('fourth_app:index'))

def signup(request):
    isUser = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            isUser = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()

    return render(request, 'fourth_app/signup.html',
                            {'user_form': user_form,
                             'profile_form': profile_form,
                             'isUser': isUser})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')



        user = authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('fourth_app:index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse('Invalid Login Supplied!')

    else:
        return render(request, 'fourth_app/signin.html')