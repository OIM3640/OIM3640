# http://www.pythonchallenge.com/pc/def/map.html


def decrypt(encrypted_message, shift):
    """Return a decrypted message"""
    s = ""

    for old_c in encrypted_message.lower():
        # we should not rotate non-letters
        # how to check whether a char is letter or not
        if old_c.isalpha():
            if old_c < "y":
                new_c = chr(ord(old_c) + shift)
            else:
                new_c = chr(ord(old_c) - (26 - shift))
            # new_c = chr(ord("a") + (ord(old_c) + shift - ord("a")) % 26)
            # print(new_c)
            s += new_c
        else:
            s += old_c

    return s


def main():
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    # print(decrypt(s, 2))
    # What if we don't know the hint (2)
    # for i in range(25):
    #     print(decrypt(s, i))

    url = "map"
    print(decrypt(url, 2))


main()
