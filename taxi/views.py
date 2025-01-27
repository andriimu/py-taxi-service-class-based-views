from django.shortcuts import render
from django.views import generic



from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)

class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by('id')
    paginate_by = 5
    template_name = 'manufacturer_list.html'  # Ensure you have this template or adjust the path as needed
    context_object_name = 'manufacturers' 

class CarListView( generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")

class CarDetailView( generic.DetailView):
    model = Car

class DriverListView( generic.ListView):
    model = Driver
    paginate_by = 5

class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")