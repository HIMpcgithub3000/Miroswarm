# Healthdoor — Complete Architecture & Specification Document

**Product Identity**: Independent Patient-Facing Healthcare Pricing Transparency Platform  
**Target Domain**: Private & Corporate Healthcare Inpatient Billing in India  
**Audience**: Patients, Family Caregivers, Insurance Claimants, and Medical Staff  

---

## 1. Executive Summary & Purpose

Healthdoor is an open healthcare intelligence platform designed to eliminate asymmetric pricing in private and corporate hospitals across India. It gives patients real-time cost estimation, bill scrutiny for inflated and disallowed consumables, A–F hospital billing transparency ratings, and legal negotiation playbooks grounded in National Pharmaceutical Pricing Authority (NPPA), Central Government Health Scheme (CGHS), and PM-JAY package benchmarks.

---

## 2. Core Functional Pillars

### 2.1 Seven-Category Hospital Bill Breakdown

Healthdoor standardizes every hospital inpatient discharge summary and estimate into seven distinct categories:

| Category ID | Category Name | Description & Regulatory Grounding |
| :--- | :--- | :--- |
| `icuCharges` | ICU & Critical Care | Daily bed tariffs, intensive care monitoring, ventilator support, and critical nursing. |
| `pharmacy` | Inpatient Pharmacy | In-hospital pharmaceuticals, IV infusions, and chemotherapy lines (benchmarked against Jan Aushadhi / DPCO price ceilings). |
| `labsDiagnostics` | Labs & Diagnostics | Pathology, histology, blood gas analysis, MRI, CT, and USG scans. |
| `implantsDevices` | Implants & Medical Devices | Cardiac drug-eluting stents (NPPA statutory cap ₹38,260), orthopedic knee implants (NPPA cap ₹54,000), pacemakers, and mesh. |
| `consumablesDisposables` | Consumables & Disposables | Surgical gloves, PPE, sterile gowns, syringes, catheters, tubing, and swabs (frequently subjected to 400%–1,200% markups). |
| `nursingBedCare` | Room Tariff & Nursing | General ward, twin sharing, single deluxe, and suite room tariffs, including routine resident doctor rounding. |
| `doctorVisits` | Surgeon & Anaesthesia Fees | Operating surgeon fee, assistant surgeon fee, anaesthesiologist fee, and specialist consultation visits. |

---

## 3. Hidden-Charge Detection Engine

### 3.1 Standard Regulatory Benchmarks
Healthdoor cross-references every billed line item against statutory benchmarks:
- **CGHS Tier-1 Rate Cards**: Benchmark for consumables and ward procedures.
- **NPPA Ceiling Orders**: Statutory price caps on coronary stents and knee prostheses.
- **TPA Non-Payable Schedules**: General Insurance Council (GIC) standard list of 108 non-payable medical items (e.g., biohazard disposal fees, admission kit charges, unbundled sanitization surcharges).

### 3.2 Severity & Defiance Scoring Algorithm
For each billed line item $i$:
$$\text{Markup Percentage} = \frac{\text{Invoiced Cost}_i - \text{Benchmark Cost}_i}{\text{Benchmark Cost}_i} \times 100$$
$$\text{Multiplier}_i = \frac{\text{Invoiced Cost}_i}{\text{Benchmark Cost}_i}$$

Line item classification:
- **Fair ($\le 25\%$ markup)**: Severity 0
- **Moderate ($26\% - 100\%$ markup)**: Severity 1
- **Excessive ($101\% - 300\%$ markup)**: Severity 2
- **Critical Defiance ($> 300\%$ markup or TPA Disallowed Item billed)**: Severity 3

**Hospital Bill Defiance Score** ($0 - 100$):
$$\text{DefianceScore} = \min\left(100, \left(\frac{\text{Flagged Excess Amount}}{\text{Total Bill Amount}} \times 70\right) + \left(\frac{\sum \text{Severity}}{3 \times N} \times 30\right)\right)$$

---

## 4. Hospital Transparency Scoring & A–F Grading

Healthdoor evaluates hospitals on an objective transparency index:
$$T = 0.30 \times \text{ComplianceScore} + 0.25 \times \text{HiddenChargeControl} + 0.25 \times \text{NegotiationSuccessRate} + 0.20 \times (100 - \text{DefianceIndex})$$

### Grading Matrix
- **A+ ($90 - 100$)**: Exemplary billing transparency; standard rate card published; zero unbundled consumables.
- **A ($80 - 89$)**: Compliant with NPPA caps; minor consumable markup ($< 30\%$).
- **B ($70 - 79$)**: Standard commercial rates; occasional unbundled PPE/gloves; responds positively to TPA billing queries.
- **C ($60 - 69$)**: Moderate pricing inflation; frequent patient disputes on ICU and surgical consumables.
- **D ($50 - 59$)**: Substantial hidden charges; frequent refusal of cashless approvals; aggressive unbundling.
- **F ($< 50$)**: Critical defiance of statutory price ceilings; systemic inflation of non-medical charges.

---

## 5. Community Negotiation Playbooks

Healthdoor provides patient negotiation templates grounded in consumer law:
1. **Consumables & PPE Overcharging Dispute**: Direct appeal to the medical superintendent referencing the 2018 NPPA directive and Consumer Protection Act 2019 against unfair trade practices.
2. **TPA Cashless Delay & Settlement Notice**: Draft escalation citing IRDAI master circular on cashless settlement turnaround times (mandating 1-hour discharge authorization).
3. **Unbundled Ancillary Fees Waiver**: Legal objection to sanitization, documentation, and admission kit line items prohibited under GIC standard insurance guidelines.
4. **State Clinical Establishments Act Ombudsman Notice**: Formal complaint format for district pricing regulatory committees.

---

## 6. Architecture & Data Schemas

- **Frontend**: Next.js 15 (App Router), TypeScript, Tailwind CSS, Lucide icons, React Hooks.
- **State & Caching**: LocalStorage and typed in-memory stores (`store.ts`, `cache.ts`).
- **REST Endpoints**:
  - `/api/procedures`: Returns procedure pricing ranges and 7-category breakdowns.
  - `/api/hospitals`: Returns hospital profiles, accreditation (NABH, JCI, NABL), and transparency scores.
  - `/api/doctors`: Specialist credentials, consultation fees, and patient recommendation rates.
  - `/api/calculator`: Real-time procedure cost estimation based on city tier and room type.
  - `/api/community`: Peer-to-peer discussion threads, bill scrutiny reports, and negotiation success stories.
  - `/api/reviews`: Verified patient discharge bill breakdowns and transparency ratings.
