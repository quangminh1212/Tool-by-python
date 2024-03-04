import cantools

# Load the DBC file using cantools
def load_dbc(dbc_file_path):
    dbc = cantools.database.load_file(dbc_file_path)
    return dbc

# Analyze a single CAN log entry
def analyze_log_entry(entry, dbc):
    try:
        can_id = int(entry['ID'], 16)  # Convert ID from hex to int
    except ValueError as e:
        print(f"\nError converting CAN ID to int: {e}\n")
        return None
    
    # Find the corresponding message in the DBC file
    try:
        message = dbc.get_message_by_frame_id(can_id)
    except KeyError as e:
        print(f"\nMessage ID {can_id} not found in DBC: {e}\n")
        return None
    
    # Decode the message data
    data = bytes.fromhex(entry['Data'])
    decoded = message.decode(data)
    return decoded

# Parse the CAN log file and analyze each entry
def parse_and_analyze_can_log(log_file_path, dbc):
    with open(log_file_path, 'r') as file:
        log_entries = file.readlines()
    # Skip header lines
    header_prefixes = ['#', 'Timestamp']
    log_entries = [line.strip() for line in log_entries if not line.startswith(tuple(header_prefixes))]
    
    for line in log_entries:
        parts = line.split(';')
        if len(parts) >= 3:  # Make sure the line has enough parts
            entry = {'Timestamp': parts[0], 'Type': parts[1], 'ID': parts[2], 'Data': parts[3]}
            analysis_result = analyze_log_entry(entry, dbc)
            if analysis_result is not None:
                print(f"\nDecoded data for ID {entry['ID']}: {analysis_result}\n")
            else:
                print(f"\nFailed to decode data for ID {entry['ID']}\n")
        else:
            print("\nInvalid log entry:\n", line)

if __name__ == "__main__":
    log_file_path = input("Enter the path to the CAN log file:")
    dbc_file_path = input("Enter the path to the DBC file:")

    dbc = load_dbc(dbc_file_path)
    parse_and_analyze_can_log(log_file_path, dbc)


# Hướng dẫn sử dụng Tool Phân Tích Log CAN
# Tool Phân Tích Log CAN được thiết kế để giải mã dữ liệu log CAN sử dụng định nghĩa từ file DBC. Dưới đây là hướng dẫn chi tiết cách sử dụng tool này.

# *Yêu Cầu Hệ Thống
# Để sử dụng tool, máy tính của bạn cần phải cài đặt Python và thư viện cantools. Cài đặt Python có thể tải về từ python.org và cantools có thể được cài đặt thông qua pip bằng lệnh sau:

# pip install cantools

# *Chuẩn Bị Files
# + File Log CAN: File log chứa dữ liệu của các gói tin CAN bạn muốn phân tích.
# + File DBC: File DBC chứa định nghĩa của các gói tin và signal.
# Đảm bảo rằng bạn biết đường dẫn chính xác đến hai file này trên hệ thống của bạn.

# *Sử Dụng Tool
# Mở Visual Studio Code: Mở ứng dụng Visual Studio Code trên máy tính của bạn.
# Mở Terminal: Mở terminal trong Visual Studio Code bằng cách nhấn Ctrl+`` (hoặc Cmd+`` trên macOS).

# *Chạy Script:
# + Điều hướng đến thư mục chứa script của bạn bằng cách sử dụng lệnh cd:

# cd path_to_your_script_folder (vd : PS C:\Users\quangbm> cd C:\Users\quangbm\Downloads)

# + Chạy script bằng cách nhập lệnh sau vào terminal:

# python toolCAN.py

# + Khi script yêu cầu, nhập đường dẫn đầy đủ đến file log CAN và file DBC khi được yêu cầu:

# Enter the path to the CAN log file: C:\path\to\your\log_file.txt
# Enter the path to the DBC file: C:\path\to\your\dbc_file.dbc

# + ví dụ :
# Enter the path to the CAN log file: C:\Users\quangbm\Downloads\1.txt
# Enter the path to the DBC file: C:\Users\quangbm\Downloads\V7_CAN DB_LFP_2021110

# + Xem Kết Quả: Các thông tin giải mã từ log file sẽ được hiển thị trên terminal. Nếu có lỗi trong quá trình xử lý, tool sẽ thông báo lỗi cụ thể để bạn có thể xác định và giải quyết vấn đề.

# Lưu Ý
# + File log và file DBC cần phải ở định dạng hợp lệ để tool có thể đọc và phân tích chính xác.
# + Đường dẫn đến file cần phải chính xác và không chứa ký tự đặc biệt nào gây ra lỗi đường dẫn.

# Troubleshooting
# + Lỗi File Not Found: Nếu bạn nhận được thông báo lỗi rằng file không tồn tại, hãy kiểm tra lại đường dẫn và định dạng file.
# + Lỗi khi chuyển đổi CAN ID sang số nguyên: Đảm bảo ID trong file log của bạn là hexa hợp lệ.
# + Lỗi Message ID not found in DBC: Kiểm tra xem file DBC của bạn có chứa định nghĩa cho ID tương ứng hay không.
# Nếu bạn gặp bất kỳ vấn đề nào khác khi sử dụng tool, hãy kiểm tra mã nguồn hoặc tìm kiếm sự trợ giúp từ cộng đồng phát triển Python hoặc các diễn đàn liên quan đến CAN và DBC.

# File LOG đầu vào yêu cầu có dạng

# # Logger type: CL2000
# # HW rev: 8.1x
# # FW rev: 5.85
# # Logger ID: id0001
# # Session No.: 29
# # Split No.: 4
# # Time: 20231005T071031
# # Value separator: ";"
# # Time format: 4
# # Time separator: ""
# # Time separator ms: ""
# # Date separator: ""
# # Time and date separator: "T"
# # Bit-rate: 250000
# # Silent mode: false
# # Cyclic mode: false
# Timestamp;Type;ID;Data
# 05T071031805;0;326;0000000000000100
# 05T071031810;0;102;1010000007000000
# 05T071031820;0;313;8228824682468246
# 05T071031840;0;314;823c82468246823c
# 05T071031855;0;133;432550bde6169ca1
# 05T071031860;0;31a;8232823c823c8232
# 05T071031870;0;10e;2422100000c20001
# 05T071031881;0;300;0352e20a04f7d45f

# KẾT QUẢ TRẢ VỀ SẼ CÓ DẠNG
# Decoded data for ID 326: {'bms_statustrust_bms1charger': 'READY', 'bms_statustrust_bms0clttrust_bms1charger': 'READY', 'bms_resulttrust_bms0charger': 'READY', 'bms_resulttrust_atustrust_bms0cbox': 'READY', 'bms_statustrust_bms3cbox': 'READY', 'bms_statustrust_bms2ms3cbox': 'READY', 'bms_resulttrust_bms2cbox': 'READY'}


# Decoded data for ID 102: {'vcu_evstatus': 1, 'vcu_drivingmode': 0, 'vcu_sidestandsignal'ck_status': 0, 'vcu_current_state': 7, 'vcu_input_sw_luglight': 0, 'vcu_input_sw_mkey': 


# Decoded data for ID 313: {'bms_statusVoltageCell09': 3.3320000000000003, 'bms_statusVolt


# Decoded data for ID 314: {'bms_statusVoltageCell13': 3.334, 'bms_statusVoltageCell14': 3


# Decoded data for ID 133: {'vcu_sync_time_data': 4838362151218748577}


# Decoded data for ID 31a: {'bms_statusVoltageCell17': 3.333, 'bms_statusVoltageCell18': 3

# atus_PositionLamp': 0, 'Vcu_Status_WakeABS': 0, 'Vcu_Status_Horn': 0, 'Vcu_Status_Battery': 0, 'Vcu_Status_LuggLamp': 0, 'Vcu_Status_Steering': 0, 'vcu_sys_status_res2': 0, 'Vcu_Status_OptigaTrust': 0, 'Vcu_Status_Can1': 0, 'Vcu_Status_Can0': 0, 'Vcu_Status_UsbCharger': 0, 'Vcu_Status_LeftLamp': 0, 'Vcu_Status_Saddle': 0, 'Vcu_PinProtectStatus': 3, 'Vcu_AdcPin': 2, 'Vcu_AdcValue': 1}    


# Decoded data for ID 300: {'bms_controlSysMaxChgCurrent': 17.0, 'bms_controlSysMaxDsgCurrent': -153.4, 'bms_controlSysMaxChgPower': 1271, 'bms_controlSysMaxDsgPower': -11169}

