from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.views import generic

# Create your views here.
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



# def detail(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# #get方法
# def search_form(request):
#     return render(request,'polls/search_form.html')
#
# def search_get(request):
#     request.encoding='utf-8'
#     ctx = {}
#     if 'q' in request.GET:
#         ctx['message'] = "你搜索的内容为:%s" %request.GET['q']
#     else:
#         ctx['message'] = "你提交了空表单"
#     return render(request,'polls/search_get.html',ctx)
#
# #post方法
#
# # 接收POST请求数据
# def search_post(request):
#     ctx ={}
#     if request.POST:
#         ctx['rlt'] = request.POST['q']
#     return render(request, "polls/search_post.html", ctx)

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
