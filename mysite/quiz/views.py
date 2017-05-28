from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages

from quiz.models import Question, Choice, Player, Personality, Compatibility

#index page
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published player."""
        return Player.objects.order_by('-pub_date')[:5]

#detail page
class DetailView(generic.ListView):
    template_name = 'detail.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all

#personality page
class PersonalityView(generic.ListView):
    template_name = 'personality.html'    
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        return Player.objects.all

#results page
class ResultsView(generic.ListView):
    template_name = 'results.html'    
    context_object_name = 'latest_Personality_list'

    def get_queryset(self):
        """Return the last five published player."""
        return Personality.objects.all

#about page
class AboutView(generic.ListView):
    template_name = 'about.html'    
    context_object_name = 'latest_Personality_list'

    def get_queryset(self):
        """Return the last five published player."""
        return Personality.objects.all

#----personality funtion----

class istjView(generic.ListView):
    template_name = 'istj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class istpView(generic.ListView):
    template_name = 'istp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class estpView(generic.ListView):
    template_name = 'estp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class estjView(generic.ListView):
    template_name = 'estj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class isfjView(generic.ListView):
    template_name = 'isfj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class isfpView(generic.ListView):
    template_name = 'isfp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class esfpView(generic.ListView):
    template_name = 'esfp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class esfjView(generic.ListView):
    template_name = 'esfj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class infjView(generic.ListView):
    template_name = 'infj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class infpView(generic.ListView):
    template_name = 'infp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class enfpView(generic.ListView):
    template_name = 'enfp.html'
    context_object_name = 'latest_player_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class enfjView(generic.ListView):
    template_name = 'enfj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class intjView(generic.ListView):
    template_name = 'intj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class intpView(generic.ListView):
    template_name = 'intp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class entpView(generic.ListView):
    template_name = 'entp.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all

class entjView(generic.ListView):
    template_name = 'entj.html'
    context_object_name = 'latest_player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all
#------------------------------------

#ฟังก์ชันคำนวณและเพิ่มชื่อผู้ใช้ใน  function เดียว
def add_player(request):
    question_amount = Question.objects.count()+1
    print(str(request.POST))
    #group point
    gp1 = 0
    gp2 = 0
    gp3 = 0
    gp4 = 0
    for i in range(1,question_amount):
        try: 
            check = int(request.POST[str(i)])
            if check == 1:
                gp1 = gp1+1
            elif check == 2:
                gp2 = gp2+1
            elif check == 3:
                gp3 = gp3+1
            elif check == 4:
                gp4 = gp4+1
        except:
            messages.add_message(request, messages.INFO, "You didn't select a choice.")
            return HttpResponseRedirect(reverse('quiz:detail'))
    #ga = group alplabet หาอักษรของบุคลิก
    if gp1 > 5:
        ga1 = "E"
    else :
        ga1 = "I"
    if gp2 > 5:
        ga2 = "S"
    else :
        ga2 = "N"
    if gp3 > 5:
        ga3 = "T"
    else :
        ga3 = "F"
    if gp4 > 5:
        ga4 = "J"
    else :
        ga4 = "P"

    the_personality = ga1 + ga2 + ga3 + ga4
    the_player = request.POST['addPlayer']
    the_facebook = request.POST['add_Facebook']
    p = Player(player_text = the_player, personaltiy = the_personality, facebook = the_facebook, pub_date=timezone.now())
    p.save()
    #link ไปยัง หน้าของบุคลิกนั้นๆหลังคำนวณเสร็จ
    link = "quiz:"+the_personality.lower()
    context = {'the_personality':the_personality , 'link':link}
    #return render(request,'results.html',context)
    return HttpResponseRedirect(reverse(link))


