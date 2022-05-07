from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# from webApp import taskBd
from . import views

urlpatterns = [
    # path('', views.index),
    # path('test/', include('taskBd.urls'))
    path('',include('taskBd.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
