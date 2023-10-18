from kink import di
from orator import Model


Model.set_connection_resolver(di["db"])


class LinkShare(Model):
    __table__ = "link_shares"
