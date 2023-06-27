from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from quizz.forms import QuestionForm, TestForm
from .models import CheckQuestion, CheckTest, Question, Test
from django.contrib.auth.decorators import login_required
# from .forms import QuestionForm, TestForm

# Create your views here.


def home(request):
    tests = Test.objects.all()
    return render(request, 'index.html', {
        'tests': tests
    })


# signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            print(form.errors)
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

# profile


@login_required(login_url='login')
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {
        'user': user
    })


@login_required(login_url='login')
def ready_to_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'ready_to_test.html', {
        'test': test
    })


@login_required(login_url='login')
def test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    attemps = CheckTest.objects.filter(student=request.user, test=test).count()
    if attemps <= test.max_attemps and (timezone.now() >= test.start_date and timezone.now() <= test.end_date):
        questions = Question.objects.filter(test=test)
        if request.method == 'POST':
            check_test = CheckTest.objects.create(
                student=request.user, test=test)
            for question in questions:
                given_answer = request.POST[str(question.id)]
                print(given_answer+'\n')
                CheckQuestion.objects.create(
                    check_test=check_test,
                    question=question,
                    given_answer=given_answer,
                    true_answer=question.true_answer)
            check_test.save()
            return redirect('check_test', check_test.id)
        return render(request, 'test.html', {
            'test': test,
            'questions': questions
        })
    else:
        print(attemps)
        return HttpResponse("Server Error")


@login_required(login_url='login')
def check_test(request, check_test_id):
    check_test = get_object_or_404(
        CheckTest, id=check_test_id, student=request.user)
    print(check_test)
    return render(request, 'check_test.html', {
        'check_test': check_test
    })


@login_required(login_url='login')
def new_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test_id = form.save(request)
            return redirect('new_question', test_id)
    form = TestForm()
    return render(request, 'new_test.html', {
        'form': form
    })


@login_required(login_url='login')
def new_question(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if test.author == request.user:
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save(test_id)
                if form.cleaned_data['submit_and_exit']:
                    return redirect('home')
                return redirect('new_question', test_id)
        form = QuestionForm()
        return render(request, 'new_question.html', {
            'test': test,
            'form': form
        })
    else:
        return HttpResponse("Server Error")
