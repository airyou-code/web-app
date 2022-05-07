from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# print(path('', views.СhangingTest.as_view(), name='iqtest'))

urlpatterns = [
    # path('', views.test2),
    path('', views.СhangingTest.as_view(), name='iqtest')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
