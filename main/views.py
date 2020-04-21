from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, UserForm, VoteForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Candidate


# Create your views here.
def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated and user.is_admin:
        return redirect('index')
    elif user.is_authenticated and not user.is_admin:
        return redirect('vote')

    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            card_id = request.POST['card_id']
            password = request.POST['password']
            user = authenticate(card_id=card_id, password=password)

            if user:
                login(request, user)
                if user.is_admin:
                    return redirect('index')
                else:
                    return redirect('vote')

    else:
        login_form = LoginForm()

    context['login_form'] = login_form
    return render(request, 'main/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def index(request):
    user = request.user
    if user.is_authenticated and user.is_admin:
        return render(request, 'main/index.html')
    else:
        return redirect('logout')


def vote(request):
    user = request.user
    if user.candidate_voted != None:
        return redirect('commit_vote')

    if user.is_authenticated:
        context = {}
        if request.POST:
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                candidate = Candidate.objects.filter(number=request.POST['candidate_number'])
                if candidate:
                    user.candidate_voted = candidate[0]
                    user.save()
                    return redirect('commit_vote')
                else:
                    vote_form = VoteForm(request.POST)
                    context['vote_form'] = vote_form
                    context['incorrect_number'] = True
        else:
            vote_form = VoteForm(request.POST)
            context['vote_form'] = vote_form
        return render(request, 'main/vote.html', context)
    else:
        return redirect('/')


def register(request):
    user = request.user
    if user.is_authenticated and user.is_admin:
        context = {}
        if request.POST:
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect('index')
            else:
                context['user_form'] = user_form
        else:
            user_form = UserForm(request.POST)
            context['user_form'] = user_form
        return render(request, 'main/register.html', context)
    else:
        return redirect('logout')


def result(request):
    user = request.user
    if user.is_authenticated and user.is_admin:
        context = {'total_votes': []}
        for candidate in Candidate.objects.all():
            context['total_votes'].append(
                (
                    candidate, 
                    len(User.objects.filter(candidate_voted=candidate))
                )
            )
        return render(request, 'main/result.html', context)
    else:
        return redirect('logout')


def commit_vote(request):
    return render(request, 'main/commit_vote.html')
