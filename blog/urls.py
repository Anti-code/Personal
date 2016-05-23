from django.conf.urls import url, include
from . import views, feed 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name = "index"),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^feed/$', feed.LatestPosts, name = "feed"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name = "entry_detail"),
    url(r'^portfolio/$', views.Portfolio.as_view(), name = "portfolio"),
    url(r'^about/$', views.About.as_view(), name = "about"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
