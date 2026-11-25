import re


def validate_dataset_name(name):
    """Clean and validate a dataset name. Returns the cleaned name."""
    cleaned = (name or "").strip().lower()

    if not cleaned:
        raise ValueError("dataset_name cannot be empty.")

    if not re.fullmatch(r"[a-z][a-z0-9_]*", cleaned):
        raise ValueError(
            "dataset_name must contain lowercase letters, digits, and underscores."
        )

    return cleaned