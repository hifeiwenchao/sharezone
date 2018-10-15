from api.service import sign_in
from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth


class SignIn(View):
    @formatting()
    @auth
    def post(self, request):
        print(request.user)
        sign_in.sign_in(request.user)



