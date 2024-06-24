from django.shortcuts import render

# Create your views here.


fulldata={
    'students_details':[
        {'id':'01','name':'Ironman','skill':'Python','percentage':'78','mock':'1*'},
        {'id':'02','name':'Batman','skill':'Java','percentage':'88','mock':'1*'},
        {'id':'03','name':'Shruthi','skill':'Python','percentage':'98','mock':'1*'},
        {'id':'04','name':'Ishwarya','skill':'Python','percentage':'68','mock':'1'},
        {'id':'05','name':'Yuvaraj','skill':'Java','percentage':'78','mock':'1*'},
        {'id':'06','name':'Vasu','skill':'Python','percentage':'74','mock':'1'},
        {'id':'07','name':'Lavanya','skill':'Java','percentage':'48','mock':'1'},
        {'id':'08','name':'Malini','skill':'Python','percentage':'58','mock':'1*'},
        {'id':'09','name':'Mani','skill':'Java','percentage':'12','mock':'1'},
        {'id':'10','name':'Santhosh','skill':'Java','percentage':'24','mock':'1*'},
    ]
}


def index(request):
    return render(request,'index.html',context=fulldata)


def Java(request):
    return render(request,'java.html',context=fulldata)


def Python(request):
    return render(request,'python.html',context=fulldata)


def Onestar(request):
    return render(request,'onestar.html',context=fulldata)