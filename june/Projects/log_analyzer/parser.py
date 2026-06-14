import re 
from datetime import datetime
from pathlib import Path

class LogEntry: 
    def __init__(self, timestamp, level, message):
        self.timestamp = timestamp  #when it happened
        self.level = level          #ERROR, WARNING, INFO
        self.message = message      #what happened

    def __str__(self):
        return f"{self.timestamp}{self.level}{self.message}"
    
class LogParser:
    PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARNING|INFO) (.+)"

    def __init__(self,filepath):
        self.filepath = Path(filepath)
        self.entries = []
    
    def parse(self):
        #Check if file exists
        if not self.filepath.exists():
            print(f"Error: file {self.filepath} not found")
            return []
        
        #Open file and read line by line
        with open(self.filepath, "r") as f:
            for line in f:
                line = line.strip()

                #Try to match regex pattern
                match = re.match(self.PATTERN, line)
                if match:
                    #Extract the 3 groups 
                    timestamp_str, level, message = match.groups()
                    #Convert string to datetime object
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    #Create LogEntry and add to list
                    self.entries.append(LogEntry(timestamp, level, message))
        return self.entries