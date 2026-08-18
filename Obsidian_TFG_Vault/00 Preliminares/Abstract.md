---
titulo: "Abstract"
numero: "-"
estado: redactada
docx_ref: "Abstract"
---

# Abstract

> [!note] Traducción fiel de [[Resumen]]
> Este texto es la versión inglesa del mismo resumen, no un texto distinto. Cualquier cambio en `Resumen.md` debe replicarse aquí.

## Title

**Machine-learning-based hybrid network intrusion detection system: cascaded anomaly and signature detection on NSL-KDD**

> [!note] Traducción del título fijado — 2026-08-18
> Versión inglesa del título definitivo cerrado por Francisco el **2026-08-18** (texto español en [[Resumen]]). No reabrir la elección: cualquier ajuste aquí es de traducción, no de contenido.

## Abstract

Network intrusion detection systems (NIDS) rely largely on signatures of known attacks, an approach that is accurate on catalogued threats but structurally blind to novel (*0-day*) attacks. This Bachelor's Thesis designs, implements and evaluates a **hybrid network intrusion detection system (H-NIDS)** that cascades an anomaly detection stage —trained solely on legitimate traffic— with a second, signature-based multiclass classification stage learned from known attacks. The aim is to retain the ability to name a known attack without giving up the detection of unknown ones, which are labelled as an actionable `unknown` category instead of being forced into an existing class.

The work is carried out on the **NSL-KDD** dataset, from which three specialised partitions are derived: D1 (normal traffic only, for the anomaly stage), D3 (known attack types only, for the signature stage) and D2 (the complete official test set, reserved for evaluation). Four anomaly detectors (Isolation Forest, One-Class SVM, Local Outlier Factor and an autoencoder) and four supervised classifiers (decision tree, random forest, k-nearest neighbours and histogram-based gradient boosting) are compared, each group under the protocol proper to its stage: a threshold at the 95th percentile of the anomaly scores on a validation partition of D1 for the first stage, and a grid search with cross-validation on `f1_macro` with within-fold class balancing for the second. As a control, a **monolithic five-class random forest** is trained, representative of the dominant pattern in the literature on this dataset. The stability of the results is assessed through a ten-seed sweep with paired comparisons.

The selected configuration, autoencoder followed by random forest, achieves on D2 a **global 0-day attack recall of 0.771 against 0.150 for the monolithic baseline**, and a five-class f1_macro of 0.641 against 0.472, with a binary accuracy of 0.860. This advantage comes at a declared cost: a false positive rate of 10.2 % and a loss of performance on known attacks with respect to the signature stage in isolation. A protocol limitation must be added: three of the system's decisions —the choice of detector, the choice of classifier and the choice of the 54-feature set over the 122-feature one— were made while observing D2, so the reported metrics are optimistic with respect to those a truly blind test set would yield. It is concluded that the hybrid architecture provides a capability for detecting the unknown that the closed classifier lacks, and that reducing the false positive rate is the priority for improvement, given its projection to low attack prevalence levels, under the illustrative scenario declared in Chapter 5.

**Keywords:** network intrusion detection; machine learning; anomaly detection; 0-day attacks; NSL-KDD; cascaded hybrid system.
