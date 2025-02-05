import re
from ipaddress import IPv4Network


def octet_to_regex(start: int, end: int, strict=False) -> str:
    """
    Generates a regex pattern to match a range of octets in an IPv4 address.

    :param start: Starting value of the octet range (0-255).
    :param end: Ending value of the octet range (0-255).
    :param strict: Whether to strictly match valid octet values (default: False).
    :return: A regex pattern as a string.
    """
    def split_ranges(start, end):
        if start == end:
            return [str(start)]
        str_start, str_end = str(start), str(end)
        if len(str_start) != len(str_end):
            return split_ranges(start, int('9' * len(str_start))) + split_ranges(int('1' + '0' * (len(str_end) - 1)), end)

        common_prefix = ""
        for i in range(len(str_start)):
            if str_start[i] == str_end[i]:
                common_prefix += str_start[i]
            else:
                break

        suffix_start = int(str_start[len(common_prefix):])
        suffix_end = int(str_end[len(common_prefix):])

        if suffix_start == suffix_end:
            return [common_prefix + str(suffix_start)]

        return [f"{common_prefix}[{suffix_start}-{suffix_end}]"]

    if start == end:
        return str(start)

    if end - start == 255:
        return r'(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})' if strict else r'\d+'

    parts = []
    current = start
    while current <= end:
        next_step = min(end, current + 9 - (current % 10))
        parts.extend(split_ranges(current, next_step))
        current = next_step + 1

    return '(' + "|".join(parts) + ')'


def ipv4_to_regex(net: IPv4Network):
    """
    Generates a regex pattern to match any IP address within the given IPv4 network.

    :param net: An IPv4Network object representing the subnet.
    :return: A regex pattern as a string.
    """

    first_ip = net.network_address.packed
    last_ip = net.broadcast_address.packed

    octets_reg = []
    for i in range(4):
        octet_first = first_ip[i]
        octet_last = last_ip[i]

        octets_reg.append(octet_to_regex(octet_first, octet_last, strict=False))

    return '^' + r'\.'.join(octets_reg) + '$'


def test_it(net: IPv4Network) -> list[str]:
    """
    Tests the generated regex pattern against all IP addresses in the given IPv4 network.
    :param net: An IPv4Network object representing the subnet.
    :return: List of ip with errors
    """
    pattern = re.compile(ipv4_to_regex(net))

    errors = []
    for ip in net:
        if not pattern.match(str(ip)):
            errors.append(str(ip))

    return errors



