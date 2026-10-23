# Design-And-Analysis-of-Algorithm
MINI PROJECT OF Design-And-Analysis-of-Algorithm (SPELL CHECKER SUGGEST)

# Spell Checker Suggestion Tracker 🔍📊

A robust algorithmic utility built to demonstrate the **Dynamic Programming (DP) Paradigm** alongside **String Matching Metrics** using the **Levenshtein Edit Distance**. This project features an embedded analytics suite built to profile computational costs for university **Design and Analysis of Algorithms (DAA)** labs.

---

## ⚡ Quick Start: Download & Run

Follow these terminal commands to execute the project pipeline inside VS Code:

### 1. Install Plotting Dependencies
Ensure your isolated virtual environment engine contains the required charting library:
```powershell
& "c:\All projects\adit\.venv\Scripts\python.exe" -m pip install matplotlib
```

### 2. Execute Code Matrix
Run the comprehensive tracking execution routine:
```powershell
& "c:\All projects\adit\.venv\Scripts\python.exe" "c:/All projects/adit/py/mauli/spell_checker.py"
```

---

## 🧠 Algorithmic Paradigm: Dynamic Programming (DP)

Unlike simple searching, generating context suggestions uses overlapping subproblem optimization:
*   **Optimal Substructure:** The minimum cost to modify an entire word string $W_1[1..m]$ into another word $W_2[1..n]$ depends directly on the minimal transformation states of their local prefixes.
*   **Tabulation Memory Framework:** Instead of tracking paths recursively (which triggers an exponential $\mathcal{O}(3^N)$ runtime blowout), a 2D grid matrix table locks computed metrics down to an analytical state flow pattern. 

---

## 📊 Complexity Breakdown

*   **Edit Distance Time Complexity:** $\mathcal{O}(M \times N)$ per entry check, where $M$ and $N$ represent string component lengths.
*   **Total Dictionary Scan:** $\mathcal{O}(D \times M \times N)$ where $D$ represents the master vocabulary density. This matches a strictly **linear growth scaling path ($\mathcal{O}(D)$)** relative to total database scale boundaries.
*   **Space Complexity:** $\mathcal{O}(M \times N)$ matrix grid tracking allocations.

---
## OUTPUT OF CODE
*   **SUGESSTED DATA OUTPUT:** 

<img width="1074" height="393" alt="image" src="https://github.com/user-attachments/assets/ae8e5b9c-c6f8-4567-9fbd-9229dc000bdb" />


## 📈 Empirical Performance Curve

The chart below visualizes the empirical runtime metrics recorded by the embedded tracker framework across varying dictionary capacities:

![Empirical Scaling Curve](spell_checker_curve.png)

---
