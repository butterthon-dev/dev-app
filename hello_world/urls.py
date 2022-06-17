from django.urls import path

from hello_world.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
