import json

print("Starting processing...")

try:
    # Read raw data
    with open("data.json") as f:
        data = json.load(f)

    print("Raw data loaded")

    # Extract useful data
    processed_data = {
        "userId": data["userId"],
        "title": data["title"],
        "status": data["completed"]
    }

    # Save processed data
    with open("processed.json", "w") as f:
        json.dump(processed_data, f, indent=4)

    print("Data processed successfully!")

except Exception as e:
    print("Error:", e)