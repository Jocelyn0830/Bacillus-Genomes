from Bio import Phylo
from ete3 import Tree

# tree = Phylo.read("ap_bootstrapped_ecotype.nhx", 'newick')

# ap_tree_filename = "ap_bootstrapped_ecotype.nhx"
# ap_tree_string = ""
# with open(ap_tree_filename, encoding='utf-8-sig') as treefile:
#     for row in treefile:
#         ap_tree_string += row

# ap_t = Tree(ap_tree_string)

# ap3 = ap_t.get_common_ancestor('CBP-1645', 'CBP-1660', 'CBP-1670', 'CBP-1652', 'CBP-3061', 'CBP-1650', 'CBP-1651', 'CBP-1668', 'CBP-1681', 'CBP-3063', 'CBP-1658', 'CBP-1661', 'CBP-2465', 'CBP-1678', 'CBP-3051', 'CBP-1646', 'CBP-3056', 'CBP-1684', 'CBP-1691', 'CBP-1771', 'CBP-2101', 'CBP-1786', 'CBP-2329', 'CBP-1790', 'CBP-2330', 'CBP-1800', 'CBP-1797', 'CBP-2331', 'CBP-2384', 'CBP-1789', 'CBP-2554', 'CBP-2387', 'CBP-2462', 'CBP-1803', 'CBP-1687', 'CBP-1746', 'CBP-1731', 'CBP-3057', 'CBP-1741', 'CBP-1742', 'CBP-3049', 'CBP-1689', 'CBP-3060', 'CBP-1682', 'CBP-1762', 'CBP-3053', 'CBP-3054', 'CBP-3055', 'CBP-1767', 'CBP-1774', 'CBP-1772', 'CBP-1796', 'CBP-2075', 'CBP-1801', 'CBP-1690', 'CBP-1752', 'CBP-1776', 'CBP-1777', 'CBP-3058', 'CBP-1760', 'CBP-3062', 'CBP-1669', 'CBP-1671', 'CBP-1672', 'CBP-2098', 'CBP-2099')
# ap16 = ap_t.get_common_ancestor('CBP-1650', 'CBP-1651', 'CBP-1668', 'CBP-1681', 'CBP-3063', 'CBP-1658', 'CBP-1661', 'CBP-2465', 'CBP-1678', 'CBP-3051', 'CBP-1646', 'CBP-3056', 'CBP-1684', 'CBP-1691', 'CBP-1771', 'CBP-2101', 'CBP-1786', 'CBP-2329', 'CBP-1790', 'CBP-2330', 'CBP-1800', 'CBP-1797', 'CBP-2331', 'CBP-2384', 'CBP-1789', 'CBP-2554', 'CBP-2387', 'CBP-2462', 'CBP-1803', 'CBP-1687', 'CBP-1746', 'CBP-1731', 'CBP-3057', 'CBP-1741', 'CBP-1742', 'CBP-3049', 'CBP-1689', 'CBP-3060', 'CBP-1682', 'CBP-1762', 'CBP-3053', 'CBP-3054', 'CBP-3055', 'CBP-1767', 'CBP-1774', 'CBP-1772', 'CBP-1796', 'CBP-2075', 'CBP-1801')
# ap76 = ap_t.get_common_ancestor('CBP-1687', 'CBP-1746', 'CBP-1731', 'CBP-3057', 'CBP-1741', 'CBP-1742', 'CBP-3049', 'CBP-1689', 'CBP-3060', 'CBP-1682', 'CBP-1762', 'CBP-3053', 'CBP-3054', 'CBP-3055', 'CBP-1767', 'CBP-1774', 'CBP-1772', 'CBP-1796', 'CBP-2075', 'CBP-1801')

# ap3.add_feature("bon", "ele")
# ap16.add_feature("bon", "ele")
# ap76.add_feature("bon", "soil")


# ia_tree_filename = "ia_bootstrapped_ecotype.nhx"
# ia_tree_string = ""
# with open(ia_tree_filename, encoding='utf-8-sig') as treefile:
#     for row in treefile:
#         ia_tree_string += row

# ia_t = Tree(ia_tree_string)

# ia7 = ia_t.get_common_ancestor('CBP-1641', 'CBP-3089', 'CBP-3090', 'CBP-3093', 'CBP-3081', 'CBP-3091', 'CBP-3088', 'CBP-3030', 'CBP-3041', 'CBP-3087', 'CBP-3083', 'CBP-3098', 'CBP-3070', 'CBP-2194', 'CBP-3071', 'CBP-1851', 'CBP-2370', 'CBP-2493', 'CBP-2320', 'CBP-2300', 'CBP-2397', 'CBP-2323', 'CBP-2457', 'CBP-2358', 'CBP-2468', 'CBP-2467', 'CBP-2466')

# ia7.add_feature("bon", "ele")
# ia_output = ia_t.write(features=["proof", "value", "bon"])
# with open("ia_bon.nhx", "w") as nhx_file:
#     nhx_file.write(ia_output)


sp_tree_filename = "sp_bootstrapped_ecotype.nhx"
sp_tree_string = ""
with open(sp_tree_filename, encoding='utf-8-sig') as treefile:
    for row in treefile:
        sp_tree_string += row

sp_t = Tree(sp_tree_string)

sp203 = sp_t.get_common_ancestor('CBP-1948', 'CBP-1949', 'CBP-2163', 'CBP-2170', 'CBP-2213', 'CBP-2200', 'CBP-2193', 'CBP-2165', 'CBP-2203', 'CBP-2164', 'CBP-2198', 'CBP-2527', 'CBP-2278', 'CBP-2487', 'CBP-2419', 'CBP-2113', 'CBP-2130', 'CBP-2136', 'CBP-2122', 'CBP-2144', 'CBP-2134', 'CBP-2121', 'CBP-2140', 'CBP-2155', 'CBP-2139', 'CBP-2141', 'CBP-2150', 'CBP-2138', 'CBP-2145', 'CBP-2129', 'CBP-2438')
sp179 = sp_t.get_common_ancestor('CBP-1702', 'CBP-1718', 'CBP-3079', 'CBP-3033', 'CBP-2283', 'CBP-2284', 'CBP-1928', 'CBP-3034', 'CBP-2127', 'CBP-1817', 'CBP-2131', 'CBP-1948', 'CBP-1949', 'CBP-2163', 'CBP-2170', 'CBP-2213', 'CBP-2200', 'CBP-2193', 'CBP-2165', 'CBP-2203', 'CBP-2164', 'CBP-2198', 'CBP-2527', 'CBP-2278', 'CBP-2487', 'CBP-2419', 'CBP-2113', 'CBP-2130', 'CBP-2136', 'CBP-2122', 'CBP-2144', 'CBP-2134', 'CBP-2121', 'CBP-2140', 'CBP-2155', 'CBP-2139', 'CBP-2141', 'CBP-2150', 'CBP-2138', 'CBP-2145', 'CBP-2129', 'CBP-2438', 'CBP-2381', 'CBP-2464', 'CBP-2463', 'CBP-1848', 'CBP-1978', 'CBP-1885', 'CBP-1887', 'CBP-1923', 'CBP-1927', 'CBP-2551', 'CBP-2550', 'CBP-2217', 'CBP-2219', 'CBP-2215', 'CBP-2218', 'CBP-2403', 'CBP-2377', 'CBP-2431', 'CBP-1961', 'CBP-1965', 'CBP-2494', 'CBP-2541')
sp3 = sp_t.get_common_ancestor('CBP-1647', 'CBP-1648', 'CBP-1705', 'CBP-1696', 'CBP-1814', 'CBP-1910', 'CBP-3035', 'CBP-2285', 'CBP-2286', 'CBP-1723', 'CBP-1838', 'CBP-1987', 'CBP-2374', 'CBP-1935', 'CBP-2405', 'CBP-2458', 'CBP-3031', 'CBP-3032', 'CBP-2440', 'CBP-2451', 'CBP-2533', 'CBP-2279', 'CBP-2507', 'CBP-2343', 'CBP-2237', 'CBP-2349', 'CBP-2365', 'CBP-2366', 'CBP-2269', 'CBP-2526', 'CBP-2489', 'CBP-2324', 'CBP-2404', 'CBP-1823', 'CBP-1804', 'CBP-1843', 'CBP-1844', 'CBP-1980', 'CBP-1975', 'CBP-1976', 'CBP-2376', 'CBP-2295', 'CBP-2367', 'CBP-2244', 'CBP-2196', 'CBP-2250', 'CBP-2348', 'CBP-2412', 'CBP-2369', 'CBP-1991', 'CBP-1992', 'CBP-2185', 'CBP-2473', 'CBP-2262', 'CBP-2310', 'CBP-2436', 'CBP-2401', 'CBP-2435', 'CBP-1704', 'CBP-2303', 'CBP-2425', 'CBP-1862', 'CBP-2287', 'CBP-2490', 'CBP-2282', 'CBP-1944', 'CBP-1947', 'CBP-2424', 'CBP-1990', 'CBP-1933', 'CBP-2280', 'CBP-2409', 'CBP-2427', 'CBP-2423', 'CBP-2531', 'CBP-2410', 'CBP-2495', 'CBP-2488', 'CBP-2406', 'CBP-1805', 'CBP-2243', 'CBP-2456', 'CBP-2499', 'CBP-2503', 'CBP-2281', 'CBP-2528', 'CBP-2535','CBP-1702', 'CBP-1718', 'CBP-3079', 'CBP-3033', 'CBP-2283', 'CBP-2284', 'CBP-1928', 'CBP-3034', 'CBP-2127', 'CBP-1817', 'CBP-2131', 'CBP-1948', 'CBP-1949', 'CBP-2163', 'CBP-2170', 'CBP-2213', 'CBP-2200', 'CBP-2193', 'CBP-2165', 'CBP-2203', 'CBP-2164', 'CBP-2198', 'CBP-2527', 'CBP-2278', 'CBP-2487', 'CBP-2419', 'CBP-2113', 'CBP-2130', 'CBP-2136', 'CBP-2122', 'CBP-2144', 'CBP-2134', 'CBP-2121', 'CBP-2140', 'CBP-2155', 'CBP-2139', 'CBP-2141', 'CBP-2150', 'CBP-2138', 'CBP-2145', 'CBP-2129', 'CBP-2438', 'CBP-2381', 'CBP-2464', 'CBP-2463', 'CBP-1848', 'CBP-1978', 'CBP-1885', 'CBP-1887', 'CBP-1923', 'CBP-1927', 'CBP-2551', 'CBP-2550', 'CBP-2217', 'CBP-2219', 'CBP-2215', 'CBP-2218', 'CBP-2403', 'CBP-2377', 'CBP-2431', 'CBP-1961', 'CBP-1965', 'CBP-2494', 'CBP-2541', 'CBP-1920', 'CBP-2214', 'CBP-2350', 'CBP-2471', 'CBP-2469', 'CBP-2433', 'CBP-2470', 'CBP-2434')
sp10 = sp_t.get_common_ancestor('CBP-1647', 'CBP-1648', 'CBP-1705', 'CBP-1696', 'CBP-1814', 'CBP-1910', 'CBP-3035', 'CBP-2285', 'CBP-2286', 'CBP-1723', 'CBP-1838', 'CBP-1987', 'CBP-2374', 'CBP-1935', 'CBP-2405', 'CBP-2458', 'CBP-3031', 'CBP-3032', 'CBP-2440', 'CBP-2451', 'CBP-2533', 'CBP-2279', 'CBP-2507', 'CBP-2343', 'CBP-2237', 'CBP-2349', 'CBP-2365', 'CBP-2366', 'CBP-2269', 'CBP-2526', 'CBP-2489', 'CBP-2324', 'CBP-2404')

sp203.add_feature("bon", "ele & soil")
sp179.add_feature("bon", "ele & soil")
sp3.add_feature("bon", "soil")
sp10.add_feature("bon", "soil")

sp_output = sp_t.write(features=["proof", "value", "bon"])
with open("sp_bon.nhx", "w") as nhx_file:
    nhx_file.write(sp_output)