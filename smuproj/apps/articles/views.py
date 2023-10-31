from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.http import HttpResponse
from .models import Article


# def index(request):
#     return HttpResponse("Йа йа, май Фюрер!")
#
#
# def test(request):
#     return HttpResponse('ВЫПЬЕМ ВОДЫ БАЙКАЛЬСКОЙ, БРАТЬЯ РУСЫ!!!')

# название приложения (для однозначного указания псевдонимов url)
app_name = 'articles'


def index(request):
    latest_articles_list = Article.objects.order_by('-pub')[:5]
    return render(request, 'articles/list.html',
                  {'latest_articles_list': latest_articles_list})

 
def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена. МОХ')
    
    latest_comm_list = a.comment_set.order_by('id')[:10]
    return render(request, 'articles/detail.html',
                  {
                      'article': a,
                      'latest_comm_list': latest_comm_list
                  })
 
 
def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена. МОХ МОХ')
    
    a.comment_set.create(author_name=request.POST['inname'],
                         comment_text=request.POST['incommenttext'])
    return HttpResponseRedirect(
        reverse('articles:detail', args=(a.id,)))
