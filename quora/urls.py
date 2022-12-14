from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from quora.core.views import (
    home,
    password,
    picture,
    profile,
    public_profile,
    settings,
)
from quora.search.views import search
from quora.profile.views import signup, login_request


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^hidden_login', login, {'template_name': 'core/cover.html'}, name='login'),
    url(r'accounts/', include('allauth.urls')),
    url(r'login', login_request, name='login'),
    url(r'^logout', logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^public_profile/(?P<id>\d+)/$', public_profile, name='public_profile'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/profile/$', profile, name='profile'),
    url(r'^settings/password/$', password, name='password'),
    url(r'^questions/', include('quora.questions.urls'), name='questions'),
    url(r'^search/$', search, name='search'),
    url(r'^(?P<username>[^/]+)/$', profile, name='profile'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
