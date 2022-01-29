CREATE TABLE "events"(
    "id" INTEGER NOT NULL,
    "log_level" VARCHAR(255) NOT NULL,
    "service_id" VARCHAR(255) NOT NULL,
    "instance_id" VARCHAR(255) NULL,
    "service_name" VARCHAR(255) NOT NULL,
    "service_info" VARCHAR(255) NULL,
    "request_id" VARCHAR(255) NULL,
    "event_action" VARCHAR(255) NOT NULL,
    "event_data" jsonb NOT NULL,
    "event_metadata" jsonb NULL,
    "timestamp" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "events" ADD PRIMARY KEY("id");
COMMENT
ON COLUMN
    "events"."log_level" IS 'Log level of the event. Should be one of:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL';
COMMENT
ON COLUMN
    "events"."service_id" IS 'An ID for the service that is generating the event';
COMMENT
ON COLUMN
    "events"."instance_id" IS 'Unique ID for the service instance incase the service is distributed';
COMMENT
ON COLUMN
    "events"."service_name" IS 'The name of the service that is generating the event';
COMMENT
ON COLUMN
    "events"."service_info" IS 'Additional information about the service that is generating the event';
COMMENT
ON COLUMN
    "events"."request_id" IS 'An ID for the request that is generating the event. Usually passed around to track events related to a request';
COMMENT
ON COLUMN
    "events"."event_action" IS 'The type of event that is being generated.

Must be one of:
- CREATE
- UPDATE
- DELETE
- RETRIEVE
- OTHER';
COMMENT
ON COLUMN
    "events"."event_data" IS 'Data generated from the service or passed to it from a request';
COMMENT
ON COLUMN
    "events"."event_metadata" IS 'Additional metadata about the event';