import zipfile

with zipfile.ZipFile('sample.zip','r') as zip_data:
    for txt in zip_data:
        i = zip_data.read()
        print(i)
