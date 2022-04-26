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
path('testcam', views.testcam, name='testcam'),
path('sentmessage', views.sentmessage, name='sentmessage'),
path('patientsending', views.patientsending, name='patientsending'),
path('workersdash', views.workersdash, name='workersdash'),
path('login', views.login, name='login'),
path('patientpage', views.patientpage, name='patientpage'),
path('addmedicalrecord', views.addmedicalrecord, name='addmedicalrecord'),
path('fichinfo', views.fichinfo, name='fichinfo'),
path('userhome', views.userdashbutton, name='userhome'),
path('doctoranswer', views.doctoranswer, name='doctoranswer'),
path('doctorinfo', views.doctorinfo, name='doctorinfo'),
path('adminsentmess', views.adminsentmess, name='adminsentmess'),
path('genmessage', views.genmessage, name='genmessage'),
path('pharmacy', views.pharmacybutton, name='pharmacy'),
path('allMedsdoc', views.allMedsdoc, name='allMedsdoc'),
path('medinfo', views.medinfo, name='medinfo'),
path('addcart', views.addcart, name='addcart'),
path('pay', views.pay, name='pay'),
path('test1', views.test1, name='test1'),
path('payement', views.payement, name='payement'),
path('checkout', views.checkout, name='checkout'),
path('addmedicalrecomandation', views.addmedicalrecomandation, name='addmedicalrecomandation'),
path('doctordash', views.dochomebut, name='doctordash'),
path('addpatpage', views.addpatpage, name='addpatpage'),
path('newcust', views.newcust, name='newcust'),
path('rdv', views.rdv, name='rdv'),
path('addprivaterecord', views.addprivaterecord, name='addprivaterecord'),
path('adminanswer', views.adminanswer, name='adminanswer'),
path('admintodoc', views.admintodoc, name='admintodoc'),
]

    # The home page