# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Protocol Constants

CMD_FIELD_LENGTH = 16  # Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4  # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10 ** LENGTH_FIELD_LENGTH - 1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol

# Protocol Messages
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
    "login_msg": "LOGIN",
    "logout_msg": "LOGOUT"
}  # .. Add more commands if needed

PROTOCOL_SERVER = {
    "login_ok_msg": "LOGIN_OK",
    "login_failed_msg": "ERROR"
}  # ..  Add more commands if needed

# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
    """
    Gets command name and data field and creates a valid protocol message
    Returns: str, or None if error occured
    """
    # Implement code ...
    len_space = 16-len(cmd)
    if len_space < 0:
        return None
    if len(data) > MAX_DATA_LENGTH:
        return  None
    full_msg = cmd + (len_space * " ") + DELIMITER + ("0"*(4-len(str(len(data))))) + str(len(data)) + DELIMITER + data
    return full_msg


def parse_message(data):
    """
    Parses protocol message and returns command name and data field
    Returns: cmd (str), data (str). If some error occured, returns None, None
    """
    split_data = data.split(DELIMITER)
    if len(split_data) < 3:
        return None, None
    try:
        split_data[1] = split_data[1].strip()
        split_data[1] = int(split_data[1])
    except:
        return None, None
    cmd = split_data[0].strip()
    msg = DELIMITER.join(split_data[2:])
    if split_data[1] != len(msg):
        return None, None
    if cmd == "" or "-" in str(split_data[1]):
        return None, None
    return cmd, msg
    # Implement code ...
    # The function should return 2 values




def split_msg(msg, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's delimiter (|) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None
    """
    msg_split = msg.split(DELIMITER)
    if len(msg_split) == expected_fields:
        return msg_split
    else:
        none_list = []
        for i in range(expected_fields):
            none_list.append(None)
        return none_list




# Implement code ...


def join_msg(msg_fields):
    """
    Helper method. Gets a list, joins all of it's fields to one string divided by the delimiter.
    Returns: string that looks like cell1|cell2|cell3
    """
    for i in range(len(msg_fields)):
        msg_fields[i] = str(msg_fields[i])
    join_ms = msg_fields.join(DELIMITER)
    return join_ms




# Implement code ...

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
