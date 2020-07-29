from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our API."""
    name = serializers.CharField(max_length=10)