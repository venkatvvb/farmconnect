# created by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def kb(request):
    return render(request, 'kb.html')
def wr(request):
    return render(request, 'wr.html')

def sp(request):
    return render(request, 'sp.html')


# def analyze(request):
#     djtext = request.POST.get('text', 'default')
#     removepunc = request.POST.get('removepunc', 'off')
#     removenewline = request.POST.get('removenewline', 'off')
#
#
#     # Check which checkbox is on
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#     elif removenewline == "on":
#         analyzed = ""
#         for char in djtext:
#             if char != "/n":
#                 analyzed = analyzed + char
#         params = {'purpose': 'analyzed = "remove new line"', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#     else:
#         return HttpResponse("Error")

