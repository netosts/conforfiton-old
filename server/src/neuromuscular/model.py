from orator import Model, SoftDeletes
from kink import di


Model.set_connection_resolver(di["db"])


class Neuromuscular(Model, SoftDeletes):
    __timestamps__ = False


class NeuromuscularRml(Model, SoftDeletes):
    __table__ = 'neuromusculars_rml'
    __timestamps__ = False
