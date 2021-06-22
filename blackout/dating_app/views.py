from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import *
from .models import *
from datetime import date

# Create your views here.
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        profiles = Profile.objects.filter(creator_id = request.session['user_id'])
        # birthdays =  Profile.objects.all()
        # birthday_list = []
        # def calculate_age(born):
        #     today = date.today()
        #     return today.year - born.year
        # for user_age in birthdays:
        #     age = calculate_age(user_age.birthday)
        #     birthday_list.append(age)

        if profiles: 
            context = {
                "creator": profiles[0],
                "profiles": Profile.objects.all(),
                "this_user": User.objects.get(id = request.session['user_id']),
                # "birthdays": birthday_list
            }
        else:
            context = {
                "profiles": Profile.objects.all(),
                "this_user": User.objects.get(id = request.session['user_id']),
                # "birthdays": birthday_list
            } 
        return render(request, "dashboard.html", context)

def edit_user(request, user_id):
    user_id = User.objects.get(id = request.session['user_id'] )
    context = {
        "user": user_id,
        'profile': Profile.objects.filter(creator_id = user_id)[0]
    }
    return render(request, 'editprofile.html', context)

def create_profile(request):
    if request.method == 'POST':
        message_errors = Profile.objects.validator(request.POST)
        if len(message_errors) > 0:
            for key, value in message_errors.items():
                messages.error(request, value)
        else:
            Profile.objects.create(
                gender = request.POST['gender'],
                birthday = request.POST['birthday'],
                color = request.POST['color'],
                sport = request.POST['sport'],
                movie = request.POST['movie'],
                music = request.POST['music'],
                creator = User.objects.get(id = request.session['user_id'])
            )
    return redirect('/dashboard')

def update(request, user_id):
    if request.method == 'POST':
        message_errors = Profile.objects.updater(request.POST)
        if len(message_errors) > 0:
            for key, value in message_errors.items():
                messages.error(request, value)
        else:
            profile = Profile.objects.get(id = user_id)
            profile.color = request.POST['color']
            profile.sport = request.POST['sport']
            profile.movie = request.POST['movie']
            profile.music = request.POST['music']
            profile.save()
    return redirect(f'/dashboard/edit/{user_id}')

def show_userprofile(request, user_id):
    context = {
        'user': User.objects.get(id = user_id),
        'profile': Profile.objects.filter(creator_id = user_id)[0]
    }
    return render(request, 'user.html', context)

def add_like(request, user_id):
    liked_user = Profile.objects.get(id = user_id)
    user_liking = User.objects.get(id = request.session['user_id'])
    liked_user.user_likes.add(user_liking)
    return redirect('/dashboard')

def remove_like(request, user_id):
    disliked_user = Profile.objects.get(id = user_id)
    user_disliking = User.objects.get(id = request.session['user_id'])
    disliked_user.user_likes.remove(user_disliking)
    return redirect('/dashboard')

def show_matches(request, user_id):
    user_id = User.objects.get(id = request.session['user_id'] )
    context = {
        'user': user_id
    }
    return render(request, 'matches.html', context)

def image_upload_view(request, user_id):
    """Process images uploaded by users"""
    if request.method == 'POST':
        profile = Profile.objects.filter(creator_id = user_id)[0]
        profile.image = request.FILES["image"]
        profile.save()
    return redirect('/dashboard')