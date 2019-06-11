from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from pos.models import Customer, Product, Order, OrderItem


def dashboard(request):
    return render(request, 'dashboard.html')

def billing(request):
    if request.method =='GET':
        return render(request, 'billing.html')
    else:
        cid = request.POST.get('customerId', None)
        customer = Customer.objects.get(pk=cid)
        products = list(Product.objects.all())

        return render(request, 'billing_details.html', {'customer': customer, 'products': products})
def order(request):
    if request.method =='POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        customer = Customer.objects.get(pk=data['customer_id'])
        order = Order.objects.create(customer=customer,
                                     total_price=data['total_price'],
                                     success=False)
        for product_id in data['product_id']:
            OrderItem(product=Product.objects.get(pk=product_id), order=order).save()
        if data['total_price'] <= customer.balance:
            customer.balance -= int(data['total_price'])
            customer.save()
            order.success = True
        order.save()
        return render(request, 'order.html', {'success': order.success})
    