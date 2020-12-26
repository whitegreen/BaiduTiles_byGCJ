# BaiduTiles_byGCJ
downloading Baidu map (zoom level 19) by GCJ coordinates

China (e.g. Amap) uses GCJ-02 coordinates, while Baidu has its own BD-09 format. 

```
bdLon, bdLat = calTiles.gcj2bd(118.984728,31.284715)  # input GCJ lon, lat
```
converts  GCJ-02 to BD-09 coordinates. Comment out this line if you already have BD-09 lon & lat.


**baiduTiles.py** download a map (made of 25 tiles) for a given GCJ lon & lat.

![image](final_map18.jpg)

Configure the number of tiles by setting, e.g., dd=3  to obtain a map of 49 tiles. number = (2*dd+1)^2.



**baiduManyTiles2.py** download multiples maps from a list of GCJ coordinates in an excel table.

![image](folder.png)
