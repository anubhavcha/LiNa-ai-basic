import psutil
from LIN2_Mouth import speak

def plug_check():
    prev_status = None  # Initialize prev_status variable
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        status = battery.power_plugged
        if prev_status is not None and status != prev_status:  # Check if the status has changed
            if status:
                print("Charger plugged in.")
                speak("Charging started.")
            else:
                print("Charger unplugged.")
                speak("Charging stopped.")
                
        prev_status = status  # Update prev_status variable


