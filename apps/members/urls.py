from django.urls import path

from . import views

urlpatterns = [
    path(r'^create/', views.MemberCreateView.as_view(), name='create'),
    path(
        r'^(?P<slug>[\w.@+-]+)/',
        views.MemberDetailView.as_view(),
        name='detail'
    ),
]
