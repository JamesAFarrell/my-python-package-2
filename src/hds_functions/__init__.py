"""Package entry point and version. Small change."""

from .data_privacy import redact_low_counts, round_counts_to_multiple

__all__ = [
    "redact_low_counts",
    "round_counts_to_multiple",
]
