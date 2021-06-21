from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Events, Learnings, Members, Stories
from .serializers import EventsSerializer, LearningsSerializer, MembersSerializer, StoriesSerializer

class EventsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
      http_method_names = ['get']
      serializer_class = EventsSerializer
      queryset = Events.objects.all()

class LearningsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
      http_method_names = ['get']
      serializer_class = LearningsSerializer
      queryset = Learnings.objects.all()
      
class MembersViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
      http_method_names = ['get']
      serializer_class = MembersSerializer
      queryset = Members.objects.all()
      
class StoriesViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
      http_method_names = ['get']
      serializer_class = StoriesSerializer
      queryset = Stories.objects.all()
