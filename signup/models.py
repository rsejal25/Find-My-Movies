from django.db import models

# Create your models here.
class Logging_User(models.Model):
 username=models.CharField(max_length=50)
 address=models.TextField()
 password=models.CharField(max_length=50)

class Play_List(models.Model):
 play_list_name=models.TextField()
 user_id=models.ForeignKey(Logging_User,on_delete=models.CASCADE)
 is_public=models.BooleanField()
 play_list_id=models.AutoField(primary_key=True,null=False)


class Movies(models.Model):
 movie_name=models.TextField()
 movie_id=models.AutoField(primary_key=True,null=False)
 movie_omdbId=models.CharField(max_length=50)
 release_year=models.IntegerField()
 

class PlayList_Movie(models.Model):
 playList=models.ForeignKey(Play_List,on_delete=models.CASCADE)
 movie=models.ForeignKey(Movies,on_delete=models.CASCADE)