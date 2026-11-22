# L6_L7_43 — Warranty Claims

## Lab 7: Fuzz Testing for Input Validation Bugs

### About
This lab explores property-based fuzz testing using **Hypothesis** to discover input validation bugs, crashes, and unhandled edge cases in the warranty claims processor, followed by defensive code hardening to ensure high resilience.

### Student Details
- **Name:** Komal S Sajja
- **SRN:** PES1UG24CS231
- **Course:** Software Engineering (UE21CS341AA2 / SE)
- **Topic:** 43 — Warranty Claims

---

### Files
| File | Description |
|------|-------------|
| `warranty_claims.py` | Hardened application module containing `parse_claim`, `age_average`, and `payable_charge` |
| `processor.py` | Alias/exact duplicate of `warranty_claims.py` for standard naming compatibility |
| `test_warranty_claims.py` | Hypothesis fuzz testing suite asserting non-crashing behavior on arbitrary text and `None` |
| `test_processor.py` | Hypothesis fuzz testing suite testing `processor.py` |
| `Lab07_Fuzzing_Report.pdf` | Comprehensive 4-page lab report document with terminal screenshots and bug analysis |
| `screenshots/` | High-resolution terminal output screenshots documenting Steps 2, 4, 5, and 6 |

---

### How to Run

1. **Install Dependencies:**
   ```bash
   pip install hypothesis pytest
   ```

2. **Run Application:**
   ```bash
   python warranty_claims.py
   # or
   python processor.py
   ```

3. **Run Fuzz Tests with Pytest:**
   ```bash
   pytest test_warranty_claims.py -v
   # or
   pytest test_processor.py -v
   ```

---

### Fuzz Testing Results
- **Initial Buggy Code:** Discovered 3 distinct failure groups across all functions on empty strings `""`, `None` objects, and bare delimiters (`":"`, `"|"`).
- **Hardened Code:** 100% test pass rate across hundreds of generated pseudo-random Unicode inputs, boundary numbers, and malformed inputs with 0 crashes.
