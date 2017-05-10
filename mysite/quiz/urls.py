from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    #หน้า index
    url(r'^$', views.IndexView.as_view(), name='index'),
    #หน้า คำถาม
    url(r'^detail/$', views.DetailView.as_view(), name='detail'),
    #หน้า ผลบุคลิก
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    #หน้า about
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    #หน้าlistรวมของบุคลิกต่างๆ
    url(r'^personality/$', views.PersonalityView.as_view(), name='personality'),
    #หน้าย่อยของบุคลิกต่าง
    url(r'^istj/$', views.istjView.as_view(), name='istj'),
    url(r'^istp/$', views.istpView.as_view(), name='istp'),
    url(r'^estp/$', views.estpView.as_view(), name='estp'),
    url(r'^estj/$', views.estjView.as_view(), name='estj'),
    url(r'^isfj/$', views.isfjView.as_view(), name='isfj'),
    url(r'^isfp/$', views.isfpView.as_view(), name='isfp'),
    url(r'^esfp/$', views.esfpView.as_view(), name='esfp'),
    url(r'^esfj/$', views.esfjView.as_view(), name='esfj'),
    url(r'^infj/$', views.infjView.as_view(), name='infj'),
    url(r'^infp/$', views.infpView.as_view(), name='infp'),
    url(r'^enfp/$', views.enfpView.as_view(), name='enfp'),
    url(r'^enfj/$', views.enfjView.as_view(), name='enfj'),
    url(r'^intj/$', views.intjView.as_view(), name='intj'),
    url(r'^intp/$', views.intpView.as_view(), name='intp'),
    url(r'^entp/$', views.entpView.as_view(), name='entp'),
    url(r'^entj/$', views.entjView.as_view(), name='entj'),
    #ฟังก์ชันคำนวณและเพิ่มชื่อผู้ใช้ใน  function เดียว
    url(r'^question/$', views.add_player, name='add_player'),
]
