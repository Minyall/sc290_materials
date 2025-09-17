# https://www.kaggle.com/datasets/sujaykapadnis/friends/data


import pandas as pd
from pathlib import Path
import numpy as np
import networkx as nx

friends_path = Path("_friends_data", "friends.csv")
export_edge_path = Path("friends_edges.csv")
export_node_path = Path("friends_nodes.csv")

all_export_edge_path = Path("all_friends_edges.csv")
all_export_node_path = Path("all_friends_nodes.csv")

friends = pd.read_csv(friends_path)
friends["scene_id"] = (
    friends["season"].astype("string")
    + "_"
    + friends["episode"].astype("string")
    + "_"
    + friends["scene"].astype("string")
)

exclude = ["#ALL#", "Scene Directions"]

friends = friends[~friends["speaker"].isin(exclude)].reset_index(drop=True)
scenes_per_char = friends.groupby("speaker").agg(n_scenes=("scene_id", "nunique"))

# ALL Characters
per_scene = friends.groupby("scene_id").agg(scene_chars=("speaker", list))
per_scene["scene_chars"] = per_scene["scene_chars"].apply(lambda x: list(set(x)))
per_scene = per_scene[per_scene["scene_chars"].str.len() > 0]

dummies = pd.get_dummies(per_scene.explode("scene_chars")["scene_chars"], dtype=int)
dummies = dummies.groupby(level=0).sum()

matrix = dummies.T.dot(dummies)

G = nx.from_pandas_adjacency(matrix)
G.remove_edges_from(list(nx.selfloop_edges(G)))

nodes = pd.DataFrame({"name": list(G.nodes)})
nodes = nodes.merge(scenes_per_char, how="left", left_on="name", right_index=True)

node_attr = nodes.set_index('name').to_dict(orient='index')

nx.set_node_attributes(G,node_attr)

edges = nx.to_pandas_edgelist(G)

edges.to_csv(all_export_edge_path)
nodes.to_csv(all_export_node_path)

nx.write_gexf(G, "friends.gexf")

# MAIN CHARACTERS

# 5. By Level of Neuroticism/Anxiety:

# High Anxiety/Obsessive Tendencies: Monica, Chandler. 
#  Monica with her obsessive-compulsive tendencies and Chandler 
#   with his insecurities and anxieties.

# Moderate Anxiety/Insecurities: Ross, Rachel. 
# Ross has relationship anxieties, Rachel with her career.

# Low Anxiety/Carefree: Phoebe, Joey. T
# hey tend to be more accepting of life's ups and downs and less prone to overthinking.

anxiety_map = {'Monica Geller':'High',
               'Chandler Bing':'High',
               'Ross Geller': 'Moderate',
               'Rachel Green': 'Moderate',
               'Joey Tribbiani':'Low',
               'Phoebe Buffay':'Low'
}

main_chars = friends["speaker"].value_counts().head(6).index
friends = friends[friends["speaker"].isin(main_chars)]

per_scene = friends.groupby("scene_id").agg(scene_chars=("speaker", list))
per_scene["scene_chars"] = per_scene["scene_chars"].apply(lambda x: list(set(x)))
per_scene = per_scene[per_scene["scene_chars"].str.len() > 0]

dummies = pd.get_dummies(per_scene.explode("scene_chars")["scene_chars"], dtype=int)
dummies = dummies.groupby(level=0).sum()

matrix = dummies.T.dot(dummies)

G = nx.from_pandas_adjacency(matrix)
G.remove_edges_from(list(nx.selfloop_edges(G)))

nodes = pd.DataFrame({"name": list(G.nodes)})
nodes['anxiety'] = nodes['name'].map(anxiety_map)
nodes = nodes.merge(scenes_per_char, how="left", left_on="name", right_index=True)


node_attr = nodes.set_index('name').to_dict(orient='index')

nx.set_node_attributes(G,node_attr)
edges = nx.to_pandas_edgelist(G)

# edges.to_csv(export_edge_path)
# nodes.to_csv(export_node_path)
nx.write_gexf(G, "friends_main.gexf")
