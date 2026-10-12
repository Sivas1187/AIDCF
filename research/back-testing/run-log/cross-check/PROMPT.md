# Prompt for the AI cross-check of exclusions (KAI or DeepSeek)

Paste the whole prompt below into a **new chat**, then paste the contents of one batch file (`batch-1.csv` to `batch-4.csv`) where it says. Use one new chat per batch. The model must be able to open web pages: ChatGPT with browsing, or DeepSeek with search turned on. Save each answer as `response-<model>-batch-<n>.csv` in this folder (for example `response-kai-batch-1.csv`).

---

```text
You are checking exclusion decisions for a research study that back-tests a data-centre assurance framework against real, publicly reported infrastructure incidents. Another screener has EXCLUDED each incident below. Your job is to independently decide whether each exclusion is correct. Disagreeing is expected and useful; do not defer to the screener.

RULES
1. Open the primary_source_url for each row and read it (and other_source_urls if needed). Judge ONLY from what those pages say. Do not use memory or other websites. If you cannot open the page, answer CANNOT_ACCESS.
2. Decide the detail level of the source:
   - HIGH: timeline with timestamps or ordered steps; at least two causal or contributing factors; affected infrastructure layer and scope stated; at least one pre-event condition (configuration, design, maintenance state, capacity or procedure) stated explicitly.
   - MEDIUM: ordered description of events; at least one causal factor expressed as a pre-event condition (something that existed before the incident and contributed to it); affected layer stated.
   - LOW: outcome and broad cause only (for example "a power issue"), no pre-event condition.
3. The exclusion codes being checked:
   - EX-02 = detail level LOW (the source is too thin).
   - EX-04 = out of scope: an application or software defect with no infrastructure, control-plane or capacity condition; a data breach with no effect on infrastructure availability, integrity or control; or a consumer-device or end-user network issue. IN scope are failures of data-centre facility infrastructure (power, cooling, fire, physical), compute, storage, network fabric, cloud infrastructure services, and the control planes and automation that operate them, including capacity limits.
4. For each row, give:
   - verdict: AGREE (the exclusion is correct), DISAGREE (the incident should be ELIGIBLE), DIFFERENT_CODE (it should be excluded, but for a different reason), or CANNOT_ACCESS.
   - your_detail_level: HIGH, MEDIUM or LOW.
   - your_code: the exclusion code you would use (EX-02 or EX-04), or ELIGIBLE.
   - evidence: max 30 words, citing what the page does or does not say (for example the pre-event condition it states).

OUTPUT
Reply with ONLY a CSV block, no other text, with exactly this header and one line per input row, in the same order:
incident_id,verdict,your_detail_level,your_code,evidence
Put the evidence field in double quotes.

ROWS TO CHECK
<paste the contents of the batch CSV file here>
```

---

## After all four batches

Send the response files to Claude, or attach them in the AIDCF thread. Claude lists only the rows where the model disagrees with the screener. You then decide those rows yourself, and the decisions are recorded in the register's `exclusion_checked_by` column and in the run log as "AI cross-check (model, date), human-confirmed".
