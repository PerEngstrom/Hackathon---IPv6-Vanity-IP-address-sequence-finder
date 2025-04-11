import ipaddress

def predict_last_ipv6_match(subnet, search_string):
    """
    Predict the last IPv6 address in a subnet containing a specific string.

    Args:
        subnet (str): The IPv6 subnet in CIDR notation (e.g., "2001:db8::/64").
        search_string (str): The string to search for in the IPv6 addresses, in hexadecimal.

    Returns:
        dict: A dictionary containing the last matching IPv6 address in both
              compressed and expanded formats, and its sequence number.
    """
    try:
        # Parse the subnet
        network = ipaddress.IPv6Network(subnet, strict=False)
    except ValueError as e:
        raise ValueError(f"Invalid IPv6 subnet: {e}")

    # Ensure the search string is valid hexadecimal
    try:
        int(search_string, 16)
    except ValueError:
        raise ValueError("Search string must be a valid hexadecimal value.")

    # The total number of addresses in the subnet (host portion)
    total_addresses = network.num_addresses  # Number of addresses in the subnet

    # Convert the network address to an integer
    network_prefix = int(network.network_address)

    # Find the highest position in the host portion where the string can appear
    host_bits = network.max_prefixlen - network.prefixlen  # Number of bits in the host portion
    max_host_value = (1 << host_bits) - 1  # Maximum value for the host portion

    # Convert the search string to an integer
    search_value = int(search_string, 16)
    search_length_bits = len(search_string) * 4  # Each hex digit is 4 bits

    # Embed the search string at the highest position in the host portion
    # Fill remaining bits (before and after the search string) with the maximum value
    host_value = (max_host_value & (~((1 << (host_bits - search_length_bits)) - 1))) | search_value

    # Ensure the calculated host value is within the valid range
    if host_value > max_host_value:
         return None

    # Combine the network prefix with the host value to create the full address
    full_address = network_prefix + host_value

    # Convert the full address back to an IPv6 address object
    ipv6_address = ipaddress.IPv6Address(full_address)

    # Calculate the sequence number (relative to the subnet size)
    sequence_number = full_address - network_prefix

    # Return the results
    return {
        "compressed": str(ipv6_address),
        "expanded": ipv6_address.exploded,
        "sequence_number": sequence_number
    }

if __name__ == "__main__":
    print("IPv6 Finder - Predict the last IPv6 address containing a specific string in a subnet.")

    # Get user input
    user_subnet = input("Enter the IPv6 subnet (e.g., '2001:db8::/64'): ").strip()
    search_text = input("Enter the text string to search for (e.g., 'faceb00c'): ").strip()

    try:
        # Predict the last matching address
        result = predict_last_ipv6_match(user_subnet, search_text)

        if result:
            print("\nResults:")
            print(f"Last matching IPv6 address (compressed): {result['compressed']}")
            print(f"Last matching IPv6 address (expanded): {result['expanded']}")
            print(f"Sequence number within the subnet: {result['sequence_number']}")
        else:
            print(f"No valid IPv6 address containing '{search_text}' could be found in the subnet {user_subnet}.")
    except ValueError as error:
        print(f"Error: {error}")

