from django.shortcuts import render
from .models import TempModel

# Create your views here.


def Home(request):

    # get today's date

    # filter temp by the date
    temp = TempModel.objects.filter()

    # render the page
    return render(request, 'index.html')


def receiveData(request):
    # get sensor data
    data = request.POST['data']

    # # create an instance of TempModel
    # temp = TempModel()

    # # assign data to the fields
    # temp['tempValue'] = data

    # # save the data
    # temp.save()

    print("data from arduino: ", data)
