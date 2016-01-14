from hazelcast.serialization.bits import *
from hazelcast.protocol.client_message import ClientMessage
from hazelcast.protocol.custom_codec import *
from hazelcast.protocol.codec.atomic_reference_message_type import *

REQUEST_TYPE = ATOMICREFERENCE_SET
RESPONSE_TYPE = 100
RETRYABLE = False


def calculate_size(name, new_value):
    """ Calculates the request payload size"""
    data_size = 0
    data_size += calculate_size_str(name)
    data_size += BOOLEAN_SIZE_IN_BYTES
    if new_value is not None:
        data_size += calculate_size_data(new_value)
    return data_size


def encode_request(name, new_value):
    """ Encode request into client_message"""
    client_message = ClientMessage(payload_size=calculate_size(name, new_value))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(name)
    client_message.append_bool(new_value is None)
    if new_value is not None:
        client_message.append_data(new_value)
    client_message.update_frame_length()
    return client_message


# Empty decode_response(client_message), this message has no parameters to decode


