from rest_framework.serializers import ModelSerializer, SerializerMethodField
from base.models import Room, Topic, Message, User


class RoomSerializer(ModelSerializer):
    topic = SerializerMethodField()
    host = SerializerMethodField()
    participants = SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id', 'host', 'topic', 'name', 'description', 'updated', 'created', 'participants']

    def get_topic(self, obj):
        return obj.topic.name if obj.topic else None

    def get_host(self, obj):
        return obj.host.username if obj.host else None

    def get_participants(self, obj):
        return [user.username for user in obj.participants.all()]