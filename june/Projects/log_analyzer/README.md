# Log Analyzer CLI 📋

A command-line tool to analyze log files and generate reports.
Built with Python — no external libraries needed.

## Usage

```bash
python analyzer.py <logfile> [options]
```

## Options

| Option | Description | Example |
|--------|-------------|---------|
| --level | Filter by log level | --level ERROR |
| --date | Filter by date | --date 2026-06-08 |
| --top | Show top N errors | --top 5 |
| --save | Save report to JSON | --save report.json |

## Examples

```bash
# Basic analysis
python analyzer.py app.log

# Show only errors
python analyzer.py app.log --level ERROR

# Filter by date
python analyzer.py app.log --date 2026-06-08

# Save report
python analyzer.py app.log --save report.json
```

## Topics Used
- Regular Expressions — parse log lines
- Classes & OOP — organize code
- Collections — count log levels
- DateTime — filter by date
- Context Managers — file handling
- List/Generator Comprehensions — filter entries
- sys.argv — CLI interface
- JSON — save reports