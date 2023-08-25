from kink import di
from orator import Model, SoftDeletes
from orator.orm import morph_many
from ..user.models import User


Model.set_connection_resolver(di["db"])


class Company(Model, SoftDeletes):
    __table__ = "companies"

    @morph_many('entity')
    def users(self):
        return User
