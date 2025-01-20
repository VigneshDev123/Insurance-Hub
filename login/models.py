from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class UserDetails(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)  # You can use choices for this
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    about_you = models.TextField()
    home_type = models.CharField(max_length=10, choices=[('rent', 'Rent'), ('own', 'Own')])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.CharField(max_length=15, choices=[('two_wheeler', '2 Wheeler'), ('four_wheeler', '4 Wheeler'), ('other', 'Other')])
    health_details = models.CharField(max_length=50, choices=[('prolonged_health_issues', 'Prolonged health issues'), ('seasonal_flu', 'Prone to seasonal flu'), ('general_health_issues', 'General health issues')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class InsurancePolicy(models.Model):
    POLICY_TYPES = [('Health', 'Health'), ('Life', 'Life'), ('Auto', 'Auto'), ('Home', 'Home')]
    policy_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(choices=POLICY_TYPES, max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PurchasedPolicy(models.Model):
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Claim(models.Model):
    CLAIM_STATUS = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]
    purchased_policy = models.ForeignKey(PurchasedPolicy, on_delete=models.CASCADE)
    claimant = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=CLAIM_STATUS, max_length=10, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

