from django.shortcuts import render
from .models import CompanyVarity, Store
from django.shortcuts import get_object_or_404
from .forms import CompanyVarityForm

# Create your views here.
def all_company(request):
    companys = CompanyVarity.objects.all()
    return render(request, 'company/all_company.html', {'companys': companys})


def company_detail(request, company_id):
    company =get_object_or_404(CompanyVarity, pk=company_id)
    return render(request, 'company/company_detail.html', {'company':company})

def company_store_view(request):
    stores = None
    if request.method == 'POST':
        form = CompanyVarityForm(request.POST)
        if form.is_valid():
            company_variety = form.cleaned_data['company_varity']
            stores = Store.objects.filter(company_varieties = company_variety)
    else:
        form = CompanyVarityForm()
    return render(request, 'company/company_stores.html', {'stores': stores, 'form': form})