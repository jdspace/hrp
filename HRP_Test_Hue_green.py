# %% hue test – auto-discover + auto-pair + green blink
from phue import Bridge, PhueRegistrationException
import time


# ---------- Bridge helpers ----------

def discover_bridge_ip(fallback_ip="192.168.88.118"):
    """
    Try to auto-discover the Hue Bridge IP.
    If that fails, fall back to a known IP.
    """
    print("🔍 Attempting to auto-discover Hue Bridge IP...")
    try:
        temp_bridge = Bridge()
        ip = temp_bridge.get_ip_address()
        print(f"📡 Auto-discovery found Hue Bridge at {ip}")
        return ip
    except Exception as e:
        print(f"⚠️ Auto-discovery failed ({e}). Falling back to {fallback_ip}")
        return fallback_ip


def connect_to_bridge():
    """
    Connect to the Hue Bridge.
    - Uses auto-discovered IP (with fallback).
    - If not yet registered, prompts user to press the bridge button,
      then retries until registration succeeds.
    """
    bridge_ip = discover_bridge_ip()

    b = Bridge(bridge_ip)

    while True:
        try:
            print(f"🔗 Connecting to Hue Bridge at {bridge_ip}...")
            b.connect()
            print("✅ Connected to Hue Bridge!")
            return b
        except PhueRegistrationException:
            print(
                "\n🚨 Bridge not yet registered with this PC."
                "\n👉 Press the physical button on the Hue Bridge now,"
                "\n   then press Enter here within 30 seconds."
            )
            input("⏸ Press Enter after pressing the bridge button...")
        except Exception as e:
            print(f"❌ Unexpected error while connecting: {e}")
            raise


# ---------- Light helpers ----------

def pick_first_light(bridge: Bridge):
    lights = bridge.get_light_objects("name")
    print(f"\n📱 Found {len(lights)} light(s):")
    for name in lights:
        print(f"  - {name}")

    if not lights:
        raise RuntimeError("No Hue lights found!")

    first_light = list(lights.values())[0]
    print(f"\n✨ Using first light: {first_light.name}")
    return first_light


def save_light_state(light):
    return {
        "on": light.on,
        "hue": light.hue,
        "saturation": light.saturation,
        "brightness": light.brightness,
    }


def restore_light_state(light, state):
    print("\n🔄 Restoring original color and state...")
    light.hue = state["hue"]
    light.saturation = state["saturation"]
    light.brightness = state["brightness"]
    light.on = state["on"]
    print("✅ Color restored!")


# ---------- Main effect ----------

def run_green_sequence(light):
    # Approximate GREEN in Hue color space
    GREEN_HUE = 25500  # 0–65535; 25500 is a nice green

    # Save original state
    original_state = save_light_state(light)
    print(f"\n💾 Saved original state: {original_state}")

    # Step 1: Solid green for 2 seconds
    print("\n🟢 Step 1: Solid green for 2 seconds...")
    light.on = True
    light.hue = GREEN_HUE
    light.saturation = 254
    light.brightness = 254
    time.sleep(2)

    # Step 2: Blink green twice (off/on, off/on)
    print("💡 Step 2: Blinking green twice...")
    for i in range(2):
        # off
        light.on = False
        time.sleep(0.3)

        # back on green
        light.on = True
        light.hue = GREEN_HUE
        light.saturation = 254
        light.brightness = 254
        time.sleep(0.3)

    # Step 3: Restore original state
    restore_light_state(light, original_state)
    time.sleep(1)


# ---------- Script entry point ----------

if __name__ == "__main__":
    bridge = connect_to_bridge()
    first_light = pick_first_light(bridge)
    run_green_sequence(first_light)
# %%