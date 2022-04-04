from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
urlpatterns = [
path('index', views.index, name='index'),
path('userlogin', views.userlogin, name='userlogin'),
path('userdash', views.userdash, name='userdash'),
path('sentmessage', views.sentmessage, name='sentmessage'),
path('patientsending', views.patientsending, name='patientsending'),
path('workersdash', views.workersdash, name='workersdash'),
path('login', views.login, name='login'),
path('patientpage', views.patientpage, name='patientpage'),
path('addmedicalrecord', views.addmedicalrecord, name='addmedicalrecord'),
path('doctest', views.doctest, name='doctest'),
path('fichinfo', views.fichinfo, name='fichinfo'),
]
    # The home page