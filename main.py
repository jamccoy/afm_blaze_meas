"""
AFM Blaze Angle Analysis
Main entry point - run this file to analyze your data
"""
import matplotlib.pyplot as plt

from afm_analysis.config import ANALYSIS_MODE
from afm_analysis.workflows import (
    run_single_file_analysis,
    run_multiple_file_analysis,
    run_comparison_analysis,
    run_boundary_profile_export,
    run_icc_report
)

# Matplotlib setup
plt.close("all")
plt.ion()
plt.rcParams.update({
    "text.usetex": False,
    "font.family": "sans-serif"
})


def main():
    """Main execution entry point"""
    
    # Route to appropriate workflow based on analysis mode
    if ANALYSIS_MODE == 'single':
        run_single_file_analysis()
        
    elif ANALYSIS_MODE == 'multiple':
        run_multiple_file_analysis()
        
    elif ANALYSIS_MODE == 'compare':
        run_comparison_analysis()

    elif ANALYSIS_MODE == 'ggp':
        run_boundary_profile_export()

    elif ANALYSIS_MODE == 'icc':
        run_icc_report()

    else:
        print(f"Unknown ANALYSIS_MODE: {ANALYSIS_MODE}")
        print("Please set ANALYSIS_MODE to 'single', 'multiple', 'compare', "
              "'ggp', or 'icc' in config.py")
        return
    
    plt.show()
    print("\n✓ Analysis complete!")


if __name__ == "__main__":
    main()