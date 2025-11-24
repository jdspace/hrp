# %% ant test
from openant.easy.node import Node
from openant.devices.heart_rate import HeartRate
import time

print("🔍 Searching for heart rate monitors...")
print("Make sure your CycPlus H1 monitors are on and nearby")

# Try to initialize with explicit backend
try:
    node = Node()
    node.start()
    print("✅ ANT+ node started successfully!")
    
    # Wait for device detection
    time.sleep(5)
    print("Waiting for heart rate data...")
    print("Put on a heart rate monitor and wait...")
    
    time.sleep(10)  # Give it time to detect
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Is the ANT+ dongle plugged in?")
    print("2. Did you install libusb? (brew install libusb)")
    print("3. Are the CycPlus monitors on and nearby?")
# %%
