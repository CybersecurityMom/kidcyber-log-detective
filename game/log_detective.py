#!/usr/bin/env python3
import json, random, os, time

# Path to the logs file
LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs", "sample_logs.jsonl")
SCOREBOARD_PATH = os.path.join(os.path.dirname(__file__), "..", "scoreboard.txt")

def load_logs(path):
    logs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                logs.append(json.loads(line.strip()))
            except:
                pass
    return logs

def pretty(log):
    return f"[{log['time']}] user={log['user']} action={log['action']} ip={log['ip']} geo={log['geo']} device={log['device']} details={log['details']}"

def explain(log, lang):
    if lang == "es" and "reason_es" in log:
        return log["reason_es"]
    return log.get("reason", "Looks ordinary.")

def ask(prompt):
    while True:
        ans = input(prompt).lower().strip()
        if ans in ("s", "n", "q"):
            return ans
        print("Type s = suspicious, n = not suspicious, q = quit")

def main():
    logs = load_logs(LOG_PATH)
    if not logs:
        print("No logs found.")
        return

    # Choose difficulty
    mode = input("Choose mode: easy or hard: ").strip().lower()
    if mode == "hard":
        logs = [log for log in logs if log.get("difficulty", "easy") == "hard"]
    else:
        logs = [log for log in logs if log.get("difficulty", "easy") == "easy"]

    # Choose language
    lang = input("Language? (en/es): ").strip().lower()
    if lang not in ("en", "es"):
        lang = "en"

    print("\n🕵🏾‍♀️ Welcome to KidCyber Log Detective!")
    print("You’ll see up to 10 short 'clues'. Decide if each is suspicious (s) or not (n).")
    print("Type: s = suspicious, n = not suspicious, q = quit\n")

    random.shuffle(logs)
    score = 0

    for idx, log in enumerate(logs[:10], 1):
        print(f"\n— Clue {idx}/10 —")
        print(pretty(log))
        ans = ask("Your call (s/n, q to quit): ")

        if ans == "q":
            break

        correct = "s" if log["label"] == "suspicious" else "n"
        if ans == correct:
            print("✅ Correct!", end=" ")
            score += 1
        else:
            print("❌ Not quite.", end=" ")

        print("Hint:", explain(log, lang))
        print("-" * 50)
        time.sleep(0.5)

    print(f"\n🎉 Final Score: {score}/10")

    # Save score to scoreboard
    with open(SCOREBOARD_PATH, "a", encoding="utf-8") as f:
        f.write(f"Mode: {mode}, Lang: {lang}, Score: {score}/10\n")

    print(f"Your score has been saved to {SCOREBOARD_PATH}")

if __name__ == "__main__":
    main()

