# %% ant test V3 using Bluetooth
import usb.core
import usb.util

print("🔍 Attempting direct USB connection to ANT+ dongle...")

# Find the ANT+ dongle (Dynastream 0x0fcf)
dev = usb.core.find(idVendor=0x0fcf, idProduct=0x1008)

if dev is None:
    print("❌ ANT+ dongle not found")
else:
    print("✅ ANT+ dongle found!")
    print(f"   Manufacturer: {usb.util.get_string(dev, dev.iManufacturer)}")
    print(f"   Product: {usb.util.get_string(dev, dev.iProduct)}")
    
    # Try to claim the interface
    try:
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)
            print("   Detached kernel driver")
        
        usb.util.claim_interface(dev, 0)
        print("   ✅ Successfully claimed USB interface")
        print("\n   This means Python CAN access the dongle!")
        print("   Your colleague's code should work on Monday.")
        
    except usb.core.USBError as e:
        print(f"   ⚠️  USB Error: {e}")
        print("   This might need admin permissions")
        print("   Try: sudo python3 test_ant_raw.py")
# %%
