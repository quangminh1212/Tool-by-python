# Giá trị mới cần ghi vào địa chỉ 0x18DF0, thay thế b'YOUR_BYTES_HERE' với giá trị mới của bạn
new_value = b'YOUR_BYTES_HERE'

# Mở file ở chế độ đọc và ghi nhị phân
with open(file_path, 'rb+') as file:
    # Di chuyển đến địa chỉ cần sửa đổi
    file.seek(0x18DF0)
    
    # Ghi thay đổi vào địa chỉ đó
    file.write(new_value)

print("Sửa đổi file hex thành công!")