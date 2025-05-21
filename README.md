# TCLP---IE-506-Course-Project
# TCLP: Time-Series Active Learning with Coherence-Based Label Propagation

> This repository contains the full implementation, experiments, and novel ideas explored during the **IE506 course project** at **IIT Bombay**. The work is based on the ICLR 2022 paper:
>
> **Coherence Based Label Propagation Over Time-Series for Accelerated Active Learning**  
> [Yooju Shin et al., ICLR 2022](https://openreview.net/pdf?id=gjNcH0hj0LM)
> **Dataset Link** : [mHealth](https://archive.ics.uci.edu/dataset/319/mhealth+dataset) 

---

## 📌 Project Summary

**Time-Series Labeling** is often expensive and labor-intensive due to the need for dense annotations across long sequences. This project focuses on improving Active Learning (AL) for time-series classification by leveraging **coherent temporal patterns**, known as **plateaus**, for efficient label propagation.

---

##  Core Idea from the Paper

- Instead of labeling random timestamps, the original method finds **“plateaus”** — temporally consistent regions — and propagates labels within them.
- Uses a **segmentation model (e.g., MSTCN)** to guide propagation.
- Propagation improves sample efficiency in **low-label regimes**.

---

##  Contributions

I went beyond replication and explored several **novel extensions**:

###  1. **Meta Active Learning Scheduler**
- Dynamically switches AL strategies (e.g., margin → core → badge) based on training rounds.
- Learns when to explore and when to exploit.
- Boosted F1@25 and stabilized learning curves.

###  2. **Class Coverage Aware Initialization**
- Ensures **at least 1 sample per class** in initial labels.
- Prevents under-representation of rare classes (e.g., Class 11 in mHealth).
- Improved early-stage generalization and propagation accuracy.

###  3. **Weighted AL Strategy (wt_cem)**
- Combines entropy, core-set, and margin scores with tunable weights.
- Balanced uncertainty, diversity, and representativeness.
- Shown to improve performance on mHealth dataset.

---

##  Experimental Setup

| Component        | Details                  |
|------------------|---------------------------|
| Model            | MSTCN (Multi-Stage Temporal ConvNet) |
| Datasets         | `mHealth`     |
| Label Propagation | PlatProb (Coherence-based) |
| AL Methods       | Random, Margin, Core, Badge, Utility, Weighted-CEM |
| Evaluation       | F1@10/25/50, Mean IoU, Timestamp Accuracy, ECE |

---







