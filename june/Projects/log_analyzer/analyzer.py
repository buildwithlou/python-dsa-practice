import sys 
from parser import LogParser
from reporter import Reporter

def print_usage():
    print("""Usage: python analyzer.py <logfile> [options]

Options:
  --level ERROR|WARNING|INFO    filter by log level
  --date  YYYY-MM-DD            filter by date
  --top   N                     show top N common errors (default 3)
  --save  output.json           save report to file

Examples:
  python analyzer.py sample.log
  python analyzer.py sample.log --level ERROR
  python analyzer.py sample.log --date 2026-06-08
  python analyzer.py sample.log --top 5
  python analyzer.py sample.log --save report.json
    """)

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    filepath = sys.argv[1]
    args = sys.argv[2:]
    parser = LogParser(filepath)
    entries = parser.parse()

    if not entries:
        print("No entries found or file is empty")
        return
    
    reporter = Reporter(entries)

    reporter.summary()
    reporter.most_common_errors()

    if "--level" in args:
        index = args.index("--level")
        level = args[index + 1]
        reporter.filter_by_level(level)

    if "--date" in args:
        index = args.index("--date")
        date = args[index + 1]
        reporter.filter_by_date(date)

    if "--top" in args:
        index = args.index("--top")
        n = int(args[index +1])
        reporter.most_common_errors(n)
    
    if "--save" in args:
        index = args.index("--save")
        output = args[index + 1]
        reporter.save_reporter(output)

if __name__ == "__main__":
    main()