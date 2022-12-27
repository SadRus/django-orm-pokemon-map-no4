from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField()
    previous_evolution = models.ForeignKey(
        'Pokemon', null=True, blank=True, on_delete=models.SET_NULL
        )
    # next_evolution = models.ForeignKey(
    #     'Pokemon', null=True, blank=True, on_delete=models.SET_NULL
    #     )
    def __str__(self) -> str:
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField() 
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)