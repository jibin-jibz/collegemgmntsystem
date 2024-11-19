from django.urls import path
from collageapp import views

urlpatterns = [
    # HOME PAGE
    path('',views.mainhome,name='mainhome'),
    path('logins',views.logins,name='logins'),
    path('logouts',views.logouts,name='logouts'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('dep_reg',views.dep_adding,name='dep_adding'),
    path('studentpage',views.studentpage,name='studentpage'),

    path('teacherpage',views.teacherpage,name='teacherpage'),
    path('studreg',views.studentreg,name='studentreg'),
    path('techerreg',views.techerreg,name='techerreg'),

    # studtable, teachtable
    path('studtable',views.studview,name='studview'),
    path('teachtable',views.teachview,name='teachview'),

    # aproval
    path('approve/<int:aid>',views.approve,name='approve'),
    path('aproved',views.approved_stud,name='approved_stud'),

    # updation stud teacher
    path('upadte',views.updates,name='updates'),
    path('update_stu/<int:uid>',views.update_stu,name='update_stu'),

    path('updat',views.updat,name='updat'),
    path('update_teach/<int:tid>',views.update_teach,name='update_teach'),

    # delete
    path('deletel/<int:dsid>',views.deletel,name='deletel'),
    path('delet2/<int:dtis>',views.delete2,name='delete2')



# view by st 
# path('t')




    
    
]
