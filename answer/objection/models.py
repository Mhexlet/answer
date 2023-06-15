from django.db import models

class Objections(models.Model):
    textObjections = models.TextField(max_length = 1000)
    answer = models.TextField()

    class Meta:
        verbose_name = "Возражение"
        verbose_name_plural = "Возражения"

    def __str__(self):
        return self.textObjections[:30]