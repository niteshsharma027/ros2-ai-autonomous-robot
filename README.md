# 🤖 ROS 2 AI Autonomous Robot

An AI-powered autonomous mobile robot project built with **ROS 2 Jazzy**, Gazebo, RViz2, LiDAR, SLAM, Nav2, OpenCV and YOLO object detection.

> 🚧 **Project status:** Initial setup — development in progress.

## 🎯 Project Goal

Build a mobile robot capable of autonomous navigation, LiDAR-based obstacle detection, SLAM mapping, localization, path planning, camera-based perception and YOLO-powered object detection.

## 🧠 System Architecture

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

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Robotics middleware | ROS 2 Jazzy |
| Simulation | Gazebo |
| Visualization | RViz2 |
| Navigation | Nav2 |
| Mapping | SLAM Toolbox |
| Computer Vision | OpenCV |
| Object Detection | YOLO |
| Programming | Python / C++ |
| Robot Description | URDF / Xacro |
| Hardware target | ESP32 + motor controller |

## 📁 Planned Structure

```text
ros2-ai-autonomous-robot/
├── README.md
├── requirements.txt
├── .gitignore
├── ros2_ws/
│   └── src/
│       ├── robot_description/
│       ├── robot_bringup/
│       ├── robot_navigation/
│       ├── robot_vision/
│       ├── robot_control/
│       └── robot_interfaces/
├── simulation/
│   ├── gazebo/
│   ├── worlds/
│   └── models/
├── config/
│   ├── nav2.yaml
│   └── slam.yaml
├── models/
│   └── yolo/
├── scripts/
└── docs/
```

## 🚀 Development Roadmap

- [ ] Create differential-drive robot URDF/Xacro
- [ ] Add Gazebo simulation
- [ ] Add LiDAR sensor and `/scan`
- [ ] Add camera sensor
- [ ] Add ROS 2 TF and odometry
- [ ] Implement SLAM mapping
- [ ] Configure Nav2
- [ ] Add autonomous waypoint navigation
- [ ] Integrate OpenCV
- [ ] Integrate YOLO object detection
- [ ] Connect AI perception to ROS 2 decisions
- [ ] Add ESP32 hardware interface
- [ ] Test on a physical mobile robot

## 💻 Target Environment

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo
- RViz2
- Python 3

## 👨‍💻 Author

**Nitesh Sharma**  
Electronics & Telecommunication Engineering | AI/ML | Robotics | Embedded Systems
