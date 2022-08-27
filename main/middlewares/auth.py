from django.shortcuts import redirect
from requests import request



def auth_middleware(get_response):
    def middleware(request):
        print(request.session.get('hodadmin'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
            return redirect(f'login?retunr_url ={returnUrl}')
        response = get_response(request)
        return response
    return middleware