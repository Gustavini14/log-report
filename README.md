# Log Report Automation & Verification Task

This repository contains a complete, robust data analysis workspace that parses server access logs, extracts key operational performance indicators, and generates an automated JSON report. It features a custom `pytest` 
validation suite integrated with the Harbor evaluation environment to test for exact mathematical compliance.

---

## Repository Structure

*   **`task.toml`** — Schema configuration defining task parameters, required metadata, and expected artifacts.
*   **`environment/`**
    *   `Dockerfile` — Pinned, secure base environment using a verified Debian image configuration.
    *   `access.log` — Raw Apache/Nginx combined format server log dataset.
*   **`solution/`**
    *   `solve.py` — Reference Python engine that scans the logs via regular expressions to compute total hits, unique frequencies, and error distribution.
    *   `solve.sh` — Bash shell entry point wrapping the execution of the Python parser.
*   **`tests/`**
    *   `test.sh` — Verifier launcher framework that runs the validation tests and exports results using required CTRF formats.
    *   `test_outputs.py` — Strict test assertions evaluating JSON structural integrity and verifying calculation metrics.
