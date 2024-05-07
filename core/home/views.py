from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from time import sleep

def home(request):
    return render(request, 'home.html')

def stream_response(request):
    
    def streaming_content():
        for i in range(100):
            sleep(0.5)
            yield f'{i}\n' #yield = fornece dados conforme a nescessidade,
    return StreamingHttpResponse(streaming_content())