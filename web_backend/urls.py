from django.conf.urls import url, include, re_path
from django.urls import path

from .views import EventsViewSet, LearningsViewSet, MembersViewSet, StoriesViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventsViewSet, 'events')
router.register(r'learnings', LearningsViewSet, 'learnings')
router.register(r'members', MembersViewSet, 'members')
router.register(r'stories', StoriesViewSet, 'stories')

urlpatterns = [
    re_path('^', include(router.urls)),
]