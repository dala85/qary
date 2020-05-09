from rest_framework import serializers
from qary_app.models import Chat, Document

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'