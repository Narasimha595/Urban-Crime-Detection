from django.shortcuts import render,redirect, get_object_or_404
from mainapp.models import *
from adminapp.models import *
from userapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
from mainapp.models import User_Model
from adminapp.models import  Upload_dataset_model
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from imblearn.over_sampling import SMOTE
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import confusion_matrix

# Create your views here.

def admin_dashboard(request):
    all_users_count = User_Model.objects.all().count()
    pending_users_count = User_Model.objects.filter(user_status='Pending').count()
    rejected_users_count = User_Model.objects.filter(user_status='removed').count()
    accepted_users_count = User_Model.objects.filter(user_status='accepted').count()
    Feedbacks_users_count = feedback.objects.all().count()
    user_uploaded_images = Dataset_Model.objects.all().count()
    return render(request,'admin/admin-dashboard.html', {
        'a': pending_users_count,
        'b': all_users_count,
        'c': rejected_users_count,
        'd': accepted_users_count,
        'e': Feedbacks_users_count,
        'f': user_uploaded_images
    })

def pending_users(request):
    pending = User_Model.objects.filter(user_status='pending')
    paginator = Paginator(pending, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin-pending-users.html', {'user': post})

def accept_user(request,id):
    status_update = User_Model.objects.get(user_id = id)
    status_update.user_status = 'accepted'
    status_update.save()
    messages.success(request, 'User was accepted..!')
    return redirect('pending_users')

def reject_user(request, id):
    status_update2 = User_Model.objects.get(user_id = id)
    status_update2.user_status = 'removed'
    status_update2.save()
    messages.warning(request, 'User was Rejected..!')
    return redirect('pending_users')

def all_users(request):
    all_users  = User_Model.objects.all()
    paginator = Paginator(all_users, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin-all-users.html', {"allu" : all_users, 'user' : post})

def change_status(request, id):
    user = get_object_or_404(User_Model, user_id=id)
    if user.user_status == 'accepted':
        user.user_status = 'rejected'
    else:
        user.user_status = 'accepted'
    user.save()
    return redirect('all_users')

def delete_user(request, id):
    User_Model.objects.get(user_id = id).delete()
    messages.warning(request, 'User was Deleted..!')
    return redirect('all_users')

def delete_dataset(request, id):
    dataset = Upload_dataset_model.objects.get(User_id = id).delete()
    messages.warning(request, 'Dataset was deleted..!')
    return redirect('admin_view')

def admin_upload(request):
    if request.method == 'POST':
        file = request.FILES['data_file']
        # print(file)
        file_size = str((file.size)/1024) +' kb'
        # print(file_size)
        Upload_dataset_model.objects.create(File_size = file_size, Dataset = file)
        messages.success(request, 'Dataset uploaded successfully!')
    return render(request,'admin/admin-upload-dataset.html')

def admin_view(request):
    dataset = Upload_dataset_model.objects.all()
    paginator = Paginator(dataset, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin-view-dataset.html', {'data' : dataset, 'user' : post})

from django.core.paginator import Paginator

def view_view(request):
    data = Upload_dataset_model.objects.last()
    file = str(data.Dataset)
    df = pd.read_csv(f'./media/{file}')
    
    # Paginate the DataFrame if needed
    paginator = Paginator(df.to_dict('records'), 50)  # 50 rows per page
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)
    
    # Convert page data into an HTML table format
    table = pd.DataFrame(page_data.object_list).to_html(
        table_id='data_table', 
        index=False, 
        classes="table table-bordered table-striped"
    )
    
    return render(request, 'admin/admin-view-result.html', {
        't': table, 
        'user': page_data
    })

def admin_Logistic_algo(request):
    return render(request,'admin/admin-log.html')

def logistic_btn(request):
    # Try to fetch the last result from the Logistic model
    model_result = Logistic.objects.last()

    if model_result:
        # If the result exists, fetch and display it
        messages.success(request, 'Results fetched from the database successfully')
        return render(request, "admin/admin-log.html", {
            'model_result': model_result,
        })
    else:
        # If no result exists, run the algorithm
        dataset = Upload_dataset_model.objects.first()
        if not dataset:
            messages.error(request, 'No dataset found. Please upload a dataset.')
            return redirect('upload_dataset')

        # Load the dataset
        df = pd.read_csv('crime_cleaned_data.csv')
        print(df)
        print(df.columns, 'Dataset Columns')

        # Assume df is your DataFrame
        # Define feature set and target label
        X = df.drop(columns=['Crime_Category'])
        y = df['Crime_Category']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X,            # Features
            y,            # Target labels
            test_size=0.3, # Proportion of the dataset to include in the test split
            random_state=11 # Seed for the random number generator
        )

        from sklearn.linear_model import LogisticRegression
        LR = LogisticRegression()
        LR.fit(X_train, y_train)

        # prediction
        train_prediction= LR.predict(X_train)
        test_prediction= LR.predict(X_test)

        # Evaluation
        from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
        accuracy = round(accuracy_score(y_test, test_prediction) * 100, 2)
        precision = round(precision_score(test_prediction, y_test, average='macro') * 100, 2)
        recall = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        f1_score = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        name = "Logistic Algorithm"

        # Print results for debugging
        print('test accuracy:',accuracy_score(y_test,test_prediction))
        print('train accuracy:',accuracy_score(y_train,train_prediction))

        score=cross_val_score(LR,X,y,cv=5)
        print(score.mean())

        print(classification_report(y_test,test_prediction))

        # Save the result to the database and display immediately
        new_result = Logistic.objects.create(
            Accuracy=accuracy,
            Precession=precision,
            F1_Score=f1_score,
            Recall=recall,
            Name=name
        )

        # Fetch the newly created result (just in case)
        model_result = Logistic.objects.last()

        # Display the results immediately without requiring a second execution
        messages.success(request, 'Algorithm executed and results saved successfully')
        return render(request, 'admin/admin-log.html', {
            'model_result': model_result,
        })

def admin_Randomforest_algo(request):
    return render(request,'admin/admin-ran.html')

def randomforest_btn(request):
    # Try to fetch the last result from the RandomForest model
    model_result = RandomForest.objects.last()

    if model_result:
        # If the result exists, fetch and display it
        messages.success(request, 'Results fetched from the database successfully')
        return render(request, "admin/admin-ran.html", {
            'model_result': model_result,
        })
    else:
        # If no result exists, run the Adaptive Region Partitioning (ARP) algorithm
        dataset = Upload_dataset_model.objects.first()
        if not dataset:
            messages.error(request, 'No dataset found. Please upload a dataset.')
            return redirect('upload_dataset')

        # Load the dataset
        df = pd.read_csv('crime_cleaned_data.csv')
        print(df)
        print(df.columns, 'Dataset Columns')

        # Assume df is your DataFrame
        # Define feature set and target label
        X = df.drop(columns=['Crime_Category'])
        y = df['Crime_Category']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X,            # Features
            y,            # Target labels
            test_size=0.3, # Proportion of the dataset to include in the test split
            random_state=11 # Seed for the random number generator
        )

        # Initialize and train RandomForestClassifier
        rfc=RandomForestClassifier(random_state=42)
        rfc.fit(X_train,y_train)

        # Predictions
        train_prediction= rfc.predict(X_train)
        test_prediction= rfc.predict(X_test)
        print('*'*20)

        # Evaluation
        from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
        accuracy = round(accuracy_score(y_test, test_prediction) * 100, 2)
        precision = round(precision_score(test_prediction, y_test, average='macro') * 100, 2)
        recall = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        f1_score = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        name = "Adaptive Region Partitioning (ARP) Algorithm"

        # Print results for debugging
        print('test accuracy:',accuracy_score(y_test,test_prediction))
        print('train accuracy:',accuracy_score(y_train,train_prediction))

        score=cross_val_score(rfc,X,y,cv=5)
        print(score.mean())

        print(classification_report(y_test, test_prediction))

        # Save the result to the database and display immediately
        new_result = RandomForest.objects.create(
            Accuracy=accuracy,
            Precession=precision,
            F1_Score=f1_score,
            Recall=recall,
            Name=name
        )

        # Fetch the newly created result (just in case)
        model_result = RandomForest.objects.last()

        # Display the results immediately without requiring a second execution
        messages.success(request, 'Algorithm executed and results saved successfully')
        return render(request, 'admin/admin-ran.html', {
            'model_result': model_result,
        })

def admin_dt_algo(request):
    return render(request,'admin/admin-dec.html') 

def Decisiontree_btn(request):
    # Try to fetch the last result from the DT_ALGO model
    model_result = DT_ALGO.objects.last()

    if model_result:
        # If the result exists, fetch and display it
        messages.success(request, 'Results fetched from the database successfully')
        return render(request, "admin/admin-dec.html", {
            'model_result': model_result,
        })
    else:
        # If no result exists, run the Decision Tree algorithm
        dataset = Upload_dataset_model.objects.first()
        if not dataset:
            messages.error(request, 'No dataset found. Please upload a dataset.')
            return redirect('upload_dataset')

        # Load the dataset
        df = pd.read_csv('crime_cleaned_data.csv')

        # Define feature set and target label
        X = df.drop(columns=['Crime_Category'])
        y = df['Crime_Category']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=11
        )

        # Initialize and train DecisionTreeClassifier
        DT = DecisionTreeClassifier()
        DT.fit(X_train, y_train)

        # Predictions (Train)
        train_pred = DT.predict(X_train)

        # Compute metrics for training set
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

        accuracy = round(accuracy_score(y_train, train_pred) * 100, 2)
        precision = round(precision_score(y_train, train_pred, average='macro') * 100, 2)
        recall = round(recall_score(y_train, train_pred, average='macro') * 100, 2)
        f1 = round(f1_score(y_train, train_pred, average='macro') * 100, 2)
        name = "Decision Tree Algorithm (Train)"

        # Print train metrics for debugging
        print('Train Accuracy:', accuracy)
        print('Train Precision:', precision)
        print('Train Recall:', recall)
        print('Train F1 Score:', f1)

        # Save the train result to the database
        new_result = DT_ALGO.objects.create(
            Accuracy=accuracy,
            Precession=precision,
            F1_Score=f1,
            Recall=recall,
            Name=name
        )

        # Fetch the newly created result
        model_result = DT_ALGO.objects.last()

        messages.success(request, 'Algorithm executed and results saved successfully')
        return render(request, 'admin/admin-dec.html', {
            'model_result': model_result,
        })

def admin_lightgbm(request):
    return render(request,'admin/admin-lgbm.html')

def lightgbm_btn(request):
    # Try to fetch the last result from the Lightgbm_ALGO model
    model_result = Lightgbm_ALGO.objects.last()

    if model_result:
        # If the result exists, fetch and display it
        messages.success(request, 'Results fetched from the database successfully')
        return render(request, "admin/admin-lgbm.html", {
            'model_result': model_result,
        })
    else:
        # If no result exists, run the LightGBM algorithm
        dataset = Upload_dataset_model.objects.first()
        if not dataset:
            messages.error(request, 'No dataset found. Please upload a dataset.')
            return redirect('upload_dataset')

        # Load the dataset
        df = pd.read_csv('crime_cleaned_data.csv')
        print(df)
        print(df.columns, 'Dataset Columns')

        # Assume df is your DataFrame
        # Define feature set and target label
        X = df.drop(columns=['Crime_Category'])
        y = df['Crime_Category']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X,            # Features
            y,            # Target labels
            test_size=0.3, # Proportion of the dataset to include in the test split
            random_state=11 # Seed for the random number generator
        )

        # Initialize and train LightGBM Classifier
        import lightgbm as lgb
        lgbm_model = lgb.LGBMClassifier(
            n_estimators=100,        # Number of boosting rounds
            random_state=11          # Seed for reproducibility
        )

        # Fitting the model
        lgbm_model.fit(X_train, y_train)

        # Predictions
        train_prediction = lgbm_model.predict(X_train)
        test_prediction = lgbm_model.predict(X_test)
        print('*' * 20)

        # Evaluation
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
        accuracy = round(accuracy_score(y_test, test_prediction) * 100, 2)
        precision = round(precision_score(test_prediction, y_test, average='macro') * 100, 2)
        recall = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        f1 = round(f1_score(test_prediction, y_test, average='macro') * 100, 2)
        name = "Lightgbm Boost Algorithm"

        # Print results for debugging
        print('Test accuracy:', accuracy_score(y_test, test_prediction))
        print('Train accuracy:', accuracy_score(y_train, train_prediction))
        
        score = cross_val_score(lgbm_model, X, y, cv=5)
        print('Cross-validation score mean:', score.mean())

        print('Classification report:\n', classification_report(y_test, test_prediction))

        # Save the result to the database and display immediately
        new_result = Lightgbm_ALGO.objects.create(
            Accuracy=accuracy,
            Precession=precision,
            F1_Score=f1,
            Recall=recall,
            Name=name
        )

        # Fetch the newly created result (just in case)
        model_result = Lightgbm_ALGO.objects.last()

        # Display the results immediately without requiring a second execution
        messages.success(request, 'Algorithm executed and results saved successfully')
        return render(request, 'admin/admin-lgbm.html', {
            'model_result': model_result,
        })

def admin_ada(request):
    return render(request,'admin/admin-ada.html') 

def ada_btn(request):
    # Try to fetch the last result from the Ada_ALGO model
    model_result = Ada_ALGO.objects.last()

    if model_result:
        # If the result exists, fetch and display it
        messages.success(request, 'Results fetched from the database successfully')
        return render(request, "admin/admin-ada.html", {
            'model_result': model_result,
        })
    else:
        # If no result exists, run the AdaBoost algorithm
        dataset = Upload_dataset_model.objects.first()
        if not dataset:
            messages.error(request, 'No dataset found. Please upload a dataset.')
            return redirect('upload_dataset')

        # Load the dataset
        df = pd.read_csv('crime_cleaned_data.csv')
        print(df)
        print(df.columns, 'Dataset Columns')

        # Assume df is your DataFrame
        # Define feature set and target label
        X = df.drop(columns=['Crime_Category'])
        y = df['Crime_Category']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X,            # Features
            y,            # Target labels
            test_size=0.3, # Proportion of the dataset to include in the test split
            random_state=11 # Seed for the random number generator
        )

        # Initialize and train AdaBoost Classifier
        from sklearn.ensemble import AdaBoostClassifier
        adb_model = AdaBoostClassifier(
            n_estimators=50,        # Number of weak learners (default is 50)
            random_state=11         # Seed for reproducibility
        )

        # Fitting the model
        adb_model.fit(X_train, y_train)

        # Predictions
        train_prediction = adb_model.predict(X_train)
        test_prediction = adb_model.predict(X_test)
        print('*' * 20)

        # Evaluation
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
        accuracy = round(accuracy_score(y_test, test_prediction) * 100, 2)
        precision = round(precision_score(test_prediction, y_test, average='macro') * 100, 2)
        recall = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        f1 = round(f1_score(test_prediction, y_test, average='macro') * 100, 2)
        name = "Ada Boost Algorithm"

        # Print results for debugging
        print('Test accuracy:', accuracy_score(y_test, test_prediction))
        print('Train accuracy:', accuracy_score(y_train, train_prediction))

        print('Classification report:\n', classification_report(y_test, test_prediction))

        # Save the result to the database and display immediately
        new_result = Ada_ALGO.objects.create(
            Accuracy=accuracy,
            Precession=precision,
            F1_Score=f1,
            Recall=recall,
            Name=name
        )

        # Fetch the newly created result (just in case)
        model_result = Ada_ALGO.objects.last()

        # Display the results immediately without requiring a second execution
        messages.success(request, 'Algorithm executed and results saved successfully')
        return render(request, 'admin/admin-ada.html', {
            'model_result': model_result,
        })

def admin_ann(request):
    return render(request,'admin/admin-ann.html') 

from django.shortcuts import render, redirect
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from django.contrib import messages
import numpy as np

def ann_btn(request):
    # Try to fetch the last result from the Ann_ALGO model
    model_result = Ann_ALGO.objects.last()

    if model_result:
        # If the result exists, fetch and display it
        messages.success(request, 'Results fetched from the database successfully')
        return render(request, "admin/admin-ann.html", {
            'model_result': model_result,
        })
    else:
        # If no result exists, run the ANN algorithm
        dataset = Upload_dataset_model.objects.first()
        if not dataset:
            messages.error(request, 'No dataset found. Please upload a dataset.')
            return redirect('upload_dataset')

        # Load the dataset
        df = pd.read_csv('crime_cleaned_data.csv')
        print(df)
        print(df.columns, 'Dataset Columns')

        # Assume df is your DataFrame
        # Define feature set and target label
        X = df.drop(columns=['Crime_Category'])
        y = df['Crime_Category']

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X,            # Features
            y,            # Target labels
            test_size=0.3, # Proportion of the dataset to include in the test split
            random_state=11 # Seed for the random number generator
        )

        # ANN model setup
        ann = Sequential()
        ann.add(Dense(units=64, input_dim=X_train.shape[1], kernel_initializer='uniform', activation='relu'))  # input_dim should be the number of features
        ann.add(Dense(units=32, kernel_initializer='uniform', activation='relu'))
        ann.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

        # Compile the model
        ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Fit the model
        ann.fit(X_train, y_train, epochs=15, batch_size=32)

        # Predictions
        train_prediction = ann.predict(X_train)
        test_prediction = ann.predict(X_test)

        # Convert predictions to binary
        test_prediction = (test_prediction >= 0.5).astype(int)
        train_prediction = (train_prediction >= 0.5).astype(int)

        # Evaluation
        accuracy = round(accuracy_score(y_test, test_prediction) * 100, 2)
        precision = round(precision_score(test_prediction, y_test, average='macro') * 100, 2)
        recall = round(recall_score(test_prediction, y_test, average='macro') * 100, 2)
        f1 = round(f1_score(test_prediction, y_test, average='macro') * 100, 2)
        name = "ANN Algorithm"

        # Print results for debugging
        print('test accuracy:', accuracy_score(y_test,test_prediction))
        print('train accuracy:', accuracy_score(y_train,train_prediction))
        print(confusion_matrix(y_test,test_prediction))

        # Save the result to the database and display immediately
        new_result = Ann_ALGO.objects.create(
            Accuracy=accuracy,
            Precession=precision,
            F1_Score=f1,
            Recall=recall,
            Name=name
        )

        # Fetch the newly created result (just in case)
        model_result = Ann_ALGO.objects.last()

        # Display the results immediately without requiring a second execution
        messages.success(request, 'Algorithm executed and results saved successfully')
        return render(request, 'admin/admin-ann.html', {
            'model_result': model_result,
        })

def graph(request):
    details4 = DT_ALGO.objects.last()
    e = details4.Accuracy
    details6 = Logistic.objects.last()
    g = details6.Accuracy
    details7 = RandomForest.objects.last()
    h = details7.Accuracy
    details3 = Lightgbm_ALGO.objects.last()
    o = details3.Accuracy
    details1 = Ada_ALGO.objects.last()
    r = details1.Accuracy
    details5 = Ann_ALGO.objects.last()
    j = details5.Accuracy
    return render(request,'admin/admin-graph.html', {'dt':e,'log':g, 'ran':h, 'lig':o, 'adb':r, 'ann':j})

def Feedback(request):
    feed =feedback.objects.all()
    return render(request,'admin/admin-feedback.html', {'back':feed}) 

def feedback_sentiment(request):
    fee = feedback.objects.all()
    return render(request,'admin/admin-feedback-sentiment.html', {'cat':fee}) 

def feedback_graph(request):
    positive = feedback.objects.filter(sentiment="positive").count()
    very_positive = feedback.objects.filter(sentiment="very positive").count()
    negative = feedback.objects.filter(sentiment="negative").count()
    very_negative = feedback.objects.filter(sentiment="very negative").count()
    neutral = feedback.objects.filter(sentiment="neutral").count()
    context = {
        "vp": very_positive,
        "p": positive,
        "neg": negative,
        "vn": very_negative,
        "ne": neutral,
    }
    return render(request,'admin/admin-feedback-graph.html',context)


import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from io import BytesIO
import base64 
def admin_data_exploration(request):
    dataset = Upload_dataset_model.objects.first()
    df = pd.read_csv(dataset.Dataset.path)

    # Create subplots with 2 rows and 2 columns
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

    # Plot the Count Chart
    create_Countplot(df, axes[0, 0])

    # Plot the Histogram
    create_histogram(df, axes[0, 1])

    # Plot the Boxplot
    create_line_chart(df, axes[1, 0])

    # Plot the Pie Chart (replace with your actual pie chart function)
    create_pie_chart(df, axes[1, 1])

    # Convert the entire figure to base64-encoded image for rendering in HTML
    figure_img = plot_to_base64(fig)

    # Close the figure to free up resources
    plt.close(fig)
    # messages.success(request, ' Exploratory Data Analysis Done Successfully')
    return render(request, 'admin/admin-data-exploration.html', {
        'figure_img': figure_img,
        'dataset': df.to_html(),  # Add the dataset to the context
    })

def create_Countplot(df, ax):
    sns.countplot(x=df['Location'], data=df, ax=ax)
    ax.set_title('Count Chart')
    ax.set_xlabel('Location')

def create_histogram(df, ax):
    ax.hist(df['Date_Reported'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Histogram')
    ax.set_xlabel('Date_Reported')

def create_line_chart(df, ax):
    sns.boxplot(df['Area_Name'], color='green', ax=ax)
    ax.set_title('Boxplot')
    ax.set_xlabel('Area_Name')

# Add a placeholder for your pie chart function
def create_pie_chart(df, ax):
    sns.countplot(x=df['Victim_Age'], data=df, ax=ax)
    ax.set_title('Pie Chart')
    ax.set_xlabel('Victim_Age')

def plot_to_base64(plt_obj):
    img_buffer = BytesIO()
    plt_obj.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    plt_obj.clf()  # Clear the plot for the next chart
    return f'data:image/png;base64,{img_data}'


def admin_data_preprocessing(request):
    dataset = Upload_dataset_model.objects.last() 
    df = pd.read_csv(dataset.Dataset.path)
     # Create subplots with 2 rows and 2 columns
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

    # Plot the Count Chart
    create_Countplot(df, axes[0, 0])

    # Plot the Histogram
    create_histogram(df, axes[0, 1])

    # Plot the Boxplot
    create_line_chart(df, axes[1, 0])

    # Plot the Pie Chart (replace with your actual pie chart function)
    create_pie_chart(df, axes[1, 1])

    # Convert the entire figure to base64-encoded image for rendering in HTML
    figure_img = plot_to_base64(fig)

    # Close the figure to free up resources
    plt.close(fig)
    messages.success(request, 'Data Preprocessing Done Successfully')
    return render(request,'admin/admin-data-preprocessing.html', {
        'figure_img': figure_img,
        'dataset': df.to_html(),})
def create_Countplot(df, ax):
    sns.countplot(x=df['Latitude'], data=df, ax=ax)
    ax.set_title('Count Chart')

def create_histogram(df, ax):
    ax.hist(df['Longitude'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Histogram')
    ax.set_xlabel('Longitude')

def create_line_chart(df, ax):
    sns.boxplot(df['Area_ID'], color='green', ax=ax)
    ax.set_title('Boxplot')
    ax.set_xlabel('Area_ID')

# Add a placeholder for your pie chart function
def create_pie_chart(df, ax):
    sns.countplot(x=df['Reporting_District_no'], data=df, ax=ax)
    ax.set_title('Count Chart')

def plot_to_base64(plt_obj):
    img_buffer = BytesIO()
    plt_obj.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    plt_obj.clf()  # Clear the plot for the next chart
    return f'data:image/png;base64,{img_data}'

def admin_logout(request):
    messages.info(request, 'You are logged out..!')
    return redirect('main_admin')