import discord
from discord.ext import tasks
import os
import json
import aiohttp
import asyncio
import io
import random
import re
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from databases import Database
import tweepy

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.json_dir = "./new_json/"
        self.phoenix = [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        ,[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253]
        ,[1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1791, 1792, 1793, 1794, 1795, 1796, 1797, 1798, 1799, 1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364,2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436, 2437, 2438, 2439, 2440, 2441, 2442, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474, 2475, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2483, 2484, 2485, 2486, 2487, 2488, 2489, 2490, 2491, 2492, 2493, 2494, 2495, 2496, 2497, 2498, 2499, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2510, 2511, 2512, 2513, 2514, 2515, 2516, 2517, 2518, 2519, 2520, 2521, 2522, 2523, 2524, 2525, 2526, 2527, 2528, 2529, 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598, 2599, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2617, 2618, 2619, 2620, 2621, 2622, 2623]]
        self.unique_alphas = [100, 135, 152, 176, 219, 256, 263, 296, 314, 365, 371, 447, 460, 578, 602, 615, 652, 754, 780, 786, 814, 827, 923, 935, 951, 975, 983]
        self.occurrences = {'common': {1: {'06': 399, '05': 339, '0e': 399, '02': 380, '04': 360, '03': 378, '08': 409, '07': 378, '01': 394, '0c': 390, '0a': 396, '0b': 389, '09': 379, '0d': 380}, 2: {'03': 710, '01': 758, '02': 720}, 3: {'04': 539, '08': 529, '01': 520, '02': 487, '06': 555, '03': 551, '07': 548, '05': 495}, 4: {'02': 762, '01': 754}, 5: {'07': 524, '03': 522, '05': 514, '01': 551, '02': 520, '08': 530, '06': 575, '04': 482}}, 'a1': 396, 'e3': 376, '94': 763, 'e1': 306, 'b2': 543, '13': 658, 'd2': 689, 'd3': 525, '44': 548, '61': 496, '34': 390, '31': 209, '14': 999, '21': 530, 'c2': 327, 'b3': 378, '41': 337, '42': 10, '43': 10, '45': 423, 'd1': 426, '32': 353, '93': 560, '64': 921, '85': 613, 'd4': 770, '15': 656, '62': 896, '63': 615, 'a5': 532, 'e4': 481, '65': 624, '54': 416, '92': 725, 'a3': 515, '22': 902, '23': 653, '84': 940, '24': 935, '35': 258, '55': 269, '91': 400, '12': 851, 'a4': 
                743, 'd5': 562, '83': 662, 'a2': 722, '25': 671, '82': 907, '95': 537, 'c3': 275, 'b4': 573, 'b1': 288, 'e2': 519, '53': 270, 'c1': 5, 'c4': 5, 'c5': 255, '81': 508, '33': 279, '52': 368, 'e5': 374, '11': 509, '51': 220, 'b5': 8}
        
        self.founder_rand = 12403320775077705976
        self.alpha_rand   = 10566023106710594524
        self.og_rand      = 8449680988540440215

        self.db_name = 'sqlite:///wen.db'

        self.consumer_key = os.environ['consumer_key']
        self.consumer_secret = os.environ['consumer_secret']
        self.access_token = os.environ['access_token']
        self.access_token_secret = os.environ['access_token_secret']
        
        self.posted_events = []

        self.latest_holders = 0
        self.latest_floor= {"cost": -1}

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.tweepy = tweepy.API(self.auth)

        self.os_key = os.environ['oskey']
        self.contract = '0x97ca7fe0b0288f5eb85f386fed876618fb9b8ab8'
    
    async def is_valid_card(self, card_number):
        if card_number.isdigit():
            if int(card_number) >= 0 and int(card_number) < 10000:
                return True
        return False

    async def get_card_type(self, card_number):
        card_number = int(card_number)
        if card_number < 10:
            card_type = 'creator'
        elif card_number < 100:
            card_type = 'og'
        elif card_number < 1000:
            card_type = 'alpha'
        else:
            card_type = 'founder'
        return card_type

    async def get_unique_alpha_status(self, card_number):
        card_number = int(card_number)
        if card_number in self.unique_alphas:
            return "None"
        else:
            with open(os.path.join(self.json_dir, str(card_number) + '.json')) as originalCardFile:
                data = json.load(originalCardFile)
                title = data['title']
                artist = data['artist']
            card_list = []
            for filename in os.listdir(self.json_dir):
                search_cardno = filename[:-5]
                if int(search_cardno) >= 100 and int(search_cardno) < 1000 and int(search_cardno) != int(card_number):
                    with open(os.path.join(self.json_dir, search_cardno + '.json')) as cardSearchFile:
                        data = json.load(cardSearchFile)
                        search_title = data['title']
                        search_artist = data['artist']
                        if title == search_title and artist == search_artist:
                            card_list.append(search_cardno)
            card_list.sort(key=int)
            return card_list

    async def get_phoenix_status(self, card_number, card_type):
        card_number = int(card_number)
        if card_type == 'founder':
            if card_number in self.phoenix[2]:
                return True
        if card_type == 'alpha':
            if card_number in self.phoenix[1]:
                return True
        if card_type == 'og':
            if card_number in self.phoenix[0]:
                return True
        return False
    
    async def create_layer_image(self, card_number):
        card_img_size = (668, 900)
        font = ImageFont.truetype('./Poppins-Regular.ttf', 48)
        bg_color = (19, 21, 26)
        txt_fill = (255, 255, 255)
        layer_location = ((735, 35), (1435, 35), (35, 1115), (735, 1115), (1435, 1115))

        url = 'https://heroku.ether.cards/card/{}/{}.json'.format(int(card_number) % 100, int(card_number))
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                data = await res.json()
                layer_artist = data['layer_artists']
                layer_url = data['layer_image']

            bg_img = Image.new('RGB', (2144, 2160), color = bg_color)
            img_w, img_h = bg_img.size

            async with session.get(layer_url) as resp:
                buffer = io.BytesIO(await resp.read())

            layer_img = Image.open(buffer)
            layer_img.thumbnail(card_img_size, Image.ANTIALIAS)
            layer_img_w, layer_img_h = layer_img.size
            bg_img.paste(layer_img, (35, 35))

            text = f"ID: {card_number} Artist: Various\nTitle: Accidental Collab"
            d = ImageDraw.Draw(bg_img)
            w, h = d.textsize(text, font=font)
            d.multiline_text((35 + (layer_img_w-w)/2, 900 + 145-h), text, font=font, fill=txt_fill, align='center')

            file_name = layer_url.split('/')[-1][:-4]
            layer_list = list(map(''.join, zip(*[iter(file_name)]*2))) #splits file name into equal parts to get layer code

            for i in range(0, len(layer_list)):
                if layer_list[i].startswith('0') != True:
                    fp = f'./layer_images/{layer_list[i]}.png'
                    layer_occurrences = self.occurrences[layer_list[i]]
                else:
                    fp = f'./layer_images/common_layers/{i+1}/{layer_list[i]}.png'
                    layer_occurrences = self.occurrences['common'][i+1][layer_list[i]]

                layer = Image.open(fp)
                layer.thumbnail(card_img_size, Image.ANTIALIAS)
                bg_img.paste(layer, layer_location[i], layer.convert('RGBA'))

                text = f"{layer_artist[i].capitalize()}\nOccurrences: {layer_occurrences}({round((layer_occurrences/9999)*100, 2)}%)"
                d = ImageDraw.Draw(bg_img)
                w, h = d.textsize(text, font=font)
                if i > 1:
                    d.multiline_text((layer_location[i][0] + (layer_img_w-w)/2, 2125-h), text, font=font, fill=txt_fill, align='center')
                else:
                    d.multiline_text((layer_location[i][0] + (layer_img_w-w)/2, 1045-h), text, font=font, fill=txt_fill, align='center')

            bg_img.save('./LayerSummary.jpg')
            return('./LayerSummary.jpg')

    async def create_summary(self, card_number, card_type, include_alpha_uniques=True):
        card_img_size = (668, 900)
        font = ImageFont.truetype('./Poppins-Regular.ttf', 48)
        bg_color = (19, 21, 26)
        txt_fill = (255, 255, 255)
        double_width = True

        url = 'https://heroku.ether.cards/card/{}/{}.json'.format(int(card_number) % 100, int(card_number))
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                data = await res.json()
                layer_artist = data['layer_artists']
                layer_url = data['layer_image']
                title = data['title']
                artist = data['artist']
                image_url = data['image']

            if layer_url == image_url:
                double_width = False

            if double_width:
                if card_type != "creator":
                    bg_img = Image.new('RGB', (2399, 1080), color = bg_color)
                else:
                    bg_img = Image.new('RGB', (1920, 1080), color = bg_color)
                img_w, img_h = bg_img.size
                async with session.get(image_url) as resp:
                    buffer = io.BytesIO(await resp.read())
                img = Image.open(buffer)
                img.thumbnail(card_img_size, Image.ANTIALIAS)
                img_w, img_h = img.size
                bg_img.paste(img, (35, 35))
                text = "Artist: {}\nTitle: {}".format(artist, title)
                d = ImageDraw.Draw(bg_img)
                w, h = d.textsize(text, font=font)
                d.multiline_text(((img_w-w)/2+35, 900 + 145-h), text, font=font, fill=txt_fill, align='center')
            else: 
                if card_type != "creator":
                    bg_img = Image.new('RGB', (1696, 1080), color = bg_color)
                else:
                    bg_img = Image.new('RGB', (1217, 1080), color = bg_color)

            async with session.get(layer_url) as resp:
                buffer = io.BytesIO(await resp.read())
            layer_img = Image.open(buffer)
            layer_img.thumbnail(card_img_size, Image.ANTIALIAS)
            layer_img_w, layer_img_h = layer_img.size
            if double_width:
                bg_img.paste(layer_img, (735, 35))
            else:
                bg_img.paste(layer_img, (35, 35))

            text = "Artist: Various\nTitle: Accidental Collab"
            d = ImageDraw.Draw(bg_img)
            w, h = d.textsize(text, font=font)
            if double_width:
                d.multiline_text((735 + (layer_img_w-w)/2, 900 + 145-h), text, font=font, fill=txt_fill, align='center')
            else:
                d.multiline_text((35 + (layer_img_w-w)/2, 900 + 145-h), text, font=font, fill=txt_fill, align='center')

            font = ImageFont.truetype('./Poppins-Regular.ttf', 42)

            phoenix_status = await self.get_phoenix_status(card_number, card_type)
            text = "Type: {} ID: {}\n\nPhoenix: {}\n\nLayer Artists:\n{}".format(card_type, card_number, phoenix_status, '\n'.join(layer_artist))
            last_price = await self.get_last_sale(card_number)
            current_price = await self.get_current_price(card_number)
            if last_price != False:
                text +="\n\nLast sold for: {}ETH".format(round(last_price[0], 2))
            if current_price != False:
                text +="\n\nCurrent price: {}ETH".format(round(current_price, 2))
            if card_type == 'alpha':
                if include_alpha_uniques:
                    dupes = await self.get_unique_alpha_status(card_number)
                    if dupes != 'None':
                        for i in range(1, len(dupes), 3):
                            dupes[i] = dupes[i] + '\n'
                        for i in range(0, len(dupes), 1):
                            dupes[i] = dupes[i] + ' '
                        dupes = ''.join(dupes)
                    text += "\n\nOthers in set: {}".format(dupes)
            
            d = ImageDraw.Draw(bg_img)
            w, h = d.textsize(text, font=font)
            if double_width:
                d.multiline_text((1663 - w/2, 1080/2 - h/2), text, font=font, fill=txt_fill, align='center')
            else:
                d.multiline_text((960 - w/2, 1080/2 - h/2), text, font=font, fill=txt_fill, align='center')

            if card_type != "creator":
                trait_font = ImageFont.truetype('./Poppins-Regular.ttf', 36)
                traits_dict = {}
                traits = await self.get_card_data(card_number, 'traits')
                if len(traits) != 0:
                    for item in traits:
                        if item['name'] not in traits_dict:
                            traits_dict.update({item['name']: 1})
                        else:
                            traits_dict[item['name']] += 1
                else:
                    traits_dict = "None"        
                
                traits = "Traits: \n\n"
                for trait in traits_dict:
                    if traits_dict[trait] != 1:
                        traits += f"{trait} x {traits_dict[trait]}\n"
                    else:
                        traits += f"{trait}\n"
                w, h = d.textsize(traits, font=font)
                if double_width:
                    d.multiline_text((2142 - w/2, 1080/2 - h/2), traits, font=trait_font, fill=txt_fill, align='center')
                else:
                    d.multiline_text((1439 - w/2, 1080/2 - h/2), traits, font=trait_font, fill=txt_fill, align='center')            

            bg_img.save('./CardSummary.jpg')
            return './CardSummary.jpg'

    async def get_card_data(self, card_number, field):
        url = 'https://heroku.ether.cards/card/{}/{}.json'.format(int(card_number) % 100, int(card_number))
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                data = await res.json()
                return data[field]

    async def get_card_holders(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.bloxy.info/token/token_stat?token={self.contract}&key=ACCHP8q4IWAZf&format=table') as res:
                try:
                    res = await res.json()
                    return res[0][-2]
                except:
                    return 0

    async def get_7day_vol(self):
        url = f"https://api.opensea.io/api/v1/asset/{self.contract}/1/?force_update=true&format=json"
        headers = {"X-API-KEY": self.os_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url,
                                    headers=headers) as res:
                try:
                    data = await res.json()   
                    return data['collection']['stats']['seven_day_volume']
                except:
                    return 0

    async def get_full_art(self, card_number, card_type):
        url = 'https://heroku.ether.cards/card/{}/{}.json'.format(int(card_number) % 100, int(card_number))
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                data = await res.json()
            if card_type != 'founder' and card_type != 'creator':
                data = data['original_art_url']
            else:
                data = data['layer_image']
            async with session.get(data) as res:
                buffer = io.BytesIO(await res.read())
                return (buffer, data.split('/')[-1])
        return False

    async def get_current_price(self, card_number):
        url = "https://api.opensea.io/wyvern/v1/orders"
        params = {"asset_contract_address":self.contract,"bundled":"false","include_bundled":"false","include_invalid":"false","token_id": str(card_number),"side":"1","sale_kind":"0","limit":"1","offset":"0","order_by":"eth_price","order_direction":"asc"}
        headers = {"X-API-KEY": self.os_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url,
                                  params=params,
                                  headers=headers) as res:
                data = await res.json()
                if len(data['orders']) != 0:
                    if data['orders'][0]['closing_date'] == None:
                        wei = data['orders'][0]['base_price']
                        return int(wei)/10**18
        return False

    async def get_last_sale(self, card_number):
        url = f"https://api.opensea.io/api/v1/asset/{self.contract}/{card_number}"
        headers = {"X-API-KEY": self.os_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url,
                                    headers=headers) as res:
                data = await res.json()
                if data['last_sale'] != None:
                    price_in_eth = int(data['last_sale']['total_price'])/10**18
                    price_in_dol = price_in_eth * float(data['last_sale']['payment_token']['usd_price'])
                    return (price_in_eth, price_in_dol)
        return False
    
    async def get_floor(self, traits):
        floor_query = {
            "id":"AssetSearchQuery",
            "query":"query AssetSearchQuery(\n  $categories: [CollectionSlug!]\n  $chains: [ChainScalar!]\n  $collection: CollectionSlug\n  $collectionQuery: String\n  $collectionSortBy: CollectionSort\n  $collections: [CollectionSlug!]\n  $count: Int\n  $cursor: String\n  $identity: IdentityInputType\n  $includeHiddenCollections: Boolean\n  $numericTraits: [TraitRangeType!]\n  $paymentAssets: [PaymentAssetSymbol!]\n  $priceFilter: PriceFilterType\n  $query: String\n  $resultModel: SearchResultModel\n  $showContextMenu: Boolean = false\n  $shouldShowQuantity: Boolean = false\n  $sortAscending: Boolean\n  $sortBy: SearchSortBy\n  $stringTraits: [TraitInputType!]\n  $toggles: [SearchToggle!]\n  $creator: IdentityInputType\n  $assetOwner: IdentityInputType\n  $isPrivate: Boolean\n  $safelistRequestStatuses: [SafelistRequestStatus!]\n) {\n  query {\n    ...AssetSearch_data_2hBjZ1\n  }\n}\n\nfragment AssetCardContent_assetBundle on AssetBundleType {\n  assetQuantities(first: 18) {\n    edges {\n      node {\n        asset {\n          relayId\n          ...AssetMedia_asset\n          id\n        }\n        id\n      }\n    }\n  }\n}\n\nfragment AssetCardContent_asset_27d9G3 on AssetType {\n  relayId\n  name\n  ...AssetMedia_asset\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    openseaVersion\n    id\n  }\n  tokenId\n  collection {\n    slug\n    id\n  }\n  isDelisted\n  ...AssetContextMenu_data_3z4lq0 @include(if: $showContextMenu)\n}\n\nfragment AssetCardFooter_assetBundle on AssetBundleType {\n  name\n  assetQuantities(first: 18) {\n    edges {\n      node {\n        asset {\n          collection {\n            name\n            relayId\n            id\n          }\n          id\n        }\n        id\n      }\n    }\n  }\n  assetEventData {\n    lastSale {\n      unitPriceQuantity {\n        ...AssetQuantity_data\n        id\n      }\n    }\n  }\n  orderData {\n    bestBid {\n      orderType\n      paymentAssetQuantity {\n        ...AssetQuantity_data\n        id\n      }\n    }\n    bestAsk {\n      closedAt\n      orderType\n      dutchAuctionFinalPrice\n      openedAt\n      priceFnEndedAt\n      quantity\n      decimals\n      paymentAssetQuantity {\n        quantity\n        ...AssetQuantity_data\n        id\n      }\n    }\n  }\n}\n\nfragment AssetCardFooter_asset_fdERL on AssetType {\n  ownedQuantity(identity: $identity) @include(if: $shouldShowQuantity)\n  name\n  tokenId\n  collection {\n    name\n    id\n  }\n  hasUnlockableContent\n  isDelisted\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    openseaVersion\n    id\n  }\n  assetEventData {\n    firstTransfer {\n      timestamp\n    }\n    lastSale {\n      unitPriceQuantity {\n        ...AssetQuantity_data\n        id\n      }\n    }\n  }\n  decimals\n  orderData {\n    bestBid {\n      orderType\n      paymentAssetQuantity {\n        ...AssetQuantity_data\n        id\n      }\n    }\n    bestAsk {\n      closedAt\n      orderType\n      dutchAuctionFinalPrice\n      openedAt\n      priceFnEndedAt\n      quantity\n      decimals\n      paymentAssetQuantity {\n        quantity\n        ...AssetQuantity_data\n        id\n      }\n    }\n  }\n}\n\nfragment AssetCardHeader_data on AssetType {\n  relayId\n  favoritesCount\n  isDelisted\n  isFavorite\n}\n\nfragment AssetContextMenu_data_3z4lq0 on AssetType {\n  ...asset_edit_url\n  ...itemEvents_data\n  isDelisted\n  isEditable {\n    value\n    reason\n  }\n  isListable\n  ownership(identity: {}) {\n    isPrivate\n    quantity\n  }\n  creator {\n    address\n    id\n  }\n  collection {\n    isAuthorizedEditor\n    id\n  }\n}\n\nfragment AssetMedia_asset on AssetType {\n  animationUrl\n  backgroundColor\n  collection {\n    description\n    displayData {\n      cardDisplayStyle\n    }\n    imageUrl\n    hidden\n    name\n    slug\n    id\n  }\n  description\n  name\n  tokenId\n  imageUrl\n  isDelisted\n}\n\nfragment AssetQuantity_data on AssetQuantityType {\n  asset {\n    ...Price_data\n    id\n  }\n  quantity\n}\n\nfragment AssetSearchFilter_data_3KTzFc on Query {\n  ...CollectionFilter_data_2qccfC\n  collection(collection: $collection) {\n    numericTraits {\n      key\n      value {\n        max\n        min\n      }\n      ...NumericTraitFilter_data\n    }\n    stringTraits {\n      key\n      ...StringTraitFilter_data\n    }\n    id\n  }\n  ...PaymentFilter_data_2YoIWt\n  ...CategoryFilter_data\n}\n\nfragment AssetSearchList_data_3Aax2O on SearchResultType {\n  asset {\n    assetContract {\n      account {\n        address\n        chain {\n          identifier\n          id\n        }\n        id\n      }\n      id\n    }\n    relayId\n    tokenId\n    ...AssetSelectionItem_data\n    ...asset_url\n    id\n  }\n  assetBundle {\n    relayId\n    id\n  }\n  ...Asset_data_3Aax2O\n}\n\nfragment AssetSearch_data_2hBjZ1 on Query {\n  ...CollectionHeadMetadata_data_2YoIWt\n  ...AssetSearchFilter_data_3KTzFc\n  ...SearchPills_data_2Kg4Sq\n  search(after: $cursor, chains: $chains, categories: $categories, collections: $collections, first: $count, identity: $identity, numericTraits: $numericTraits, paymentAssets: $paymentAssets, priceFilter: $priceFilter, querystring: $query, resultType: $resultModel, sortAscending: $sortAscending, sortBy: $sortBy, stringTraits: $stringTraits, toggles: $toggles, creator: $creator, isPrivate: $isPrivate, safelistRequestStatuses: $safelistRequestStatuses) {\n    edges {\n      node {\n        ...AssetSearchList_data_3Aax2O\n        __typename\n      }\n      cursor\n    }\n    totalCount\n    pageInfo {\n      endCursor\n      hasNextPage\n    }\n  }\n}\n\nfragment AssetSelectionItem_data on AssetType {\n  backgroundColor\n  collection {\n    displayData {\n      cardDisplayStyle\n    }\n    imageUrl\n    id\n  }\n  imageUrl\n  name\n  relayId\n}\n\nfragment Asset_data_3Aax2O on SearchResultType {\n  asset {\n    assetContract {\n      account {\n        chain {\n          identifier\n          id\n        }\n        id\n      }\n      id\n    }\n    isDelisted\n    ...AssetCardHeader_data\n    ...AssetCardContent_asset_27d9G3\n    ...AssetCardFooter_asset_fdERL\n    ...AssetMedia_asset\n    ...asset_url\n    ...itemEvents_data\n    id\n  }\n  assetBundle {\n    slug\n    assetCount\n    ...AssetCardContent_assetBundle\n    ...AssetCardFooter_assetBundle\n    id\n  }\n}\n\nfragment CategoryFilter_data on Query {\n  categories {\n    imageUrl\n    name\n    slug\n  }\n}\n\nfragment CollectionFilter_data_2qccfC on Query {\n  selectedCollections: collections(first: 25, collections: $collections, includeHidden: true) {\n    edges {\n      node {\n        assetCount\n        imageUrl\n        name\n        slug\n        id\n      }\n    }\n  }\n  collections(assetOwner: $assetOwner, assetCreator: $creator, onlyPrivateAssets: $isPrivate, chains: $chains, first: 100, includeHidden: $includeHiddenCollections, parents: $categories, query: $collectionQuery, sortBy: $collectionSortBy) {\n    edges {\n      node {\n        assetCount\n        imageUrl\n        name\n        slug\n        id\n        __typename\n      }\n      cursor\n    }\n    pageInfo {\n      endCursor\n      hasNextPage\n    }\n  }\n}\n\nfragment CollectionHeadMetadata_data_2YoIWt on Query {\n  collection(collection: $collection) {\n    bannerImageUrl\n    description\n    imageUrl\n    name\n    id\n  }\n}\n\nfragment CollectionModalContent_data on CollectionType {\n  description\n  imageUrl\n  name\n  slug\n}\n\nfragment NumericTraitFilter_data on NumericTraitTypePair {\n  key\n  value {\n    max\n    min\n  }\n}\n\nfragment PaymentFilter_data_2YoIWt on Query {\n  paymentAssets(first: 10) {\n    edges {\n      node {\n        asset {\n          symbol\n          id\n        }\n        relayId\n        id\n        __typename\n      }\n      cursor\n    }\n    pageInfo {\n      endCursor\n      hasNextPage\n    }\n  }\n  PaymentFilter_collection: collection(collection: $collection) {\n    paymentAssets {\n      asset {\n        symbol\n        id\n      }\n      relayId\n      id\n    }\n    id\n  }\n}\n\nfragment Price_data on AssetType {\n  decimals\n  imageUrl\n  symbol\n  usdSpotPrice\n  assetContract {\n    blockExplorerLink\n    account {\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    id\n  }\n}\n\nfragment SearchPills_data_2Kg4Sq on Query {\n  selectedCollections: collections(first: 25, collections: $collections, includeHidden: true) {\n    edges {\n      node {\n        imageUrl\n        name\n        slug\n        ...CollectionModalContent_data\n        id\n      }\n    }\n  }\n}\n\nfragment StringTraitFilter_data on StringTraitType {\n  counts {\n    count\n    value\n  }\n  key\n}\n\nfragment asset_edit_url on AssetType {\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    id\n  }\n  tokenId\n  collection {\n    slug\n    id\n  }\n}\n\nfragment asset_url on AssetType {\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    id\n  }\n  tokenId\n}\n\nfragment itemEvents_data on AssetType {\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    id\n  }\n  tokenId\n}\n",
            "variables":{
                "categories":None,
                "chains":None,
                "collection":"ether-cards-founder",
                "collectionQuery":None,
                "collectionSortBy":"SEVEN_DAY_VOLUME",
                "collections":[
                "ether-cards-founder"
                ],
                "count":1,
                "cursor":None,
                "identity":None,
                "includeHiddenCollections":False,
                "numericTraits":None,
                "paymentAssets":None,
                "priceFilter":None,
                "query":"",
                "resultModel":"ASSETS",
                "showContextMenu":False,
                "shouldShowQuantity":False,
                "sortAscending":True,
                "sortBy":"PRICE",
                "stringTraits": traits,
                "toggles":[
                "BUY_NOW"
                ],
                "creator":None,
                "assetOwner":None,
                "isPrivate":None,
                "safelistRequestStatuses":None
            }
        }
        url = "https://api.opensea.io/graphql/"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, json=floor_query) as res:
                    data = await res.json()
                    floor = data['data']['query']['search']['edges'][0]['node']['asset']
                    id = floor['tokenId']
                    cost = int(floor['orderData']['bestAsk']['paymentAssetQuantity']['quantity']) /10**18
            return({'cost': cost, 'id': id})
        except Exception as e:
            print(e)
            return({'cost': -1, 'id': -1})

    async def floor_update(self, traits=None):
        data = {}
        if traits != None:
            floor = await self.get_floor(traits)
            data.update({'cost': floor['cost'], 'id': floor['id']})
        else:
            for series in ('Founder', 'Alpha', 'OG'):
                traits = [{"name": "type", "values": [series]}]
                floor = await self.get_floor(traits)
                data.update({series: {'cost': floor['cost'], 'id': floor['id']}})
                await asyncio.sleep(1)
        return data

    async def get_events(self):
        url = "https://api.opensea.io/api/v1/events"
        async with aiohttp.ClientSession() as session:
            params = {"asset_contract_address":self.contract,"only_opensea":"true","offset":"0","limit": 25}
            async with session.get(url, params=params) as res:
                if res.status == 200:
                    try:
                        data = await res.json()
                        return data
                    except Exception as e:
                        print(f"Failed to get events {e}")
                        return False
                    
        
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.update_status.start()
        self.opensea_activity.start()
        #db setup (idk if this is the best place but seems like it to me)
        self.wen_db = Database(self.db_name)
        await self.wen_db.connect()
        query = """CREATE TABLE IF NOT EXISTS wens (
                    id   INTEGER PRIMARY KEY,
                    wen  TEXT    NOT NULL,
                    res  TEXT    NOT NULL,
                    UNIQUE(wen)
                )"""
        await self.wen_db.execute(query=query)
        await self.wen_db.disconnect()

    @tasks.loop(seconds=60)
    async def update_status(self):
        activities = ['holders', 'Alpha', 'OG', 'Founder', 'vol']
        choice = random.choice(activities)
        activity = ''
        if choice == 'holders':
            holders = await self.get_card_holders()
            if holders != 0:
                self.latest_holders = holders
            if self.latest_holders != -1:
                activity = f'{self.latest_holders} hodlers'
        elif choice == 'vol':
            vol = await self.get_7day_vol()
            if vol != 0:
                activity = f'7 Day vol: {round(vol, 2)}ETH'
        else:
            traits = [{"name": "type", "values": [choice]}]
            floor = await self.floor_update(traits)
            if floor['cost'] != -1:
                self.latest_floor = floor
            if self.latest_floor["cost"] != -1:
                activity = f'{choice} floor: {self.latest_floor["cost"]}ETH'
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='{}'.format(activity)))
    
    @update_status.before_loop
    async def before_update_status(self):
        await self.wait_until_ready()

    @tasks.loop(seconds=5)
    async def opensea_activity(self):
        data = await self.get_events()
        if data:
            for event in reversed(data['asset_events']):
                event_info = {'id': event['id'], 'type': event['event_type']}
                if event['event_type'] in ['created', 'successful']:
                    if event_info not in self.posted_events:
                        if event['auction_type'] == None or event['auction_type'] == 'dutch':
                            buyer = None
                            seller = None
                            if event['asset_bundle'] == None:
                                id = event['asset']['token_id']
                                if event['event_type'] == "created":
                                    price_in_eth = int(event['starting_price'])/10**18
                                    title = f"EC {id} listed for sale for {round(price_in_eth, 4)}ETH (${round(price_in_eth * float(event['payment_token']['usd_price']), 2)})"
                                    if event['seller']['user'] != None:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})({event['seller']['user']['username']})"
                                    else:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})"
                                elif event['event_type'] == "successful":
                                    price_in_eth = int(event['total_price'])/10**18
                                    title = f"EC {id} just sold for {round(price_in_eth, 4)}ETH (${round(price_in_eth * float(event['payment_token']['usd_price']), 2)})"
                                    if event['seller']['user'] != None:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})({event['seller']['user']['username']})"
                                    else:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})"
                                    if event['winner_account']['user'] != None:
                                        buyer = f"[{event['winner_account']['address'][:8]}](https://opensea.io/accounts/{event['winner_account']['address']})({event['winner_account']['user']['username']})"
                                    else:
                                        buyer = f"[{event['winner_account']['address'][:8]}](https://opensea.io/accounts/{event['winner_account']['address']})"
                                card_type = await self.get_card_type(id)
                                image = await self.create_summary(id, card_type, False)
                                file = discord.File(image, filename="CardSummary.jpg")
                                embed=discord.Embed(title=title, color=0xbe1fda)
                                embed.add_field(name=f"{id}", value=f"[OpenSea]({event['asset']['permalink']})\n[Explorer]({event['asset']['external_link']})", inline=True)
                                if seller != None:
                                    embed.add_field(name="Seller", value=seller, inline=True)
                                if buyer != None:
                                    embed.add_field(name="Buyer", value=buyer, inline=True)
                                embed.set_image(url="attachment://CardSummary.jpg")
                                date = datetime.strptime(event['created_date'], "%Y-%m-%dT%H:%M:%S.%f")
                                embed.set_footer(text=f"Occured at: {date:%H:%M:%S - %d/%m/%Y}")
                                channel = client.get_channel(842492651395481640)
                                await channel.send(file=file, embed=embed)
                                media = self.tweepy.media_upload("CardSummary.jpg")
                                self.tweepy.update_status(status=f"{title} {event['asset']['external_link']} {event['asset']['permalink']} #ethercards", media_ids=[media.media_id])
                                self.posted_events.append(event_info)                                
                            else:
                                if event['event_type'] == "created":
                                    price_in_eth = int(event['starting_price'])/10**18
                                    title = f"A bundle with {event['quantity']} items was listed for sale for {round(price_in_eth, 2)}ETH (${round(price_in_eth * float(event['payment_token']['usd_price']), 2)})"
                                    if event['seller']['user'] != None:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})({event['seller']['user']['username']})"
                                    else:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})"
                                elif event['event_type'] == "successful":
                                    price_in_eth = int(event['total_price'])/10**18
                                    title = f"A bundle with {event['quantity']} items just sold for {round(price_in_eth, 2)}ETH (${round(price_in_eth * float(event['payment_token']['usd_price']), 2)})"
                                    if event['seller']['user'] != None:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})({event['seller']['user']['username']})"
                                    else:
                                        seller = f"[{event['seller']['address'][:8]}](https://opensea.io/accounts/{event['seller']['address']})"
                                    if event['winner_account']['user'] != None:
                                        buyer = f"[{event['winner_account']['address'][:8]}](https://opensea.io/accounts/{event['winner_account']['address']})({event['winner_account']['user']['username']})"
                                    else:
                                        buyer = f"[{event['winner_account']['address'][:8]}](https://opensea.io/accounts/{event['winner_account']['address']})"
                                embed=discord.Embed(title=title, color=0xbe1fda)
                                embed.add_field(name="Bundle", value=f"[OpenSea]({event['asset_bundle']['permalink']})", inline=True)
                                if seller != None:
                                    embed.add_field(name="Seller", value=seller, inline=True)
                                if buyer != None:
                                    embed.add_field(name="Buyer", value=buyer, inline=True)
                                items = ""
                                for asset in event['asset_bundle']['assets']:
                                    card_type = await self.get_card_type(asset['token_id'])
                                    items += f"[{asset['token_id']}]({asset['permalink']}) - {card_type.capitalize()}\n"
                                embed.add_field(name=f"Name: {event['asset_bundle']['slug']}", value=items)
                                date = datetime.strptime(event['created_date'], "%Y-%m-%dT%H:%M:%S.%f")
                                embed.set_footer(text=f"Occured at: {date:%H:%M:%S - %d/%m/%Y}")
                                channel = client.get_channel(842492651395481640)
                                await channel.send(embed=embed)
                                self.tweepy.update_status(status=f"{title} {event['asset_bundle']['permalink']} #ethercards")
                                self.posted_events.append(event_info)
                        if len(self.posted_events) > 50:
                            self.posted_events.pop(0)

    @opensea_activity.before_loop
    async def before_opensea_activity(self):
        data = await self.get_events()
        if data:
            for event in reversed(data['asset_events']):
                if event['event_type'] in ['created', 'successful']:
                    self.posted_events.append({"id": event["id"], "type": event["event_type"]})
        await self.wait_until_ready()

    async def on_message(self, message):
        if message.author.id == self.user.id: #stop bot replying to its self
            return

        if message.content.startswith('!help'):
            await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            embed=discord.Embed(title="EtherCards Helper Bot", color=0xbe1fda)
            embed.add_field(name="EC Commands", value="`!summary      0-9999` Show all art and features of a card.\n`!fullart      0-9999` Show the full original art. (Videos have to be linked due to discord size limits)\n`!title        0-9999` Show the title of the artwork.\n`!artist       0-9999` Show the artist of the artwork.\n`!layerartists 0-9999` Show the artists of the individual layers.\n`!traits       0-9999` Show the traits of the card for up to 10 cards.\n`!phoenix      0-9999` Show the phoenix status of a card.\n`!layers       0-9999` Show the individual layers and occurrences.\n`!set         100-999` Show other cards in set for an alpha.\n`!traitinfo      name` Show details about a trait.\n`!stats              ` Show a range of useful statistics about EC.", inline=False)
            embed.add_field(name="OS Commands", value="`!lastsale      0-9999` Show the price the card last sold for on OS.\n`!currentprice  0-9999` Show the price the card is currently available for.\n`!floor` Show the floor price of each card type.\n`!traitfloors` Show the floor price for each trait type.\n`!hodlers` Show how many hodlers there currently are", inline=False)
            embed.add_field(name="Ether Cards", value="The [Ether Cards](https://ether.cards/) platform is a community-driven NFT framework. It enables creators to maximize the value of their NFT art or series by expanding the capability of NFT Marketplaces. It allows anyone to set up events, puzzles, bounties, and a dozen other different utilities for any NFT asset of their choice. [Ether Cards](https://ether.cards/) is a fully integrated ecosystem, composed of two major parts. These are the [platform](https://docs.ether.cards/faq.html#platform) and the [Ether Cards](https://ether.cards/) (membership card NFTs).", inline=False)
            embed.add_field(name="Admin Commands", value="`!addwen wen response` Allows an admin to add a call and response for when a message starts with w(h)en.\n`!updwen wen response` Allows an admin to update the call and response for a w(h)en.\n`!delwen wen         ` Allows an admin to delete a call and response for when a message starts with w(h)en.", inline=False)
            embed.add_field(name="About", value="A discord bot created by <@145303558110183424>(0x1aD45017b09D2C36b84440cB82426dA645F8048A) for the Ether Cards server. The bot provides a range of functions useful to members regarding their ether cards. With some assisstance from <@390320089527746560> and <@302134640947232768>", inline=False)
            embed.set_footer(text="Help requested by {}".format(message.author.name))
            await message.reply(embed=embed, mention_author=True)
            
        if message.content.startswith('!summary'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    card_type = await self.get_card_type(card_number)
                    image = await self.create_summary(card_number, card_type)
                    await message.reply('Summary of EtherCard ID {}:'.format(card_number), file=discord.File(image), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)

        if message.content.startswith('!title'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    card_type = await self.get_card_type(card_number)
                    if(card_type != 'founder'):
                        title = await self.get_card_data(card_number, 'title')
                    else:
                        title = 'Accidental Collaboration'
                    await message.reply('Title for EtherCard ID {}: {}'.format(card_number, title), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)
        
        if message.content.startswith('!artist'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    card_type = await self.get_card_type(card_number)
                    if(card_type != 'founder'):
                        artist = await self.get_card_data(card_number, 'artist')
                    else:
                        artist = 'Various'
                    await message.reply('Artist for EtherCard ID {}: {}'.format(card_number, artist), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)

        if message.content.startswith('!layerartists'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    artists = await self.get_card_data(card_number, 'layer_artists')
                    await message.reply('Layer artists for EtherCard ID {}: {}'.format(card_number, artists), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)                    

        if message.content.startswith('!phoenix'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    card_type = await self.get_card_type(card_number)
                    phoenix = await self.get_phoenix_status(card_number, card_type)
                    await message.reply('EtherCard ID {} phoenix status: {}'.format(card_number, phoenix), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)   

        if message.content.startswith('!set'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if card_number.isdigit():
                    if int(card_number) >= 100 and int(card_number) < 1000:
                        await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                        dupes = await self.get_unique_alpha_status(card_number)
                        if dupes != 'None':
                            dupes = ', '.join(dupes)
                        await message.reply('EtherCard ID {} others in set: {}'.format(card_number, dupes), mention_author=True)
                    else: 
                        await message.add_reaction('\N{CROSS MARK}')
                        await message.reply('Please enter a card number between 100 and 999', mention_author=True)
                else: 
                        await message.add_reaction('\N{CROSS MARK}')
                        await message.reply('Please enter a card number between 100 and 999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)   
        
        if message.content.startswith('!lastsale'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    last_price = await self.get_last_sale(card_number)
                    if last_price != False:
                        await message.reply('EtherCard ID {} last sold for: {}ETH (${:,.2f})'.format(card_number, last_price[0], last_price[1]), mention_author=True)
                    else:
                        await message.reply('EtherCard ID {} has never been sold.'.format(card_number), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True) 
        
        if message.content.startswith('!currentprice'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    current_price = await self.get_current_price(card_number)
                    if current_price != False:
                        await message.reply('EtherCard ID {} is for sale for: {}ETH'.format(card_number, current_price), mention_author=True)
                    else:
                        await message.reply('EtherCard ID {} is not for sale.'.format(card_number), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True) 

        if message.content.startswith('!fullart'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    card_type = await self.get_card_type(card_number)
                    if card_type != 'founder' and card_type != 'creator':
                        url = await self.get_card_data(card_number, 'original_art_url')
                        if url[-4:] != '.mp4':
                            attach = await self.get_full_art(card_number, card_type)
                            if attach:
                                await message.reply('Full original art for EtherCard ID {}:'.format(card_number), file=discord.File(fp=attach[0], filename=attach[1]), mention_author=True)
                            else:
                                await message.reply('Failed to get art for EtherCard ID {}'.format(card_number), mention_author=True)
                        else:
                            await message.reply('Full original art url for EtherCard ID {}: {}'.format(card_number, url), mention_author=True)
                    else:
                        attach = await self.get_full_art(card_number, card_type)
                        if attach:
                            await message.reply('Full original art for EtherCard ID {}:'.format(card_number), file=discord.File(fp=attach[0], filename=attach[1]), mention_author=True)
                        else:
                            await message.reply('Failed to get art for EtherCard ID {}'.format(card_number), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)  
        
        if message.content.startswith('!stats'):
            await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            holders = await self.get_card_holders()
            unique_alphas_count = len(self.unique_alphas)
            embed=discord.Embed(title="EtherCards Statistics", color=0xbe1fda)
            embed.add_field(name="All Cards", value="Count: 9999 Cards.\nThere are currently {} holders.\nThere are 1803 phoenix cards.\nThere are 136 cards with perfect accidental art.".format(holders), inline=False)
            embed.add_field(name="OG 10-99", value="Count: 90 Cards\n25 of these phoenix cards. (10-34)\nThere are 2 cards with perfect accidental art. (0.02%)", inline=False)
            embed.add_field(name="Alpha 100-999", value="Count: 900\n153 of these phoenix cards. (100-253)\nThere are 17 cards with perfect accidental art. (0.17%)\nThere are {} unique alphas\nUnique alphas: {}".format(unique_alphas_count, self.unique_alphas), inline=False)
            embed.add_field(name="Founder 1000-9999", value="Count: 9000\n1624 of these phoenix cards. (1000-2623)\nThere are 117 cards with perfect accidental art. (1.17%)", inline=False)
            embed.set_footer(text="Statistics requested by {}".format(message.author.name))
            await message.reply(embed=embed, mention_author=True)

        if message.content.startswith('!floor'):
            args = message.content.split(' ')
            embed=discord.Embed(title="OpenSea floors", color=0xbe1fda)
            if len(args) == 1:                
                await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                floor = await self.floor_update()
                embed_text = ""
                for card_type in floor:
                    if floor[card_type]["cost"] != -1:
                        embed_text += f'{card_type}: ID - [{floor[card_type]["id"]}](https://opensea.io/assets/{self.contract}/{floor[card_type]["id"]}) - {floor[card_type]["cost"]}ETH - [Browse](https://opensea.io/collection/ether-cards-founder?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=type&search[stringTraits][0][values][0]={card_type}&search[toggles][0]=BUY_NOW)\n'
                if embed_text != "":
                    embed.add_field(name="Floors:", value=embed_text, inline=False)
                else:
                    embed.add_field(name="Floors:", value="Failed to get floors.", inline=False)
                await message.reply(embed=embed, mention_author=True)
            else:
                await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                args.pop(0)
                args = ' '.join(args)
                trait_query_list = []
                embed_text = ''
                pattern = '([a-zA-Z ]*):([a-zA-Z ]*)'
                floor = None
                for match in re.findall(pattern, args):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    category = match[0].lower()
                    value = match[1].lower().title()
                    embed_text += f'{category}: {value}\n'
                    trait_query_list.append({"name": category, "values": value})
                floor = await self.get_floor(trait_query_list)
                if floor is None or floor['cost'] == -1:
                    await message.reply('Floor not found for trait that trait combination. Please check the filters on OpenSea for valid combinations.', mention_author=True)
                else:
                    embed.add_field(name='Traits:', value=embed_text)
                    embed.add_field(name='Floor:', value=f'ID: [{floor["id"]}](https://opensea.io/assets/{self.contract}/{floor["id"]}) - {floor["cost"]}ETH - [Browse](https://opensea.io/assets/{self.contract}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW)', inline=False)
                    await message.reply(embed=embed, mention_author=True)     

        if message.content.startswith('!vol'):
            await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            volume = await self.get_7day_vol()
            await message.reply(f'OpenSea 7 day volume: {round(volume, 2)}ETH', mention_author=True)

        if message.content.startswith('!hodlers'):
            await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            holders = await self.get_card_holders()
            await message.reply(f'There are currently {holders} hodlers.', mention_author=True)
        
        if message.content.startswith('!layers'):
            args = message.content.split(' ')
            if len(args) == 2:            
                card_number = args[1].strip()
                if await self.is_valid_card(card_number):
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    image = await self.create_layer_image(card_number)
                    await message.reply('Layers for EtherCard ID {}:'.format(card_number), file=discord.File(image), mention_author=True)
                else: 
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a card number between 0 and 9999', mention_author=True)
            elif len(args) > 2:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter only one card number', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)

        if message.content.startswith('!traits'):
            args = message.content.split(' ')
            if len(args) >= 2 and len(args) <= 11:
                numbers = False
                for card_number in args: 
                    if card_number != "!traits":
                        if await self.is_valid_card(card_number.strip()):
                            numbers = True
                            break
                if numbers:
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')                
                else:
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a valid card number', mention_author=True)
                traits_dict = {}
                for card_number in args: 
                    if card_number != "!traits":
                        if await self.is_valid_card(card_number.strip()):
                            traits = await self.get_card_data(card_number, 'traits')
                            if len(traits) != 0:
                                for item in traits:
                                    if card_number in traits_dict:
                                        if item['name'] not in traits_dict[card_number]:
                                            traits_dict[card_number].update({item['name']: 1})
                                        else:
                                            traits_dict[card_number][item['name']] += 1
                                    else:
                                        traits_dict[card_number] = {item['name']: 1}
                            else:
                                traits_dict[card_number] = "None"        
                traits = ""
                for card in traits_dict:
                    if traits_dict[card] != 'None':
                        trait_list = []
                        for trait in traits_dict[card]:
                            if traits_dict[card][trait] != 1:
                                trait_list.append(f"{trait} x {traits_dict[card][trait]}")
                            else:
                                trait_list.append(f"{trait}")
                        traits += f"**ID {card}**: {', '.join(trait_list)}\n\n"
                    else:
                        traits += f"**ID {card}**: None\n\n"
                if traits != "":
                    await message.reply('Traits for: \n{}'.format(traits), mention_author=True)
            elif len(args) > 10:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a maximum of 10 card numbers', mention_author=True)  
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a card number', mention_author=True)
        
        if message.content.startswith('!traitinfo'):
            args = message.content.split(' ')
            args.pop(0)
            trait = ' '.join(args)
            if trait != "":
                with open('random_traits.json', encoding="utf8") as trait_data:
                    data = json.load(trait_data)
                    new_data = list(map(str.lower, data.keys()))
                    originals = list(map(str, data.keys()))
                    if trait.lower() in new_data:
                        for i in range(0, len(new_data)):
                            if new_data[i] == trait.lower():
                                original_trait_name = originals[i]
                        await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                        embed=discord.Embed(title=f"The {original_trait_name} trait", color=0xbe1fda)
                        embed.add_field(name="Description", value=f"{data[original_trait_name]['Short description'].capitalize()}", inline=False)
                        if "card_ids" in data[original_trait_name]:
                            lowest_available_price = await self.get_floor([{"name": "trait", "values": original_trait_name},])
                            if lowest_available_price["cost"] != -1:
                                embed.add_field(name="Statistics", value=f"Card type: {data[original_trait_name]['card type'].capitalize()}\nFloor price: {lowest_available_price['cost']}ETH ID: [{lowest_available_price['id']}](https://opensea.io/assets/{self.contract}/{lowest_available_price['id']})\nPercentage: {data[original_trait_name]['percentage']}", inline=False)
                            else:
                                embed.add_field(name="Statistics", value=f"Card type: {data[original_trait_name]['card type'].capitalize()}\nPercentage: {data[original_trait_name]['percentage']}", inline=False)
                            if len(data[original_trait_name]['card_ids']) < 300:
                                embed.add_field(name="Appears on", value=f"Card type: {data[original_trait_name]['card type'].capitalize()}\nAppears on: {', '.join(str(x) for x in data[original_trait_name]['card_ids'])}\nPercentage: {data[original_trait_name]['percentage']}", inline=False)
                        else:
                            embed.add_field(name="Statistics", value=f"Card type: {data[original_trait_name]['card type'].capitalize()}\nPercentage: {data[original_trait_name]['percentage']}", inline=False)
                        embed.set_footer(text="Information requested by {}".format(message.author.name))
                        await message.reply(embed=embed, mention_author=True)
                    else:
                        await message.add_reaction('\N{CROSS MARK}')
                        await message.reply('Please enter a valid trait', mention_author=True)
            else:
                await message.add_reaction('\N{CROSS MARK}')
                await message.reply('Please enter a trait', mention_author=True)

        if message.content.startswith('!traitfloors'):
            return
            await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            with open('random_traits.json', encoding="utf8") as trait_data:
                data = json.load(trait_data)
                embed=discord.Embed(title="Trait floors", color=0xbe1fda)
                floors = ""#have to do this because 1024 embed field limit even though it's all hyperlinks
                floors2 = ""
                floors3 = ""
                for key in data:
                    if "card_ids" in data[key]:
                        lowest_available_price = await self.get_trait_floor(data[key]['card_ids'])
                        if lowest_available_price:
                            text = f"{key}: {lowest_available_price['cost']}ETH - [{lowest_available_price['id']}](https://opensea.io/assets/{self.contract}/{lowest_available_price['id']})\n"
                            if (len(floors) + len(text)) < 1024:
                                floors += text
                            elif (len(floors2) + len(text)) < 1024:
                                floors2 += text
                            else:
                                floors3 += text
                embed.add_field(name="Floors", value=f"{floors}", inline=False)
                if floors2 != "":
                    embed.add_field(name="More floors", value=f"{floors2}", inline=False)
                if floors3 != "":
                    embed.add_field(name="Even More floors", value=f"{floors3}", inline=False)
                embed.set_footer(text="Information requested by {}".format(message.author.name))
                await message.reply(embed=embed, mention_author=True)
        
        if message.content.lower().startswith('wen') or message.content.lower().startswith('when'):
            await self.wen_db.connect()
            query = "SELECT wen,res FROM wens"
            rows = await self.wen_db.fetch_all(query=query)
            await self.wen_db.disconnect()
            for word in rows:
                if word[0] in message.content.lower():
                    await message.reply(word[1], mention_author=True)

        if message.content.startswith('!addwen'):
            if discord.utils.get(message.author.roles, name="admin"):
                args = message.content.split(' ')
                args.pop(0)
                if len(args) >= 2:
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    wen = args.pop(0)
                    res = ' '.join(args)
                    await self.wen_db.connect()
                    query = "INSERT OR IGNORE INTO wens(wen, res) VALUES (:wen, :res)"
                    values = {"wen": wen.lower(), "res": res}
                    response = await self.wen_db.execute(query=query, values=values)
                    await self.wen_db.disconnect()
                    if response != 0:
                        await message.reply('Wen successfully added', mention_author=True)
                    else:
                        await message.reply('Wen already exists. Try !updwen or !delwen', mention_author=True)
                else:
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a wen and a response', mention_author=True)

        if message.content.startswith('!updwen'):
            if discord.utils.get(message.author.roles, name="admin"):
                args = message.content.split(' ')
                args.pop(0)
                print(len(args))
                if len(args) >= 2:
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    wen = args.pop(0)
                    res = ' '.join(args)
                    await self.wen_db.connect()
                    query = "UPDATE wens SET res = :res WHERE wen = :wen"
                    values = {"wen": wen.lower(), "res": res}
                    response = await self.wen_db.execute(query=query, values=values)
                    await self.wen_db.disconnect()
                    if response != 0:
                        await message.reply('Wen successfully updated', mention_author=True)
                    else:
                        await message.reply('Wen doesn\'t exist. Try !addwen', mention_author=True)
                else:
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a wen and a response', mention_author=True)

        if message.content.startswith('!delwen'):
            if discord.utils.get(message.author.roles, name="admin"):
                args = message.content.split(' ')
                args.pop(0)
                arg_len = len(args)
                if arg_len == 1:
                    await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                    wen = args[0]
                    await self.wen_db.connect()
                    query = "DELETE FROM wens WHERE wen = :wen"
                    values = {"wen": wen.lower()}
                    response = await self.wen_db.execute(query=query, values=values)
                    await self.wen_db.disconnect()
                    if response != 0:
                        await message.reply('Wen successfully deleted', mention_author=True)
                    else:
                        await message.reply('Wen doesn\'t exist. Try !addwen', mention_author=True)
                elif arg_len > 1:
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter one argument', mention_author=True)
                else:
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.reply('Please enter a wen', mention_author=True)

if __name__ == "__main__":
    client = MyClient()
    client.run(os.environ['token'])