BROADCAST ENGINEERING CONSULTANTS INDIA LIMITED
(A Government of India Enterprise under Ministry of Information & Broadcasting
(A Mini Ratna Company)
VACANCY ADVERTISEMENT NO. 31
Pre-Assessment for the post of Software Developer-MIC to be submitted by 30th December 2020
As per mail,I choose Question a. a.Create HTML5, jquery (use any js library) and create Interactive video. ex : https://h5p.org/image-pairing
Submitted By: Dewangshu Pandit 				Application No: 115009
_______________________________________________________________________________
Technology Useed:
HTML5, CSS3, Jquery, Bootstrap, Python Framework (Django) , Windows or Ubuntu


1. Output/Result/Screenshots of My Developed Application:

























2.Coding
Important Logic (image validation ,matching and find score):

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    {% load static %}
    <style>
  .ui-draggable-disabled>img{
    opacity: 0.5;
  }


.draggable>img,.droppable>img{

width: 150px ;
height: 100px ;

}

img.check{
  width: 40px ;
height: 40px ;
}
.draggable>img:hover{
  border-radius: 5px;
}
    </style>
<link rel="stylesheet" href="{% static 'bootstrap.min.css' %}">
<link rel="stylesheet" href="{% static 'font-awesome.css' %}"> 

<script src="{% static 'jquery-3.3.1.min.js' %}"></script>
<script src="{% static 'bootstrap.min.js' %}"></script>


<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
  <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
</head>
<body>

  <div class="container">
    <div class="row">
      <br>
      <br>
      <br>
      <div class="header clearfix">
        <h3 class="text-muted">Darg the Animal with their food</h3>
        
    </div>
  <div class="col-md-12">



          <!-- DRAGGABLE DIVS -->
          <div class="row">
            <h3 class="text-centre">DRAGGABLE AREA</h3><hr>
          <div class="row image-grid">

            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body draggable" id="1" data-ques="horse.jpg">
                  
                    <img alt="" class="img-responsive center-block img"  src="/media/image/horse.jpg" id="1" height="100" width="150">
                  
                </div>
              </div>
            </div>

            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body draggable" id="2" data-ques="lion.png">
                  
                    <img alt="" class="img-responsive center-block img" src="/media/image/lion.png" id="2" height="100" width="150">
                 
                </div>
              </div>
            </div>

            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body draggable" id="3" data-ques="parrot.jpg">
                  
                    <img alt="" class="img-responsive center-block img" src="/media/image/parrot.jpg" id="3" height="100" width="150">
                  
                </div>
              </div>
            </div>
            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body draggable" id="4" data-ques="monkey.jpeg">
                  
                    <img alt="" class="img-responsive center-block img" src="/media/image/monkey.jpeg" id="4" height="100" width="150">
                  
                </div>
              </div>
            </div>

          </div>
        </div>



          <!-- DROPPABLE DIVS -->
          <div class="row">
            <h3 class="text-centre">DROPPABLE AREA</h3><hr>
          <div class="row image-grid">

            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body droppable" id="1" data-ques="grass.jpeg" data-ans="horse.jpg" data-givenans="">
                  
                    <img alt="" class="img-responsive center-block" src="/media/image/grass.jpeg" height="100" width="150">
                  
                </div>
              </div>
            </div>

            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body droppable" id="2" data-ques="nuts.jpg" data-ans="parrot.jpg" data-givenans="">
                  
                    <img alt="" class="img-responsive center-block" src="/media/image/nuts.jpg" height="100" width="150">
                 
                </div>
              </div>
            </div>

            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body droppable" id="3" data-ques="meat.jpg" data-ans="lion.png" data-givenans="">
                  
                    <img alt="" class="img-responsive center-block" src="/media/image/meat.jpg" height="100" width="150">
                  
                </div>
              </div>
            </div>
            <div class="col-sm-3 col-md-3">
              <div class="panel panel-default">
                <div class="panel-body droppable" id="4" data-ques="banana.jpg" data-ans="monkey.jpeg" data-givenans="">
                  
                    <img alt="" class="img-responsive center-block" src="/media/image/banana.jpg" height="100" width="150">
                  
                </div>
              </div>
            </div>

            <div class="row ">
              <div class="col-md-12">
                  <button class="btn btn-primary"  id="result">Check Result</button>
                  <a class="btn btn-primary" href="{% url 'FileCompare:home' %}">Home</a>
              </div>
            </div>

            <br/>
            <br/>

          </div>
          <div class="text-centre" id="score" style="display: none;"> 
            <div class="header clearfix">
              <h3 class="text-muted" id="sc">Your Score</h3>
            </div>
            <div class="progress" >
              <div class="progress-bar progress-bar-success" id="my_progress" role="progressbar" aria-valuenow="50"
              aria-valuemin="0" aria-valuemax="100" style="width:10%">
                
              </div>
            </div>
          </div>
          </div>








</div>
</div>
</div>
<script>
var Y;
$(function () {
  $('.draggable').draggable({
    revert: "invalid",
    stack: ".draggable",
    helper:'clone',
    drag: function() 
    { 
      // dd= $(this).data("ans"); 
      // alert(dd);
    }
  }).resizable();


  $('.droppable').droppable({
    // accept: ".draggable",
    drop: function(event, ui) {
        //console.log(ui)
        //$(this).append(ui.draggable.clone().removeClass().removeAttr('style'));
        console.log(ui.draggable);
        //validation
        Y=$(this);
        let length=Y.children('img.center-block.img').length;
        console.log('length',length)
        if(length<1){
          $(this).append(ui.draggable.context.innerHTML);

          let selected_ans=ui.draggable[0].dataset['ques'];
          // alert(selected_ans);
          // $(this).data('givenans',selected_ans);
          $(this).attr("data-givenans", selected_ans);
          let id=ui.draggable.context.id;
          console.log(id);
          $('.draggable#'+id).draggable( "disable" );

          $(this).children("img.center-block").width("150px");
          $(this).children("img.center-block").height("100px");
          
        }
    }
    });

    $("#result").click(function(){

      total_ques=0;
      crt_ans=0;
      score_percent=0;
      $(".droppable").each(function() {
          given_ans=$(this).data("givenans");
          correct_ans=$(this).data("ans");
          // alert("Given ans:"+given_ans+" :Correct ans:"+correct_ans);

          total_ques++;

          if(given_ans==correct_ans)
          {
            crt_ans+=1;
            $(this).append("<img src='/media/image/correct.png' class='check' width='50' height='50'>");
          }
          else{
            $(this).append("<img src='/media/image/incorrect.jpg' class='check' width='50' height='50'>");
          }
          score_percent=(crt_ans*100)/total_ques;
      });
      // alert("Your total correct match:"+crt_ans+" out of "+total_ques+",you got"+score_percent +" % score");
    
      $("#result").html("Your total correct match:"+crt_ans+" out of "+total_ques);
      $("#my_progress").css("width", score_percent+"%");
      $(".progress").append("You got "+score_percent+"%");
      $("#sc").append(score_percent+"%")
      $("#score").show();
    });

    $(".droppable").click(function() {
     
        let id=$(this).children("img.center-block.img")[0].id;
       $('.draggable#'+id).draggable( "enable" );
       $('.droppable#'+$(this).context.id+'>img.center-block.img').remove();
     
    });
  
});

</script>
</body>
</html>


Views.py


from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AnimalFoodForm
from .models import AnimalFood





def add_photo(request, template_name='add_photo.html'):
    form = AnimalFoodForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        # return  HttpResponse("ok saved")
        return redirect('FileCompare:manage_photo')
    return render(request, template_name, {'form':form})


def manage_photo(request, template_name='manage_photo.html'):
    std_data = AnimalFood.objects.all() 
    data = {}
    data['object_list'] = std_data
    return render(request, template_name, data)


def edit_photo(request, pk, template_name='add_photo.html'):
    book= get_object_or_404(AnimalFood, pk=pk)
    form = AnimalFoodForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('FileCompare:manage_photo')
    return render(request, template_name, {'form':form})

def delete_photo(request, pk):
    obj = get_object_or_404(AnimalFood, pk=pk)
    obj.delete()
    return redirect('FileCompare:manage_photo')

def home(request, template_name='home.html'):
    return render(request, template_name)

    
def image_match_static(request, template_name='image_match_static.html'):
    return render(request, template_name)

Urls.py

from django.urls import path

from FileCompare import views

app_name = 'FileCompare'

urlpatterns = [
    path('add_photo', views.add_photo, name='add_photo'),
    path('add_photo', views.add_photo, name='add_photo'),
    path('edit_photo/<int:pk>', views.edit_photo, name='edit_photo'),
    path('delete_photo/<int:pk>', views.delete_photo, name='delete_photo'),
    path('manage_photo', views.manage_photo, name='manage_photo'),
    path('', views.home, name='home'),
    path('image_match_static', views.image_match_static, name='image_match_static'),

]


Settings.py

"""
Django settings for CRUD project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

Created By: Dewangshu Pandit
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l_o4$g@m_d!8pxavp=)=%m8=se&w_5gl$za83y2yzn!+kzh@*a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'FileCompare'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CRUD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CRUD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


How to run the Project on Ubuntu 20.04 LTS/or latest earlier

Step 1: Open Ubuntu Terminal (ctrl+alt+T)

---------------------------Ubuntu commands Virtual env setup-----------------

Step 2: python3  -V ##check the python version

Step 3: sudo apt install python3 -venv ## install virtual env for 1st time

Step 4: python3 m venv myproject_env ##create env a/c to project , particulat location

Step 5: source myproject_env/bin/activate ##activate the virtual environment

	deactivate ##command for deactivate the environment

Step 6:pip3 install Django  ##to install django in active vir enviroment

Step 7:pip install library_name  ##to install any library like requests

Step 8:pip install -r requirements.txt ## install all libarry once in single file 

Step 9: pip freeze ## to see the list of library under the vir env

Setp 10: pip freeze >requirements.txt ## export all installed library list in this text file

-----------------Run Django Project on virtual env on Ubuntu-------------------------------
source myproject_env/bin/activate




python3 manage.py runserver   ##run your project on localhost:8000

python3 managae.py createsuperuser  ##to create admin login (django)

python manage.py makemigrations  ##create migrations files

python3 manage.py migrate  ##to migrate database tables

How to run the Project on Windows:

Step 1: Install Python 3.x

Step 2: pip install virtualenvwrapper-win # first time only

Step 3: mkvirtualenv myproject ##you can change myproject to anything

Step 4 :workon myproject

Step 5 :pip install -r requirements.txt

Step 6: python managae.py createsuperuser 

Step 7: python manage.py makemigrations 

Step 8: python3 manage.py runserver 

Step 10: Open Browser and type localhost:8000 or 127.0.0.1:8000


Download Complete Source Code from Github:

