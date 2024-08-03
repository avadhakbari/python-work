from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from decimal import Decimal
from django.db.models import Sum

from .models import LaborRegistration,Party,Task,TaskPayment,LaborProfile
from master.utils.WB_UNIQUE.create_otp import generate_otp


from functools import wraps


# Create your views here.

# for login required 

def login_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if 'labor_id' not in request.session:
            messages.info(request, 'your are not logged in yet')
            return redirect('login_view')
        
        else:
            return function(request, *args, **kwargs)
        
    return wrapper
            

#auth view
def login_view(request):
    if request.method == 'POST':
        labor_id_ = request.POST['labor_id']
        password_ = request.POST['password']

        try:
            get_labor = get_object_or_404(LaborRegistration, labor_id=labor_id_)

            if get_labor.is_activate:
                if get_labor.password == password_:
                    #store labor id into the session
                    request.session['labor_id'] = labor_id_
                    messages.info(request, f'Hello, {labor_id_}, Now you are logged In.')
                    return redirect('dashboard_view')
                else:
                    messages.info(request, f'Labor_id or password does not match')
                    return redirect('login_view')
            else:
                messages.info(request, f'Your account is deactivated.\nPlease contact to admin.')
                return redirect('login_view')
            
        except LaborRegistration.DoesNotExist:
            messages.info(request, f'Labor_id or password does not match')
            return redirect('login_view')


    return render(request, 'labor\login.html')


def register_view(request):
    if request.method == 'POST':
        addhar_card_ = request.FILES['addhar_id']
        email_ = request.POST['email']
        mobile_ = request.POST['mobile']

        new_labor = LaborRegistration.objects.create(
            addhar_card=addhar_card_,
            email=email_,
            mobile=mobile_
        )
        new_labor.save()
        new_labor_profile = LaborProfile.objects.create(
                labor_id_id=new_labor.labor_id
            )
        new_labor_profile.save()
        context = {
            'labor_email':email_
        }
        messages.success(request, f'Please check your {email_} for OTP verificaation.')
        return render(request, 'labor\otp_verification.html', context)

    return render(request, r'labor\register.html')


def otp_varification_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']

        try:
            get_labor = get_object_or_404(LaborRegistration, email=email_)
            if get_labor.otp == otp_:
                get_labor.is_email_verified = True
                get_labor.save()


                #when submited OTP than after send labor_id and password
                subject = 'your id and password | work-book'
                message = f"""
                Dear Labor,

                Your Id and Password  is [{get_labor.labor_id},{get_labor.password}]. please save this password for your information..
                Thank you,
                WORK-BOOK admin
                """
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [f'{get_labor.email}']
                send_mail(subject, message, from_email, recipient_list)


                messages.success(request, f"your {email_} is varified successfully...!!!" )
                return redirect('login_view')
            
            else:
                messages.error(request, 'Invalid OTP!!!')
                context = {
                    'labor_email':email_
                }
                return render(request, 'labor\otp_verification.html', context)

            
        except LaborRegistration.DoesNotExist:
            messages.info(request, f" your {email_} is invalid...!!!")

          
            return redirect('login_view')
        

def  forgot_pass_email(request):
    
    if request.method == "POST":
        email_ = request.POST['email']
        

        try:
            print("hello")
            get_labor = get_object_or_404(LaborRegistration, email=email_)
            
            print(get_labor)
            if get_labor.email == email_:
                otp = generate_otp()
                get_labor.otp = otp
              
                get_labor.save()
        

                subject = 'Your OTP for Email Verification | WORK-BOOK'

                message = f"""
                Dear Labor,

                Your OTP for the forgot password is [{otp}]. Please enter this code to complete the generate a new password.
                Thank you,
                WORK-BOOK admin
                """
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [f'{email_}']
                send_mail(subject, message, from_email, recipient_list)
                
                return redirect('new_password')

            else:
               
                messages.info(request, f"your {email_} is does not match...!!!" )
                return redirect('login_view')
                

        except LaborRegistration.DoesNotExist:
            messages.info(request, f" your emial does not match...!!!")
            return redirect('login_view')

        except Exception as error:
            messages.info(request, f"{error}")
            return redirect('login_view')     

    return render(request, r'labor\forgot_pass_email.html')



def new_password(request):
    if request.method == 'POST':
        otp_ = request.POST['otp']
        new_password_ = request.POST['new_password']
        conf_password_ = request.POST['conf_password']

        try:
            get_labor =  get_object_or_404(LaborRegistration, otp = otp_)
            if get_labor.otp == otp_:
                if new_password_ == conf_password_:
                    get_labor.password = new_password_
                    get_labor.save()

                    subject = 'your id and password | work-book'
                    message = f"""
                    Dear Labor,

                    Your Id and Password is : [{get_labor.labor_id}, {get_labor.password}]. please save this password and id for your informations.
                    Thank you,
                    WORK-BOOK admin
                    """
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [get_labor.email]
                    send_mail(subject, message, from_email, recipient_list)

                    messages.success(request, "your Password is changed successfully...!!!")
                    return redirect('login_view')
                else:
                    messages.error(request, 'Not Match your both Password....!!!')
                    return redirect('new_password')
            else:
                messages.error(request, 'your otp does not match.....!!!!')
                return redirect('forgot_pass_email')
            
        except LaborRegistration.DoesNotExist:
            messages.info(request, "your OTP is invalid...!!!")
            return redirect('login_view')
        
        except Exception as error:
            messages.info(request, f"{error}") 
            return redirect('forgot_pass_email')

    return render(request, r"labor\new_password.html")


# dashboard views
@login_required       
def logout(request):
    del request.session['labor_id']
    messages.success(request, 'Now you are logged out.')
    return redirect('login_view')

@login_required
def dashboard_view(request):
    if Task.objects.filter(labor_id_id=request.session.get('labor_id')).count() != 0:
        total_payments_ = Task.objects.filter(labor_id_id=request.session.get('labor_id')).aggregate(total_amount=Sum('task_total_amount'))
        total_remaining_ = Task.objects.filter(labor_id_id=request.session.get('labor_id')).aggregate(total_remaining=Sum('task_remaining_amount'))
        total_paid_ = Task.objects.filter(labor_id_id=request.session.get('labor_id')).aggregate(total_paid=Sum('task_paid_amount'))
    else:
        total_payments_ = {
            'total_amount':0
        }
        total_remaining_ = {
            'total_remaining':0
        }
        total_paid_ = {
            'total_paid':0
        }
    
    context = {
        'parties_count': Party.objects.filter(labor_id_id=request.session.get('labor_id')).count(),
        'tasks_count': Task.objects.filter(labor_id_id=request.session.get('labor_id')).count(),
        'total_payments' : total_payments_,
        'task_remaining_amount' : total_remaining_,
        'total_paid_amount': total_paid_,
    }
    return render(request,'labor/dashboard.html',context)

@login_required
def parties_view(request):
    if request.method == 'POST':
        labor_id_ = request.POST.get('labor_id')
        party_name_ = request.POST['party_name']
        party_address_ = request.POST['party_address']
        party_mobile_ = request.POST['party_mobile']
        party_email_ = request.POST['party_email']

        if party_email_:
            try:
                get_party = Party.objects.get(party_email=party_email_)
                if get_party:
                    messages.info(request, f'Party {party_name_} is already exist.')
                    return redirect('parties_view')
                
            except Party.DoesNotExist:
                new_party = Party.objects.create(
                    labor_id_id=labor_id_,
                    party_name=party_name_,
                    party_address=party_address_,
                    party_mobile=party_mobile_,
                    party_email=party_email_
                )

                new_party.save()
                messages.success(request, f'Party {party_name_} is added successfully.')
                return redirect('parties_view')
            
            except Exception as e:
                messages.info(request, f'{e}')
                return redirect('parties_view')
            
    context = {
        'parties':Party.objects.filter(labor_id_id=request.session.get('labor_id'))
    }
    print(context)
    return render(request, 'labor/parties.html', context)


def edit_party(request, party_id):
    edit_party = get_object_or_404(Party, pk=party_id)
    if request.method == 'POST':
        edit_party.party_name = request.POST['party_name']
        edit_party.party_email= request.POST['party_email']
        edit_party.party_mobile = request.POST['party_mobile']
        edit_party.party_address= request.POST['party_address']
        
        edit_party.save()
        messages.success(request, f'"{edit_party.party_name}_{edit_party.party_id}" is updated successfully.')
        return redirect('parties_view')
    context = {
        'party':edit_party,
        'parties':Party.objects.filter(labor_id_id=request.session.get('labor_id')),
    }

    return render(request, 'labor\edit_party.html',context)


def delete_party(request, party_id):
    delete_party = Party.objects.get(party_id=party_id)
    party_name = delete_party.party_name
    delete_party.delete()
    messages.success(request, f'{party_name} is deleted successfully.')
    return redirect('parties_view')


@login_required
def tasks_view(request):
    if request.method == 'POST':
        party_id_ = request.POST.get('task_party_id')
        task_name_ = request.POST['task_name']
        task_description_ = request.POST['task_description']
        task_start_date_ = request.POST['task_start_date']
        task_end_date_ = request.POST['task_end_date']
        task_total_amount_ = request.POST['task_total_amount']

        new_task = Task.objects.create(
            labor_id_id=request.session.get('labor_id'),
            party_id_id=party_id_,
            task_name=task_name_,
            task_description=task_description_,
            task_start_date=task_start_date_,
            task_end_date=task_end_date_,
            task_total_amount=task_total_amount_
        )
        new_task.save()
        messages.success(request, f'Task {task_name_} is added successfully.')
        return redirect('tasks_view')


    context = {
        'parties':Party.objects.filter(labor_id_id=request.session.get('labor_id')),
        'tasks':Task.objects.filter(labor_id_id=request.session.get('labor_id'))
    }
    return render(request, 'labor/tasks.html', context)


def task_details(request, task_id):
    task_details = Task.objects.filter(task_id=task_id)
    context = {
        'parties':Party.objects.filter(labor_id_id=request.session.get('labor_id')),
        'tasks':task_details
    }
        
    return render(request, 'labor/task_details.html', context)


def task_payments(request, task_id):
    task_details = Task.objects.get(task_id=task_id)
    task_payments_entries = TaskPayment.objects.filter(task_id_id=task_id)
    if request.method == 'POST':
        proof_ = request.FILES['proof']
        payment_date_ = request.POST['paid_date']
        payment_amount_ = request.POST['amount']
        print(proof_, payment_date_, payment_amount_)

        payment_amount_ = Decimal(payment_amount_)

        if payment_amount_ != 0:
            if payment_amount_ <= task_details.task_remaining_amount:
                new_payment = TaskPayment.objects.create(
                    task_id_id=task_id,
                    proof=proof_,
                    payment_date=payment_date_,
                    payment_amount=payment_amount_
                )
                new_payment.save()
                task_details.task_remaining_amount -= payment_amount_
                task_details.task_paid_amount += payment_amount_
                if task_details.task_remaining_amount == 0:
                    print(task_details.task_remaining_amount, task_details.task_status)
                    task_details.task_payment_status = 'done'
                    task_details.save()
                else:
                    task_details.task_payment_status = 'partial'
                    messages.success(request, f'')
                task_details.save()

                
                messages.success(request, f'Payment of {payment_amount_} is added successfully.')
                return redirect('task_payments', task_id=task_id)
            else:
                messages.info(request, f'Payment amount should be less than or equal to remaning amount.')
                return redirect('task_payments', task_id=task_id)
        else:
            messages.info(request, f'Payment amount should be greater than 0.')
            return redirect('task_payments', task_id=task_id)
    context = {
        'task': task_details,
        'task_payments_entries':task_payments_entries
    }
    return render(request, 'labor/task_payments.html', context)



def edit_task(request, task_id):
    edit_task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        edit_task.party_id_id = request.POST.get('task_party_id')
        edit_task.task_name = request.POST['task_name']
        edit_task.task_description = request.POST['task_description']
        edit_task.task_start_date = request.POST['task_start_date']
        edit_task.task_end_date = request.POST['task_end_date']
        edit_task.task_total_amount = request.POST['task_total_amount']
        edit_task.save()
        
        messages.success(request, f'"{edit_task.task_name}_{edit_task.task_id}" is updated successfully.')
        return redirect('tasks_view')

    context = {
        'task': edit_task,
        'parties': Party.objects.filter(labor_id_id=request.session.get('labor_id')),
    }
    return render(request, 'labor/edit_task.html', context)


def delete_task(request, task_id):
    delete_task = Task.objects.get(task_id=task_id)
    task_name = delete_task.task_name
    delete_task.delete()
    messages.success(request, f'"{task_name}_{task_id}" is deleted successfully.')
    return redirect('tasks_view')


@login_required
def profile_view(request):
    labor_infos = LaborRegistration.objects.get(labor_id=request.session.get('labor_id'))
    labor_profile = LaborProfile.objects.get(labor_id=request.session.get('labor_id'))
    if request.method == 'POST':
        profile_ = request.FILES['profile']
        first_name_ = request.POST['fname']
        last_name_ = request.POST['lname']
        mobile_ = request.POST['mobile']

        labor_infos.mobile = mobile_
        labor_infos.save()
        labor_profile.first_name = first_name_
        labor_profile.last_name = last_name_
        labor_profile.profile = profile_
        labor_profile.save()
        messages.success(request, f'Profile is updated successfully.')
        return redirect('profile_view')


    context = {
        'labor_infos':labor_infos,
        'labor_profile':labor_profile
        }
    return render(request, 'labor/profile.html', context)


