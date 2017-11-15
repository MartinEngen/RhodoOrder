# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    # Check if the session (for this user) has any errors.
    # If the error exists, use give it to the template and delete the processed error from the session.
    if 'search_car_error_message' in request.session:
        message = request.session['search_car_error_message'].encode('utf8')
        context = {
            'error': True,
            'message': message
        }
        del request.session['search_car_error_message']

    else:
        # Telling the Template that there is no error.
        context = {
            'error': False,
        }

    return render(request, 'frontPage/index.html', context)
