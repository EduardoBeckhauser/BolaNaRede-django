from rest_framework.serializers import ModelSerializer

from bolanarede.models import Camisa

class CamisaSerializer(ModelSerializer):
    class Meta:
        model = Camisa
        fields = "__all__"