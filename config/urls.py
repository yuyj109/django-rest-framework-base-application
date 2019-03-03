from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('users/', include('users.urls', namespace='users'))
    ])),
    re_path(r'^', RedirectView.as_view(url=reverse_lazy('api/users/'), permanent=False)),
]
