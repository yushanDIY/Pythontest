
import random


def getadd(a, b):
    d = a+b
    e = a-b
    return d, e


j, k = getadd(7, 8)
print("j=%d", j)
print("k=%d", k)


# strb = "nihaoganmna"

# for item in strb:
#     print(item, end="")
# print("")
# print(strb[2:3])
# print(strb[-1:-3:-1])


# print(strb.find("hao"))

# print(strb.replace("n", "da", -1))


# test = FTP()
# test.connect("182.92.66.170", port=21)
# test.login(user="admintbt", passwd="Zlxytbt")
# test.encoding = "utf-8"
# print(test.getwelcome())

# print(test.dir())

# for (name, entry) in test.mlsd(path="/", ):
#     print(name+"__"+entry["type"]+"__"+entry["modify"]+"__"+entry["size"])

# for (name, empty) in test.mlsd():
#     print(name)
# # for (dirname, subdirs, files) in aftp.walk("/"):
# #     print(dirname + ";".join(files) + "__" + ";;;;".join(subdirs))
# #     print("\r\n")


# for (name, entry) in aftp.mlsd():
#     print(name)
