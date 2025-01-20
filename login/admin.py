from django.contrib import admin
from .models import Profile,UserDetails,Claim,PurchasedPolicy,InsurancePolicy

admin.site.register(Profile)
admin.site.register(UserDetails)
admin.site.register(Claim)
admin.site.register(PurchasedPolicy)
admin.site.register(InsurancePolicy)