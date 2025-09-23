# Gephi Session Notes
> Open friends_main.gexf
> Three finger double tap to activate zoom. Three finger double tap and drag to alter zoom amount.

## Interface overview

1. Main window
2. Nodes and edges numbers
3. Note the various appearance, layout and filter sections.
4. Data lab view

## Visual Adjustments

1. Resize nodes by n_scenes (10,20)
2. Color nodes by anxiety
3. Add node labels
4. Show edge labels of weight

## Layouts

### Fruchterman Rheingold
Think of edges as springs, where nodes are repelled but stronger edges pull nodes back together. In dense networks like this you’ll end up with this kind of equidistant layout.

### Force Atlas
Force Atlas is similar, but runs constantly, nodes bouncing off one another and updating each other’s position. Eventually it reaches a convergence but you need to turn it off.
- Key settings are usually Normalize edge weights, as high value edge weights can make finding a shape difficult, and prevent overlap.
- Show magnifying glass to relocate missing networks.
- Can either use the ‘Scaling’ value to space out the nodes a bit OR
-  Use the expansion layout to scale it up

## Scaling Up

> Switch to larger dataset friends.gexf

- Note the number of nodes and edges
- Scan through the nodes and edges tables

### Splines

- Resize by n_scenes again
  - Default is linear, higher the number bigger the node. Our data is very skewed. The majority of characters have very few scenes, whilst the six main ones have 1000+.
  - However a character with 50 scenes when the majority have 1 is still significant, even if the mains have thousands.
- Spline button
  - Graphs show node size change over the range of values. Left to right, smallest to largest node value. Bottom to top is change in node size. Currently it is linear, every step up in node value means a step up in node size. But if we switch to a different shape we can emphasise more change in the lower value ranges, and not worry so much about the top. Template 2

## Filtering 

- Layout data again - Don't normalise edge weight this time, try scaling.
- Big mess, need to filter.

### Filtering by Attribute

- Use Statistics average degree to calculate the degree for each node.
- Filter by degree, anyone with that has interacted with only one other character.
- Remove anyone with less than 5 scenes.
  - Attributes > Range > n_scenes
- Keep in mind, if we had filtered by n_scenes first, then calculated degree, the result would be different, because we'd have cut off a lot of edges before calculating.
- Now try redoing the layout.
- Redo the sizing - Make sure to press the 'local scale' button. This means sizing is based on whats visible, not ther whole dataset.
- Use expansion and label adjust layouts to finesse the final positions.
- Try coloring by ranking instead, showing n_scenes decreasing as you move further from the centre.

## Communities

> Switch to GOT Data

- Review the data again
- Layout the unfiltered data with force atlas 2.
- Resize by n_scenes. This time because the show is less focussed on a core of characters a linear Spline may be more appropriate.
- Set decent sized labels then run label adjust
- Color by house

Currently looking at our graph, we can see that in some areas, certain houses are clustered together, whilst others are spread. Think about what this graph is showing us. It is co-occurrence of characters in a scene, not necessarily family relations between those characters. Characters are closer if they interact more acrosss the series.

- Let's trim off any characters with less than 20 scenes.
- Run modularity. Increasing resolution to 1.2 improves score past 0.4.
- This now looks like storylines, or regions (The Wall, Daenerys across the ocean away from Westeros, the Lannisters in Kings Landing, then for Bran, Robb and Catelyn - elsewhere, North/Winterfell/Riverfell )
- It's not a perfect divison, (Arya moves all over)

## Partitioning

- Partition allows you to select a group of nodes and associated edges. Selecting more than one partition shows you multiple groups and edges between them.
- Partition to just show the Stark House.
- Re-run avg weighted degree. Reapply it to the size of the nodes.
- Re-layout - Shows us the extent to which Starks interacted with one another and which characters had overall most interaction by weighted degree.

## Exporting

- You can save your work in gephi as a Gephi file, retaining all your changes and filters.
- You can also export to an image or PDF using Preview.
- Usually default straight, with some tweaks...
  - rescale weight for edges. Adjust font size for labels. If sizes seem tricky try going back to the overview and using the expansion layout to make the whole graph bigger. (contraction for smaller.)
- Hit refresh to see changes
- When ready select export button
- Choose file type
- Options, recommend setting to 4096*4096 - multiples of 1024,  to ensure good size to examine.