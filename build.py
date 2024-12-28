import os
import subprocess

# Define directories
BUILD_DIR = "build"
REPORTS_DIR = "reports"
SRC_DIR = "src"  # Update this to match your subdirectory name

def create_directories():
    """Create build and reports directories."""
    os.makedirs(BUILD_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)
    print(f"Directories '{BUILD_DIR}' and '{REPORTS_DIR}' created/verified.")

def run_tests():
    """Run tests with pytest and save the results as XML."""
    print("Running tests...")
    result = subprocess.run(
        ["pytest", f"--junit-xml={REPORTS_DIR}/test-results.xml"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode == 0:
        print("Tests passed successfully.")
    else:
        print("Some tests failed. Check the test report for details.")
    print(result.stdout)
    with open(f"{REPORTS_DIR}/pytest_output.txt", "w") as f:
        f.write(result.stdout)

def compute_metrics():
    """Run OpenSCC (or a similar tool) for code metrics."""
    print("Computing metrics...")
    metrics_file = f"{REPORTS_DIR}/metrics_report.txt"
    try:
        result = subprocess.run(
            ["openscc", "--report", metrics_file, SRC_DIR],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("OpenSCC not installed or not found in PATH.")
        return
    print(f"Metrics report saved to {metrics_file}")

def detect_bad_smells():
    """Run pylint to detect bad smells."""
    print("Detecting bad smells...")
    pylint_file = f"{REPORTS_DIR}/bad_smells_report.txt"
    result = subprocess.run(
        ["pylint", "--output-format=text", f"{SRC_DIR}/loan_calculator.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        print("PyLint reported issues. Check the bad smells report for details.")
    with open(pylint_file, "w") as f:
        f.write(result.stdout)
    print(f"Bad smells report saved to {pylint_file}")

def main():
    """Main function to orchestrate the build process."""
    create_directories()
    run_tests()
    compute_metrics()
    detect_bad_smells()
    print("Build process completed. Check the reports directory for outputs.")

if __name__ == "__main__":
    main()



