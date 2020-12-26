import os
import pandas as pd
import requests
import urllib
from PIL import Image
import random
from heiSci import calTiles

def getimg(Tpath, x, y):
    try:
        req = urllib.request.Request(Tpath)
        req.add_header('User-Agent', random.choice(calTiles.agent_list))
        pic = urllib.request.urlopen(req, timeout=60)   #timeout=60
        myImage= Image.open(pic)
        print( '_',end="")
        return myImage
    except Exception:
        print('*', end="")
        return None

def myDownload(x_range, y_range, place_id):
    toImage = Image.new('RGB', (256 * (x_range[1] + 1 - x_range[0]), 256 * (y_range[1] + 1 - y_range[0])))
    print(place_id, end="")
    fail_count = 0
    for y in range(y_range[0],y_range[1]+1):
        for x in range(x_range[0],x_range[1]+1):
            tilepath ="http://shangetu1.map.bdimg.com/it/u=x={x};y={y};z={z};v=009;type=sate&fm=46".format(x=x, y=y, z=z, udt=udt, ak=ak, style=style)
            pic=getimg(tilepath,  x, y)
            if None is pic:
                fail_count +=1
            else:
                toImage.paste(pic,  ((x - x_range[0]) * 256, (y_range[1] - y) * 256  ))
    toImage.save(save_dir + "final_map" + str(place_id) + ".jpg")
    return 0<fail_count


save_dir = "C:\\Users\\Hua\\Desktop\\amapData\\zj6\\"
# ak = "8d6c8b8f3749aed6b1aff3aad6f40e37"
# ak = "ZAFbYKUGwx8lwAQVm5KS8dYm5urzRzPj"  #hua
ak = "vRwOWhE1MrLUEynioFxvfSUh4nUtSwu5"  #hua2
style = "t%3Abuilding%7Ce%3Aall%7Cv%3Aon%7Cc%3A%23ff0000ff%2Ct%3Apoi%7Ce%3Aall%7Cv%3Aoff%2Ct%3Aroad%7Ce%3Al%7Cv%3Aoff%2Ct%3Aroad%7Ce%3Ag%7Cv%3Aon%7Cc%3A%23ff00ffff%2Ct%3Aall%7Ce%3Al%7Cv%3Aoff%2Ct%3Agreen%7Ce%3Ag%7Cc%3A%2346b316ff%2Ct%3Awater%7Ce%3Ag%7Cc%3A%230000ffff"
z = 19
udt = 20200418
dd = 2
file=os.path.abspath("C:/Users/Hua/Desktop/amapData/POI镇江GCJ.xlsx")
df= pd.read_excel(file)
fail_ids = [i for i in range(6500, 7000)]
while 0 < len (fail_ids):
    print( fail_ids)
    new_list=[]
    for i in fail_ids:
        ss = df.iloc[i, 2]
        arr = ss.split(',')
        bdLon, bdLat = calTiles.gcj2bd(float(arr[0]), float(arr[1]))  # input GCJ lon, lat
        xx, yy = calTiles.bdlonlat_tiles(bdLon, bdLat, z)  # BD-0 lan lat
        x_range = [xx - dd, xx + dd]
        y_range = [yy - dd, yy + dd]
        fail=myDownload(x_range, y_range, i)
        print(df.iloc[i, 1])
        if fail:
            new_list.append(i)
    fail_ids = new_list






