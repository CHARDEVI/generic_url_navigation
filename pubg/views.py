from django.shortcuts import render

# Create your views here.

def bot(request):
    return render(request,'bot.html')


def pro(request):
    return render(request,'pro.html')