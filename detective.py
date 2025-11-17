# Cyber Log Detective - Simple Yes/No Game (EST times, kid-friendly)

logs = [
    {
        "time": "September 19, 2025 – 9:31 PM EST",
        "user": "admin",
        "action": "password_reset",
        "geo": "Poland",
        "device": "Windows",
        "details": "reset for 5 accounts",
        "suspicious": True,
    },
    {
        "time": "September 20, 2025 – 10:10 AM EST",
        "user": "maria",
        "action": "login_success",
        "geo": "North Carolina, USA",
        "device": "iPad",
        "details": "home wifi",
        "suspicious": False,
    },
    {
        "time": "September 20, 2025 – 10:18 AM EST",
        "user": "eli",
        "action": "login_failed",
        "geo": "Singapore",
        "device": "Linux",
        "details": "wrong password 6x",
        "suspicious": True,
    },
    {
        "time": "September 21, 2025 – 3:00 AM EST",
        "user": "guest",
        "action": "login_success",
        "geo": "Local Network",
        "device": "Chromebook",
        "details": "library kiosk",
        "suspicious": False,
    },
    {
        "time": "September 21, 2025 – 3:12 AM EST",
        "user": "admin",
        "action": "account_delete",
        "geo": "Unknown",
        "device": "Unknown",
        "details": "deleted 20 test users",
        "suspicious": True,
    },
    {
        "time": "September 21, 2025 – 5:55 PM EST",
        "user": "noah",
        "action": "login_success",
        "geo": "Brazil",
        "device": "Android",
        "details": "travel SIM",
        "suspicious": False,
    },
    {
        "time": "September 21, 2025 – 6:03 PM EST",
        "user": "noah",
        "action": "login_success",
        "geo": "North Carolina, USA",
        "device": "Android",
        "details": "minutes after Brazil",
        "suspicious": True,
    },
    {
        "time": "September 21, 2025 – 10:12 PM EST",
        "user": "sara",
        "action": "login_success",
        "geo": "Unknown",
        "device": "Unknown",
        "details": "new device at 3am",
        "suspicious": True,
    },
    {
        "time": "September 22, 2025 – 11:05 AM EST",
        "user": "sara",
        "action": "file_share",
        "geo": "North Carolina, USA",
        "device": "Mac",
        "details": "shared math.png with mom",
        "suspicious": False,
    },
    {
        "time": "September 22, 2025 – 1:22 PM EST",
        "user": "teacher",
        "action": "group_create",
        "geo": "North Carolina, USA",
        "device": "Windows",
        "details": "created class group",
        "suspicious": False,
    },
    {
        "time": "September 22, 2025 – 1:25 PM EST",
        "user": "teacher",
        "action": "file_delete",
        "geo": "Germany",
        "device": "Windows",
        "details": "deleted 100 photos",
        "suspicious": True,
    },
    {
        "time": "September 23, 2025 – 7:01 AM EST",
        "user": "dad",
        "action": "login_success",
        "geo": "North Carolina, USA",
        "device": "iPhone",
        "details": "lunch break",
        "suspicious": False,
    },
    {
        "time": "September 23, 2025 – 7:02 AM EST",
        "user": "dad",
        "action": "settings_change",
        "geo": "North Carolina, USA",
        "device": "iPhone",
        "details": "turned on MFA",
        "suspicious": False,
    },
    {
        "time": "September 23, 2025 – 6:59 PM EST",
        "user": "guest",
        "action": "login_failed",
        "geo": "Unknown",
        "device": "Unknown",
        "details": "wrong password 9x",
        "suspicious": True,
    },
    {
        "time": "September 25, 2025 – 10:30 AM EST",
        "user": "sara",
        "action": "login_success",
        "geo": "California, USA",
        "device": "New Laptop",
        "details": "first time seen",
        "suspicious": True,
    },
    {
        "time": "September 25, 2025 – 5:22 AM EST",
        "user": "emma",
        "action": "file_share",
        "geo": "UK",
        "device": "Mac",
        "details": "shared cat.png",
        "suspicious": False,
    },
    {
        "time": "September 24, 2025 – 9:40 PM EST",
        "user": "admin",
        "action": "settings_change",
        "geo": "Russia",
        "device": "Linux",
        "details": "disabled MFA",
        "suspicious": True,
    },
    {
        "time": "September 26, 2025 – 5:10 PM EST",
        "user": "mom",
        "action": "login_success",
        "geo": "North Carolina, USA",
        "device": "Family Laptop",
        "details": "evening login",
        "suspicious": False,
    },
    {
        "time": "September 27, 2025 – 4:15 AM EST",
        "user": "teacher",
        "action": "settings_change",
        "geo": "Vacation Resort",
        "device": "Tablet",
        "details": "changed grading settings",
        "suspicious": True,
    },
]

print("\n🕵️ Cyber Log Detective — Yes/No Game (EST)\n")

score = 0

for entry in logs:
    print(f"[{entry['time']}] user={entry['user']} {entry['action']}")
    print(f"geo={entry['geo']} device={entry['device']} details={entry['details']}\n")

    answer = input("Question: Is this suspicious? (yes/no): ").strip().lower()
    correct = "yes" if entry["suspicious"] else "no"

    if answer.startswith(correct[0]):  # y/n shortcut
        score += 1
        if correct == "yes":
            print("✅ Correct! This one IS suspicious.\n")
        else:
            print("✅ Correct! This one is NORMAL.\n")
    else:
        if correct == "yes":
            print("❌ Not quite. This one IS suspicious.\n")
        else:
            print("❌ Not quite. This one is actually normal.\n")

print(f"Game over! You answered {score} out of {len(logs)} correctly.\n")

