# 🧠 Computer Science Interview Cheat Sheet

## 1. Operating Systems (OS) 🖥️

### Core Concepts 📚

- **Processes & Threads:** *Process states*, **PCB**, *context switching*, **multithreading**, **concurrency**.
- **Scheduling Algorithms:** **FCFS**, **SJF**, **RR**, **Priority**, **MLFQ** — know tradeoffs (*throughput*, *turnaround*, *starvation*).
- **Synchronization:** *Race conditions*, **critical section**, **mutex**, **semaphores**, **monitors**, **deadlock** (4 conditions, avoidance via *Banker’s algorithm*).
- **Memory Management:** **Paging**, **segmentation**, **virtual memory**, page replacement (**LRU**, **FIFO**, **Optimal**), **TLB**.
- **File Systems:** **Inodes**, allocation (*contiguous*, *linked*, *indexed*), **journaling**.
- **System Calls & Kernel/User Mode**.

#### One-liners 💡

- Process states: A process moves through states like *new*, *ready*, *running*, *waiting*, *terminated* representing its lifecycle stage.
- PCB: Process Control Block — OS data structure storing a process's metadata (PID, registers, memory map, state).
- Context switching: Saving and restoring CPU registers and state to switch execution between processes/threads.
- Multithreading: Multiple threads within the same process that share address space but can run independently.
- Concurrency: Multiple tasks making progress in overlapping time requiring coordination to avoid races.
- FCFS: First-Come-First-Served — simple queue-based scheduling, can cause long wait times.
- SJF: Shortest Job First — minimizes average turnaround but may starve long jobs.
- RR: Round Robin — time-sliced fair scheduling useful for time-sharing systems.
- Priority: Schedules tasks by priority, can cause priority inversion if unmanaged.
- MLFQ: Multi-Level Feedback Queue — adapts priorities based on observed behavior to balance responsiveness and throughput.
- Critical section: Code region where shared resources are accessed and must be protected.
- Mutex: Mutual exclusion primitive allowing only one thread to enter a critical section.
- Semaphore: Counter-based synchronization for signaling or resource counting.
- Monitor: High-level synchronization construct combining mutexes and condition variables.
- Deadlock: Situation where processes wait forever due to circular resource holds (mutual exclusion, hold-and-wait, no preemption, circular wait).
- Paging: Memory management that divides memory into fixed-size pages mapped to frames.
- Segmentation: Memory organized into variable-sized logical segments (code, stack, heap).
- Virtual memory: Illusion of large contiguous memory using disk backing and paging.
- LRU/FIFO/Optimal: Page replacement policies — LRU uses recent history, FIFO uses arrival order, Optimal is theoretical best.
- TLB: Translation Lookaside Buffer — cache for virtual-to-physical address translations.
- Inodes: File metadata structures storing permissions, pointers to data blocks, and file attributes.
- Contiguous/linked/indexed allocation: Different strategies for placing file data on disk balancing performance and fragmentation.
- Journaling: File system technique to record metadata changes for faster recovery.
- System call: Controlled interface for user programs to request kernel services.

#### Common Interview Questions ❓

- Difference between **process** vs **thread**?
- How does *context switching* work?
- What happens on a *page fault*?
- How does the OS handle **deadlocks**?

## 2. Database Management Systems (DBMS) 💾

### Core Concepts 📚

- **Data Models:** *Relational model*, **schema**, **ER diagrams** → relations.
- **SQL Essentials:** **SELECT**, **JOINs**, **GROUP BY**, *subqueries*, **indexes**.
- **Normalization:** *1NF → BCNF*, anomalies (insertion, deletion, update).
- **Transactions:** **ACID** properties, *Commit/Rollback*, *Serializability*, **2-Phase Locking**.
- **Concurrency Control:** **Locks**, **deadlocks**, *isolation levels* (Read Uncommitted → Serializable).
- **Indexing & Query Optimization:** **B+ Trees**, **Hash Indexing**, *clustered vs non-clustered*.
- **Storage & Recovery:** **WAL (Write-Ahead Log)**, *checkpoints*.

#### One-liners 💡

- Relational model: Data represented as tables (relations) with rows and columns.
- Schema: Definition of table structures, types, and constraints.
- ER diagrams: Visual modeling of entities and relationships.
- SELECT/JOIN/GROUP BY: Basic SQL operations for querying and combining data.
- Indexes: Data structures (B+ trees, hashes) that speed up lookup at the cost of extra storage and maintenance.
- 1NF→BCNF: Normal forms progressively reduce redundancy and anomalies.
- ACID: Atomicity, Consistency, Isolation, Durability — properties that make transactions reliable.
- Commit/Rollback: Finalize or undo a transaction's changes.
- Serializability: Correctness criterion ensuring concurrent transactions have serial-equivalent effect.
- 2-Phase Locking: Locking protocol that helps ensure serializability by acquiring then releasing locks.
- Isolation levels: Trade correctness vs performance (Read Uncommitted → Serializable).
- B+ Tree: Balanced tree index optimized for range queries and disk access.
- Hash indexing: Fast lookups for equality queries, not suitable for range scans.
- WAL: Write-Ahead Log ensures changes are logged before being applied for recovery.
- Checkpoints: Periodic flushes of state to speed recovery.

#### Interview Topics 📝

- Why use **normalization**?
- How do **indexes** speed up queries?
- Difference between **SQL** & **NoSQL**?
- What is the difference between **inner**, **left**, **right** joins?

## 3. Computer Networks (CN) 🌐

### Core Concepts 📚

- **OSI vs TCP/IP Layers:** functions + protocols in each.
- **Application Layer:** **HTTP/HTTPS**, **DNS**, **SMTP**, **FTP**.
- **Transport Layer:** **TCP** (3-way handshake, flow control, congestion control), **UDP** differences.
- **Network Layer:** **IP addressing**, **routing** (static vs dynamic, shortest path), **ICMP**.
- **Data Link Layer:** **MAC**, **ARP**, **CSMA/CD**, **switching**.
- **Physical Layer:** *bandwidth*, *latency*, transmission media.
#### Networking Concepts 🔌

- **DNS resolution process**
- **NAT**, **Subnetting**
- Difference between **switch**, **hub**, **router**
- **CDN**, **load balancing**, **reverse proxy**
#### One-liners 💡

- OSI vs TCP/IP: Layered models separating concerns from physical link up to application protocols.
- HTTP/HTTPS: Protocols for web requests (HTTPS = HTTP over TLS for security).
- DNS: Maps human names to IP addresses via hierarchical queries and caching.
- TCP: Reliable, ordered, connection-oriented transport with flow and congestion control.
- UDP: Connectionless, low-overhead transport for latency-sensitive apps without reliability guarantees.
- IP addressing: Logical addressing for routing packets across networks.
- Routing: Process of selecting paths for packets using algorithms like shortest-path.
- ICMP: Network diagnostic and error messaging protocol (e.g., ping).
- MAC/ARP: Link-layer addressing and mapping IP to physical addresses.
- CSMA/CD: Media access control used in older Ethernet to avoid collisions.
- Bandwidth vs latency: Bandwidth is transfer rate; latency is delay — both affect throughput.
- DNS resolution: Iterative/recursive queries from resolver → root → TLD → authoritative nameserver.
- NAT: Translates private IPs to public IPs enabling address reuse.
- Subnetting: Dividing IP address space into smaller networks using masks.
- Switch/hub/router: Hub broadcasts, switch forwards by MAC, router routes between networks by IP.
- CDN/load balancer/reverse proxy: Infrastructure to speed content delivery and distribute traffic.

**Key Formulas:** `Bandwidth = bits/time`, *Throughput ≠ Bandwidth necessarily*.

## 4. Distributed Systems 🔗

### Core Concepts 📚

- **Goals:** *Scalability*, *fault tolerance*, *transparency*.
- **Architectures:** *Client-server*, *peer-to-peer*, *microservices*.
- **Consistency Models:** *Strong*, *eventual*, *causal*.
- **CAP Theorem:** **Consistency**, **Availability**, **Partition tolerance** (choose 2).
- **Consensus:** *Paxos*, *Raft* basics.
- **Replication & Sharding:** *Horizontal vs vertical scaling*, replication lag.
- **Fault Tolerance:** *Leader election*, heartbeats, failover.
- **Synchronization:** **Lamport** (logical clocks), *vector clocks*.

#### One-liners 💡

- Scalability: Ability to handle growth by adding resources (horizontal/vertical scaling).
- Fault tolerance: System continues to operate correctly despite failures.
- Client-server/peer-to-peer/microservices: Architectural styles for distributing functionality.
- Strong/eventual/causal consistency: Different guarantees on how up-to-date replicas appear to clients.
- CAP theorem: In presence of partitions choose two of Consistency, Availability, Partition tolerance.
- Paxos/Raft: Consensus algorithms to agree on a value among unreliable nodes.
- Replication vs sharding: Replication copies data for redundancy; sharding splits data for scale.
- Leader election: Process to choose a coordinator for tasks like committing logs.
- Heartbeat/failover: Mechanisms to detect failures and switch to backups.
- Lamport/vector clocks: Logical time systems to order events without synchronized clocks.

**System Design Connection:** load balancers, caching, distributed databases, message queues (**Kafka**, **RabbitMQ**).

## 5. Data Structures & Algorithms (Quick Ref) 🧮

### Core Structures 🧱

- **Array**, **Linked List**, **Stack**, **Queue**, **HashMap**, **Tree**, **Graph**, **Heap**, **Trie**, **Union-Find**.

### Algorithm Patterns ⚙️

- **Sorting:** *Quick*, *Merge*, *Heap*.
- **Searching:** *Binary*, *BFS*, *DFS*.
- **Patterns:** Greedy, DP, Backtracking, Sliding Window, Two Pointers.
- **Complexity:** Know **Big O** for standard operations.

#### One-liners 💡

- Array: Fixed-size contiguous memory offering O(1) access by index.
- Linked List: Nodes with pointers allowing O(1) inserts/deletes at known positions.
- Stack/Queue: LIFO and FIFO abstract data types for last-in-first-out and first-in-first-out behavior.
- HashMap: Key-value store offering average O(1) lookup via hashing.
- Tree/Binary Tree: Hierarchical structure for sorted data and logarithmic ops.
- Graph: Nodes and edges modeling arbitrary relationships; traversed with BFS/DFS.
- Heap: Binary heap supports efficient min/max extraction used in priority queues.
- Trie: Prefix tree for fast string prefix queries.
- Union-Find: Disjoint-set structure for tracking components with union and find operations.
- Quick/Merge/Heap sorts: Common sorting algorithms with different tradeoffs (avg-case, stability, memory).
- Binary/BFS/DFS searches: Fundamental search algorithms for sorted arrays and graphs.
- Greedy/DP/Backtracking: Common algorithmic patterns for optimization and combinatorial problems.
- Big O: Notation describing asymptotic time/space complexity.

**Interview focus:** Implementations + reasoning.

## 6. System Design (For MAANG) 🏗️

### Low-Level 🛠️

- Threads, caching, concurrency, database schema design.

### High-Level 🚀

- Scalability (load balancing, sharding, caching).
- High availability (replication, failover).
- Databases: **SQL** vs **NoSQL**.
- Consistency: *Eventual* vs *strong*.
- Queueing: **Kafka**, **SQS**, **RabbitMQ**.
- Caching: **Redis**, **Memcached**.

#### One-liners 💡

- Threads: Lightweight execution contexts within a process sharing memory.
- Caching: Storing frequently accessed data in fast storage to reduce latency and load.
- Concurrency: Coordinating multiple executing units to safely access shared resources.
- Database schema design: Structuring tables and relationships to efficiently model and query data.
- Load balancer: Distributes incoming traffic across multiple servers to improve availability.
- Sharding: Partitioning data across machines to scale storage and queries.
- Replication: Copying data across nodes for redundancy and read scalability.
- Kafka/SQS/RabbitMQ: Message-oriented systems for decoupling producers and consumers.
- Redis/Memcached: In-memory stores used for caching and fast lookups.

#### Common Designs 🧩

- **URL shortener**
- **Chat system**
- **Feed system** (like *Twitter*)
- **Rate limiter**
- **Distributed file storage**

## 7. Compiler / Theory of Computation (Quick glance) 📐

- **Phases:** Lexical → Syntax → Semantic → Intermediate → Optimization → Code Gen.
- **Regular vs Context-free languages.**
- **Finite Automata:** DFA/NFA.
- **Complexity classes:** *P*, *NP*, *NP-complete* basics.

#### One-liners 💡

- Lexical/Syntax/Semantic/Optimization/CodeGen: Compiler phases transforming source code to optimized machine code.
- Regular vs Context-free: Classes of languages recognized by finite automata vs pushdown automata.
- DFA/NFA: Deterministic and nondeterministic finite automata for regular languages.
- P/NP/NP-complete: Complexity classes describing tractable vs intractable decision problems.

## 8. Software Engineering + Misc 🧰

- **Version control:** Git branching, *merge vs rebase*.
- **Testing:** Unit, integration, regression.
- **Agile & CI/CD** basics.
- **API Design:** **REST** vs **gRPC**.
- **Security:** HTTPS, encryption, *authentication vs authorization*, **OAuth**.

#### One-liners 💡

- Git branching/merge/rebase: Techniques for managing parallel development and integrating changes.
- Unit/integration/regression testing: Levels of testing from individual units to full-system checks and preventing regressions.
- Agile & CI/CD: Iterative development practices and automated build/test/deploy pipelines.
- REST vs gRPC: API styles — REST uses HTTP/JSON, gRPC uses protobufs and HTTP/2 for performance.
- Authentication vs Authorization: Authentication verifies identity; authorization checks access rights.
- HTTPS/OAuth: HTTPS secures transport; OAuth is an authorization framework for delegated access.

---

## ⚡ Bonus Tip

When revising for interviews:

- For each subject, be able to explain a core concept in *60 seconds* (an elevator pitch).
- Keep a mental map: “**OS → concurrency**, **DBMS → ACID**, **CN → layers**, **DS → CAP theorem**”.