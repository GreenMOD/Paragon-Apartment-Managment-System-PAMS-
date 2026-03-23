from db import (
    fetch_notifications,
    mark_notification_as_read
)


class NotificationService:

    def __init__(self, tenant_id, location_id):
        self.tenant_id = tenant_id
        self.location_id = location_id
        self.last_notification_id = 0

    def get_notifications(self, personal, public):

        tenant = self.tenant_id if personal else None
        location = self.location_id if public else None

        notifications = fetch_notifications(tenant, location)

        return notifications

    def mark_as_read(self, notification_id):
        mark_notification_as_read(notification_id)