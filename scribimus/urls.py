from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    #path(r'^$', TemplateView.as_view(template_name='home.html')),
    path(r'^admin/', admin.site.urls),
    path(r'^members/', include('apps.members.urls', namespace='members')),
    path(r'^stories/', include('apps.stories.urls', namespace='stories')),
    #path(r'^members/', include('members.urls', namespace='members')),
    #path(r'^stories/', include('stories.urls', namespace='stories')),
    path(r'^login/$', 'apps.members.views.login_view', name='login'),
    path(r'^logout/$', 'apps.members.views.logout_view', name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
