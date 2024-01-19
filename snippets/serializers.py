from rest_framework import serializers
from .models import Snippet
from django.contrib.auth import get_user_model


# Сериализатор для модели Snippet
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # Поле "owner" только для чтения, используется для представления имени владельца
    owner = serializers.ReadOnlyField(source="owner.username")
    # Поле "highlight" для представления гиперссылки на подсвеченный код
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        # Указание модели Snippet как основы для сериализатора
        model = Snippet
        # Определение полей, включаемых в сериализацию
        fields = ["url", "id", "highlight", "owner", "title", "code", "linenos", "language", "style", "views"]
