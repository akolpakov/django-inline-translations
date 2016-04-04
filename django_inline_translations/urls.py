from django.conf.urls import url, patterns
from .views import translate

urlpatterns = patterns('',
    url(r'^$', translate, name='login'),
)
