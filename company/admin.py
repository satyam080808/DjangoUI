from django.contrib import admin
from .models import CompanyVarity, CompanyReview, Store, CompanyCertificate


class CompanyReviewInline(admin.TabularInline):
    model = CompanyReview
    extra = 2

class CompanyVarirtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CompanyReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('company_varieties',)

class CompanyCertificateAdmin(admin.ModelAdmin):
    list_display = ('company', 'certificate_number')

# Register your models here.
admin.site.register(CompanyVarity, CompanyVarirtyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(CompanyCertificate, CompanyCertificateAdmin)