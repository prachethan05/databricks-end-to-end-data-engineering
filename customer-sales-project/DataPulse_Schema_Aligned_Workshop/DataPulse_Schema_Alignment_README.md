# DataPulse schema-aligned Bronze + Silver workshop

## What changed
- Corrected Silver column names and candidate keys to match the saved DataPulse reference PDFs for Google Ads, Amazon Ads, Magento, and SAP.
- Added typed casts based on the suggested column types in those references.
- Bronze keeps CSV values as strings and reads JSON primitive values as strings where supported, protecting identifiers from numeric inference.
- The Silver notebook covers all 25 dataset names.

## Source references found
The saved Library contains detailed reference PDFs for 20 datasets:
- Google Ads: 5
- Amazon Ads: 5
- Magento: 5
- SAP logical extracts: 5

Individual column-dictionary PDFs for the five Meta Ads datasets were not found in the saved reference set. Meta definitions in the notebook are explicitly provisional and should be replaced/verified using the Meta source export schema.

## Important
These PDFs define illustrative DataPulse learning schemas, not verified private company schemas or guaranteed vendor API payloads. Confirm exact landed columns, nested JSON shapes, key/grain, and type conversions before production.

The manifest schema is not hardcoded because the actual DataPulse manifest implementation has not been verified in this workshop. Connect the real manifest lookup/status update logic. Append is not retry-safe; implement MERGE or controlled slice replacement for incremental processing.
