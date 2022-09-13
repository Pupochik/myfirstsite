from django.shortcuts import render, redirect
from .models import news_list
from .forms import news_listForm
from django.views.generic import DetailView


def news_home(request):
    news = news_list.objects.order_by('-date')
    return render (request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = news_list
    template_name = 'news/detail_view.html'
    context_object_name = 'object'

def create(request):
    error = ''
    if request.method == 'POST':
        form = news_listForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма невірно заповнена'

    form = news_listForm()

    data = {
        'form': form,
        'error': error
    }
    return render (request, 'news/create.html', data)


