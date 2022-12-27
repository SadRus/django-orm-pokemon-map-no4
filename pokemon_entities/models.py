from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    title_en = models.CharField(max_length=200, verbose_name='Имя на английском')
    title_jp = models.CharField(max_length=200, verbose_name='Имя на японском')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images',
                              null=True,
                              blank=True,
                              verbose_name='Изображение')
    previous_evolution = models.ForeignKey('Pokemon',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL,
                                           verbose_name='Предыдущая эволюция')
    def __str__(self) -> str:
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name='Широта') 
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, verbose_name='Появился в')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Исчез в')
    level = models.IntegerField(null=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')