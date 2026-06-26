import re
from multiprocessing import Pool


def analyze_log(filepath):
    """Count errors in a single log file"""
    errors = 0
    with open(filepath) as f:
        for line in f:
            if re.search(r"ERROR", line):
                errors += 1
    return {"file": filepath, "errors": errors}


if __name__ == "__main__":
    # Imagine you have 100 log files to analyze
    # log_files = ["sample.log", "sample.log", "sample.log"] #using the same file 3x

    with Pool(processes=3) as pool:
        results = pool.map(analyze_log, log_files)

    for result in results:
        print(f"{result['file']}: {result['errors']} errors")
