from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from mobile_core.models import Address
from .abstract_models import AbstractShipMaster, AbstractTimeStampedModel


class IndividualShipMaster(AbstractShipMaster):
    auth_user = models.OneToOneField(User,
                                    related_name="ind_ship_master_user")       
    locations = models.ForeignKey(Address,
                                related_name="ind_ship_master_location")
    
    def __str__(self):
        return "ID: %s, Name: %s %s" % (self.auth_user.id,
                                        self.auth_user.first_name,
                                        self.auth_user.last_name)

    def __repr__(self):
        return "ID: %s, Name: %s %s" % (self.auth_user.id,
                                        self.auth_user.first_name,
                                        self.auth_user.last_name)


class BusinessShipMaster(AbstractShipMaster):
    auth_user = models.OneToOneField(User,
                                    related_name="bus_ship_master_user")
    business_name = models.CharField("Nom de l'entreprise")
    locations = models.ForeignKey(Address,
                                related_name="bus_ship_master_location")

    def __str__(self):
        return "ID: %s, Business Name: %s" % (self.auth_user.id, 
                                                self.auth_user.business_name)

    def __repr__(self):
        return "ID: %s, Business Name: %s" % (self.auth_user.id, 
                                                self.auth_user.business_name)


class ShipmentDestinataire(AbstractTimeStampedModel):
    auth_user = models.OneToOneField(User,
                                    related_name="destinataire_user")
    phone_number = models.CharField("Téléphone", blank=True, null=True)

    def __str__(self):
        return "ID: %s, Name: %s %s" % (self.auth_user.id,
                                        self.auth_user.first_name,
                                        self.auth_user.last_name)

    def __repr__(self):
        return "ID: %s, Name: %s %s" % (self.auth_user.id,
                                        self.auth_user.first_name,
                                        self.auth_user.last_name)


class ShipmentOwner(AbstractTimeStampedModel):
    auth_user = models.OneToOneField(User,
                                    related_name="ship_owner_user")
    phone_number = models.CharField("Téléphone", blank=True, null=True)

    def __str__(self):
        return "ID: %s, Name: %s %s" % (self.auth_user.id,
                                        self.auth_user.first_name,
                                        self.auth_user.last_name)

    def __repr__(self):
        return "ID: %s, Name: %s %s" % (self.auth_user.id,
                                        self.auth_user.first_name,
                                        self.auth_user.last_name)


class Shipment(AbstractTimeStampedModel):
    description = models.CharField("Description", blank=True, null=True)
    owner = models.ForeignKey(User, related_name="shipment_owner")


class ShippingMovement(AbstractTimeStampedModel):
    #Create generic relation for shipmaster
    #shipmaster = models.ForeignKey()

    