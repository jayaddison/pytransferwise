from apiron import JsonEndpoint
from munch import munchify

from pytransferwise.base import Base


class SubscriptionService(Base):
    list = JsonEndpoint(path="/v3/profiles/{profile_id}/subscriptions")
    get = JsonEndpoint(path="/v3/profiles/{profile_id}/subscriptions/{subscription_id}")


class Subscription(object):
    service = SubscriptionService()

    def list(self, profile_id):
        return munchify(self.service.list(profile_id=profile_id))

    def get(self, profile_id, subscription_id):
        return munchify(
            self.service.get(profile_id=profile_id, subscription_id=subscription_id)
        )
