from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import News, Category
from .forms import ContactForm

def news_list(request):
    news_list = News.published.all()
    # news_list = News.objects.filter(status = News.Status.Published)
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }

    return render(request, 'news/news_detail.html', context)

# def homePage(request):
#     categories = Category.objects.all()
#     news_list1 = News.published.all().order_by('-publish_time')[:5]
#     mahalliy_bir = News.published.filter(category__name = 'Mahalliy').order_by('-publish_time')[:1]
#     mahalliy_news = News.published.all().filter(category__name = 'Mahalliy').order_by('-publish_time')[1:5]
#     context = {
#         'categories': categories,
#         'news_list1': news_list1,
#         'mahalliy_bir' : mahalliy_bir,
#         'mahalliy_news':mahalliy_news
#
#     }
#
#     return render(request, 'news/home.html', context)

class homePage(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list1'] = News.published.all().order_by('-publish_time')[:5]
        context['mahalliy_news'] = News.published.all().filter(category__name = 'Mahalliy').order_by('-publish_time')[:5]
        context['xorij_news']  = News.published.all().filter(category__name = 'Xorij').order_by('-publish_time')[:5]
        context['texnologiya_news'] = News.published.all().filter(category__name = 'Texnologiya').order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name = 'Sport').order_by('-publish_time')[:5]

        return context

# def contactPageview(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():  ### yani request ni oladi va formlarni olganda
#         ### hammasi to'liq kiritilganmi yo'qmi shuni tekshiradi is_valid()
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur!!!</h2>")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)


class contactPageview(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form":form
        }

        return render(request, "news/contact.html", context)

    def post(self,request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur!!! </h2>")
        context = {
            'form':form
        }
        return render(request, "news/contact.html", context)


def errorPageview(request):
    context = {

    }
    return render(request, 'news/404.html', context)

class MahalliyNewsVeiw(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Mahalliy')
        return news

class XorijNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Xorij')
        return news

class TexnoListView(ListView):
    model = News
    template_name = 'news/texno.html'
    context_object_name = 'texno_yangiliklar'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Texnologiya')
        return news

class SportListView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Sport')
        return news
