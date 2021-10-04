from django.db import models


class RequestStatus(models.TextChoices):
    """Статусы выполнения задачи."""
    SUCCESS = "success", "Успешно выполнен"
    FAILURE = "failure", "Завершен с ошибкой"


class RequestResult(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name="Статус запроса",
                              choices=RequestStatus.choices, max_length=100,
                              default=RequestStatus.SUCCESS, blank=True)
    text = models.TextField(verbose_name="Результат запроса")

    def __str__(self) -> str:
        return str(self.id)

    @property
    def is_successful(self):
        return self.status == RequestStatus.SUCCESS
    
    @property
    def is_failed(self):
        return self.status == RequestStatus.FAILURE
