from urllib.request import urlopen
from datetime import datetime
import re
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pandas")
install("matplotlib")

def go(url):
    print("")
    location = url.find("#")
    print(url[45:location])

    lcv = 0
    trythis = False
    while lcv < 4:
        try:
            page = urlopen(url)
            trythis = True
        except:
            print("failed to open. trying again... {}".format(lcv))
        lcv +=1
    if trythis == False:
        return [0, True]
    page
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    locations = [m.start() for m in re.finditer("stock_table_display", html)]
    rel = html[locations[0]:locations[len(locations)-1]]
    lists = rel.split("stock_table_display")
    total = 0
    plus = ""
    del lists[0]
    del lists[0]
    for x in lists:
        x = x[149:]
        location = x.find("<")
        print(x[:location], end = " ")
        location = x.find("tock'>")
        string_withnum = x[location+6:location+10]
        newstring = ""
        for x in string_withnum:
            if x in "1234567890":
                newstring = newstring + x
        try:
            total = total + int(newstring)
        except:
            pass
        if newstring == "30":
            plus = "+"
        print(newstring)

    print("total = {}".format(total))
    return([total, False])

def update(total):
    if total > 0:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        file_object = open('info.txt', "a")
        a = "{} {}\n".format(str(total),dt_string)
        print(a)
        file_object.write(a)
        file_object.close()
        print(total)
        
    print(total)

    exec(open('graphpython.py').read())
    
urls = []
urls.append("https://www.pbtech.co.nz/product/VGAPOW16715/Powercolor-Red-Devil-AMD-Radeon-RX-6700-XT-Graphic")
urls.append("https://www.pbtech.co.nz/product/VGASAP16715/Sapphire-NITRO-Radeon-RX-6700-XT-Graphics-Card-12G")
urls.append("https://www.pbtech.co.nz/product/VGAASR06712/ASRock-AMD-Radeon-Challenge-Pro-12G-OC-RX-6700-XT")
urls.append("https://www.pbtech.co.nz/product/VGAGBA06710/Gigabyte-Radeon-RX-6700-XT-Gaming-OC-Graphics-Card")
urls.append("https://www.pbtech.co.nz/product/VGAMSI66713/MSI-Gaming-X-RX-6700-XT-Graphics-Card-12GB-GDDR6-P")
urls.append("https://www.pbtech.co.nz/product/VGAASR06711/ASRock-AMD-Radeon-Phantom-Gaming-D-RX-6700-XT-Grap")
urls.append("https://www.pbtech.co.nz/product/VGAAS06715/ASUS-ROG-STRIX-Radeon-RX-6700-XT-OC-Edition-12GB-G")
urls.append("https://www.pbtech.co.nz/product/VGAAS06712/ASUS-TUF-Radeon-RX-6700-XT-Graphics-Card-12GB-GDDR")
urls.append("https://www.pbtech.co.nz/product/VGAMSI66712/MSI-Radeon-RX-6700-XT-Graphics-Card-12GB-GDDR6-PCI")

total = 0
broken = False
for x in urls:
    ans = go(x)
    print(ans)
    broken = broken or ans[1]
    total = total + ans[0]

if not broken:
    update(total)




