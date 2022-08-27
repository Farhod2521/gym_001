
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy
from .models import Customers
from .forms import CustomersForms
from django.views.generic import  UpdateView, DetailView, DeleteView

def error404(request, exception):
    return render(request, '404.html')
class CustomerUpdate(UpdateView):
    model = Customers
    template_name  = 'customer_edit1.html'
    fields = "__all__"
class CustomersDeleteView(DeleteView):
    model = Customers
    template_name = "customer_delete.html"
    success_url = reverse_lazy("customers_table")
    
class CustomersDetail(DetailView):
    model= Customers
    template_name = 'customers_edit.html'
    fields = '__all__'
def home(request):
    return render(request, 'index.html')


def customers_edit(request, pk):
    customers = Customers.objects.filter(id=pk)
    content = {
        'customers':customers
    }
    return render(request,'customers_edit.html', content)

def customer_form_views(request):
    if request.method == 'POST':
        form = CustomersForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("customers_table")

    else:
        form = CustomersForms()
        content = {
            'form':form,
        }
        return render(request, 'customer_form.html', content)








def customers_table(request):
    customers =  Customers.objects.all()
    
    #customer.delete()


    content = {
        'customers':customers
    }
    return render(request, 'table.html', content)
# Create your views here.
