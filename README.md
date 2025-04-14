Hackathon---IPv6-Vanity-IP-Address-Sequence-Finder
==================================================
Welcome to the world of Vanity IPv6 addresses! Imagine having an IP address that's not just a random jumble of numbers and letters, but something memorable, aesthetically pleasing, or even downright cool. This Python script is here to make that dream a reality.

What Does This Script Do?
=========================
This script takes user input of a string (in hex) that they would like to find in a given subnet and returns the IPv6 value as well as the sequence number of the IPv6 subnet size. Think of it as your personal IP address stylist, making sure your network presence is as fashionable as possible.

What Are Vanity IPv6 Addresses?
===============================
Vanity IPv6 addresses are custom IP addresses that include specific, human-readable patterns or sequences within the address. These addresses are designed to be memorable, aesthetically pleasing, or meaningful, making them easier to recognize and recall. It's like having a personalized license plate for your car, but for your network!

Examples of Vanity IPv6 Addresses
=================================
Vanity IPv6 addresses incorporate specific hexadecimal characters or patterns that are visually appealing or have mnemonic value. For example, addresses like ::face: or DEAD:BEEF are used to create recognizable and memorable sequences. These addresses can be used for various purposes, such as identifying specific servers or services, simplifying network management, or adding a fun element to IP addressing.

Practical examples include addresses like ::cafe for guest Wi-Fi or ::feed for an RSS syndication feed server. Imagine telling your guests to connect to ::cafe—they'll think you're the coolest host ever!

Why Use This Tool?
==================
The purpose of this tool is for the user to input a text string (according to hexadecimal rules) and a subnet mask, and the script will determine what the "position" or "sequence" in the total number of addresses in a given subnet that the text string appears. This would be useful in Lumen NaaS IoD with BGP where the user is prompted to define the sequence number of the BGP peer or static route next-hop. The sequence number will determine how the customer configures the WAN IP of their CPE.

Determining sequence numbers for small subnets (e.g., IPv4 /30, /29, /28 and IPv6 /126, /125) is easy and not likely large enough to contain space for any vanity selection. However, a /64 option is available in Lumen's implementation to support auto-discovery capabilities unique to IPv6 services. A /64 of IPv6 space contains a total of 18,446,744,073,709,551,616 available addresses. This offers the ability for the customer to choose a sequence number within that range that includes a specific hex-string, thus allowing the customer to number their equipment with a COOL IPv6 address.
