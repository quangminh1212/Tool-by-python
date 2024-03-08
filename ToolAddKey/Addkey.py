# Đường dẫn đến file hex cần sửa
file_path = 'path_to_your_hex_file.hex'
# Giá trị bạn KEY_0 muốn chuyển đổi và ghi vào file
Bluetooth_key_0 = 1222
# Giá trị bạn KEY_1 muốn chuyển đổi và ghi vào file
Bluetooth_key_1 = 1222
# Giá trị bạn BLE name muốn chuyển đổi và ghi vào file
BLE_name = 1222


# Chuyển đổi giá trị thập phân thành hexa
hex_value_key_0 = format(Bluetooth_key_0, '04x') # Đảm bảo chuỗi hex có đủ độ dài, ở đây là 4 kí tự
# Đảo ngược chuỗi hex theo cặp bytes
reversed_hex_str_key_0 = ''.join(reversed([hex_value_key_0[i:i+2] for i in range(0, len(hex_value_key_0), 2)]))
# Chuyển đổi chuỗi hex đảo ngược thành chuỗi bytes
reversed_hex_bytes_key_0 = bytes.fromhex(reversed_hex_str_key_0)


# Chuyển đổi giá trị thập phân thành hexa
hex_value_key_1 = format(Bluetooth_key_1, '04x') # Đảm bảo chuỗi hex có đủ độ dài, ở đây là 4 kí tự
# Đảo ngược chuỗi hex theo cặp bytes
reversed_hex_str_key_1 = ''.join(reversed([hex_value_key_1[i:i+2] for i in range(0, len(hex_value_key_1), 2)]))
# Chuyển đổi chuỗi hex đảo ngược thành chuỗi bytes
reversed_hex_bytes_key_1 = bytes.fromhex(reversed_hex_str_key_1)

# Chuyển đổi giá trị thập phân thành hexa
hex_value_ble = format(BLE_name, '04x') # Đảm bảo chuỗi hex có đủ độ dài, ở đây là 4 kí tự
# Đảo ngược chuỗi hex theo cặp bytes
reversed_hex_str_ble = ''.join(reversed([hex_value_ble[i:i+2] for i in range(0, len(hex_value_ble), 2)]))
# Chuyển đổi chuỗi hex đảo ngược thành chuỗi bytes
reversed_hex_bytes_ble = bytes.fromhex(reversed_hex_str_ble)

# Mở file ở chế độ đọc và ghi nhị phân
with open(file_path, 'rb+') as file:

    # Thêm mã key_0 vào xe (pair key)
        # Di chuyển đến địa chỉ cần sửa đổi (18DB0)
        file.seek(0x18DB0)
        # Ghi thay đổi vào 4 vị trí đầu tiên tại địa chỉ này
        file.write(reversed_hex_bytes_key_0)


    # Sửa Key status key_0 thành Enable Key
        # Đọc dữ liệu hiện có tại địa chỉ 0x18DC0
        file.seek(0x18DC0)
        current_data_key_0 = bytearray(file.read(6))  # Đọc 6 bytes để bao gồm vị trí thứ 5
        # Thay đổi giá trị ở vị trí thứ 5 thành 01
        current_data_key_0[4] = 0x01  # Vị trí thứ 5 là chỉ số 4 vì chỉ số bắt đầu từ 0
        # Ghi lại chuỗi bytes đã chỉnh sửa vào địa chỉ 0x18DC0
        file.seek(0x18DC0)
        file.write(current_data_key_0)


    # Thêm mã key_1 vào xe (pair key)
        # Di chuyển đến địa chỉ cần sửa đổi (18DD0)
        file.seek(0x18DD0)
        # Ghi thay đổi vào 4 vị trí đầu tiên tại địa chỉ này
        file.write(reversed_hex_bytes_key_1)


    # Sửa Key status key_1 thành Enable Key
       # Đọc dữ liệu hiện có tại địa chỉ 0x18DE0
        file.seek(0x18DE0)
        current_data_key_1 = bytearray(file.read(5))  # Đọc 6 bytes để bao gồm vị trí thứ 5
        # Thay đổi giá trị ở vị trí thứ 5 thành 01
        current_data_key_1 [4] = 0x01  # Vị trí thứ 5 là chỉ số 4 vì chỉ số bắt đầu từ 0
        # Ghi lại chuỗi bytes đã chỉnh sửa vào địa chỉ 0x18DC0
        file.seek(0x18DE0)
        file.write(current_data_key_1)


    # Sửa BLE BOND STATUS thành Key được gen khi nhấn giữ 3s SMK đã học.
        # Đọc dữ liệu hiện có tại địa chỉ 0x18DE0
        file.seek(0x18DE0)
        current_data_ble = bytearray(file.read(10))  # Đọc 10 bytes để bao gồm vị trí thứ 9
        # Thay đổi giá trị ở vị trí thứ 9 thành 00
        current_data_ble [8] = 0x00  # Vị trí thứ 9 là chỉ số 8 vì chỉ số bắt đầu từ 0
        # Ghi lại chuỗi bytes đã chỉnh sửa vào địa chỉ 0x18DC0
        file.seek(0x18DE0)
        file.write(current_data_ble)


    # Thêm mã key_1 vào xe (pair key)
        # Di chuyển đến địa chỉ cần sửa đổi (18DD0)
        file.seek(0x18DF0)
        # Ghi thay đổi vào 4 vị trí đầu tiên tại địa chỉ này
        file.write(reversed_hex_bytes_key_1)



print("Sửa đổi file hex thành công!")

# Key status:
    # 00: Disable KEY
    # 01: Enable KEY
    # 02: Learn KEY

# BLE BOND STATUS:
# -	00: Key được gen khi nhấn giữ 3s SMK đã học.
# -	01: Mặc định khi mới sản xuất.
# -	02: Key mặc định là “123456” ngay khi khởi động.


#  18DB0 0-3 : KEY 0 ID được chuyển sang mã hex và viết ngược lại theo cặp
#  18DC0 4   : KEY 0 status
#  18DD0 0-3 : KEY 1 ID được chuyển sang mã hex và viết ngược lại theo cặp
#  18DE0 4   : KEY 1 status
#  18DE0 8   : BLE BOND STATUS
#  18DF0 0-3 : BLE NAME