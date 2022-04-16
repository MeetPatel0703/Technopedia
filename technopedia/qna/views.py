from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Answer, Question
from .forms import QuestionForm, AnswerForm, StatusQuestionForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class AddQue(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'question/addque.html'
    success_url = '/question'


class QdetailView(TemplateView):
    template_name = 'question/quedetail.html'

    def get_context_data(self, id, *args, **kwargs):
        context = super(QdetailView, self).get_context_data(**kwargs)
        fm = AnswerForm
        context['form'] = fm
        question = Question.objects.get(id=id)
        context['question'] = question
        answer = Answer.objects.all().values(
            'id', 'user_id', 'queid', 'answer', 'likecount', 'dislikecount', 'user__username').filter(queid=id)
        context['answer'] = answer

        return context

    def post(self, request, id):
        fm = AnswerForm(request.POST)
        if fm.is_valid():
            user = request.user
            queid = Question.objects.get(id=id)
            answer = fm.cleaned_data['answer']
            reg = Answer(user=user, queid=queid, answer=answer)
            reg.save()
            return HttpResponseRedirect(f'/question/detail/{id}')
        else:
            return render(request, 'question/quedetail.html', {'form': fm})


def addques(request):
    if request.method == 'POST':
        fm = QuestionForm(request.POST)
        if fm.is_valid():
            user = fm.cleaned_data['user']
            title = fm.cleaned_data['title']
            des = fm.cleaned_data['description']
            reg = Question(user_id=user, title=title, description=des)
            reg.save()
            return HttpResponseRedirect('/questions/success/')

    else:
        fm = QuestionForm()
    return render(request, 'question/addque.html', {'form': fm})


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/addque.html'
    success_url = '/question/myque'


class StatusUpdateView(UpdateView):
    model = Question
    form_class = StatusQuestionForm
    template_name = 'question/queanswer.html'
    success_url = '/question/myque'


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'question/quedelete.html'
    success_url = '/question/myque'


class QuestionListView(ListView):
    model = Question
    template_name = 'question/quelist.html'
    context_object_name = 'questions'
    ordering = ['status']
    paginate_by = 5
    paginate_orphans = 1

    def get_ordering(self):
        self.order = self.request.GET.get('order', 'desc')
        selected_ordering = self.request.GET.get('ordering', 'status')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_context_data(self, *args, **kwargs):
        try:
            return super(QuestionListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(QuestionListView, self).get_context_data(*args, **kwargs)


class UserQuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'question/userque.html'
    context_object_name = 'questions'
    ordering = ['id']
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *args, **kwargs):
        try:
            return super(UserQuestionListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(UserQuestionListView, self).get_context_data(*args, **kwargs)


class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Answer.objects.get(pk=pk)

        is_dislike = False
        for dislike in post.dislikecount.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikecount.remove(request.user)

        is_like = False
        for like in post.likecount.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            print(type(post.likecount))
            post.likecount.add(request.user)

        if is_like:
            post.likecount.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class DislikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Answer.objects.get(pk=pk)
        is_like = False
        for like in post.likecount.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likecount.remove(request.user)

        is_dislike = False
        for dislike in post.dislikecount.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike:
            post.dislikecount.add(request.user)

        if is_dislike:
            post.dislikecount.remove(request.user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class QuestionSearch(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        if query:
            question = Question.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query))
            return render(request, 'question/search.html', {'question': question})
        else:
            return render(request, 'question/search.html')
