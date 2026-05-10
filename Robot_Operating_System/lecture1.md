# ROS Communication Concepts

## 1. Node

A **Node** is an individual executable entity/process in ROS that performs a specific task.

### Examples

- Node 1 → Sends Data
- Node 2 → Receives Data
- Node 3 → Receives Data and Applies Logic

Each node works independently but communicates with other nodes.

---

# 2. Topics

A **Topic** is a communication channel used to exchange data between nodes.

- Topics carry pathway data/messages.
- Multiple nodes can publish or subscribe to the same topic.

### Example Topics

- `/robot_position`
- `/sensor_data`

---

# 3. Publisher and Subscriber

## Publisher

A publisher sends data to a topic.

## Subscriber

A subscriber receives data from a topic.

### Communication Flow

```text
Node 1 (Publisher) ---> Topic ---> Node 2 (Subscriber)
```
