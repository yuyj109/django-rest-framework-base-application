from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include([
        path('users/', include('myapps.users.urls', namespace='users'))
    ])),
    re_path(r'^', RedirectView.as_view(url=reverse_lazy('api/users/'), permanent=False)),
]
