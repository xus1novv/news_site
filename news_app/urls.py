from django.urls import path

from .views import news_list, news_detail, homePage, contactPageview, errorPageview, \
    MahalliyNewsVeiw, SportListView, TexnoListView, XorijNewsView

urlpatterns = [
    path('', homePage.as_view(), name = 'home_page'),
    path('news/', news_list, name = "all_news_list"),
    path('news/<slug:news>/', news_detail, name = "news_detail_page"),
    path('contact-us/', contactPageview.as_view(), name = "contact_page"),
    path('error_404', errorPageview, name = "404_page"),
    path('mahalliy-news/', MahalliyNewsVeiw.as_view(), name = 'mahalliy_news'),
    path('xorij-news/', XorijNewsView.as_view(), name = 'xorij_news'),
    path('texno-news/', TexnoListView.as_view(), name = 'texno_news'),
    path('sport-news/', SportListView.as_view(), name = 'sport_news')
]
