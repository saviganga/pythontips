from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('sync-db/', views.sync_db, name='sync_db'),
    path('', views.index, name='homepage'),
    path('search/', views.search_result, name='search-page'),
    path('post/', views.post_tip, name='post-tip'),
    path('signup', views.signup, name='sign-up'),
    path('api/', include('tips.api.url')),
]