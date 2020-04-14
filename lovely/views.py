from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def holy(request):
    return render(request, 'holy.html')

def main2(request):
    if request.method == "POST":
        receivetitle = request.POST.get('title')
        receivecontent = request.POST.get('content')
        return render(request, 'main2.html', {'puttitle': receivetitle, 'putcontent': receivecontent})
    else:
        receivetitle = "값 없음"
        receivecontent = "값 없음"
        return render(request, 'main2.html', {'puttitle': receivetitle, 'putcontent': receivecontent})
