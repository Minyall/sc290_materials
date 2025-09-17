import pandas as pd
import networkx as nx
from collections import Counter
from pathlib import Path

GOT_dir = Path("_GOT_data")
char_path = GOT_dir / Path("characters-groups.json")
episode_path = GOT_dir / Path("episodes.json")

export_edge_path = Path("GOT_edges.csv")
export_node_path = Path("GOT_nodes.csv")

char_groups = (
    pd.json_normalize(pd.read_json(char_path)["groups"])
    .explode("characters")
    .rename(columns={"name": "house", "characters": "name"})
    .drop_duplicates(subset=["name"])
)

char_list = char_groups["name"].tolist()

eps = pd.read_json(episode_path)
eps = pd.json_normalize(eps["episodes"])


scenes = [scene for episode in eps["scenes"].tolist() for scene in episode]
scene_counts = Counter()
data = []
for s in scenes:
    scene_chars = []
    for char in s["characters"]:
        if char["name"] in char_list:
            scene_chars.append(char["name"])
    scene_counts.update(scene_chars)
    data.append(scene_chars)

data = [x for x in data if len(x) > 1]
n_valid_scenes = len(data)

data = pd.Series(data, name="character").to_frame()
data = pd.get_dummies(data.explode("character")["character"], dtype=int)
data = data.groupby(level=0).sum()
assert data.shape[0] == n_valid_scenes

adjacency = data.T.dot(data)

G = nx.from_pandas_adjacency(adjacency)


G.remove_edges_from(list(nx.selfloop_edges(G)))

nodes = pd.DataFrame({"name": list(G.nodes)})
nodes = nodes.merge(char_groups, on="name", how="left")
nodes = nodes.merge(
    pd.Series(scene_counts, name="n_scenes"),
    how="left",
    left_on="name",
    right_index=True,
)

edges = nx.to_pandas_edgelist(G)

edges.to_csv(export_edge_path)
nodes.to_csv(export_node_path)

nx.write_gexf(G,'GOT_graph.gexf')
