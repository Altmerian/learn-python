from zipfile import ZipFile

with ZipFile("zip/test.zip", "r") as f:
    f.extractall("zip/extracted")
