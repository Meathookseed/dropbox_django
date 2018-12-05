from rest_framework import serializers
from dropbox import models
from rest_framework_jwt.settings import api_settings
import facebook
"""------------------------------------------------------"""
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'


class VaultSerializer(serializers.ModelSerializer):
    file = FileSerializer(many=True,required=False)
    class Meta:
        model = models.Vault
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    vault = VaultSerializer(many=True,required=False)

    class Meta:
        model = models.Profile
        fields = ['username', 'password', 'first_name', 'image','profile_site','vault']
        extra_kwargs = {'password': {'required': False},
                        'username':{'required': False}}


"--------------------------------------------------------------------"
class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):

        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = models.Profile
        fields = ['token', 'username', 'password','image']


