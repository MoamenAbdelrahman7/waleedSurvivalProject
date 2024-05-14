from django.urls import path
from . import views
urlpatterns=[
    path("home/",views.home,name="home"),
    path("profile/",views.profile,name="profile"),
    path("upload/",views.upload,name="upload"),
    path("interests/",views.interests,name="interests"),
    path("",views.log_in,name="log_in"),
    path("sign_up/",views.sign_up,name="sign_up"),
    path("log_out/",views.log_out,name="log_out"),
    path("suggest/",views.suggest,name="suggest"),
    path("visite_profile/<str:username>",views.visite_profile,name="visite_profile"),

]