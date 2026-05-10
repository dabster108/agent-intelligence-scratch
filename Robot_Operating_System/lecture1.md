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
nODE 2 -> ADCTOPMS AMD ,PVE ,NACL TO TPNOT 1 FEED NACL AMD
```

# Parameter - > Environment Config

# Actions 1 -> 1

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

```md
Node 1 (Publisher) ---> Topic ---> Node 2 (Subscriber)
```

### Bidirectional Communication Example

```md
Node 1 publishes data
↓
Topic
↓
Node 2 receives data and performs actions

Node 2 sends feedback/data
↓
Another Topic
↓
Node 1 receives feedback
```

---

# 4. Parameters

A **Parameter** is used to store configuration data in ROS.

Parameters help nodes access shared settings and environment configurations.

### Examples

- Robot speed
- Sensor threshold
- Environment configuration
- Camera resolution

### Parameter Example

```md
Parameter: robot_speed = 5
Parameter: environment_mode = simulation
```

### Purpose of Parameters

- Store global configuration
- Share environment settings between nodes
- Avoid hardcoding values

---

# 5. Services

A **Service** is used for request-response communication.

### Service Communication

```md
Node 1 ---> Service Request ---> Node 2
Node 2 ---> Service Response ---> Node 1
```

### Example

```md
Request: Move Robot 1 cm
Response: Movement Completed
```

---

# 6. Actions

Actions are used for long-running tasks where continuous feedback is required.

### Features of Actions

- Continuous feedback
- Goal-based communication
- Can be cancelled during execution

### Action Communication

```md
Action Client ---> Action Server
```

### Workflow

```md
Node 1 sends action request
↓
Node 2 processes the task
↓
Node 2 sends continuous feedback
↓
Node 1 receives final result
```

---

# 7. One-to-One Communication

ROS supports direct one-to-one communication between two entities.

### Example

```md
Node 1 <----> Node 2
```

### Uses

- Robot movement
- Device control
- Command execution
- Real-time feedback

---

# 8. ROS Communication Overview

```md
Publisher ---> Topic ---> Subscriber

Node ---> Service ---> Response

Action Client ---> Action Server

Parameters ---> Environment Configuration
```

---

# Key Concepts Summary

| Concept                  | Description                               |
| ------------------------ | ----------------------------------------- |
| Node                     | Individual executable process             |
| Topic                    | Communication channel                     |
| Publisher                | Sends data                                |
| Subscriber               | Receives data                             |
| Parameter                | Stores environment configuration          |
| Service                  | Request-response communication            |
| Action                   | Long-running task with feedback           |
| One-to-One Communication | Direct communication between two entities |
