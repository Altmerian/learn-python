import zipfile

with zipfile.ZipFile("zip/test.zip", "w", zipfile.ZIP_BZIP2) as f:
    f.write("zip/Python.png", "Python.png")
    f.write("zip/ZipLogo.png", "ZipLogo.png")
