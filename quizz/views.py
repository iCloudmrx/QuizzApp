from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Test
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


@login_required(login_url='login')
def ready_to_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'ready_to_test.html', {
        'test': test
    })


@login_required(login_url='login')
def test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)
    if request.method == 'POST':
        for question in questions:
            given_answer = request.POST[str(question.id)]
    return render(request, 'test.html', {
        'test': test,
        'questions': questions
    })
