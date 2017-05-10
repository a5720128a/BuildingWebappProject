import datetime

from django.db import models
from django.utils import timezone

#ผู้เล่นเก็บนามแฝงกับ facebook (ถ้าใส่)
class Player(models.Model):
    player_text = models.CharField(max_length=200)
    personaltiy = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.player_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#เก็บคำถาม
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

#เก็บตัวเลือกของคำถาม
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    corrects = models.IntegerField(default=0)
    #corrects ในไปใช้ในในฟังก์ชันหาบุคลิก (รวมในฟังก์ชัน add_player) ใน view
    def __str__(self):
        return self.choice_text

#Personality กับ Compatibility ไว้แสดงบุคลิกที่เข้ากันได้ในหน้าแสดงผล
class Personality(models.Model):
    personality_text = models.CharField(max_length=200)
    def __str__(self):
        return self.personality_text

class Compatibility(models.Model):
    c_personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    compatibility_text = models.CharField(max_length=200)
    def __str__(self):
        return self.compatibility_text
