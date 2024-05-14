from django.shortcuts import render,redirect,reverse,HttpResponse
from .models import Video,UserInfo,UserInterests,Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def recommend_videos(videos, interests):
    recommendations = []
    for video in videos:
        # Calculate intersection of video tags and user interests
        video_tags=[video.tag1,video.tag2,video.tag3]
        print("video_tags",video_tags)
        common_tags = set(video_tags).intersection(set(interests))
        # Add video to recommendations if there are common tags
        if common_tags:
            recommendations.append((video, len(common_tags)))

    # Sort recommendations based on the number of common tags, descending
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [rec[0] for rec in recommendations]  # Return only video data, not the count

@login_required
def home(request):
    print(request.user)
    videos = Video.objects.filter().exclude(user__username=request.user.username)
    user_interests = UserInterests.objects.get(user__username=request.user.username)
    if user_interests is not None and user_interests.name is not None:
        user_interests=user_interests.name.split(",")
        print("user_interests", user_interests)
        recommended_videos = recommend_videos(videos, user_interests)
    else:
        recommended_videos=Video.objects.filter().exclude(user__username=request.user.username)
    context={
         "videos":recommended_videos,

     }
    return render(request,"index.html",context)

@login_required
def profile(request):
    profile_videos=Video.objects.filter(user__username=request.user.username)
    context={
        "profile_videos":profile_videos,
        "user":Account.objects.get(username=request.user.username),

    }
    return render(request,"profile.html",context)

@login_required
def upload(request):  # GET
    if request.method=="POST":
        new_video=Video(
            title= request.POST.get("title"),
            category = request.POST.get("category"),
            video_url = request.FILES.get("video_url"),
            description = request.POST.get("description"),
            tag1 = request.POST.get("tag1"),
            tag2 = request.POST.get("tag2"),
            tag3 = request.POST.get("tag3"),
            love = request.POST.get("love"),
            comment = request.POST.get("comment"),
            share = request.POST.get("share"),
            user= request.user,
        )
        new_video.save()
        return redirect(reverse("home"))
    return render(request,"upload.html")

def interests(request): # GET
    if request.method=="POST":
        interests=UserInterests(
            name=request.POST.get("name"),
            user= request.user,
        )
        interests.save()
        return redirect(reverse("home"))
    return render(request,"interests.html")

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user,"================================")
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    return render(request,"login.html")

def sign_up(request):
    if request.method=="POST":
        new_account=Account(
            username=request.POST.get("username"),
            name = request.POST.get("name"),
            birthday =request.POST.get("birthday"),
            personal_img =request.FILES.get("personal_img"),
        )
        new_account.save()
        user = User.objects.create(username=request.POST.get("username"))
        user.set_password(request.POST.get("password"))
        user.save()
        login(request,user)
        return redirect(reverse("interests"))
    return render(request,"signup.html")

def log_out(request):
    logout(request)
    return redirect(reverse("log_in"))


def suggest(request):
    friends=Account.objects.filter().exclude(username=request.user.username)
    context={
        "friends":friends
    }
    return render(request,"Friends_suggission.html",context)

def visite_profile(request,username):
    if username:
        friend=Account.objects.get(username=username)
        profile_videos=Video.objects.filter(user__username=username)
        context={
            "user":friend,
            "profile_videos":profile_videos,
        }
        return render(request,"visite_profile.html",context)
    else:
        return HttpResponse("<Invaid username>")



# Sample videos data
# videos = [
#     {'id': 1, 'title': "How to Start Programming", 'tags': ['programming', 'coding', 'tutorial']},
#     {'id': 2, 'title': "Top 10 Python Tips", 'tags': ['python', 'programming', 'tips']},
#     {'id': 3, 'title': "The History of Python", 'tags': ['python', 'history']},
#     {'id': 4, 'title': "Nature Documentary", 'tags': ['nature', 'wildlife']},
#     {'id': 5, 'title': "Deep Dive into Java", 'tags': ['java', 'programming', 'tutorial']},
# ]

"""def recommendation():
    videos=Video.objects.filter().exclude(user__username=request.user.username)
    user_interests=UserInterests.objects.get(user__username=request.user.username).name.split(",")
    print("user_interests",user_interests)
    recommended_videos=recommend_videos(videos,user_interests)
    return recommended_videos"""


# User profile
# user_interests = ['python', 'programming']




# recommend vedios based on similarity
"""def recommend_videos(videos, interests):
    recommendations = []
    for video in videos:
        # Calculate intersection of video tags and user interests
        video_tags=[video.tag1,video.tag2,video.tag3]
        print("video_tags",video_tags)
        common_tags = set(video_tags).intersection(set(interests))
        # Add video to recommendations if there are common tags
        if common_tags:
            recommendations.append((video, len(common_tags)))

    # Sort recommendations based on the number of common tags, descending
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [rec[0] for rec in recommendations]  # Return only video data, not the count"""

# Get recommendations
# recommended_videos = recommend_videos(videos, user_interests)

# Display recommended videos
# for video in recommended_videos:
#     print(f"Recommended Video: {video['title']} - Tags: {', '.join(video['tags'])}")



























