from rest_framework import serializers
from .models import User, Service, Bill, ResidentFamily, TuDo, Package, Feedback, Survey, \
    SurveyQuestion, SurveyAnswer


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar', 'role', 'is_active']
        extra_kwargs = {
            'password': {
                'write_only': 'true'
            }
        }

    def to_representation(self, instance):
        # để hiển thị dường dân tuyệt đối của ảnh trên swagger
        rep = super().to_representation(instance)
        avatar = instance.avatar
        if avatar:
            rep['avatar'] = avatar.url
        return rep


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']


class BillSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    services = ServiceSerializer(many=True)

    class Meta:
        model = Bill
        fields = ['id', 'name', 'payment_method', 'bill_date', 'bill_image', 'amount', 'status', 'services', 'user']

    def to_representation(self, instance):
        # để hiển thị dường dân tuyệt đối của ảnh trên swagger
        rep = super().to_representation(instance)
        bill_image = instance.payment_image
        if bill_image:
            rep['bill_image'] = bill_image.url
        return rep


class ResidentFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentFamily
        fields = ['id', 'name', 'cccd', 'sdt', 'relationship', 'user_id', 'status']


class TuDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuDo
        fields = ['id', 'name', 'created_date', 'active']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'tuDo', 'status']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'content', 'created_at', 'user_id']


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'type_survey', 'is_active']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ['id', 'survey', 'question_text']


class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = ['id', 'user', 'question', 'answer']