from django.shortcuts import render, redirect

def index(request):
    return render(request, 'amadon_store/index.html')


def buy(request):
    if 'grand_total' not in request.session:
        request.session['grand_total'] = 0
    if 'order_total' not in request.session:
        request.session['order_total'] = 0
    if  'total_number_orders' not in  request.session:
         request.session['total_number_orders'] = 0

    product_id =request.POST['product_id']
    product_guide = {
        '1020' : {'item': 'Acoustic Guitar', 
                'price' : 10000},
        '1005' : {'item': 'Electric Guitar', 
                'price' : 800},
        '1074' : {'item': 'Bass', 
                'price' : 10}      
        }

    current_purchase = {
        'quantity' : request.POST['quantity'],
        'item' : product_guide[product_id]['item'],
        'price' : product_guide[product_id]['price']
        }

    request.session['item'] =  product_guide[product_id]['item']
    order_total = int(current_purchase['quantity']) * current_purchase['price']
    request.session['order_total'] = order_total
    request.session['grand_total'] += order_total
    request.session['total_number_orders'] += 1

    return redirect(checkout)


def checkout(request):
    context = {
        "item": request.session["item"],
        "order_total": request.session["order_total"],
        "total_number_orders": request.session["total_number_orders"],
        "grand_total": request.session["grand_total"]
    }
    return render(request, 'amadon_store/checkout.html', context)