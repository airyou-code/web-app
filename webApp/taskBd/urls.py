from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# print(path('', views.СhangingTest.as_view(), name='iqtest'))

urlpatterns = [
    path('', views.First),
    # path('<int:pk>', views.СhangingTest.as_view(), name='iqtest'),
    path('get/<int:pk>', views.test),
    path('test/', views.test)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
