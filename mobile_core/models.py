from django.db import 
from django.utils.text import slugify
from .abstract_models import AbstractTimeStampedModel 


class Country(AbstractTimeStampedModel):
    english_name = models.CharField(_("Nom Anglais"), max_length=100)
    french_name = models.CharField(_("Nom Français"), max_length=100)
    local_name = models.CharField(_("Nom Locale"), max_length=100)
    code = models.CharField(_("Code"), max_length=20)
    region = models.CharField(_("Region du Globe"), max_length=100)
    continent = models.CharField(_("Continent"), max_length=50)

    def __repr__(self):
        return "Nom du Pays: %s" % self.french_name

    def __str__(self):
        return self.code + " - " + self.french_name

    class Meta:
        verbose_name = _("Pays")
        verbose_name_plural = _("Pays")


class Address(models.Model):
    street = models.CharField(_("Avenue"), max_length=200, blank=True)
    city = models.CharField(_("Ville"), max_length=50, blank=True)
    commune = models.CharField(_("Commune"), max_length=50, blank=True)
    region = models.CharField(_("Province"), max_length=50, blank=True)
    country = models.CharField(_("Pays"), max_length=50, default="R.D. Congo")

    def __repr__(self):
        return "street: %s, city %s, commune: %s, region: %s" % \
                    (self.street, self.city,
                    self.commune, self.region)

    def __str__(self):
        return self.street + " " + self.commune + self.city + " " + self.region

    class Meta:
        verbose_name = _("Adresse")
        verbose_name_plural = _("Adresses")





