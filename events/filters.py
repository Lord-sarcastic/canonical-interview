from django_filters import rest_framework as filters

from .models import Event


class EventFilter(filters.FilterSet):
    log_level = filters.ChoiceFilter(
        field_name="log_level", choices=Event.LogLevel.choices
    )
    service_id = filters.CharFilter(field_name="service_id", lookup_expr="icontains")
    instance_id = filters.CharFilter(field_name="instance_id", lookup_expr="icontains")
    request_id = filters.CharFilter(field_name="request_id", lookup_expr="icontains")
    event_action = filters.ChoiceFilter(
        field_name="event_action`", choices=Event.Actions.choices
    )
    timestamp_gt = filters.DateTimeFilter(field_name="timestamp", lookup_expr="gt")
    timestamp_lt = filters.DateTimeFilter(field_name="timestamp", lookup_expr="lt")

    class Meta:
        model = Event
        fields = [
            "log_level",
            "service_id",
            "instance_id",
            "request_id",
            "event_action",
            "timestamp_gt",
            "timestamp_lt",
        ]
