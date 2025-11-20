import string
from django.db import models
from django.utils.crypto import get_random_string
from places.models import Place

def generate_player_code():
    return get_random_string(12, allowed_chars=string.ascii_letters + string.digits)

class Player(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(
        max_length=12,
        unique=True,
        editable=False
    )
    current_place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.code:
            new_code = generate_player_code()
            while Player.objects.filter(code=new_code).exists():
                new_code = generate_player_code()
            self.code = new_code

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"
