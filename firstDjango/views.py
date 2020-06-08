from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    var = {'name': 'krishna', 'place': 'sasni'}
    return render(request, 'index.html', var)


def analyzer(request):
    text = request.POST.get('analyze', default='true')
    removepunc = request.POST.get('removepunc', 'off')
    upperc = request.POST.get('upperc', 'off')
    removeLine = request.POST.get('removeLine','off')
    analyzed_text = ""
    counter = 0
    punctuations = '''!()-[]{};:'"\+,<>./?@#$%^&*_~'''
    if removepunc == 'on':
        for i in text:
            if i not in punctuations:
                analyzed_text = analyzed_text + i
        counter = 1
    if upperc == 'on':
        if counter == 1:
            analyzed_text = analyzed_text.upper()
        else:
            analyzed_text = text.upper()
        counter = 1
    if removeLine == 'on':
        t =""
        if counter == 1:
            for i in analyzed_text:
                if i != '\n' and i != '\r':
                    t = t + i
            analyzed_text = t
        else:
            analyzed_text = text.replace('\n' , "").replace('\r' , '')
        counter = 1
    if upperc == 'off' and removepunc == 'off' and removeLine == 'off':
        return HttpResponse("hello")
    var1 = {'after_remove_punctuation': analyzed_text}
    return render(request, 'links.html', var1)
