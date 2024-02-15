import re
def main():
    print(validate(input("IPv4 Address: ")))
def validate(ip):
    leng = ip.split(".")
    if len(leng) != 4:
        return False
    if leng[0] == "0" or leng[0] == "0.":
        return False
    if re.search(r"\b(?:25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b\.\b(0|25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b\.\b(0|25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b\.\b(0|25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b", ip):
        #\.\b(0|25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b\.\b(0|25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b\.\b(0|25[0-5]|2[0-4][0-9]|[1]?[1-9][0-9]?)\b
        return True
    else:
        return False

if __name__ == "__main__":
    main()
