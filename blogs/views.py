from django.shortcuts import render
# Create your views here.
def HomePage(request):
    tags = ['depth camera','teensy3.5','stepping motor','battery']
    return render(request,'templates.html',
    {
        'name':'my senior project',
        'author':'Tanaporn',
        'tags':tags
    })
#hello
