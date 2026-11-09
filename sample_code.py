from django.shortcuts import render,redirect
import time
from mainapp.models import *
from userapp.models import *
from adminapp.models import *
import os
import base64
import pytz
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth import login
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
import time
from django.core.paginator import Paginator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report



def user_dashboard(request):
    prediction_count = User_Model.objects.count()  # Simplified
    user_id = request.session.get("user_id")  # Safer way to get session data
    if not user_id:
        # Handle case where user_id is not present in session
        return redirect('user')  # Redirect to user if no user session exists

    try:
        user = User_Model.objects.get(user_id=user_id)
    except User_Model.DoesNotExist:
        # Handle case where user is not found in the database
        return redirect('user')

    if user.Last_Login_Time is None:
        # Set time zone
        IST = pytz.timezone('Asia/Kolkata')
        current_time_ist = datetime.now(IST).time()
        user.Last_Login_Time = current_time_ist
        
    # Update Last Login Date and Time on every login
    user.Last_Login_Date = timezone.now().date()  # Set the date
    user.No_Of_Times_Login += 1  # Increment login count
    user.save()

    # Pass user details and prediction count to the template
    return render(request, 'user/user-dashboard.html', {'predictions': prediction_count, 'la': user})


def profile(request):
    # Check if the user_id is in the session
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this page.")
        return redirect("user_dashboard")  # Redirect to the login page or any other appropriate page
    
    user_id = request.session["user_id"]
    
    try:
        user = User_Model.objects.get(user_id=user_id)
    except User_Model.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("login")  # Redirect to the login page or any other appropriate page

    if request.method == 'POST':
        user_name = request.POST.get('fullname')
        user_age = request.POST.get('age')
        user_phone = request.POST.get('phonenumber')
        user_email = request.POST.get('email')
        user_address = request.POST.get("address")
        
        user.fullname = user_name
        user.age = user_age
        user.address = user_address
        user.phonenumber = user_phone
        user.email = user_email

        if 'profilepic' in request.FILES:
            image = request.FILES['profilepic']
            user.Image = image

        user.save()
        messages.success(request, 'Updated Successfully!')

    context = {"i": user}
    return render(request,'user/user-profile.html', context)

def user_feedback(request):
    id=request.session['user_id']
    user= User_Model.objects.get(user_id=id)
    if request.method=="POST":
        rating=request.POST.get('rating')
        review=request.POST.get('review')
        sid=SentimentIntensityAnalyzer()
        score=sid.polarity_scores(review)
        sentiment=None
        if score['compound']>0 and score['compound']<=0.5:
            sentiment='positive'
        elif score['compound']>=0.5:
            sentiment='very positive'
        elif score['compound']<-0.5:
            sentiment='very negative'
        elif score['compound']<0 and score['compound']>=-0.5:
            sentiment='negative'
        else :
            sentiment='neutral'
        feedback.objects.create(rating=rating, review=review,sentiment=sentiment, reviewer=user)
        messages.success(request,'Feedback recorded')
        return redirect('user_feedback')
    return render(request,'user/user-feedback.html')

from django.shortcuts import render, redirect
from django.contrib import messages
import pickle
import pandas as pd
import folium
from folium.plugins import HeatMap
from django.core.files.storage import default_storage
from django.conf import settings
import os

def detect(request):
    if request.method == 'POST':
        # Extracting data from the form
        Location = request.POST.get('Location')
        Latitude = request.POST.get('Latitude')
        Longitude = request.POST.get('Longitude')
        Date_Reported = request.POST.get('Date_Reported')
        Area_ID = request.POST.get('Area_ID')
        Area_Name = request.POST.get('Area_Name')
        Reporting_District_no = request.POST.get('Reporting_District_no')
        Victim_Age = request.POST.get('Victim_Age')
        Victim_Sex = request.POST.get('Victim_Sex')
        Premise_Code = request.POST.get('Premise_Code')
        Weapon_Used_Code = request.POST.get('Weapon_Used_Code')
        Status = request.POST.get('Status')

        # Check for empty fields and display a warning message
        if not all([Location, Latitude, Longitude, Date_Reported, Area_ID, Area_Name, Reporting_District_no, Victim_Age, Victim_Sex, Premise_Code, Weapon_Used_Code, Status]):
            messages.warning(request, "Please fill in all input details.")
            return render(request, "user/user-detect.html")
        
        try:
            # Convert to float
            Location = float(Location)
            Latitude = float(Latitude)
            Longitude = float(Longitude)
            Date_Reported = float(Date_Reported)
            Area_ID = float(Area_ID)
            Area_Name = float(Area_Name)
            Reporting_District_no = float(Reporting_District_no)
            Victim_Age = float(Victim_Age)
            Victim_Sex = float(Victim_Sex)
            Premise_Code = float(Premise_Code)
            Weapon_Used_Code = float(Weapon_Used_Code)
            Status = float(Status)
        except ValueError:
            messages.warning(request, "Please enter valid numbers.")
            return render(request, "user/user-detect.html")
        
        # Load the RandomForestClassifier model
        file_path = 'DT-cyber.pkl'
        try:
            with open(file_path, 'rb') as file:
                loaded_model = pickle.load(file)
        except FileNotFoundError:
            messages.error(request, "Model file not found.")
            return redirect("detect")

        # Ensure the model predicts correctly
        try:
            prediction = loaded_model.predict([[Location, Latitude, Longitude, Date_Reported, Area_ID, Area_Name, Reporting_District_no, Victim_Age, Victim_Sex, Premise_Code, Weapon_Used_Code, Status]])
            prediction_result = int(prediction[0])  # Convert predictions to standard Python int
        except Exception as e:
            messages.error(request, "Error in model prediction: {}".format(str(e)))
            return render(request, "user/user-detect.html")

        request.session['prediction_result'] = prediction_result
        return redirect("userresult")

    return render(request, "user/user-detect.html")