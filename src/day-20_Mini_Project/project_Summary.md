# Customer Analytics Dataset - Data Summary

## Dataset Overview

This document provides a comprehensive summary of the Customer Analytics dataset used for exploratory data analysis (EDA). The dataset contains customer behavioral and demographic information across multiple dimensions.

### Basic Statistics

| Metric | Value |
|--------|-------|
| **Total Records** | 255 |
| **Total Columns** | 14 |
| **Date Generated** | 2026-02-25 |

---

## Column Description

| Column | Data Type | Description | Missing Values |
|--------|-----------|-------------|-----------------|
| **CustomerID** | Integer | Unique customer identifier (1001-1250) | 0 |
| **Age** | Integer | Customer's age in years (21-54 years) | 0 |
| **Gender** | Categorical | Customer's gender (Male/Female) | 0 |
| **City** | Categorical | City of residence (6 major Indian cities) | 0 |
| **Education** | Categorical | Highest education level (Bachelors, Masters, PhD) | 12 (4.71%) |
| **MaritalStatus** | Categorical | Marital status (Married/Single) | 0 |
| **AnnualIncome** | Float | Annual income in rupees | 12 (4.71%) |
| **SpendingScore** | Integer | Customer spending score (0-100) | 0 |
| **YearsEmployed** | Integer | Years of employment | 0 |
| **PurchaseFrequency** | Integer | Number of purchases per period | 0 |
| **OnlineVisitsPerMonth** | Integer | Monthly website/app visits | 0 |
| **ReturnedItems** | Integer | Number of returned items (0-4) | 0 |
| **PreferredDevice** | Categorical | Device used for shopping (Laptop, Desktop, Mobile, Tablet) | 0 |
| **LastPurchaseAmount** | Integer | Amount spent in last purchase (₹566-₹4,996) | 0 |

---

## Missing Data Summary

The dataset contains **12 missing values (4.71%)** distributed across two columns:

| Column | Missing Count | Percentage | Action Taken |
|--------|---------------|-----------|--------------|
| **Education** | 12 | 4.71% | Filled with mode (most frequent value) |
| **AnnualIncome** | 12 | 4.71% | Filled with mean value |

**Treatment Strategy**: Missing values were imputed using appropriate methods:
- **Education**: Filled with mode (most frequent category)
- **AnnualIncome**: Filled with mean (average value)

---

## Numerical Features Statistics

### Age Distribution
- **Count**: 255
- **Mean**: 37.73 years
- **Median**: 38 years
- **Std Dev**: 9.77 years
- **Min**: 21 years
- **Max**: 54 years
- **IQR (25%-75%)**: 29-46 years

### Annual Income Distribution
- **Count**: 243 (after imputation)
- **Mean**: ₹58,632.47
- **Median**: ₹58,783.50
- **Std Dev**: ₹24,583.45
- **Min**: ₹21,000
- **Max**: ₹102,458

### Spending Score Distribution
- **Count**: 255
- **Mean**: 46.14
- **Median**: 46
- **Std Dev**: 14.81
- **Min**: 15
- **Max**: 81

### Purchase Frequency Distribution
- **Count**: 255
- **Mean**: 12.38 purchases
- **Median**: 12 purchases
- **Std Dev**: 6.45
- **Min**: 1 purchase
- **Max**: 23 purchases

### Online Visits Per Month
- **Count**: 255
- **Mean**: 14.43 visits
- **Median**: 14 visits
- **Std Dev**: 8.13 visits
- **Min**: 1 visit
- **Max**: 29 visits

### Years Employed Distribution
- **Count**: 255
- **Mean**: 12.21 years
- **Median**: 12 years
- **Std Dev**: 9.46 years
- **Min**: 1 year
- **Max**: 33 years

### Returned Items Distribution
- **Count**: 255
- **Mean**: 1.86 items
- **Median**: 2 items
- **Std Dev**: 1.41 items
- **Min**: 0 items
- **Max**: 4 items

### Last Purchase Amount Distribution
- **Count**: 255
- **Mean**: ₹2,795.07
- **Median**: ₹2,705
- **Std Dev**: ₹1,328.77
- **Min**: ₹566
- **Max**: ₹4,996

---

## Categorical Features Distribution

### Gender Distribution
| Gender | Count | Percentage |
|--------|-------|-----------|
| Male | 132 | 51.76% |
| Female | 123 | 48.24% |
| **Total** | **255** | **100%** |

**Insight**: Nearly balanced gender distribution with slight male dominance.

### City Distribution
| City | Count | Percentage |
|------|-------|-----------|
| Chennai | 49 | 19.22% |
| Pune | 48 | 18.82% |
| Bangalore | 41 | 16.08% |
| Hyderabad | 40 | 15.69% |
| Delhi | 40 | 15.69% |
| Mumbai | 37 | 14.51% |
| **Total** | **255** | **100%** |

**Insight**: Chennai and Pune have the highest customer concentration, while Mumbai has the lowest.

### Education Distribution
| Education Level | Count | Percentage |
|-----------------|-------|-----------|
| PhD | 92 | 36.08% |
| Masters | 79 | 30.98% |
| Bachelors | 72 | 28.24% |
| Missing | 12 | 4.71% |
| **Total** | **255** | **100%** |

**Insight**: Highly educated customer base with PhD holders forming the largest segment.

### Marital Status Distribution
| Status | Count | Percentage |
|--------|-------|-----------|
| Married | 131 | 51.37% |
| Single | 124 | 48.63% |
| **Total** | **255** | **100%** |

**Insight**: Nearly balanced distribution between married and single customers.

### Preferred Device Distribution
| Device | Count | Percentage |
|--------|-------|-----------|
| Tablet | 78 | 30.59% |
| Mobile | 61 | 23.92% |
| Desktop | 60 | 23.53% |
| Laptop | 56 | 21.96% |
| **Total** | **255** | **100%** |

**Insight**: Tablet is the most preferred device for shopping, followed by Mobile and Desktop.

---

## Data Quality Assessment

### Strengths
-  No duplicate records identified
-  Minimal missing values (< 5%)
-  Good data consistency across categorical variables
-  Reasonable range for numerical values
-  Complete coverage for critical fields (CustomerID, Gender, City)

### Data Issues
-  4.71% missing values in Education and AnnualIncome
-  Some income outliers present (wide range: ₹21,000 to ₹102,458)

### Recommendations
1. Investigate reasons for missing values in Education and AnnualIncome
2. Verify outlier values in AnnualIncome (very low and very high values)
3. Validate returned items distribution (skewed towards 1-3 items)

---

## Statistical Summary

| Statistic | Value |
|-----------|-------|
| **Completeness** | 95.29% |
| **Uniqueness** | 100% (no duplicates) |
| **Outliers Potential** | Low to Moderate |
| **Data Quality Score** | 95/100 |

---

## Conclusion

The Customer Analytics dataset is a well-structured, high-quality dataset with **255 customer records across 14 attributes**. The data represents customers from major Indian cities with diverse demographics and purchasing behaviors. With minimal missing values and good data consistency, the dataset is suitable for exploratory data analysis and customer segmentation studies.
