# Đường dẫn đến file hex cần sửa
file_path = 'path_to_your_hex_file.hex'

# Giá trị bạn muốn chuyển đổi và ghi vào file
Bluetooth_key_0 = 1222
# Chuyển đổi giá trị thập phân thành hexa
hex_value_key_0 = format(Bluetooth_key_0, '04x') # Đảm bảo chuỗi hex có đủ độ dài, ở đây là 4 kí tự
# Đảo ngược chuỗi hex theo cặp bytes
reversed_hex_str_key_0 = ''.join(reversed([hex_value_key_0[i:i+2] for i in range(0, len(hex_value_key_0), 2)]))
# Chuyển đổi chuỗi hex đảo ngược thành chuỗi bytes
reversed_hex_bytes_key_0 = bytes.fromhex(reversed_hex_str_key_0)

# Giá trị bạn muốn chuyển đổi và ghi vào file
Bluetooth_key_1 = 1222
# Chuyển đổi giá trị thập phân thành hexa
hex_value_key_1 = format(Bluetooth_key_1, '04x') # Đảm bảo chuỗi hex có đủ độ dài, ở đây là 4 kí tự
# Đảo ngược chuỗi hex theo cặp bytes
reversed_hex_str_key_1 = ''.join(reversed([hex_value_key_1[i:i+2] for i in range(0, len(hex_value_key_1), 2)]))
# Chuyển đổi chuỗi hex đảo ngược thành chuỗi bytes
reversed_hex_bytes_key_1 = bytes.fromhex(reversed_hex_str_key_1)

# Mở file ở chế độ đọc và ghi nhị phân
with open(file_path, 'rb+') as file:

    # Di chuyển đến địa chỉ cần sửa đổi (18DB0)
    file.seek(0x18DB0)
    # Ghi thay đổi vào 4 vị trí đầu tiên tại địa chỉ này
    file.write(reversed_hex_bytes_key_0)

    # Đọc dữ liệu hiện tại tại địa chỉ (0x18DC0)
    file.seek(0x18DC0)
    current_data = file.read(5)  # Đọc 5 bytes, bao gồm cả vị trí thứ 4 cần sửa
    # Sửa đổi byte thứ 4 thành 00 mà không ảnh hưởng đến các byte khác
    modified_data = current_data[:3] + b'\x00' + current_data[4:]
    # Quay lại vị trí 0x18DC0 và ghi dữ liệu đã sửa
    file.seek(0x18DC0)
    file.write(modified_data)

    # Di chuyển đến địa chỉ cần sửa đổi (18DB0)
    file.seek(0x18DE0)
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
#  18DD0 0-3 : KEY 0 ID được chuyển sang mã hex và viết ngược lại theo cặp
#  18DE0 9   : KEY 0 status
#  18DF0 5   : KEY 0 status