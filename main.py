"""
AFM Blaze Angle Analysis
Run this file to analyze your data, with the mode set in afm_analysis/config.py

Kept at the project root because it is the entry point the README has always
documented and the one muscle memory reaches for. It delegates to the same
dispatch as the `afm-analysis` console script, so the two cannot drift.
"""
import os
import sys

# Support running from a checkout without installing the package first.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from afm_analysis.cli import main

if __name__ == "__main__":
    sys.exit(main())
