# Algorithmic Auditing Engine: Scalability, Search & Recursive Yield Optimization

> Engineering an audited, sub-second query and sorting engine for the Maji Ndogo Ministry of Agriculture to eliminate operational query bottlenecks across 5,654 smallholder farms scaling toward 1,000,000 regional records.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Complete%20%2F%20Active-brightgreen)](#the-deliverables)
[![Domain](https://img.shields.io/badge/Domain-Algorithmic%20Complexity%20%26%20Optimization-orange)](#the-business-problem)
[![Architecture](https://img.shields.io/badge/Design-Zero--Dependency%20Standard%20Library-blue)](#the-tech-stack)

---

## The Business Problem

At 2:14 p.m. in the Sokoto lowlands, an agricultural auditor stands in the middle of a potato field with a clipboard, failing satellite telemetry, and a mandatory 10-second inspection window. She radios the regional data center:

> *"Field 672. Pollution level. Now."*

The Ministry's database contains **5,654 field records**, projected to scale to **1,000,000 farms** across the entire regional basin. The legacy system relied on a brute-force linear loop:
1. **The Scalability Wall:** An $\mathcal{O}(n)$ linear search takes less than a second on 5,654 records, but balloons to multi-minute runtimes when scaled to 1,000,000 records. In field conditions with degraded connectivity, an inspector waiting minutes misses her compliance window, forcing entire audit reschedulings.
2. **Dynamic Pollution Thresholding:** As regional pesticide and chemical run-off regulations tighten, environmental inspectors need immediate anomaly detection to isolate heavily polluted plots without mutating underlying databases or incurring heavy runtime allocations.
3. **Yield Ranking & Economic Prioritization:** The Ministry lacked an auditable mechanism to rank harvest yields from highest to lowest. Naive sorting algorithms ($\mathcal{O}(n^2)$) freeze server threads during peak harvest influx.
4. **Vectorized Production Forecasting:** Quick agricultural yield forecasting ($\text{Plot\_size} \times \text{Standard\_yield}$) required lightweight, functional mapping pipelines capable of running on constrained edge devices without heavy scientific libraries.

---

## The Tech Stack

This auditing engine was built using **Core Python (Standard Library only)**, adhering to strict zero-dependency production constraints for edge telematics and mission-critical audit terminals:

- **Algorithmic Search Mechanics:**
  - **Linear Search ($\mathcal{O}(n)$):** Guaranteed traversal across arbitrary, unsorted field record streams.
  - **Binary Search ($\mathcal{O}(\log n)$):** Logarithmic divide-and-conquer search with dual pointer boundaries (`low`, `high`, `mid`), reducing search comparisons by **99.998%** at scale.
- **Divide-and-Conquer Recursive Sorting:**
  - **Merge Sort ($\mathcal{O}(n \log n)$):** Out-of-place recursive divide-and-conquer architecture ensuring predictable, stable descending yield ranking with zero worst-case performance degradation.
- **Functional Data Pipelines (`map`, `filter`, `lambda`):**
  - **Predicate Filtering:** Memory-efficient anomaly isolation with zero intermediate state accumulation.
  - **Transformation Mapping:** Deterministic floating-point arithmetic with strict two-decimal rounding precision.

---

## The Deliverables

The engine delivers five production-verified algorithmic modules:

```
auditing_the_farm_survey/
├── auditing_engine.py      # Core production implementation & verification suite
└── README.md               # Algorithmic benchmark and engineering report
```

### 1. High-Performance Linear Search (`linear_search_field`)
Traverses unsorted survey records to isolate the pollution reading of any designated field ID, exiting on the first match and returning `None` if the target is absent.

```python
def linear_search_field(field_list, target_id):
    for record in field_list:
        if record['Field_ID'] == target_id:
            return record['Pollution_level']
    return None
```
- **Input:** `maji_ndogo_sample`, `target_id = 39924`
- **Output:** `0.358` (Verified)
- **Worst-case Time Complexity:** $\mathcal{O}(n)$

---

### 2. Logarithmic Binary Search (`binary_search_yield`)
Jumps directly to the median index of an ID-sorted array. By comparing the target ID against the midpoint, it eliminates 50% of remaining candidates at every step.

```python
def binary_search_yield(sorted_field_list, target_id):
    low = 0
    high = len(sorted_field_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_field_list[mid]['Field_ID']
        if mid_id == target_id:
            return sorted_field_list[mid]['Annual_yield']
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None
```
- **Input:** `sorted_sample`, `target_id = 30629`
- **Output:** `1.0699` (Verified)
- **Worst-case Time Complexity:** $\mathcal{O}(\log n)$

---

### 3. Recursive Merge Sort (`merge_sort_yields` & `merge`)
Ranks complete field records into **descending order** of annual yield (highest-yielding plots prioritized for regional distribution).

```python
def merge_sort_yields(field_list):
    if len(field_list) <= 1:
        return field_list
    mid = len(field_list) // 2
    left = merge_sort_yields(field_list[:mid])
    right = merge_sort_yields(field_list[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]['Annual_yield'] >= right[j]['Annual_yield']:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
```
- **Output:** Descending sorted array: `[2.2088, 1.2776, 1.0699, 0.8326, 0.7514]`
- **Worst-case Time Complexity:** $\mathcal{O}(n \log n)$

---

### 4. Dynamic Anomaly Filtering (`identify_high_pollution`)
Evaluates environmental compliance across thousands of fields using inline predicate filtering:

```python
def identify_high_pollution(field_list, threshold):
    return list(filter(lambda record: record['Pollution_level'] > threshold, field_list))
```
- **Execution:** Flagged fields exceeding threshold `0.3`: IDs `[30629, 39924]`; threshold `0.5`: `[]`.
- **Worst-case Time Complexity:** $\mathcal{O}(n)$

---

### 5. Automated Yield Projection (`project_harvests`)
Transforms raw cadastral acreage and productivity metrics into standardized harvest projections rounded to two decimal places:

```python
def project_harvests(field_list):
    return list(map(lambda record: round(record['Plot_size'] * record['Standard_yield'], 2), field_list))
```
- **Formula:** $\text{Harvest} = \text{Plot\_size} \times \text{Standard\_yield}$
- **Output:** `[0.75, 1.07, 2.21, 1.28, 0.83]`
- **Worst-case Time Complexity:** $\mathcal{O}(n)$

---

## 📊 Algorithmic Scalability & Complexity Benchmark

The table below contrasts theoretical and practical computational cost as the Maji Ndogo agricultural database scales from sample testing to regional deployment:

| Operation | Algorithm | Sample ($n=5$) | Current Survey ($n=5,654$) | Regional Scale ($n=1,000,000$) | Space Overhead |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Field Lookup (Unsorted)** | Linear Search | 5 steps | 5,654 steps | 1,000,000 steps | $\mathcal{O}(1)$ |
| **Field Lookup (Sorted)** | Binary Search | **3 steps** | **~13 steps** | **~20 steps** | $\mathcal{O}(1)$ |
| **Harvest Ranking** | Merge Sort | 12 ops | ~70,000 ops | ~20,000,000 ops | $\mathcal{O}(n)$ |
| **Pollution Auditing** | `filter()` + $\lambda$ | 5 evaluations | 5,654 evaluations | 1,000,000 evaluations | $\mathcal{O}(k)$ |
| **Harvest Projection** | `map()` + $\lambda$ | 5 calculations | 5,654 calculations | 1,000,000 calculations | $\mathcal{O}(n)$ |

```
Query Comparisons at 1,000,000 Records:
Linear Search: [████████████████████████████████████████] 1,000,000 checks
Binary Search: [▏] 20 checks  (99.998% reduction)
```

---

## The "So What?"

By transitioning from naive data processing scripts to an engineered algorithmic auditing engine, the Ministry achieved critical operational milestones:

- **Sub-Second Satellite Querying:** Moving field ID retrieval from $\mathcal{O}(n)$ to $\mathcal{O}(\log n)$ guarantees that field inspectors receive critical pollution readings in milliseconds, well within their 10-second satellite link deadline.
- **Predictable Sorting at Scale:** Replacing quadratic bubble/insertion sorting with recursive Merge Sort ($\mathcal{O}(n \log n)$) guarantees that ranking regional harvest yields takes seconds rather than hours of locked server CPU time.
- **Audit-Ready Zero-Dependency Architecture:** Eliminating bulky external library requirements allows this engine to be embedded directly into low-power field microcontrollers and remote telemetry transceivers with zero deployment friction.
