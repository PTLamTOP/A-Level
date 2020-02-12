from rest_framework import serializers
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "password", )