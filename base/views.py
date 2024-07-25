from django.shortcuts import render,redirect
from base.models import Coffee
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def menu (request):
    coffees_obj = Coffee.objects.all()
    context ={'coffees':coffees_obj}
    return render(request,'menu.html',context)

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render, redirect
from .models import Coffee

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')  # Retrieve the uploaded image
        
        if name and price:
            try:
                price = float(price)
                Coffee.objects.create(name=name, price=price, image=image)
                return redirect('menu')
            except ValueError:
                # Handle the case where price is not a valid float
                return render(request, 'create.html', {'error': 'Invalid price'})
    
    return render(request, 'create.html')

def edit(request, pk):
    coffees_obj = Coffee.objects.get(id=pk)
    
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')  # Use request.FILES for file uploads

        # Update fields if they are provided
        if name:
            coffees_obj.name = name
        if price:
            try:
                coffees_obj.price = float(price)  # Convert price to float
            except ValueError:
                # Handle invalid price input
                return render(request, 'edit.html', {'coffees': coffees_obj, 'error': 'Invalid price'})
        if image:
            coffees_obj.image = image
        
        coffees_obj.save()
        return redirect('menu')  # Redirect to the menu page
    
    context = {'coffees': coffees_obj}
    return render(request, 'edit.html', context)








def order_dish(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')
        if dish_id:
            try:
                coffee = Coffee.objects.get(id=dish_id)
                # Perform action for the order
                return JsonResponse({'message': 'Your dish has been successfully ordered'}, status=200)
            except Coffee.DoesNotExist:
                return JsonResponse({'error': 'Dish not found'}, status=404)
        return JsonResponse({'error': 'Dish ID not provided'}, status=400)
    
    # For debugging purposes, log the method and return a message
    print(f"Request method: {request.method}")
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def delete(request,pk):
    coffees_obj= Coffee.objects.get(id=pk)
    coffees_obj.delete()
    return redirect('menu')