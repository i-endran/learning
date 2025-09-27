# Event-Driven Architecture (EDA), Pub-Sub, and Observer Pattern

**Interview Preparation Notes (FAANG-ready)**

---

## 1. Core Concepts

### **Observer Pattern (Design Pattern)**

* **Level**: Code-level (in-process).
* **Definition**: One-to-many dependency between objects. Subject notifies observers when state changes.
* **Example**: UI button click → triggers callbacks (`onClick`).
* **Traits**:

  * Tight coupling (observers tied to subject’s interface).
  * Usually synchronous, single process.
  * No external infra required.

👉 **Good to know for interviews**: This is the foundation of UI programming, often asked in OOP/design pattern rounds.

---

### **Publish–Subscribe (Messaging Pattern)**

* **Level**: Integration-level (services/apps).
* **Definition**: Publisher emits messages to a topic/channel; subscribers consume asynchronously. Publishers don’t know who listens.
* **Example**: Kafka topic `OrderPlaced` consumed by Inventory and Notification services.
* **Traits**:

  * Loose coupling.
  * Supports async and distributed systems.
  * Needs broker (Kafka, RabbitMQ, Pulsar, SNS/SQS).

👉 **Good to know for interviews**: Often used as a stepping stone when asked *“How do you decouple microservices?”*

---

### **Event-Driven Architecture (EDA)**

* **Level**: System-level architecture.
* **Definition**: Architectural style where events are the main communication mechanism. Services produce, publish, and react to events.
* **Example**: E-commerce → `OrderPlaced` drives Inventory, Payment, Notification, Analytics.
* **Traits**:

  * Very loose coupling.
  * Enables scalability, resilience, extensibility.
  * Built on top of patterns like pub-sub.
  * Supports event replay, event sourcing, CQRS.

👉 **Good to know for interviews**: FAANG often tests how you handle **scalability, resilience, and loose coupling** — EDA is a go-to answer.

---

## 2. Ways to Implement EDA

### 1. **Pub-Sub**

* Common, simplest.
* Producer publishes → broker → consumers subscribe.

### 2. **Event Streaming**

* Events stored as immutable logs.
* Consumers replay events at their own pace.
* Example: Kafka, Redpanda.

### 3. **Event Sourcing**

* Persist all events, not just state.
* System state = replay of events.
* Usually paired with CQRS.

### 4. **Direct Event Notification**

* Services send events via callbacks/webhooks (no broker).
* Lightweight, less scalable.

### 5. **Choreography vs Orchestration**

* **Choreography**: Services react to each other’s events (decentralized).
* **Orchestration**: Central coordinator drives the workflow (not pure EDA).

---

## 3. EDA vs Pub-Sub vs Observer (Comparison Table)

| Aspect             | Observer Pattern      | Pub-Sub Messaging      | Event-Driven Architecture                 |
| ------------------ | --------------------- | ---------------------- | ----------------------------------------- |
| **Level**          | Design pattern (code) | Messaging pattern      | System-level architecture                 |
| **Scope**          | In-process            | Across apps/services   | Entire distributed system                 |
| **Coupling**       | Tight                 | Loose (via broker)     | Very loose                                |
| **Sync/Async**     | Mostly sync           | Mostly async           | Async (eventual consistency)              |
| **Infrastructure** | None                  | Broker required        | Broker + storage + design                 |
| **Example**        | Button click listener | Kafka topic subscriber | Microservices reacting to business events |

---

## 4. When to Use EDA

* **Best fit**:

  * Systems needing **scalability** (independent services scale separately).
  * **Loose coupling** is critical.
  * **Eventual consistency** acceptable.
  * **Real-time processing** (IoT, fraud detection, analytics, notifications).

* **Not ideal**:

  * When strong **synchronous consistency** is required.
  * Simple CRUD apps with minimal integration.

---

## 5. Example: E-commerce Order Flow

### Microservices (sync, no EDA)

1. User places order → Order Service.
2. Order Service calls Inventory, Payment, Notification synchronously.
3. Failures block the flow.

### EDA (async with events)

1. Order Service publishes `OrderPlaced`.
2. Inventory, Payment, Notification, Analytics independently consume.
3. Failure in one service doesn’t block others.

👉 Hybrid model often used: Payment is synchronous; other side-effects (email, analytics) are async via events.

---

## 6. Quick Interview Tips (FAANG-Focused)

1. **Be precise with scope**:

   * If asked about **Observer**, keep it in design pattern context (UI, callbacks).
   * If asked about **Pub-Sub**, talk about messaging systems.
   * If asked about **EDA**, talk at system-level (microservices, distributed design).

2. **Stress trade-offs**:

   * **EDA** = scalable, resilient, but complex (debugging, eventual consistency).
   * **Sync APIs** = simple, but tightly coupled.
   * A **hybrid** is usually best.

3. **Use real-world examples**:

   * “Placing an order on Amazon is a classic EDA case: order triggers dozens of services asynchronously.”
   * “Facebook likes update asynchronously (EDA), but login is synchronous.”

4. **Mention tooling**:

   * Kafka, RabbitMQ, Pulsar, SQS/SNS for messaging.
   * CQRS + Event Sourcing for advanced use.
   * Tracing tools (Jaeger, OpenTelemetry) to handle complexity.

5. **Show awareness of pitfalls**:

   * Harder debugging (need correlation IDs).
   * Event duplication/out-of-order issues.
   * Eventual consistency not always acceptable.

---

## 7. FAANG-Level “Know This” Checklist

✅ Observer = local callbacks (UI, OOP pattern).
✅ Pub-Sub = decoupled messaging via broker.
✅ EDA = architectural style for distributed systems.
✅ EDA can be implemented via pub-sub, event streaming, event sourcing, direct notifications, choreography.
✅ Hybrid model (sync + async) is common in real-world systems.
✅ Always mention **trade-offs** (coupling, latency, consistency).
✅ Be able to sketch an **e-commerce order flow** with and without EDA.
✅ Know at least one tool (Kafka) in detail for scaling conversations.

---

**Bottom line for interviews**:

* Start with **Observer** (local), move to **Pub-Sub** (distributed messaging), then **EDA** (system-wide design).
* Highlight **scalability, resilience, and decoupling** as key benefits.
* Acknowledge **complexity and eventual consistency** as trade-offs.
