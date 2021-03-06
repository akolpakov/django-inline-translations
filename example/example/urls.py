from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from .views import index, login_view, logout_view

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^django-inline-translate/', include('django_inline_translations.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', index),
)
