# CYB333-Final-Project
Honey Pot
# CYB 333 Final Project – Honeypot Monitoring System  
**Author:** Dustin Allen  
**Course:** CYB 333 – Security Automation  
**Instructor:** Bruce Tukuafu

---

## 📌 Project Overview

This project is a Python-based honeypot designed to detect and log unauthorized access attempts. It simulates a vulnerable service to attract potential attackers, records key indicators of compromise (IOCs), and sends alerts when suspicious behavior is detected. The goal is to demonstrate automated security monitoring and response through a simplified honeypot deployment.

---

## 🎯 Objectives

- Create a functioning honeypot that can log network connections and suspicious commands.
- Automate alerts and event handling using Python.
- Demonstrate basic logging, monitoring, and response techniques.
- Learn and apply core concepts of security automation in a practical environment.

---

## 🛠️ Features

- TCP socket listener acting as a fake service  
- Logs incoming connections with IP, port, and timestamps  
- Command-line interaction logging  
- Optional integration with email or file-based alerts  
- Commented and clean Python codebase

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.x
- Git
- Linux environment (recommended: Ubuntu or Kali VM)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/honeypot-project.git
   cd honeypot-project
