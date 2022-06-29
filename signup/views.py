from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Logging_User,Play_List,Movies,PlayList_Movie
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import PlayListSerializer,MovieSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets


def index(request):
 print('hello sejal')
 return render(request,'registerForm.html')


class RegisterView(APIView):
 def post(self,request):
  print('hello beta')
  if request.method=="POST":
    username=request.data['name']
    address=request.data['address']
    password=request.data['password']
    print(username,password,password)
    user=Logging_User.objects.filter(username=username).first()
    print(user)
    if user is not None: return Response({'success':'fail','message':'user already registered'})
    logging_user=Logging_User.objects.create(username=username,password=password,address=address)
    user=User(username=username)
    user.set_password(password)
    user.save()
    user1=User.objects.get(username=username)
    print(user1.password)
    return Response({'status':'success'})
   #return 'sejal rawat'


class LoginView(APIView):
 def post(self,request):
  username=request.data['name']
  password=request.data['password']
  user=Logging_User.objects.filter(username=username).first()
  if user is None: return Response({'status':'fail','message':'user does not exists'})
  if user.password!=password: return Response({'status':'fail','message':'incorrecr username or password'})
  user1=User.objects.filter(username=username).first()
  refresh=RefreshToken.for_user(user1)
  return Response({'status':'success','message':'logged in','refresh':str(refresh),'access':str(refresh.access_token)})


def login_page(request):
 return render(request,'loginForm.html')

def home_page(request):
 return render(request,'home_page.html')

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_playlist(request):
  user_id=request.data['user_id']
  playlist_name=request.data['playlist_name']
  is_public=request.data['is_public']
  user=User.objects.filter(id=user_id)
  if user:
    username=user[0].username
    user1=Logging_User.objects.get(username=username)
    play_list=Play_List.objects.create(user_id=user1,is_public=is_public,play_list_name=playlist_name)
    return JsonResponse({'success':True})
  return JsonReponse({'success':False})       
# Create your views here.



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_movies(request):
 movies_list=request.data['moviesList']
 playlist_name=request.data['playlist_name']
 user_id=request.data['user_id']
 print(movies_list)
 print(playlist_name)
 user=User.objects.get(id=user_id)
 if user:
  logging_user=Logging_User.objects.get(username=user.username)
  if logging_user:
    play_list=Play_List.objects.filter(user_id=logging_user,play_list_name=playlist_name).first()
    if play_list is not None:
     for movie in movies_list:
       movie_omdbID=movie['omdbId']
       movie_entry=Movies.objects.filter(movie_omdbId=movie_omdbID).first()
       if movie_entry is None:
        movie_entry=Movies.objects.create(movie_name=movie['title'],release_year=int(movie['release_year']),movie_omdbId=movie['omdbId'])
       movie_playlist_entry=PlayList_Movie.objects.filter(playList=play_list,movie=movie_entry).first()
       if movie_playlist_entry is None:
        movie_playList_entry=PlayList_Movie.objects.create(playList=play_list,movie=movie_entry)
     return JsonResponse({'success':True})
  return JsonResponse({'success':False})


@api_view(['GET'])
def get_all_playlists(request):
 items=Play_List.objects.all()
 serializer=PlayListSerializer(items,many=True)
 return JsonResponse(serializer.data,safe=False)



@api_view(['GET'])
def get_all_movies_for_playlist(request,playlistid,user_id):
 playlist=Play_List.objects.get(play_list_id=playlistid)
 user=User.objects.filter(id=user_id).first()
 if user is None:
   if playlist.is_public==False:
     return JsonResponse({'success':'fail','message':'cannot display private playlist'},status=403)  
 else:
  logging_user=Logging_User.objects.get(username=user.username)
  if playlist.is_public==False:
   if playlist.user_id.id!=logging_user.id:
    return JsonResponse({'success':'fail','message':'cannot display private playlist'},status=403)
 playList_movies=PlayList_Movie.objects.filter(playList=playlistid)
 print(playList_movies)
 list=[]
 for i in playList_movies:
  movie=Movies.objects.get(movie_id=i.movie.movie_id)
  list.append(movie)
 serializer=MovieSerializer(list,many=True)
 print(serializer.data)
 return JsonResponse(serializer.data,safe=False)
 
 

def get_list_page(request,playlistid,user_id):
 info={'playlistid':playlistid,'user_id':user_id}
 context={'info':info}
 return render(request,'listPage.html',context)

 
    
 