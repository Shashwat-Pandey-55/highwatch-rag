# Sample Queries & Actual Outputs

This file contains real test cases run against the Highwatch RAG System after syncing Google Drive documents.

---

## Test Case 1

**Query:** What is our refund policy?

**Actual API Response:**

**Answer:**

Highwatch AI offers a transparent and customer-friendly refund policy.

- **Full Refund:** Customers are eligible for a full refund within 30 days of the subscription start date, provided no more than 10 API calls have been made during the period.
- **Partial Refund:** If usage exceeds 10 API calls but the request is made within 30 days, a prorated refund will be issued based on unused days.
- **No Refund:** Refunds will not be issued after 30 days or for annual plans that have been active for more than 30 days.

To request a refund, customers should submit a refund request via the support portal at support.highwatch.ai with their registered email and order ID. Approved refunds are processed within 5–7 business days to the original payment method. Custom enterprise contracts may have separate refund clauses as defined in the signed agreement.

**Sources:** `Highwatch_Company_Knowledge_Base.md.pdf`

---

## Test Case 2

**Query:** What are the company's compliance requirements?

**Actual API Response:**

**Answer:**

The company's compliance requirements include:

**2.1 Data Privacy:**
- Handling customer data in accordance with GDPR and CCPA
- Not selling or sharing personal data with third parties without explicit consent
- Retaining customer data for a maximum of 90 days after account termination

**2.2 Security Standards:**
- Maintaining SOC 2 Type II certification, audited annually
- Encrypting data in transit using TLS 1.2 or higher
- Encrypting data at rest using AES-256

**2.3 Employee Compliance:**
- Completing mandatory security awareness training within the first 2 weeks of joining and annually thereafter
- Following the Principle of Least Privilege (PoLP) for access to production systems
- Conducting quarterly access control audits
- Reporting suspected data breaches to the security team within 1 hour of discovery

**2.4 Regulatory Reporting:**
- Generating compliance reports quarterly
- Communicating regulatory changes company-wide within 5 business days of identification

**Sources:** `Highwatch_Company_Knowledge_Base.md.pdf`

---

## Test Case 3

**Query:** Summarize the onboarding process

**Actual API Response:**

**Answer:**

The onboarding process at Highwatch AI can be summarized as follows:

**Day 1:**
- Attend company orientation session
- Complete HR documentation (employment contract, tax forms, emergency contact information)
- Receive company email, Slack invite, and access to internal wiki

**Week 1:**
- IT provisioning (laptop setup, VPN access, GitHub access, AWS IAM account)
- Meet assigned buddy/mentor
- Complete mandatory Information Security Training module
- Attend team standups and introduce yourself

**Week 2:**
- Complete GDPR & Data Privacy Training module
- Shadow team members on ongoing projects
- Set up local development environment using Engineering Setup Guide

**Days 15–30:**
- Begin contributing to a starter task or onboarding project assigned by manager
- Complete Company Values & Culture module
- Schedule 30-day check-in with manager to discuss progress and goals
- Ensure all tool access and permissions are fully provisioned

**Sources:** `Highwatch_Company_Knowledge_Base.md.pdf`

---

## Test Case 4 — Cross-Document Retrieval

**Query:** What is the research about suspended particulate matter?

**Actual API Response:**

**Answer:**

The FT-IR spectra of bioflocculant indicated the presence of compounds with hydroxyl (-OH), carboxyl (-COOH), amide (-CONH2), and aliphatic alcohol (-C-OH) groups. The existence of such groups can increase hydrophobicity and flocculant activity.

Key wavenumber findings:

| Wavenumber | Bond Type | Range | Description |
|---|---|---|---|
| 3421.35 | O–H stretching | 3200–3600 | Hydrogen-bonded hydroxyl groups |
| 2924.65 | C–H stretching | 2800–3000 | Asymmetric C–H stretching of methyl and methylene groups |
| 1614.15 | C=O stretching | 1550–1750 | Amide I band |
| 1401.15 | O–C stretching | 1200–1400 | Stretching of C–O from carboxylic acids |
| 1086.45 | C–O–C stretching | 1000–1200 | Anomeric region, stretching of C–O from aliphatic alcohols |
| 625.85 | C–C stretching | 500–800 | Stretching of C–C |

**Sources:** `R2.pdf`
