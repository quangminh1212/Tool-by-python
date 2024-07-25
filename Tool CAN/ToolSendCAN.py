import pyautogui
import time

def send_can_message_via_cantest(can_id, data):
    # Convert CAN ID and data to hex strings
    can_id_str = f"{can_id:08X}"
    data_str = ' '.join(f"{byte:02X}" for byte in data)

    # Activate CANTest window (assuming it's already open)
    pyautogui.getWindowsWithTitle("CANTest")[0].activate()

   
    # Enter Data
    pyautogui.click(1942, 1320)  # Adjust coordinates to the Data input box
    pyautogui.press('delete', presses=20, interval=0.02) 
    pyautogui.typewrite(data_str)
    
    # Click Send button
    pyautogui.click(2200, 1320)  # Adjust coordinates to the Send button


def main():
    # Danh sách các bản tin CAN cần gửi
    messages = [
        [0x07, 0x01, 0x60],
        [0x07, 0x02, 0x62, 0x06, 0x05],
        [0x07, 0x10, 0x08, 0x62, 0x06, 0x05, 0x09, 0x41],
        [0x07, 0x21, 0x54, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],
        [0x07, 0x01, 0x61]
    ]
    
    # ID CAN
    can_id = 0x0A
    
    # Gửi từng bản tin
    for data in messages:
        send_can_message_via_cantest(can_id, data)

if __name__ == "__main__":
    main()
