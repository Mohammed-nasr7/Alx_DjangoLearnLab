from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate

# استيراد النموذج المخصص للمستخدم
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # تعريف الحقول التي سيتم استخدامها في النموذج
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'bio', 'profile_picture')

    # تأكد من أن كلمة المرور مشفرة
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)  # استخدام create_user لإنشاء مستخدم آمن
        Token.objects.create(user=user)  # إنشاء توكن مرتبط بالمستخدم
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # التحقق من صحة اسم المستخدم وكلمة المرور
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return {'user': user}
