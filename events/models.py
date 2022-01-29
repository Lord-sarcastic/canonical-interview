from django.db import models


class Event(models.Model):
    class Actions(models.TextChoices):
        CREATE = "CREATE", "Create"
        UPDATE = "UPDATE", "Update"
        DELETE = "DELETE", "Delete"
        RETRIEVE = "RETRIEVE", "Retrieve"
        OTHER = "OTHER", "Other"

    class LogLevel(models.TextChoices):
        DEBUG = "DEBUG", "Debug"
        INFO = "INFO", "Info"
        WARNING = "WARNING", "Warning"
        ERROR = "ERROR", "Error"
        CRITICAL = "CRITICAL", "Critical"

    log_level = models.CharField(
        max_length=50, choices=LogLevel.choices, help_text="Log level of the event"
    )
    service_id = models.CharField(
        max_length=255, help_text="An ID for the service that is generating the event"
    )
    instance_id = models.CharField(
        help_text="Unique ID for the service instance incase the service is distributed",
        blank=True,
        null=True,
        max_length=255,
    )
    service_name = models.CharField(
        max_length=255, help_text="The name of the service that is generating the event", blank=True, null=True
    )
    service_info = models.CharField(
        max_length=255,
        help_text="Additional information about the service that is generating the event",
        blank=True,
        null=True,
    )
    request_id = models.CharField(
        max_length=255,
        help_text="An ID for the request that is generating the event. Usually passed around to track events related to a request",
        blank=True,
        null=True
    )
    event_action = models.CharField(
        max_length=255,
        choices=Actions.choices,
        help_text="The type of event that is being generated",
    )
    event_data = models.JSONField(
        default=dict,
        help_text="Data generated from the service or passed to it from a request",
    )
    event_metadata = models.JSONField(
        default=dict, help_text="Additional metadata about the event",
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
