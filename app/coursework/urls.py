from django.contrib import admin
from django.urls import path
from tcgr import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('partnerstores/',views.partnerstores,name='partnerstores'),
    path('referees/',views.referees,name='referees'),
    path('referees/<int:referee_id>/',views.referee_detail,name='referee_detail'),
    path('partnerstores/<int:store_id>/',views.store_detail,name='store_detail'),
    path('cardgames/',views.cardgames,name='cardgames'),
    path('referee_search/',views.searchref,name='referee_search'),
    path('store_search/',views.searchstore,name='store_search'),
    path('login',views.LoginInterfaceView.as_view(), name="login"),
    path('logout',views.LogoutInterfaceView.as_view(), name="logout"),
    path('signup',views.SignupView.as_view(), name="signup"),
    path('profile',views.ProfileView.as_view(),name="profile"),
    path('password/',views.PasswordView.as_view(template_name='change_password.html'),name="password_change"),
    path('category/<str:category>/',views.CategoryView, name="category"),
    path('like/<int:pk>', views.LikeView, name = 'like_referee'),
    path('rate/',views.rate_store,name="rateView"),

]