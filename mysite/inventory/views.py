from django.shortcuts import render
# from django.http import HttpResponse -> Only need this if you're directly writing html

# Create your views here.

#posts is used for variables. It is a list of dicts
posts = [
    {
        'author':'Abdul Shaik',
        'title':'ML in Mfg.',
        'content':'First post content',
        'date_posted':'2024-11-04'
    },
    {
         'author':'Reena Shaik',
        'title':'React racha',
        'content':'Second post content',
        'date_posted':'2024-11-05'
    }

]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'inventory/home.html',context)#context will used in the template to pass variables

def about(request):
    # return HttpResponse('<h1> Blog: about <h1> Best site ever')
    return render(request,'inventory/about.html',{'title':'About'}) #This is passing the data to the variable in about.html title
