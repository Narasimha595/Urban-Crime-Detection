"""
URL configuration for crime_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as main_views
from userapp import views as user_views
from adminapp import views as admin_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.home,name='home'),
    path('about',main_views.about,name='about'),
    path('contact',main_views.contact,name='contact'),
    path('user',main_views.user,name='user'),
    path('main-admin',main_views.main_admin,name='main_admin'),
    path('registration',main_views.registration,name='registration'),
    path('otp',main_views.otp,name='otp'),

    path('user-dashboard',user_views.user_dashboard,name='user_dashboard'),
    path('profile',user_views.profile,name='profile'),
    path('user-feedback',user_views.user_feedback,name='user_feedback'),
    path('detect',user_views.detect,name="detect"),
    path('userresult',user_views.userresult,name='userresult'),
    path('userlogout',user_views.userlogout, name = 'userlogout'),
    path('detection/new',user_views.detection_new, name = 'detection_new'),
    path('process-detection/', user_views.process_detection, name='process_detection'),
    path('process-result/', user_views.prediction_result, name='prediction_result'),
    path("check-crimes/", user_views.check_crimes, name="check_crimes"),
    path("result-map/", user_views.result_page, name="crime_result_new"),

    path('admin-dashboard',admin_views.admin_dashboard,name='admin_dashboard'),
    path('pending-users',admin_views.pending_users,name='pending_users'),
    path('all-users/',admin_views.all_users,name='all_users'),
    path('accept-user/<int:id>/', admin_views.accept_user, name = 'accept_user'),
    path('reject-user/<int:id>/', admin_views.reject_user, name = 'reject'),
    path('delete-user/<int:id>/', admin_views.delete_user, name = 'delete_user'),
    path('change-status/<int:id>/', admin_views.change_status, name = 'change_status'),
    path('delete-dataset/<int:id>',admin_views.delete_dataset, name = 'delete_dataset'),
    path('admin-upload',admin_views.admin_upload,name='admin_upload'),
    path('admin-view',admin_views.admin_view,name='admin_view'),
    path('view-view',admin_views.view_view,name='view_view'),
    
    path('admin-Logistic-algo',admin_views.admin_Logistic_algo,name='admin_Logistic_algo'),
    path('logistic_btn', admin_views.logistic_btn, name='logistic_btn'),
    path('admin-Randomforest-algo',admin_views.admin_Randomforest_algo,name='admin_Randomforest_algo'),
    path('randomforest_btn', admin_views.randomforest_btn, name='randomforest_btn'),
    path('admin-dt-algo',admin_views.admin_dt_algo,name='admin_dt_algo'),
    path('Decisiontree_btn', admin_views.Decisiontree_btn, name='Decisiontree_btn'),
    path('admin-lightgbm',admin_views.admin_lightgbm,name='admin_lightgbm'),
    path('lightgbm-btn',admin_views.lightgbm_btn,name='lightgbm_btn'),
    path('admim-ada',admin_views.admin_ada,name='admin_ada'),
    path('ada-btn',admin_views.ada_btn,name='ada_btn'),
    path('admin-ann',admin_views.admin_ann,name='admin_ann'),
    path('ann-btn',admin_views.ann_btn,name='ann_btn'),

    path('admin-data-exploration',admin_views.admin_data_exploration,name="admin_data_exploration"),
    path('admin-data-preprocessing',admin_views.admin_data_preprocessing,name="admin_data_preprocessing"),
    path('graph',admin_views.graph,name='graph'),
    path('feedback-admin',admin_views.Feedback,name='Feedback'),
    path('feedback-sentiment',admin_views.feedback_sentiment,name='feedback_sentiment'),
    path('feedback-graph',admin_views.feedback_graph,name='feedback_graph'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)