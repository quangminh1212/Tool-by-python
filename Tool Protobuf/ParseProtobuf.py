from google.protobuf.json_format import MessageToJson
import telemetry_pb2  # Thay thế bằng tên file Python được tạo từ .proto

def protobuf_to_json(raw_protobuf_file, output_json_file, proto_message):
    # Đọc tin nhắn protobuf
    with open(raw_protobuf_file, 'rb') as file:
        message = proto_message()
        message.ParseFromString(file.read())

    # Chuyển đổi sang JSON
    json_data = MessageToJson(message)

    # Ghi vào file JSON
    with open(output_json_file, 'w') as json_file:
        json_file.write(json_data)

# Sử dụng
protobuf_to_json('your_raw_file.raw', 'output.json', telemetry_pb2.py)  # Thay thế YourMessage bằng lớp tin nhắn thực tế của bạn
