from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import uuid
from django.contrib.auth import get_user_model


# Получение всех доступных лексеров и стилей Pygments
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Модель для представления кодовых сниппетов
class Snippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGES_CHOICES, default="python", max_length=100)
    style = models.CharField(choices=STYLES_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="snippets")
    highlighted = models.TextField()
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created"]

    # Сохраняем подсвеченный код вместе с исходным кодом
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
