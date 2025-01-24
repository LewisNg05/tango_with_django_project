from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def index2(request):
    # Add view specific logic.
    # Construct dictionary object.
    context_dict_2 = {'italicmessage': 'Not crunchy, creamy, cookie, candy, nor cupcake.'}

    # Pass to template engine as part of the context.
    # Make use of render().
    return render(request, 'rango/index2.html', context=context_dict_2)

def about(request):
    # Context dictionary is needed.
    context_dict_3 = {'allcapmessage': 'Very crunchy, creamy, a cookie, candy, and cupcake.'}

    # Make use again of render().
    return render(request, 'rango/about.html', context=context_dict_3)
