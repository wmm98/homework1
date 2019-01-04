def dec2bin8bits(n):
    bin_str = ""
    for i in range(8):
        bin_str = str(n % 2) + bin_str
        n //= 2
    return bin_str

def convert(ip_str):
    ip_result = ""
    ip_subs = ip_str.split('.')
    for i in range(4):
        ip_sub = int(ip_subs[i])
        ip_binary = dec2bin8bits(ip_sub)
        ip_result += ip_binary
    return ip_result

while True:
    ip_str = input().strip()
    if ip_str == "-1":
        break

    print(convert(ip_str))
'''
192.168.0.1
255.255.0.0
1.0.0.1
-1
'''