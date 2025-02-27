# Tank Floodfill Demo

This repo demonstrates how an agent will move (with minimal cost) across an obstacle-riddled grid towards a command center.

## Running

`$ python3 main.py`

## Program output

The output contains the following:

- The random seed for debugging purposes.
- The grid (`A` is the agent, `C` is the command center, `#` is an obstacle).
- The cost of each cell (`.` is a truncated number greater than 9, `#` has undefined cost).
- The cardinal move the agent will take to approach the command center.

## Example outputs

```
Seed: 4500632734785793791
Grid:
+-------------------+
|# # . . # . . . # .|
|# . # . . # . # . #|
|. # . . . # . # # .|
|. # . . # . A . # .|
|# . . . . # . . . .|
|. . . . # . . . # .|
|# # . # # . . . . .|
|. # # # . # . # . .|
|. . # # . . # # C .|
|. . # # # # # . # .|
+-------------------+
Cell cost:
+-------------------+
|# # # # # . . . # #|
|# # # # # # 9 # # #|
|# # # # # # 8 # # 7|
|# # # # # 8 7 6 # 6|
|# # # # # # 6 5 6 5|
|# # # # # 6 5 4 # 4|
|# # # # # 5 4 3 2 3|
|# # # # # # 5 # 1 2|
|# # # # # # # # 0 1|
|# # # # # # # # # 2|
+-------------------+
Cardinal move: W
```

```
Seed: 6279981314768827316
Grid:
+-------------------+
|. . A # . . . . . .|
|. . # . . . . # . .|
|. # . . . . . . . #|
|. . # . # . # . . .|
|# # . # . # C # # .|
|. # . . . . # . . #|
|. . . # # # # . . .|
|. . # . . . # . . #|
|. # . . . # . . . .|
|. . . . # . . . . #|
+-------------------+
Cell cost:
+-------------------+
|# # # # # # # # # #|
|# # # # # # # # # #|
|# # # # # # # # # #|
|# # # # # # # # # #|
|# # # # # # 0 # # #|
|# # # # # # # # # #|
|# # # # # # # # # #|
|# # # # # # # # # #|
|# # # # # # # # # #|
|# # # # # # # # # #|
+-------------------+
Agent is blocked! :(
Cardinal move: X
```
