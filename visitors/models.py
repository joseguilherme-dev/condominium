from django.db import models

class Visitor(models.Model):
    complete_name = models.CharField(
        verbose_name="Nome completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    birthday_date = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    house_num = models.PositiveSmallIntegerField(
        verbose_name="Número da casa que será visitada"
    )

    vehicle_plate = models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        blank=True,
        null=True,
    )

    entrance_hour = models.DateTimeField(
        verbose_name="Hora que o visitante entrou no condomínio",
        auto_now_add=True,
    )

    exit_hour = models.DateTimeField(
        verbose_name="Hora que o visitante saiu do condomínio",
        auto_now=False,
        blank=True,
        null=True,
    )

    responsible_resident = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
    )

    related_concierge = models.ForeignKey(
        "concierges.Concierge",
        verbose_name="Concierge responsável pelo registro do visitante",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table= "visitor"
    
    def __str__(self):
        return self.complete_name