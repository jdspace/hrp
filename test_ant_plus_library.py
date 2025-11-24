from ant.plus.plus import HeartRate
import time

print("🔍 Testing ant-plus library with CycPlus H1 monitors...")
print("Make sure ANT+ dongle is plugged in")
print("Make sure at least one monitor is ON and worn on your arm\n")

try:
    # Create heart rate sensor object
    hr = HeartRate()
    
    print("✅ ant-plus library initialized")
    print("🔍 Searching for heart rate monitors...")
    print("This may take 10-20 seconds...\n")
    
    # Start searching for devices
    hr.open()
    
    print("Listening for heart rate data...")
    print("Press Ctrl+C to stop\n")
    
    # Listen for data
    for i in range(60):  # Listen for 60 seconds
        data = hr.get_data()
        if data:
            print(f"❤️  Heart Rate: {data.get('heart_rate', 'N/A')} BPM")
            print(f"   Device: {data.get('device_id', 'Unknown')}")
        time.sleep(1)
    
    hr.close()
    print("\n✅ Test complete!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Is ANT+ dongle plugged in?")
    print("2. Is a CycPlus monitor ON and worn?")
    print("3. Try running with: sudo python3 test_ant_plus_library.py")
