from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TempModel
from datetime import date

# Create your views here.


def Home(request):
    # filter temp saved last
    temp = TempModel.objects.last()
    context = {'temperature': temp}

    # render the page
    return render(request, 'index.html', context)

@csrf_exempt
def receiveData(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the API token is valid
        api_token = request.GET.get('token', '')
        if api_token != 'your_API_token':
            return HttpResponse('Invalid API token', status=401)

        # Extract the temperature value from the POST request body
        temperature = request.POST.get('temperature', '')
        if not temperature:
            return HttpResponse('Temperature value is missing', status=400)

        # Create a new Temperature object and save it to the database
        temperature_obj = TempModel(tempValue=temperature)
        temperature_obj.save()

        return HttpResponse('Temperature value saved successfully')
    else:
        return HttpResponse('Invalid request method', status=405)