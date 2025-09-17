import pandas as pd
from pathlib import Path
import networkx as nx

data_dir = Path("_HP_data")
dialogue_path = data_dir / Path("Dialogue.csv")
character_path = data_dir / Path("Characters.csv")
output_path = Path("HP.gexf")


df = pd.read_csv(dialogue_path, encoding="unicode_escape")
characters = pd.read_csv(character_path, encoding="unicode_escape")

chars_per_scene_place = df.groupby(["Chapter ID", "Place ID"], as_index=False).agg(
    characters=("Character ID", list)
)
chars_per_scene_place["characters"] = chars_per_scene_place["characters"].apply(
    lambda x: list(set(x))
)
chars_per_scene_place["scene_ID"] = (
    chars_per_scene_place["Chapter ID"].astype("string")
    + "_"
    + chars_per_scene_place["Place ID"].astype("string")
)
chars_per_scene_place = chars_per_scene_place.set_index("scene_ID")

dummies = pd.get_dummies(
    chars_per_scene_place.explode("characters")["characters"], dtype=int
)
n_scenes = dummies.sum(axis=0).rename("n_scenes")
characters["House"] = characters["House"].fillna("None")
characters = characters.merge(
    n_scenes, left_on="Character ID", right_index=True, how="left"
)
character_attr = (
    characters.set_index("Character ID")[["Character Name", "House", "n_scenes"]]
    .rename(columns={"Character Name": "Label", "House": "house"})
    .to_dict(orient="index")
)

per_scene_dummies = dummies.groupby(level=0).sum()
adjacency = per_scene_dummies.T.dot(per_scene_dummies)

G = nx.from_pandas_adjacency(adjacency)
G.remove_edges_from(list(nx.selfloop_edges(G)))
nx.set_node_attributes(G, character_attr)
nx.write_gexf(G, output_path)
