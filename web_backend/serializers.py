from rest_framework.serializers import ModelSerializer

from .models import Events, Learnings, Members, Stories

class EventsSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = (
            'id', 'title', 'venue', 'url', 'start_at', 'end_at', 'image_url'
        )
        
class LearningsSerializer(ModelSerializer):
    class Meta:
        model = Learnings
        fields = (
            'id', 'title', 'proficiency', 'type', 'url', 'image_url'
        )
        
class MembersSerializer(ModelSerializer):
    class Meta:
        model = Members
        fields = (
            'id', 'name', 'image_url', 'bio', 'twitter_url', 'linkedin_url', 'website_url', 'is_active', 'member_type'
        )
        
class StoriesSerializer(ModelSerializer):
    class Meta:
        model = Stories
        fields = (
            'id', 'title', 'speaker_name', 'poster_url', 'date', 'content', 'preview_image_url'
        )