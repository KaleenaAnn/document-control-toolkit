import csv
from collections import Counter
from pathlib import Path

# Engineering Document Control Validation
# Uses fictional manufacturing records.

file_path = Path(__file__).with_name("document-register.csv")

with file_path.open("r", encoding="utf-8-sig", newline="") as file:
    documents = list(csv.DictReader(file))

print("ENGINEERING DOCUMENT CONTROL REPORT")
print("=" * 40)
print(f"Total documents: {len(documents)}")

status_counts = Counter(
    doc["Status"].strip() for doc in documents
)

print("\nDOCUMENT STATUS SUMMARY")
for status, count in sorted(status_counts.items()):
    print(f"{status}: {count}")

print("\nDATA VALIDATION")

issues = []
seen_ids = set()

for doc in documents:
    doc_id = doc["Document_ID"].strip()
    status = doc["Status"].strip()
    effective_date = doc["Effective_Date"].strip()

    if not doc_id:
        issues.append("Missing document ID")
    elif doc_id in seen_ids:
        issues.append(f"{doc_id}: Duplicate document ID")

    seen_ids.add(doc_id)

    if status == "Released" and not effective_date:
        issues.append(
            f"{doc_id}: Released without an effective date"
        )

if issues:
    for issue in issues:
        print("WARNING:", issue)
else:
    print("All basic validation checks passed.")

print("\nValidation complete.")
