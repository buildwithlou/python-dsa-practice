from collections import Counter

class Reporter:
    def __init__(self, entries):
        self.entries = entries

    def summary(self):
        total = len(self.entries)
        counts = Counter(entry.level for entry in self.entries)

        print("\n" + "="*40)
        print("LOG ANALYSIS REPORT")
        print("="*40)
        print(f"Total entries:  {total}")
        print(f"Errors:         {counts['ERROR']}")
        print(f"Warnings:       {counts['WARNING']}")
        print(f"Info:           {counts['INFO']}")
        print("="*40)

    def most_common_errors(self, n=3):
        errors = [e.message for e in self.entries if e.level == "ERROR"]
        common = Counter(errors).most_common(n)

        print(f"\nTop {n} Most Common Errors:")
        print("-"*40)
        for message, count in common:
            print(f" {count}x -> {message}")

    def filter_by_level(self, level):
        filtered = [e for e in self.entries if e.level == level.upper()]

        print(f"\n{level.upper()} entries ({len(filtered)} total):")
        print("-"*40)
        for entry in filtered:
            print(f" {entry.timestamp.strftime('%H:%M:%S')} -> {entry.message}")
    
    def filter_by_date(self, date_str):
        filtered = [e for e in self.entries
                    if e.timestamp.strftime("%Y-%m-%d") == date_str]
        
        print(f"\nEntries for {date_str} ({len(filtered)} total):")
        print("-"*40)
        for entry in filtered:
            print(f"{entry.timestamp.strftime('%H:%M:%S')} {entry.level} -> {entry.message}")

    def save_report(self, output_path):
        import json
        report = {
            "total" : len(self.entries),
            "counts": dict(Counter(e.level for e in self.entries)),
            "errors": [
                {
                    "timestamp" : e.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "message" : e.message

                }
                for e in self.entries if e.level == "ERROR"
            ]
        }
        with open(output_path, "w") as f:
            json.dump(report, f, indent=4)
        print(f"\nReport saved to {output_path}")

