from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    task = serializers.CharField()
    date = serializers.DateField()
    important = serializers.BooleanField()
    completed = serializers.BooleanField()