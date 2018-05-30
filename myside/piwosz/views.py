from django.shortcuts import render

def post_list(request):
    return render(request, 'piwosz/post_list.html', {})
