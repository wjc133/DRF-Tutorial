from django.conf.urls import url, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from snippets.views import SnippetViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    # url(r'^root/$', views.api_root),
    # url(r'^snippets/$', snippet_list, name='snippet-list'),
    # url(r'^snippet/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    # url(r'^snippet/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    # url(r'^users/$', user_list, name='user-list'),
    # url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
