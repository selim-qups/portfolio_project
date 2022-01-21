from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('', include('second_app.urls')),
    path('dashboard/', include('dashboard_app.urls')),
    # path('accounts/', include('allauth.urls')),
]
