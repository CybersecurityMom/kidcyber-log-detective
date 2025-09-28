#!/usr/bin/env python3
import json, random, os, time

# Simple, kid-friendly console game:
# Show 10 short "logs", ask: suspicious (s) or not (n)?
# Then reveal answer + reasoning. No external libraries.

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs", "sample_logs.jsonl")

def load_logs(path):
    logs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            try:
                logs.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return logs

def pretty(log):
    # Make the "log" read like a short clue
    t = log.get("time")
    user = log.get("user")
    action = log.get("action")
    ip = log.get("ip")
    place = log.get("geo")
    device = log.get("device")
    details = log.get("details")
    return (f"[{t}] user={user} action={action} "
            f"ip={ip} geo={place} device={device} details={details}")

def explain(log):
    # Kid-friendly reasons for why it's suspicious or fine
    reason = log.get("reason", "")
    if not reason:
        return "Looks ordinary."
    return reason

def ask_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("s", "n", "q"):
            return ans
        print("Type s = suspicious, n = not suspicious, or q = quit")

def banner():
    print("\n🕵🏾‍♀️  Welcome to KidCyber Log Detective!")
    print("You’ll see 10 short 'clues'. Decide if each is suspicious (s) or not (n).")
    print("Type: s = suspicious, n = not suspicious, q = quit\n")

def main():
    logs = load_logs(LOG_PATH)
    if not logs:
        print("No logs found. Make sure sample_logs.jsonl exists.")
        return

    banner()
    random.shuffle(logs)
    round_logs = logs[:10]
    score = 0

    for idx, log in enumerate(round_logs, 1):
        print(f"— Clue {idx}/10 —")
        print(pretty(log))
        ans = ask_yes_no("Your call (s/n, q to quit): ")

        if ans == "q":
            print("\nThanks for playing! 👋")
            return

        gold = "s" if log.get("label") == "suspicious" else "n"
        if ans == gold:
            print("✅ Correct!", end=" ")
            score += 1
        else:
            print("❌ Not quite.", end=" ")

        print("Hint:", explain(log))
        print("-" * 60)
        time.sleep(0.4)

    print(f"\n🎉 Final Score: {score}/10")
    if score == 10:
        print("Legend status! Print your Detective Badge in printables/worksheet.md 🏅")
    elif score >= 7:
        print("Great eye! You’re ready for harder clues. 🧠")
    else:
        print("Nice start! Replay and look for late nights, fails, and far-away places.")
    print("Thanks for keeping the internet a little safer today. 🌟")

if __name__ == "__main__":
    main()
