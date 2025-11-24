# %% hue test
from phue import Bridge
import time

# Bridge IP address
bridge_ip = "192.168.88.118"  #

print(f"🔍 Connecting to Hue Bridge at {bridge_ip}...")

b = Bridge(bridge_ip)
b.connect()

print("✅ Connected to Hue Bridge!")

# Get lights
lights = b.get_light_objects('name')
print(f"\n📱 Found {len(lights)} light(s):")
for name, light in lights.items():
    print(f"  - {name}")

# Get first light
first_light = list(lights.values())[0]

# Save FULL original state
original_state = {
    'on': first_light.on,
    'hue': first_light.hue,
    'saturation': first_light.saturation,
    'brightness': first_light.brightness
}

print(f"\n💾 Saved original state: {original_state}")

# Test: Turn red
print("\n🔴 Testing: Light should turn red for 2 seconds...")
first_light.on = True
first_light.hue = 0
first_light.saturation = 254
first_light.brightness = 254

time.sleep(5)

# Restore original color
print("🔄 Restoring original color...")
first_light.hue = original_state['hue']
first_light.saturation = original_state['saturation']
first_light.brightness = original_state['brightness']
first_light.on = original_state['on']

time.sleep(1)
print("✅ Color restored!")
# %%
