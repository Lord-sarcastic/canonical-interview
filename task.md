# Task
Please build a service that provides access to an audit log of events that have taken place within a system of microservices. Services forward events to this service to provide a record of what, when, and where happened. Examples include:

- a new customer account was created for a given identity;
- a customer record was correlated with an external identity / record in another system;
- a customer was billed a certain amount;
- a customer account was deactivated.

The types of events are open-ended. We do not know all kinds of events we might need to add in the future. There will likely be new services created that will need to be audited with new types of events.

Your task is to model an audit trail of events received from such services with a schema that captures the invariant data content along with the variant, application-specific content. Design and (quickly and informally is fine, just capture the intent!) document a microservice API that can receive, store and retrieve these events, and implement it as a proof-of-concept (PoC) HTTP server in Python or Go.

The microservice must be developed in Python or Go and any data storage mechanism may be used for the PoC. In case you decide to use an in-memory data storage, make sure it is concurrency-safe. Simple sequential flat files of records are also fine. Also note that this service is write-mostly, read-seldom.

As this is a PoC you are not expected to solve all possible operational and scalability issues. However, please make notes in the code why you decided to take a shortcut or how it can be addressed in the future as a TODO item for the code reviewer. You will also be asked for a plan to address these concerns in your interview.