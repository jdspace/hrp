# %% csv test
import csv
from datetime import datetime
import random

print("📊 Testing CSV data logging...")

# Create a test log file
filename = f"hrp_test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header
    writer.writerow(['timestamp', 'person1_bpm', 'person2_bpm', 'sync_score'])
    
    # Write 10 rows of fake data
    for i in range(10):
        timestamp = datetime.now().isoformat()
        person1_bpm = random.randint(60, 100)
        person2_bpm = random.randint(60, 100)
        sync_score = random.random()
        
        writer.writerow([timestamp, person1_bpm, person2_bpm, sync_score])
        print(f"  Logged: {timestamp} | P1: {person1_bpm} | P2: {person2_bpm}")

print(f"\n✅ CSV logging works! File saved: {filename}")
print("You can open this in Excel to verify")
# %%
