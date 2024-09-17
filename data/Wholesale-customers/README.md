# Wholesale Customers

The data set refers to clients of a wholesale distributor. It includes the annual spending in monetary units (m.u.) on diverse product categories.

## Dataset Characteristics

- **Type:** Multivariate
- **Subject Area:** Business
- **Associated Tasks:** Classification, Clustering
- **Feature Type:** Integer
- **# Instances:** 440
- **# Features:** 7

### Dataset Information

- **Has Missing Values?** No

## Variables Table

| Variable Name       | Role    | Type         | Description | Units | Missing Values |
|---------------------|---------|--------------|-------------|-------|----------------|
| Channel             | Feature | Categorical  |             |       | no             |
| Region              | Target  | Categorical  |             |       | no             |
| Fresh               | Feature | Integer      |             |       | no             |
| Milk                | Feature | Integer      |             |       | no             |
| Grocery             | Feature | Integer      |             |       | no             |
| Frozen              | Feature | Integer      |             |       | no             |
| Detergents_Paper    | Feature | Integer      |             |       | no             |
| Delicatessen        | Feature | Integer      |             |       | no             |

## Additional Variable Information

1. **FRESH:** Annual spending (m.u.) on fresh products (Continuous)
2. **MILK:** Annual spending (m.u.) on milk products (Continuous)
3. **GROCERY:** Annual spending (m.u.) on grocery products (Continuous)
4. **FROZEN:** Annual spending (m.u.) on frozen products (Continuous)
5. **DETERGENTS_PAPER:** Annual spending (m.u.) on detergents and paper products (Continuous)
6. **DELICATESSEN:** Annual spending (m.u.) on delicatessen products (Continuous)
7. **CHANNEL:** Customers’ Channel - Horeca (Hotel/Restaurant/Café) or Retail channel (Nominal)
8. **REGION:** Customers’ Region – Lisbon, Oporto, or Other (Nominal)

## Descriptive Statistics

| Feature            | Minimum | Maximum | Mean    | Std. Deviation |
|--------------------|---------|---------|---------|----------------|
| FRESH              | 3       | 112151  | 12000.30 | 12647.329      |
| MILK               | 55      | 73498   | 5796.27  | 7380.377       |
| GROCERY            | 3       | 92780   | 7951.28  | 9503.163       |
| FROZEN             | 25      | 60869   | 3071.93  | 4854.673       |
| DETERGENTS_PAPER   | 3       | 40827   | 2881.49  | 4767.854       |
| DELICATESSEN       | 3       | 47943   | 1524.87  | 2820.106       |

## Region Frequency

| Region      | Frequency |
|-------------|-----------|
| Lisbon      | 77        |
| Oporto      | 47        |
| Other Region| 316       |
| **Total**   | 440       |

## Channel Frequency

| Channel | Frequency |
|---------|-----------|
| Horeca  | 298       |
| Retail  | 142       |
| **Total** | 440     |

