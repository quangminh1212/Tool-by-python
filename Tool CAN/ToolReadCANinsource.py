import cantools

# Define the path to your DBC file
dbc_path = 'C:\VF\V7L.dbc'

# Load the DBC file
db = cantools.database.load_file(dbc_path)

# Define your CAN messages
can_messages = [
    "0x00000303 1f 00 00 00 10 00 00 01",
    "0x00000303 10 00 00 00 10 00 00 01",
    "0x00000110	30 00 00 00 00 00", 
    "0x00000110	30 00 00 00 00 00", 
    "0x00000110	30 00 00 01 00 00", 
    "0x00000110	30 00 00 01 00 00", 
    "0x00000303	17 00 00 00 10 00 00 01", 
    "0x00000110	30 00 00 01 00 00", 
    "0x00000303	18 00 00 00 10 00 00 01", 
    "0x00000110	30 00 00 01 00 00"
]

# Function to decode CAN messages
def decode_can_messages(messages, database):
    decoded_messages = []
    for message in messages:
        parts = message.split()  # Tách thông điệp bằng khoảng trắng
        message_id = parts[0]  # Phần đầu tiên là ID thông điệp
        data = ' '.join(parts[1:])  # Phần còn lại là dữ liệu
        message_id = int(message_id, 16)  # Chuyển đổi hex sang int
        data = bytes.fromhex(data.replace(' ', ''))  # Loại bỏ khoảng trắng và chuyển đổi dữ liệu sang bytes
        decoded = database.decode_message(message_id, data)
        decoded_messages.append((message, decoded))  # Lưu cả thông điệp gốc và thông điệp đã giải mã
    return decoded_messages
# Decode and print the messages
decoded_messages = decode_can_messages(can_messages, db)
for raw_message, decoded in decoded_messages:
    print(f"Raw message: {raw_message}\nDecoded: {decoded}\n")

# Đầu tiên, bạn cần cài đặt thư viện cantools vào môi trường làm việc của bạn. Bạn có thể làm điều này bằng câu lệnh sau:

# pip install cantools
# Sau khi đã cài đặt thư viện, hãy làm theo các bước sau:

# Lưu đoạn mã Python trên vào một tệp tin với tên, ví dụ: decode_can.py.
# Thay đổi đường dẫn tới tệp tin DBC trong biến dbc_path trong đoạn mã để phản ánh đường dẫn chính xác đến tệp tin DBC của bạn.
# Chạy đoạn mã Python này trong môi trường của bạn. Đoạn mã sẽ tải tệp tin DBC và sử dụng nó để giải mã các bản tin CAN mà bạn cung cấp.
# Đoạn mã có các chức năng sau:

# cantools.database.load_file(dbc_path): Tải và phân tích cú pháp tệp tin DBC.
# decode_can_messages(can_messages, db): Hàm này nhận vào danh sách các bản tin CAN và database được tải từ tệp tin DBC, sau đó giải mã mỗi bản tin và trả về kết quả đã giải mã.
# Đối với các bản tin CAN của bạn, hãy chắc chắn rằng chúng được định dạng đúng và thêm vào danh sách can_messages. Đoạn mã sẽ chạy và in ra kết quả đã giải mã cho mỗi bản tin CAN.


    # cd đến file chứa tệp chương trình
    # python -m venv cantools_env
    # cantools_env\Scripts\activate
    # pip install cantools
    # py .\ToolReadCANinsource.py
