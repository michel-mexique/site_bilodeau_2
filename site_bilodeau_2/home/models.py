from django.db import models

# Create your models here.

from django.db import models
from django.core.exceptions import ValidationError
import html
html.unescape('Suzy &amp; John')

# Create your models here.

def validate_image(image):

    height = image.height 

    width = image.width

    if width / height != 1:

        raise ValidationError("Mauvais format d'image. Utilisez un carré parfait.")

class Team(models.Model):
    name = models.CharField('Nom', max_length=100)
    title = models.CharField('Titre', max_length=300)
    image = models.ImageField('Image', upload_to='team_pics', validators=[validate_image], default='team_pics/default.jpg')
    lienlinkedin = models.CharField('Lien LinkedIn', blank=True, max_length=500)
    
    def __str__(self):
        return self.name

class PageDeRedirection(models.Model):
    home_url = models.CharField('Nom sur bilodeau.co/', max_length=200)
    url = models.URLField('Lien URL vers', max_length=2000)

    def save(self, *args, **kwargs):
     self.url = html.unescape(self.url)
     super().save(*args, **kwargs)

    def __str__(self):
        return self.home_url

class RedirectionInfolettre(models.Model):
    pass


class TextePageDAccueil(models.Model):

    un_a = models.CharField('1A', max_length=200)
    un_b = models.TextField('1B', max_length=1000)
    deux_a = models.CharField('2A', max_length=200)
    deux_b = models.TextField('2B', max_length=1000)
    trois_a = models.CharField('3A', max_length=200)
    trois_b = models.TextField('3B', max_length=1000)