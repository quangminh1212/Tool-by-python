#!/bin/bash

# Chạy script Python để chỉnh sửa firmware
python3 modify_firmware.py input_firmware.hex output_firmware.hex

# Nạp firmware đã chỉnh sửa vào thiết bị
# Lệnh sau đây là ví dụ và sẽ thay đổi dựa trên công cụ nạp và thiết bị của bạn
nrfjprog --program output_firmware.hex --sectorerase
nrfjprog --reset