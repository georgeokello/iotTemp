from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TempModel
from django.utils import timezone


def Home(request):
    # render the page
    return render(request, 'index.html')


def getSensorData(request):
    # filter temp saved last
    temp = TempModel.objects.last()
    context = {'temperature': str(temp)}
    return JsonResponse(context, safe=False)


@csrf_exempt
def receiveData(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the token is valid
        token = request.GET.get('token', '')
        if token != 'iot_token':
            return HttpResponse('Invalid token', status=401)

        # Extract the temperature value from the POST request body
        temperature = request.POST.get('temp', '')
        if not temperature:
            return HttpResponse('Temperature value is missing', status=400)

        # Create a new Temperature object and save it to the database
        temperature_obj = TempModel(tempValue=temperature)
        temperature_obj.save()

        return HttpResponse('Temperature value saved successfully')
    else:
        return HttpResponse('Invalid request method', status=405)


def liveGraph(request):
    today = timezone.now().date()
    temp = TempModel.objects.filter(time__date =today).values_list('tempValue', flat=True)
    tempArray = [i for i in temp]
    print(tempArray)
    context = tempArray
    return JsonResponse(context, safe=False)