from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from django.http import JsonResponse

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://solid-lamp-76qwrw7559hr457-8000.app.github.dev/'
    return Response({
        'users': f"{base_url}{reverse('user-list', request=request, format=format)}",
        'teams': f"{base_url}{reverse('team-list', request=request, format=format)}",
        'activities': f"{base_url}{reverse('activity-list', request=request, format=format)}",
        'leaderboard': f"{base_url}{reverse('leaderboard-list', request=request, format=format)}",
        'workouts': f"{base_url}{reverse('workout-list', request=request, format=format)}",
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer