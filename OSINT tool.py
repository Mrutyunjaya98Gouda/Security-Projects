import ipwhois
from ipwhois import IPWhois

import socket

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def main():
    domain = input("Enter the domain: ")
    ip_address = get_ip_address(domain)
    if ip_address:
        print(f"The IP address of {domain} is {ip_address}")
        obj = IPWhois(ip_address)

        # Perform the lookup and get the results as a dictionary
        results = obj.lookup_rdap(depth=1)

        #Print some information from the results
        print(f"IP address: {ip_address}")
        print(f"Country: {results['asn_country_code']}")
        print(f"Organization: {results['asn_description']}")
        #print(f"Abuse contact: {results['objects']['GOGL']['contact']['email'][0]['value']}")

    else:
        print(f"Could not resolve the domain {domain}")

if __name__ == "__main__":
    main()