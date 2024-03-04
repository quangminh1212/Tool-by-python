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
def parse_and_analyze_can_log(can_messages, dbc):
    # Skip header lines if present in the list, based on our predefined header structure
    header_prefixes = ['#', 'Timestamp']
    log_entries = [msg for msg in can_messages if not msg.startswith(tuple(header_prefixes))]

    for line in log_entries:
        parts = line.split(';')
        if len(parts) >= 4:  # Make sure the line has enough parts
            entry = {'Timestamp': parts[0], 'Type': parts[1], 'ID': parts[2], 'Data': parts[3]}
            analysis_result = analyze_log_entry(entry, dbc)
            if analysis_result is not None:
                print(f"\nDecoded data for ID {entry['ID']}: {analysis_result}\n")
            else:
                print(f"\nFailed to decode data for ID {entry['ID']}\n")
        else:
            print("\nInvalid log entry:\n", line)

if __name__ == "__main__":
    dbc_file_path = input("Enter the path to the DBC file: ")
    dbc = load_dbc(dbc_file_path)

    # User inputs list of CAN messages
    can_messages = []  # Initialize empty list to hold CAN messages
    print("Enter CAN messages (type 'done' when finished):")
    while True:
        line = input()
        if line == 'done':
            break
        can_messages.append(line)
    
    # Process the list of CAN messages
    parse_and_analyze_can_log(can_messages, dbc)


#C:\Users\quangbm\Downloads\V7_CAN DB_LFP_20211105.dbc