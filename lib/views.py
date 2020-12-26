from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from .forms import ShippingForm
# Create your views here.
def home(request):

    item= Item.objects.all()
    context={
        'item':item
    }

    return render(request, 'index.html', context)




def singleproduct(request,id):
    pro= Item.objects.get(id=id)
    context={'pro':pro}

    return render(request, 'product-details.html',context)



@login_required
def add_to_cart(request, id):
    item= get_object_or_404(Item, id=id)
    order_item, created= Orderitem.objects.get_or_create(item=item,
    user=request.user,
    ordered=False
    )
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order= order_qs[0]
        if order.items_order.filter(item__id=item.id).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item was updated")
        else:
            order.items_order.add(order_item)
            messages.info(request, "Your book was added to your cart")
            return redirect("cart")
    else:
        order= Order.objects.create(user=request.user)
        order.items_order.add(order_item)
        messages.info(request, "Your book was added to your cart")
        
    return HttpResponseRedirect(reverse("cart"))   

        
@login_required
def remove_from_cart(request,id):
    item= get_object_or_404(Item, id=id)
    order_qs= Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order=order_qs[0]
        if order.items_order.filter(item__id=item.id).exists():
            order_item= Orderitem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items_order.remove(order_item)
            messages.info(request, "Your book was removed from your cart")
            return redirect("cart")
        else:
            messages.info(request, "Your book was not in your cart")
            return redirect("singleproduct", id=id)
    else:
        messages.info(request, "You donot have an active order")
        return redirect("singleproduct", id=id)
        
@login_required
def remove_single_item_cart(request,id):
    item= get_object_or_404(Item, id=id)
    order_qs= Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order=order_qs[0]
        if order.items_order.filter(item__id=item.id).exists():
            order_item= Orderitem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity>1:
                order_item.quantity -=1
                order_item.save()
            else:
                order.items_order.remove(order_item)

            messages.info(request, "Your book was updated")
            return redirect("cart")
        else:
            messages.info(request, "Your book was not in your cart")
            return redirect("cart")
    else:
        messages.info(request, "You donot have an active order")
        return redirect("cart")
        

@login_required
def cart(request):
    try:
        crt_order= Order.objects.get(user=request.user, ordered=False)
        context= {'crt_order':crt_order}
        return render(request, 'cart.html', context)

    except ObjectDoesNotExist:
        messages.error(request,"You do not have an active order")
        return redirect("/")


def shipping(request):
    
    if request.method=='POST':
        form= ShippingForm(request.POST)
        
        # order= Order.objects.get(user=self.request.user, ordered=False)
        if form.is_valid():
            form.save()
            print("data saved")
            return redirect('/shipping')
        
    
    context={'form': form}

    return render(request, 'checkout.html', context)
    
# class ShippingView(View):
#     def get(self, *args, **kwargs):
#         form= ShippingForm()
#         context={'form': form}

#         return render(self.request, 'checkout.html', context)
    
#     def post(self, *args, **kwargs):
#         form= ShippingForm(self.request.POST or None)
#         if form.is_valid():
#             print("correct")
#             return redirect('/shipping')

        