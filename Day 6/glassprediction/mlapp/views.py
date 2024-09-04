from django.shortcuts import render
from django.template import loader
import joblib

def predict(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        cls = joblib.load('glass.sav')
        lis = []
        lis.append(float(request.POST['RI']))
        lis.append(float(request.POST['Na']))
        lis.append(float(request.POST['Mg']))
        lis.append(float(request.POST['Al']))
        lis.append(float(request.POST['Si']))
        lis.append(float(request.POST['K']))
        lis.append(float(request.POST['Ca']))
        lis.append(float(request.POST['Ba']))
        lis.append(float(request.POST['Fe']))

        print(lis)

        ans = cls.predict([lis])
        return render(request, 'result.html', context={'answer':ans})

    return render(request, 'result.html')
