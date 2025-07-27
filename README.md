# 🚘 Ethical Driving Simulation in CARLA

**Dissertation Topic - Research And Application Of Ethical Decision-Making Frameworks In The Design And Development Of A Prototype Of An Autonomous Vehicle**  
Author: Dilasha Ghimire

This project demonstrates how ethical decision-making frameworks - **Utilitarianism**, **Deontological Ethics**, and **Virtue Ethics**, can be encoded into the behavior of autonomous vehicles using the CARLA simulator. It is designed as a proof-of-concept for academic research.

---

## 📌 Project Overview

This simulator tests how autonomous vehicles can make decisions in ethically challenging situations such as:

- Pedestrian crossings
- Obstacles on the road

Each situation is simulated multiple times using three distinct ethical logic modules. Outcomes are logged and analyzed for consistency, safety, and moral alignment.

---

## 🧠 Ethical Frameworks Implemented

- **Utilitarianism**: Minimize overall harm
- **Deontology**: Follow moral rules regardless of outcomes
- **Virtue Ethics**: Focus on moral character and context

---

## 🛠 Project Structure

```bash
EthicalDrivingCARLA/
├── ethics_engine.py                   # Ethical logic implementations for simulator
├── ethics_logic_reporting.py          # Ethical logic theoritical implementations
├── run_simulation.py                  # Simulation runner for logic
├── simulation.py                      # Simulation runner (3 scenarios × 3 modes)
├── results/                           # Output logs and CSVs
├── recordings/                        # Video recordings of simulator
└── screenshots/                       # Screenshots of every scenario
```

---

## ▶️ Getting Started

### 1. Prerequisites

- CARLA Simulator (Download: https://carla.org/)
- Python 3.7+
- NVIDIA GPU (recommended)

### 2. Setup

```bash
pip install carla numpy matplotlib
```

### 3. Run a Simulation

```bash
python simulation.py
```

### 4. Run the theoritical simulation

```bash
python run_simulation.py
```

---

## 📊 Output

Each simulation run generates:

- Logged outcomes (success/failure)
- Decision taken by the AV
- Charts comparing ethical modes

Example visualizations include:

- CSV
- Annotated screenshots or videos

---

## 🎓 Academic Relevance

This project contributes to research on:

- Machine ethics in autonomous vehicles
- Safe and explainable AI decisions
- Ethical AI design and simulation-based validation

It demonstrates that rule-based ethical frameworks can be logically applied to AVs and yield consistent, transparent behavior in simulated environments.

---

## 📝 Acknowledgements

- [CARLA Simulator](https://carla.org/)
- Coventry University / Softwarica College
- Supervisor: Mr. Manoj Shrestha

---

## ✅ License

This project is for academic demonstration purposes only. Not intended for commercial use or real-world deployment.
