<div align="center">

# 🚗 HIGH-SPEED ROBO CAR

### ⚡ ESP32 • Bluetooth Control • L298N • 300 RPM Motors

<p>
  <img src="https://img.shields.io/badge/ESP32-MicroPython-000000?style=for-the-badge&logo=espressif&logoColor=white">
  <img src="https://img.shields.io/badge/Bluetooth-Wireless-blue?style=for-the-badge&logo=bluetooth&logoColor=white">
  <img src="https://img.shields.io/badge/L298N-Motor%20Driver-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/300%20RPM-DC%20Motors-orange?style=for-the-badge">
</p>

<p>
  <b>A wireless-controlled robotic car built using ESP32 and DC motors.</b>
</p>

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-hardware">Hardware</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-code">Code</a> •
  <a href="#-future-scope">Future Scope</a>
</p>

</div>

---

## 📸 Project Gallery

<div align="center">

<img src="Images/Picture1.jpg" width="42%">
<img src="Images/Picture2.jpg" width="42%">

<br><br>

<img src="Images/Picture3.png" width="42%">
<img src="Images/Picture4.jpg" width="42%">

<br><br>

<img src="Images/Picture5.jpg" width="42%">
<img src="Images/Picture6.jpg" width="42%">

</div>

---

# 🚀 Overview

**High-Speed Robo Car** is an academic robotics project developed using an **ESP32 microcontroller**, wireless communication, an **L298N motor driver**, and **four 300 RPM DC motors**.

The ESP32 acts as the main controller of the vehicle. Commands received wirelessly are processed and converted into motor-control signals, allowing the car to move in different directions.

### 🎮 Supported Controls

```text
        ┌─────────────┐
        │   FORWARD   │
        └──────┬──────┘
               │
     ┌─────────┼─────────┐
     ▼         ▼         ▼
   LEFT      STOP      RIGHT
     │                   │
     └─────────┬─────────┘
               ▼
        ┌─────────────┐
        │  BACKWARD   │
        └─────────────┘
