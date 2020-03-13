from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Girl

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new', views.add_new, name="add_NEW"),
    path('top_list', ListView.as_view(queryset=Girl.objects.all(), ordering=['-rating'], template_name='comparing_app/top-list.html')),
    re_path(r'^(?P<pk>\d)$', DetailView.as_view(model=Girl, template_name='comparing_app/individual.html'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
