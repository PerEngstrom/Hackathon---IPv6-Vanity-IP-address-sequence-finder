# Hackathon---IPv6-Vanity-IP-address-sequence-finder
python script to take user input of a string (in hex) they would like to find in a given subnet and return the IPv6 value as well as the sequence number of the IPv6 subnet size

Vanity IPv6 addresses are custom IP addresses that include specific, human-readable patterns or sequences within the address. These addresses are designed to be memorable, aesthetically pleasing, or meaningful, making them easier to recognize and recall.

Vanity IPv6 addresses incorporate specific hexadecimal characters or patterns that are visually appealing or have mnemonic value. For example, addresses like ::face: or DEAD:BEEF are used to create recognizable and memorable sequences. These addresses can be used for various purposes, such as identifying specific servers or services, simplifying network management, or adding a fun element to IP addressing.

Practical examples include addresses like ::cafe for guest wifi or ::feed for an RSS syndication feed server.  

Here is an external web page explaining in more detail - https://circleid.com/posts/9049/10864/  "New Trend: Vanity IPv6 Addresses"

The purpose of this tool is for the user to be able to input a text string (according to hexadecimal rules) and a subnet mask and the script will determine what the "position" or "sequence" in the total number of addresses in a given subnet that the text string appears.  This would be useful in Lumen NaaS IoD with BGP where the user is prompted to define the sequence number of the BGP peer or static route next-hop.  The sequence number will determine how the cusotmer configures the WAN IP of their CPE.  Determining sequence number for small subnets (e.g. IPv4 /30, /29, /28 and IPv6 /126, /125) is easy and not likely large enough to contain space for any vanity selection.  However, a /64 option is available in lumen's implementation in order for customers to support auto-discovery capabilities unique to IPv6 services.  A /64 of IPv6 space contains a total of  18,446,744,073,709,551,616 available addresses.  This offers the ability for the customer to choose a sequence number within that range that includes a specific hex-string thus allowing the customer to number their equipment with a COOL IPv6 address. 
