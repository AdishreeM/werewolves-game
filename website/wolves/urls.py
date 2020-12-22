from django.urls import include, path
from . import views

urlpatterns = [
    # UI Bundle
    path('', views.IndexView.as_view(), name='index'),

    # APIs
    path('api/', include('wolves.api.urls')),
    path('ui/', include('wolves.ui.urls'))
]