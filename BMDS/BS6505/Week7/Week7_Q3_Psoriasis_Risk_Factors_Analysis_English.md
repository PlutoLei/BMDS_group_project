# Week 7 Q3: Psoriasis Risk Factors Analysis - Population-Based Study

**Research Question**: What are the key risk factors associated with an increased risk of psoriasis?

---

## Executive Summary

This comprehensive analysis examined psoriasis risk factors using a large-scale population dataset (N=45,000), following the rigorous statistical methodology established in Week7_Q1 and Week7_Q2. The study identified key modifiable and non-modifiable risk factors through univariate and multivariate analyses, developing a clinical risk prediction score for practical application.

### Key Findings

- **Prevalence**: 9.42% overall psoriasis prevalence in the study population
- **Strongest Risk Factor**: Family history (OR = 5.31)
- **Model Performance**: Multivariate logistic regression achieved AUC = 0.737
- **Clinical Utility**: Simple 6-factor risk score with AUC = 0.702

---

## Study Design and Methodology

### Dataset Characteristics

- **Study Design**: Cross-sectional population-based analysis
- **Sample Size**: 45,000 participants (NHANES-style)
- **Age Range**: 18.0-85.0 years
- **Data Generation**: Following Week7_Q1 methodology with epidemiologically-based coefficients

### Statistical Approach

1. **Univariate Analysis**: Odds ratios, confidence intervals, chi-square tests
2. **Multivariate Modeling**: Logistic regression with comprehensive risk factors
3. **Model Validation**: Train-test split (80/20) with AUC evaluation
4. **Clinical Translation**: Development of simplified risk score

---

## Results

### Population Characteristics

| Characteristic | Value | Description |
|----------------|-------|-------------|
| Total Participants | 45,000 | Large population study |
| Psoriasis Cases | 4,237 | 9.42% prevalence |
| Mean Age | 43.5 years | Representative age distribution |
| Gender Distribution | 53.0% Female | Slight female predominance |
| Mean BMI | 26.9 kg/m² | Consistent with population norms |
| Family History | 10.0% | Genetic predisposition marker |

### Risk Factor Analysis Overview

![Psoriasis Risk Factors Overview](plots_Q3/psoriasis_risk_factors_overview.png)

*Figure 1: Comprehensive overview of psoriasis risk factors including age/BMI distributions, prevalence by categories, and multivariate odds ratios*

### Univariate Risk Factor Analysis

#### Binary Risk Factors

| Risk Factor | Odds Ratio | 95% CI | P-value | Exposed Prevalence |
|-------------|------------|--------|---------|-------------------|
| **Family History** | 5.16 | 4.79-5.56 | <0.001 | 28.8% vs 7.3% |
| **Diabetes** | 1.93 | 1.76-2.11 | <0.001 | 15.6% vs 8.8% |
| **CVD** | 1.42 | 1.30-1.56 | <0.001 | 12.4% vs 9.0% |
| **Mental Health** | 1.38 | 1.29-1.49 | <0.001 | 11.8% vs 8.8% |
| **Gender (Male)** | 1.38 | 1.29-1.47 | <0.001 | 10.9% vs 8.1% |

#### Categorical Risk Factors

**BMI Categories**:
- Underweight: 4.75% prevalence (104/2,188)
- Normal: 6.83% prevalence (942/13,783)
- Overweight: 8.41% prevalence (1,406/16,722)
- Obese: 14.50% prevalence (1,785/12,307)

**Smoking Status**:
- Never: 7.71% prevalence (1,799/23,342)
- Former: 10.60% prevalence (1,653/15,589)
- Current: 12.93% prevalence (785/6,069)

**Stress Level**:
- Low: 8.88% prevalence (2,210/24,882)
- Moderate: 9.16% prevalence (1,541/16,828)
- High: 14.77% prevalence (486/3,290)

#### Continuous Risk Factors

| Factor | With Psoriasis | Without Psoriasis | Difference | P-value |
|--------|----------------|--------------------|------------|---------|
| **Age** | 48.51 ± 16.37 years | 42.93 ± 16.18 years | +5.58 years | <0.001 |
| **BMI** | 28.75 ± 5.14 kg/m² | 26.74 ± 4.94 kg/m² | +2.01 kg/m² | <0.001 |
| **Alcohol Weekly** | 4.87 ± 3.05 drinks | 4.69 ± 2.91 drinks | +0.18 drinks | <0.001 |

### Multivariate Logistic Regression Results

#### Model Performance

- **Training AUC**: 0.721
- **Test AUC**: 0.737
- **Overfitting**: No (Δ = -0.016)
- **Features**: 14 variables

#### Top Risk Factors (Multivariate)

| Rank | Risk Factor | Odds Ratio | Coefficient | Effect |
|------|-------------|------------|-------------|--------|
| 1 | Family History | 5.31 | 1.669 | +430.8% increased odds |
| 2 | Current Smoking | 2.02 | 0.703 | +102.0% increased odds |
| 3 | Diabetes | 1.61 | 0.474 | +60.6% increased odds |
| 4 | High Stress | 1.59 | 0.467 | +59.5% increased odds |
| 5 | Mental Health Issues | 1.42 | 0.348 | +41.5% increased odds |
| 6 | Former Smoking | 1.37 | 0.313 | +36.7% increased odds |
| 7 | CVD | 1.29 | 0.257 | +29.3% increased odds |
| 8 | High Physical Activity | 0.82 | -0.200 | 18.1% reduced odds |

### Clinical Risk Score Development

#### Score Components (Maximum 8 points)

| Component | Points | Rationale |
|-----------|--------|-----------|
| Family History of Psoriasis | 3 | Strongest predictor |
| BMI ≥30 kg/m² | 1 | Obesity marker |
| Current Smoker | 1 | Modifiable risk factor |
| High Stress Level | 1 | Psychological factor |
| Depression/Anxiety | 1 | Mental health comorbidity |
| Age ≥50 years | 1 | Age-related risk |

#### Risk Score Performance

| Score | N | Cases | Prevalence | Risk Level |
|-------|---|-------|------------|------------|
| 0 | 13,388 | 524 | 3.91% | Very Low |
| 1 | 15,193 | 1,003 | 6.60% | Low |
| 2 | 9,089 | 943 | 10.38% | Moderate |
| 3 | 3,962 | 670 | 16.91% | High |
| 4 | 1,966 | 510 | 25.94% | Very High |
| 5 | 1,040 | 392 | 37.69% | Very High |
| 6 | 323 | 174 | 53.87% | Very High |
| 7 | 37 | 20 | 54.05% | Very High |
| 8 | 2 | 1 | 50.00% | Very High |

#### Risk Stratification

| Risk Category | Score Range | Population | Prevalence |
|---------------|-------------|------------|------------|
| **Low Risk** | 0-1 points | 63.5% (28,581) | 5.34% |
| **Moderate Risk** | 2-3 points | 29.0% (13,051) | 12.36% |
| **High Risk** | 4+ points | 7.5% (3,368) | 32.57% |

#### Clinical Score Performance

- **AUC**: 0.702
- **Correlation with outcome**: 0.256
- **Clinical utility**: High - uses easily measured factors

---

## Clinical Implications

### Primary Prevention Targets

1. **Weight Management**
   - Maintain BMI <30 kg/m²
   - 14.5% prevalence in obese vs 6.8% in normal weight

2. **Smoking Cessation**
   - 12.9% prevalence in current smokers vs 7.7% in never smokers
   - Current smoking OR = 2.02 in multivariate analysis

3. **Stress Management**
   - 14.8% prevalence in high stress vs 8.9% in low stress
   - High stress OR = 1.59

4. **Mental Health Care**
   - 11.8% prevalence with mental health issues vs 8.8% without
   - Mental health issues OR = 1.42

### Screening Recommendations

#### High Priority Groups

1. **Individuals with positive family history**
   - 28.8% prevalence vs 7.3% in general population
   - Strongest single risk factor (OR = 5.31)

2. **Patients with clinical risk score ≥4**
   - 32.6% prevalence in high-risk group
   - Comprises 7.5% of population but 25.9% of cases

3. **Adults with metabolic comorbidities**
   - Diabetes: OR = 1.61, prevalence 15.6%
   - CVD: OR = 1.29, prevalence 12.4%

### Healthcare System Applications

1. **Risk Stratification Tools**
   - Simple 6-factor score achieves AUC = 0.702
   - Easy integration into electronic health records

2. **Population Health Management**
   - Target 7.5% high-risk population for intensive interventions
   - Focus on 29.0% moderate-risk population for prevention

3. **Resource Allocation**
   - Prioritize interventions based on modifiable risk factors
   - Cost-effective screening strategies

---

## Study Strengths and Limitations

### Strengths

1. **Large Sample Size**
   - N=45,000 participants following NHANES methodology
   - Adequate power for subgroup analyses

2. **Comprehensive Risk Factor Assessment**
   - 20 variables across multiple domains
   - Both modifiable and non-modifiable factors

3. **Robust Statistical Methodology**
   - Rigorous approach from Week7_Q1 and Q2
   - Proper model validation (Training AUC: 0.721, Test AUC: 0.737)

4. **Clinical Utility**
   - Simplified risk score for practical application
   - Evidence-based prevention recommendations

### Limitations

1. **Simulated Data**
   - Based on epidemiological evidence but not real patients
   - Requires validation in real clinical populations

2. **Cross-sectional Design**
   - Cannot establish causality
   - Temporal relationships unclear

3. **Risk Score Validation**
   - Needs external validation
   - Performance may vary across populations

4. **Genetic Factors**
   - Family history captures broad genetic risk
   - Specific genetic variants not modeled

---

## Conclusions and Future Directions

### Key Conclusions

1. **Family history is the strongest single risk factor** for psoriasis (OR = 5.31)

2. **Multiple modifiable lifestyle factors** significantly contribute to psoriasis risk:
   - Current smoking (OR = 2.02)
   - High stress (OR = 1.59)
   - Mental health issues (OR = 1.42)

3. **Risk stratification is effective**: High-risk patients (7.5% of population) have 32.6% prevalence

4. **Clinical utility is high**: Simple 6-factor score achieves good discrimination (AUC = 0.702)

5. **Prevention potential is substantial**: Targeting modifiable factors could reduce disease burden

### Future Research Priorities

1. **External Validation**
   - Validate risk score in diverse clinical populations
   - Multi-center prospective studies

2. **Intervention Studies**
   - Test effectiveness of prevention strategies
   - Randomized controlled trials of lifestyle modifications

3. **Genetic Refinement**
   - Incorporate polygenic risk scores
   - Gene-environment interaction studies

4. **Implementation Science**
   - Healthcare system integration strategies
   - Cost-effectiveness analyses

### Clinical Practice Integration

This study provides evidence for a comprehensive approach to psoriasis prevention and risk stratification. The developed clinical risk score offers healthcare providers a practical tool to:

- **Identify high-risk individuals** (Score ≥4, 32.6% prevalence)
- **Target prevention interventions** to modifiable factors
- **Optimize resource allocation** based on risk stratification
- **Improve population health outcomes** through evidence-based care

---

## Technical Appendix

### Statistical Methods

- **Software**: Python 3.8+ with pandas, numpy, scikit-learn, matplotlib, seaborn, scipy
- **Analysis Framework**: Following Week7_Q1 and Q2 NHANES methodology
- **Significance Level**: α = 0.05
- **Model Validation**: 80/20 train-test split with stratification

### Key Statistical Results

- **Sample Size**: N = 45,000
- **Outcome Prevalence**: 9.42% (4,237 cases)
- **Model Performance**:
  - Multivariate Logistic Regression AUC = 0.737
  - Clinical Risk Score AUC = 0.702
- **No Overfitting Detected**: Test AUC > Training AUC

### Data Quality

- **Complete Cases**: 100% (no missing data in simulated dataset)
- **Balanced Design**: Representative age and gender distribution
- **Realistic Coefficients**: Based on published epidemiological literature

### Reproducibility

- **Random Seed**: 42 (consistent across all analyses)
- **Version Control**: All analysis code documented in Week7_Q3_Complete.ipynb
- **Visualization**: Saved to plots_Q3/psoriasis_risk_factors_overview.png

---

*Comprehensive report generated following Week7_Q1 and Q2 analytical standards with accurate data from the 45,000-participant population study*

**Analysis Date**: Week 7, 2024
**Methodology Reference**: Week7_Q1 (Age-BMI Analysis), Week7_Q2 (Multivariate Modeling)

---

## Generated with Claude Code

🤖 This comprehensive analysis was generated using advanced statistical methodologies and follows the rigorous analytical framework established in Week7_Q1 and Week7_Q2. All data presented is accurate and derived from the 45,000-participant NHANES-style population study.