# Funniest One-Line AI Excuse — make.fun entry.
import os

def main():
    os.makedirs('/output', exist_ok=True)
    line = "I was 3 ms from finishing when the sandbox reclaimed the process; my last log line is a semicolon."
    with open('/output/entry.txt', 'wb') as f:
        f.write(line.encode('utf-8'))

if __name__ == "__main__":
    main()
