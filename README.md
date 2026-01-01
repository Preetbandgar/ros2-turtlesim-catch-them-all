# 🐢 ROS2 Turtlesim – Catch Them All

![ROS2](https://img.shields.io/badge/ROS2-Jazzy-blue)
![Python](https://img.shields.io/badge/Python-3.12-green)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-orange)

---

## 📌 Overview
This project demonstrates a **multi-node ROS2 application** built on top of the Turtlesim simulator. A main turtle autonomously chases and catches dynamically spawned turtles using ROS2 publishers, subscribers, services, timers, and custom interfaces.

> ⚠️ **Transparency Note**: This project was built as a hands-on learning exercise by following a structured ROS2 course. While the system was successfully built, launched, and introspected, the primary goal was understanding ROS2 architecture and tooling rather than inventing new algorithms.

---

## 🧠 System Architecture

### Nodes
- **`/turtlesim`** (ROS2 provided)
  - Simulation environment
  - Provides `/spawn` and `/kill` services
  - Publishes turtle pose and sensor topics

- **`/turtle_spawner`**
  - Periodically spawns new turtles
  - Publishes the list of active turtles on `/alive_turtles`

- **`/turtle_controller`**
  - Subscribes to `/turtle1/pose`
  - Subscribes to `/alive_turtles`
  - Publishes velocity commands to `/turtle1/cmd_vel`

---

## 🔄 Communication

### Topics
- `/turtle1/pose`
- `/turtle1/cmd_vel`
- `/alive_turtles`

### Services
- `/spawn`
- `/kill`

### Custom Interfaces

**`Turtle.msg`**

```text
string name
float32 x
float32 y
float32 theta
```

**`TurtleArray.msg`**

```text
Turtle[] turtles
```

---

## 📂 Repository Structure
```text
ros2-turtlesim-catch-them-all/
├── README.md
├── screenshots/
├── videos/
├── src/
│   ├── my_robot_bringup/
│   │   ├── launch/
│   │   │   └── turtlesim_catch_them_all.launch.xml
│   │   ├── config/
│   │   │   └── catch_them_all_config.yaml
│   │   ├── CMakeLists.txt
│   │   └── package.xml
│   ├── my_robot_interfaces/
│   │   ├── msg/
│   │   │   ├── Turtle.msg
│   │   │   └── TurtleArray.msg
│   │   ├── srv/
│   │   │   └── CatchTurtle.srv
│   │   └── package.xml
│   └── turtlesim_catch_them_all/
│       ├── turtlesim_catch_them_all/
│       │   ├── turtle_controller.py
│       │   └── turtle_spawner.py
│       ├── setup.py
│       └── package.xml
```

---

## 🛠 Prerequisites
- Ubuntu 24.04 LTS
- ROS2 Jazzy

---

## ⚙️ Build Instructions

### Update dependencies
```bash
  rosdep update
  rosdep install --from-paths src --ignore-src -y
```

### Build workspace
```bash
  colcon build --symlink-install
```

### Source environment
```bash
  source install/setup.bash
```

---

## ▶️ Run the Project

```bash
ros2 launch my_robot_bringup turtlesim_catch_them_all.launch.xml
```

---

## 🔍 Runtime Introspection

### Node List

```bash
ros2 node list
```

![Node List](./screenshots/node_list.png)

### Topic List

```bash
ros2 topic list
```

![Topic List](./screenshots/topic_list.png)

### Topic Info

```bash
ros2 topic info /alive_turtles
```

![Alive Turtles Topic Info](./screenshots/alive_turtles_echo.png)

### Node & Topic Graph

```bash
rqt_graph
```

![RQT Graph](./screenshots/rqt_graph.png)

---

## 🎥 Demo
A short demo video showing:
- Launch execution
- Turtle spawning
- Autonomous chasing behavior
- ROS2 introspection

📽 **Demo Video**:

![Demo Video](./videos/turtlesim_demo.gif)
---

## 🧪 Expected Behavior
- New turtles spawn periodically
- Main turtle (`turtle1`) chases active turtles
- System continues autonomously

---

## 🧠 ROS2 Concepts Demonstrated
- Nodes & packages
- Publishers & subscribers
- Services
- Timers
- Custom interfaces
- Launch files
- Runtime introspection (`ros2 node`, `ros2 topic`, `rqt_graph`)

---

## 🚀 Possible Improvements
- Smarter target selection
- Multi-hunter turtles
- Event-based architecture
- Dockerized deployment

---

## 📜 Credits
Built by following the **ROS2 for Beginners** course by **Edouard Renard (Udemy)** as a learning exercise.

---

## 👤 Author

GitHub: https://github.com/Preetbandgar

