from django.db import models

class Place(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Route(models.Model):
    from_place = models.ForeignKey(Place, related_name='routes_from', on_delete=models.CASCADE)
    to_place = models.ForeignKey(Place, related_name='routes_to', on_delete=models.CASCADE)
    direction_name = models.CharField(max_length=50)
    is_bidirectional = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_bidirectional:
            if not Route.objects.filter(
                from_place=self.to_place,
                to_place=self.from_place
            ).exists():
                Route.objects.create(
                    from_place=self.to_place,
                    to_place=self.from_place,
                    direction_name=self.direction_name,
                    is_bidirectional=False
                )

    def __str__(self):
        if(self.is_bidirectional):
            return f"{self.from_place} <-> {self.to_place} ({self.direction_name})"
        return f"{self.from_place} -> {self.to_place} ({self.direction_name})"