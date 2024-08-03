
from django.urls import path

from .views import *

urlpatterns = [

    #auth urls
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('otp_varification_view/', otp_varification_view, name='otp_varification_view'),
    path('forgot_pass_email/', forgot_pass_email, name='forgot_pass_email'),
    path('new_password/', new_password, name='new_password'),
    path('logout/', logout, name='logout'),

    #dashboard urls
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('parties/', parties_view, name="parties_view"),
    path('party-edit/<str:party_id>', edit_party, name='edit_party'),
    path('party-delete/<str:party_id>', delete_party, name='delete_party'),
    path('tasks/', tasks_view, name='tasks_view'),
    path('task-details/<str:task_id>', task_details, name='task_details'),
    path("task-payments/<str:task_id>", task_payments, name='task_payments'),
    path('task-edit/<str:task_id>', edit_task, name='task_edit'),
    path('task-delete/<str:task_id>', delete_task, name='task_delete'), 
    path('profile_view/',profile_view, name='profile_view')
    ]

 
 