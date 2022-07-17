import django.urls
from django.contrib import admin

urlpatterns = [
    django.urls.path('', django.urls.include('infra_app.urls',
                                             namespace='infra_app')),
    django.urls.path('admin/', admin.site.urls),
]
