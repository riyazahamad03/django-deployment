from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    context_dict={'text':"Welcome To Django Website ",'Number':0}
    return render(request,'basic_app/other.html',context_dict)

def relative(request):
    return render(request,'basic_app/relative_url_template.html')
