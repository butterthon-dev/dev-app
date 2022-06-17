from django.http import HttpResponse
from django.views import View

from hello_world.models import User


class IndexView(View):
    def get(self, request):
        user = User.objects.first()
        return HttpResponse(f'Hello World <br /> {user.email}')
