from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from core.models import Events ,Product , Category
# from shopDashboard.models import Shop
# from userauth.models import User
# from .forms import AddEventForm
from django.contrib import messages

# Create your views here.
def dashboard_view(request):
    # user_id = request.user
    event = Events.objects.all()

    context = {
        'event':event,
    }

    return render(request, './dash_users/index.html',context)


# def add_view(request):
#     if request.method == 'POST':
        

#     return render(request, './dash_users/add.html')


def product_view(request):
    cat = request.GET.get('cat')
    category = Category.objects.filter(title=cat).first()
    product = Product.objects.filter(category=category)

    context = {
        'product':product,
    }

    return render(request, './dash_users/products.html',context)


def profile_view(request):
    return render(request, './dash_users/profiles.html')