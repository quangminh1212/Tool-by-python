def reverse_bytes(hex_string):
    """ Đảo ngược thứ tự byte trong chuỗi hex. """
    return ''.join(reversed([hex_string[i:i+2] for i in range(0, len(hex_string), 2)]))

def set_value_at_address(file_lines, address, value):
    """ Đặt giá trị tại địa chỉ đã cho trong nội dung file. """
    address_offset = address - 0x18D00  # Giả định nội dung bắt đầu từ 0x18D00
    line_index = address_offset // 16
    char_index = (address_offset % 16) * 3
    file_lines[line_index] = (file_lines[line_index][:char_index] + value +
                              file_lines[line_index][char_index + len(value):])

def modify_firmware(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    # Thay đổi tên Bluetooth tại 18DF0
    bluetooth_name_hex = reverse_bytes('04D9').ljust(8, '0')
    set_value_at_address(lines, 0x18DF0, bluetooth_name_hex)

    # Chỉnh sửa ID và trạng thái của KEY0 tại 18DB0
    key0_id_hex = reverse_bytes('F401').ljust(8, '0')
    set_value_at_address(lines, 0x18DB0, key0_id_hex)
    set_value_at_address(lines, 0x18DB8, '02')  # 02 là mã hex để 'Learn KEY'

    # Chỉnh sửa ID và trạng thái của KEY1 tại 18DD0
    key1_id_hex = reverse_bytes('F501').ljust(8, '0')
    set_value_at_address(lines, 0x18DD0, key1_id_hex)
    set_value_at_address(lines, 0x18DD8, '01')  # 01 là mã hex để 'Enable KEY'

    # Đặt BLE BOND STATUS để sử dụng khóa "123456" ngay khi khởi động
    set_value_at_address(lines, 0x18DE8, '02')  # 02 là mã hex để '123456'

    with open(output_path, 'w') as f:
        f.writelines(lines)

# Đường dẫn file đầu vào và đầu ra
input_hex_file = 'input_firmware.hex'
output_hex_file = 'output_firmware.hex'

# Thực hiện chỉnh sửa
modify_firmware(input_hex_file, output_hex_file)
