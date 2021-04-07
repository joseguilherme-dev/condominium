from django.db import models

class Concierge(models.Model):
    user = models.OneToOneField(
        "users.User",
        verbose_name="Usuário",
        on_delete=models.PROTECT,
    )

    complete_name = models.CharField(
        verbose_name="Nome completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    cellphone = models.CharField(
        verbose_name="Celular para contato",
        max_length=11,
    )

    birthday_date = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = "Concierge"
        verbose_name_plural = "Concierges"

    def __str__(self):
        return self.complete_name