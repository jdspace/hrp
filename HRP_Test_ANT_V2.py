# %% ant test V2 (different library)
import usb.core
import usb.util
import time

print("🔍 Searching for ANT+ USB Dongles...")

# Find all USB devices
devices = usb.core.find(find_all=True)

print("\n📱 USB Devices found:")
for device in devices:
    try:
        print(f"  Vendor: {hex(device.idVendor)}, Product: {hex(device.idProduct)}")
        if device.idVendor == 0x0fcf:  # Dynastream (ANT+)
            print(f"  ✅ ANT+ Dongle detected!")
            print(f"     Product ID: {hex(device.idProduct)}")
            print(f"     Bus: {device.bus}, Address: {device.address}")
    except:
        pass

print("\n" + "="*50)
print("Expected: Vendor: 0xfcf (Dynastream)")
print("If you see it above, the dongle is recognized!")
# %%
