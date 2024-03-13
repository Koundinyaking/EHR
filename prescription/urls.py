from django.urls import path
from . import views
app_name = 'prescription'

urlpatterns=[
path('upload/',views.upload,name="upload"),
path('list/',views.record_list,name="list"),
path('delete/<uuid:pk>/',views.delete,name="delete"),
path('ocr/<uuid:pk>',views.ocr,name="ocr"),
path('view/<uuid:pk>/' , views.view , name="view"),
path('download/<uuid:pk>/' , views.download , name="download"),
path('xray/' , views.xray , name="xray"),
path('doctor_view/' , views.doctor_view , name="doctor_view"),
path('xray_list/',views.xray_list,name="xray_list"),
path('xray_delete/<int:pk>/',views.xray_delete,name="xray_delete"),
# path('ocr/<int:pk2>/delete/<int:pk1>',views.delete,name="goback_delete")
]
