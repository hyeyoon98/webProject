from django.urls import path
from django.conf.urls import url

from .djangoapps.sample import views as SampleViews
from .djangoapps.login import views as LoginViews
from .djangoapps.index import views as IndexViews

urlpatterns = [
    url('sample$', SampleViews.sample, name='sample'),

    url('login$', LoginViews.login, name='login'),

    url('$', IndexViews.index, name='index'),
]
