from django.db import models
from django.core.mail import send_mail 
from django.conf import settings

from master.models import BaseModel
from master.utils.WB_UNIQUE.create_password import generate_password
from master.utils.WB_UNIQUE.create_otp import generate_otp
from master.utils.WB_UNIQUE.create_primary_key import generate_primary_key
from master.constants.WZ_LABOR_CONST import TASK_STATUS_CHOICES,TASK_PAYMENT_STATUS_CHOICES
from master.utils.WB_UNIQUE.create_filename import generate_filename

import os

# Create your models here.
class LaborRegistration(BaseModel):
    PREFIX = "WBL"
    labor_id = models.CharField(primary_key=True, max_length=255, blank=True)
    addhar_card = models.ImageField(upload_to='')
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True)
    otp = models.CharField(max_length=10, default='111111', blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=False)
    
    def __str__(self):
        return self.labor_id

    def save(self, *args, **kwargs):
        if not self.pk:

            # generate labor_id
            last_labor = LaborRegistration.objects.order_by('-create_at').first()
            if last_labor:
                last_numeric_part = int(last_labor.labor_id[len(self.PREFIX):])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:04}" 
            else:
                new_id = f"{self.PREFIX}0001"

            self.labor_id = new_id

            # generate password
            self.password = generate_password()

            # generate otp
            self.otp = generate_otp()

            subject = 'Your OTP for Email Verification | WORK-BOOK'

            message = f"""
            Dear Labor,

            Your OTP for email verification is [{self.otp}]. Please enter this code to complete the verification process.
            Thank you,
            WORK-BOOK admin
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [f'{self.email}']
            send_mail(subject, message, from_email, recipient_list)


        super().save(*args, **kwargs)


class LaborProfile(BaseModel):
    POSTFIX = 'labor_profile'
    DIR_NAME = 'labor_profiles'
    labor_id = models.ForeignKey(LaborRegistration, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to=generate_filename, default='default_images/labor_profile_images.jpg')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

        
class Party(BaseModel):
    POSTFIX = 'party'
    party_id = models.CharField(max_length=255, primary_key=True, blank=True)
    labor_id = models.ForeignKey(LaborRegistration, on_delete=models.CASCADE)
    party_name = models.CharField(max_length=255, unique=True)
    party_email = models.EmailField(max_length=255, unique=True)
    party_mobile = models.CharField(max_length=255)
    party_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.party_id}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.party_id = generate_primary_key(self)
        super().save(*args, **kwargs)


class Task(BaseModel):
    POSTFIX = 'task'
    task_id = models.CharField(max_length=255, primary_key=True, blank=True)
    labor_id = models.ForeignKey(LaborRegistration, on_delete=models.CASCADE)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    task_start_date = models.DateField()
    task_end_date = models.DateField()
    task_status = models.CharField(max_length=255, default='waiting', choices=TASK_STATUS_CHOICES)
    task_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    task_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    task_remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    task_payment_status = models.CharField(max_length=255, default='pending', choices=TASK_PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return self.task_id
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.task_id = generate_primary_key(self)
            self.task_remaining_amount = self.task_total_amount
        super().save(*args, **kwargs)


class TaskPayment(BaseModel):
    POSTFIX = 'task_payment'
    DIR_NAME = 'payment_proofs'
    task_payment_id = models.CharField(max_length=255, primary_key=True, blank=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    proof = models.ImageField(upload_to=generate_filename)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.task_payment_id = generate_primary_key(self)
        super().save(*args, **kwargs)