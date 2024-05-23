def GetVersion(self):
    print(222)

cls_dict = {}
cls_dict["version"] = GetVersion
cls_dict["name"] = "Vasya"

new_cls = type("Test", (), cls_dict)

if __name__ == "__main__":
    nc = new_cls()
    nc.version()
    print(nc.name)