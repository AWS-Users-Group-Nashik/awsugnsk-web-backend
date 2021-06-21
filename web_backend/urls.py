from django.conf.urls import url, include, re_path
from django.urls import path

from .views import EventsViewSet, LearningsViewSet, MembersViewSet, StoriesViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventsViewSet, 'applications')
router.register(r'learnings', LearningsViewSet, 'custom-tags')
router.register(r'members', MembersViewSet, 'reply-review-templates')
router.register(r'stories', StoriesViewSet, 'review-tags')

urlpatterns = [
    re_path('^', include(router.urls)),
]