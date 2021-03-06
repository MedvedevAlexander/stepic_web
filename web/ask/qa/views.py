from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST
from .models import Question, Answer
from django.contrib.auth.models import User
import random
from .forms import NameForm, AuthorForm, BookForm, AskForm, AnswerForm
from django.urls import reverse


@require_GET
def index(request, *args, **kwargs):
    questions = Question.objects.new()
    limit = 10

    # check data type
    try:
        page = int(request.GET['page'])
    except ValueError:
        raise Http404

    paginator = Paginator(questions, limit)

    # check page range
    if page > max(paginator.page_range):
        raise Http404

    p = paginator.page(page)
    context = {
        'paginator': p
    }

    return render(request, 'qa/index.html', context)


@require_GET
def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    limit = 10

    # check data type
    try:
        page = int(request.GET['page'])
    except ValueError:
        Http404

    paginator = Paginator(questions, limit)

    # check page range
    if page > max(paginator.page_range):
        raise Http404

    p = paginator.page(page)
    context = {
        'paginator': p
    }

    return render(request, 'qa/index.html', context)


def question(request, *args, **kwargs):
    # check data type
    try:
        question_id = int(kwargs['question_id'])
    except ValueError:
        raise Http404
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(question)
            url = reverse('ask:question', args=[question_id])
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()

    context = {
        'question': question,
        'form': form
    }

    return render(request, 'qa/question.html', context)


def test(request, *args, **kwargs):
    return HttpResponse('OK test')


def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = reverse('ask:question', args=[question.pk])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    context = {
        'form': form
    }
    return render(request, 'qa/ask.html', context)


def get_name(request, *args, **kwargs):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = AuthorForm()
    context = {
        'form': form
    }

    return render(request, 'qa/name.html', context)


def thanks(request, *args, **kwargs):
    return HttpResponse('Thank you for your attention')
'''
Пользователи лайкают вопросы случайным образом

    users = User.objects.all()
    questions = Question.objects.all()

    for question in questions:
        for user in users:
            if random.randint(0, 1):
                question.likes.add(user)
            else:
                continue
'''

