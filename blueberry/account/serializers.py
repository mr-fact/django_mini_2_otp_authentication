from rest_framework import serializers

from account.models import User


class UserStatusSerializer(serializers.ModelSerializer):
    password = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'password',
        ]
        read_only_fields = [
            'password',
        ]

    def get_password(self, obj):
        return True if obj.password else False
