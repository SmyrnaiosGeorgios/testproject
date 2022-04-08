from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from .models import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignupForm, ProfileForm, ChangePasswordForm
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse

def rate_store(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Store.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score' :val},safe=False)
    return JsonResponse({'success':'false'})


def LikeView(request, pk):
    referee = get_object_or_404(Referee, id=request.POST.get('pk'))
    referee.likes.add(request.user)
    return HttpResponseRedirect(reverse('referee_detail', args=[int(pk)]))


def home(request):
    categories = CategoryStore.objects.all()
    return render(request, 'home.html',{
        'categories': categories,
    })

def CategoryView(request, category):
    categories = CategoryStore.objects.all()
    category_stores = Store.objects.filter(entry_fee = category)
    return render(request, 'categories.html', {
        'category_stores' : category_stores,
        'category': category,
        'categories': categories,
    })


def about(request):
    categories = CategoryStore.objects.all()
    return render(request, 'about.html',{
        'categories': categories,
    })

def partnerstores(request):
    categories = CategoryStore.objects.all()
    stores = Store.objects.all()
    return render(request,'partnerstores.html',{
        'stores': stores,
        'categories': categories,
    })

def referees(request):
    categories = CategoryStore.objects.all()
    refs = Referee.objects.all()
    return render(request,'referees.html',{
        'refs' : refs,
        'categories': categories,
    })

def referee_detail(request, referee_id):
    categories = CategoryStore.objects.all()
    try:
        referee = Referee.objects.get(id=referee_id)
    except Referee.DoesNotExist:
        raise Http404('This referee does not exist')
    return render(request,'referee_detail.html',{
        'referee' : referee,
        'categories': categories,
    })


def store_detail(request, store_id):
    categories = CategoryStore.objects.all()
    try:
        store = Store.objects.get(id=store_id)
    except Store.DoesNotExist:
        raise Http404('This store does not exist')
    return render(request,'store_detail.html',{
        'store' : store,
        'categories': categories,
    })

def cardgames(request):
    categories = CategoryStore.objects.all()
    cardgames = Cardgame.objects.all()
    return render(request,'cardgames.html',{
        'cardgames' : cardgames,
        'categories': categories,
    })

def searchref(request):
    if request.method == "POST":
        keyword = request.POST["q"]
        categories = CategoryStore.objects.all()
        results = Referee.objects.filter(name__icontains = keyword) | Referee.objects.filter(lastname__icontains = keyword) | Referee.objects.filter(gender__iexact = keyword)
        return render(request, 'referee_search.html', {
        "referee_results" : results,
        'categories': categories,
        })

def searchstore(request):
    if request.method == "POST":
        categories = CategoryStore.objects.all()
        keyword = request.POST["q"]
        results = Store.objects.filter(name__icontains = keyword) | Store.objects.filter(description__icontains = keyword) | Store.objects.filter(entry_fee__iexact = keyword)
        return render(request, 'store_search.html', {
        "store_results" : results,
        'categories': categories,
        })

class LoginInterfaceView(LoginView):
    template_name = 'login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = 'login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = 'home'

    def get_object(self):
        return self.request.user

class PasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('profile')