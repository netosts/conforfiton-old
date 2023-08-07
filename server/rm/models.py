from orator import Model
from kink import di


Model.set_connection_resolver(di["db"])


class RmConfig(Model):
    __table__ = "tbl_rm_config"
    __timestamps__= False