from asyncio import QueueEmpty
from itertools import count
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import QuestionForm, CommentForm
from .models import Question, Comment
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)

@login_required
@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {
        'form':form
    }
    return render(request, 'eithers/create.html', context)

@require_safe
def detail(request, pk):
    question = Question.objects.get(pk=pk)

    count_a = question.comment_set.filter(pick=1).count()
    count_b = question.comment_set.filter(pick=0).count()
    total_count = count_a+count_b

    per_a = round(count_a / total_count * 100, 1)
    per_b = round(count_b / total_count * 100, 1)

    print('========================================')
    print(count_a)
    print(count_b)
    print('========================================')

    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
        'count_a':count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
    }
    return render(request, 'eithers/detail.html', context)

@login_required
@require_http_methods(['POST', 'GET'])
def comments_create(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
    return redirect('eithers:detail', pk)
    
@login_required
@require_http_methods(['POST', 'GET'])
def update(request, pk):
    
    question = Question.objects.get(pk=pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail', pk)
    else:
        form = QuestionForm(instance=question)
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'eithers/update.html', context)
    
@require_POST
def delete(request, pk):
    question = Question.objects.get(pk=pk)
    question.delete()
    return redirect('eithers:index')

@require_POST
def comments_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('eithers:detail', pk)