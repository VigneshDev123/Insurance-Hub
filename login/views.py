from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AgencyLoginForm,CustomerLoginForm,SignUpForm,UserDetailsForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import InsurancePolicy, PurchasedPolicy, Claim
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def customer_login(request):
    form = CustomerLoginForm()
    return render(request, 'customer_login.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('user_details.html')  
            else:
                return render(request,"user_details.html")
    else:
        form = CustomerLoginForm()
    
    return render(request, 'customer_login.html', {'form': form})

def customer_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('user_details.html')  
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = SignUpForm()
    return render(request, 'customer_signup.html', {'form': form})

def agency_login_view(request):
    form = AgencyLoginForm()
    return render(request, 'agency_login.html', {'form': form})

def agency_login(request):
    if request.method == "POST":
        form = AgencyLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home.html") 
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AgencyLoginForm()
    return render(request, "agency_login.html", {"form": form})

def Main(request):
    return render(request, "Main.html")

def user_details(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return render(request, 'Main.html')  # Redirect to a success page or URL
    else:
        form = UserDetailsForm()
    return render(request, 'user_details.html', {'form': form})

@login_required
def file_claim(request, purchased_policy_id):
    purchased_policy = get_object_or_404(PurchasedPolicy, id=purchased_policy_id)
    if request.method == 'POST':
        description = request.POST['description']
        claim_amount = request.POST['claim_amount']
        Claim.objects.create(
            purchased_policy=purchased_policy,
            claimant=request.user,
            description=description,
            claim_amount=claim_amount,
        )
        return redirect('claim_list')
    return render(request, 'file_claim.html', {'purchased_policy': purchased_policy})

@login_required
def claim_list(request):
    claims = Claim.objects.filter(claimant=request.user)
    return render(request, 'claim_list.html', {'claims': claims})

@login_required
def policy_list(request):
    policies = InsurancePolicy.objects.all()
    return render(request, 'policy_list.html', {'policies': policies})

@login_required
def purchase_policy(request, policy_id):
    policy = get_object_or_404(InsurancePolicy, id=policy_id)
    PurchasedPolicy.objects.create(policy=policy, customer=request.user)
    return redirect('purchased_policies')

@login_required
def purchased_policies(request):
    purchased_policies = PurchasedPolicy.objects.filter(customer=request.user)
    return render(request, 'purchased_policies.html', {'purchased_policies': purchased_policies})

from django.shortcuts import render
from .models import InsurancePolicy

def policy_list(request):
    policies = InsurancePolicy.objects.all()
    return render(request, 'Main.html', {'policies': policies})



