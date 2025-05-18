import osmnx as ox

place_name = "Cống Vị, Ba Đình, Hà Nội, Việt Nam"
G = ox.graph_from_place(place_name, network_type="all", simplify=False)

ox.save_graphml(G, "congvi_badinh_hanoi_graph2.graphml")
print("Done!")
