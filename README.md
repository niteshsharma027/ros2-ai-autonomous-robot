# 🤖 ROS 2 AI Autonomous Robot

An AI-powered autonomous mobile robot built with **ROS 2 Jazzy**, Gazebo, RViz2, LiDAR, SLAM, Nav2, OpenCV and YOLO object detection.

> 🚧 **Project status:** Phase 1 — robot simulation foundation.

## 🎯 Goal

Build a mobile robot capable of autonomous navigation, LiDAR obstacle detection, SLAM mapping, localization, path planning, camera perception and YOLO-powered object detection.

## 🧠 Architecture

```text
                    ROS 2 Jazzy
                         │
          ┌──────────────┼──────────────┐
          │              │              │
        LiDAR          Camera       Robot Model
          │              │              │
          ↓              ↓              ↓
        SLAM            YOLO          Gazebo
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                       Nav2
                         ↓
                   Path Planning
                         ↓
                 Autonomous Robot
```

## 📁 ROS 2 Workspace

```text
ros2-ai-autonomous-robot/
├── README.md
├── requirements.txt
├── .gitignore
└── ros2_ws/
    └── src/
        ├── robot_description/       # URDF/Xacro, links, sensors
        │   ├── urdf/
        │   ├── meshes/
        │   └── launch/
        ├── robot_bringup/            # Gazebo + ROS-Gazebo bridge
        │   ├── launch/
        │   ├── worlds/
        │   └── config/
        ├── robot_navigation/         # SLAM + Nav2 configs
        │   ├── config/
        │   ├── launch/
        │   └── maps/
        ├── robot_vision/              # OpenCV + YOLO perception
        │   ├── scripts/
        │   ├── config/
        │   └── launch/
        ├── robot_control/             # Motion and future ESP32 control
        │   ├── scripts/
        │   ├── config/
        │   └── launch/
        └── robot_interfaces/          # Future custom ROS messages/services
```

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Middleware | ROS 2 Jazzy |
| Simulation | Gazebo Harmonic |
| Visualization | RViz2 |
| Navigation | Nav2 |
| Mapping | SLAM Toolbox |
| Vision | OpenCV |
| AI detection | YOLO / Ultralytics |
| Description | URDF / Xacro |
| Language | Python / C++ |
| Target hardware | ESP32 + motor controller |

## 🚀 Phase 1 Features

- Differential-drive robot model
- Gazebo simulation world
- Left and right drive wheels
- Caster wheel
- LiDAR sensor
- RGB camera sensor
- Gazebo DiffDrive system
- ROS 2 `/cmd_vel` bridge
- ROS 2 `/odom` bridge
- ROS 2 `/scan` bridge
- ROS 2 `/camera/image_raw` bridge
- Robot State Publisher

## 💻 Build and Run

On **Ubuntu 24.04 with ROS 2 Jazzy**:

```bash
cd ~/ros2-ai-autonomous-robot/ros2_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

Launch the simulation:

```bash
ros2 launch robot_bringup sim.launch.py
```

In another terminal, verify the main ROS topics:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2-ai-autonomous-robot/ros2_ws/install/setup.bash
ros2 topic list
```

Expected topics include:

```text
/cmd_vel
/odom
/scan
/camera/image_raw
/tf
/tf_static
/clock
```

Send a simple forward command:

```bash
ros2 topic pub --rate 10 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"
```

Stop the robot with:

```bash
ros2 topic pub --rate 10 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.0}}"
```

## 🗺️ Development Roadmap

- [x] Create differential-drive robot URDF/Xacro
- [x] Add Gazebo simulation foundation
- [x] Add LiDAR sensor
- [x] Add camera sensor
- [x] Add ROS-Gazebo topic bridges
- [x] Add ROS 2 TF / robot state publisher
- [ ] Add RViz configuration
- [ ] Implement SLAM mapping
- [ ] Configure Nav2
- [ ] Add autonomous waypoint navigation
- [ ] Add OpenCV perception node
- [ ] Integrate YOLO object detection
- [ ] Connect AI perception to navigation decisions
- [ ] Add ESP32 hardware interface
- [ ] Test on a physical mobile robot

## 👨‍💻 Author

**Nitesh Sharma**  
Electronics & Telecommunication Engineering | AI/ML | Robotics | Embedded Systems
