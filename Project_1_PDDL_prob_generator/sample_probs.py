"""
File: sample_probs.py
Author: Dana Nau <nau@cs.umd.edu>
Last updated: Feb 18, 2020

These are some made-by-hand test problems for Project 1

Here's a list of all the test problems in this file,
roughly in increasing order of difficulty:

[rect20, rect20a, rect20b, rect20c, rect20d, rect20e, rect50, wall8a, wall8b, \
    lhook16, rhook16a, rhook16b, spiral16, spiral24, pdes30, pdes30b, \
    rectwall8, rectwall16, rectwall32, rectwall32a, twisty0]

Each test problem is a list of the form [p0, finish, walls], where
   p0 is the starting point;
   finish is the finish line;
   walls is a list of walls.

If you want to see what one of the problems (say, rect20a) looks like,
you can do it like this:

   import sample_probs, tdraw
   tdraw.draw_problem(sample_probs.rect20a, title='rect20a')

If you have a heuristic named h1 in a file named heuristics.py, and you
want GBF to use it on rect20a, you can do it like this:

   import racetrack, sample_probs, heuristics
   racetrack.main(sample_probs.rect20a, 'gbf', heuristics.h1, 1, 1, 'rect20a')
"""

# A small rectangular region, with no obstacles in the way. There are four
# different orientations of the starting point and finish line, so you can
# check whether you're handling your x and y coordinates consistently.

rect20 = [(9,10), [(15,8),(15,12)],
    [[(0,0),(20,0)], [(20,0),(20,20)], [(20,20),(0,20)], [(0,20),(0,0)]]]

rect20a = [(5,12), [(15,5),(15,15)],
    [[(0,0),(20,0)], [(20,0),(20,20)], [(20,20),(0,20)], [(0,20),(0,0)]]]

rect20b = [(15,12), [(5,5),(5,15)],
    [[(0,0),(20,0)], [(20,0),(20,20)], [(20,20),(0,20)], [(0,20),(0,0)]]]

rect20c = [(12,5), [(5,15),(15,15)],
    [[(0,0),(20,0)], [(20,0),(20,20)], [(20,20),(0,20)], [(0,20),(0,0)]]]

rect20d = [(12,15), [(5,5),(15,5)],
    [[(0,0),(20,0)], [(20,0),(20,20)], [(20,20),(0,20)], [(0,20),(0,0)]]]

rect20e = [(12,15), [(1,5),(10,5)],
    [[(0,0),(20,0)], [(20,0),(20,20)], [(20,20),(0,20)], [(0,20),(0,0)]]]


# A larger rectangular region, with the starting point farther from the finish
# line. This is useful for testing whether you're overshooting.

rect50 = [(3,40), [(30,10),(30,30)],
    [[(0,0),(50,0)], [(50,0),(50,50)], [(50,50),(0,50)], [(0,50),(0,0)]]]

# the finish line is behind a wall

wall8a = [(2,1), [(4,5),(5,5)],
    [[(0,0),(8,0)], [(8,0),(8,8)], [(8,8),(0,8)], [(0,8),(0,0)], [(4,0),(4,5)]]]

wall8b = [(2,1), [(4,1),(5,1)],
    [[(0,0),(8,0)], [(8,0),(8,8)], [(8,8),(0,8)], [(0,8),(0,0)], [(4,0),(4,5)]]]


lhook16 = [(2,1), [(13,1),(14,1)],
    [[(0,0),(16,0)], [(16,0),(16,16)], [(16,16),(0,16)], [(0,16),(0,0)], [(9,0),(9,11)], [(9,11),(6,11)], [(6,11),(6,7)]]]

rhook16a = [(2,2), [(10,7),(11,7)],
    [[(0,0),(16,0)], [(16,0),(16,16)], [(16,16),(0,16)], [(0,16),(0,0)], [(4,0),(4,12)], [(4,12),(12,12)], [(12,12),(12,5)]]]

rhook16b = [(2,2), [(10,7),(11,7)],
    [[(0,0),(16,0)], [(16,0),(16,16)], [(16,16),(0,16)], [(0,16),(0,0)], [(4,0),(4,12)], [(4,12),(12,12)], [(12,12),(12,4)]]]

# a spiral-shaped wall

spiral16 = [(2,2), [(10,6),(11,6)],
    [[(0,0),(16,0)], [(16,0),(16,16)], [(16,16),(0,16)], [(0,16),(0,0)], [(4,0),(4,12)], [(4,12),(12,12)], [(12,12),(12,4)], [(12,4),(8,4)], [(8,4),(8,8)]]]

spiral24 = [(3,3), [(15,10),(17,10)],
    [[(0,0),(24,0)], [(24,0),(24,24)], [(24,24),(0,24)], [(0,24),(0,0)], [(6,0),(6,18)], [(6,18),(18,18)], [(18,18),(18,6)], [(18,6),(12,6)], [(12,6),(12,12)]]]

# the example in the project description, and a variant with the wall farther down

pdes30 = [(4,5), [(24,8),(26,8)],
    [[(0,0),(10,0)], [(10,0),(10,10)], [(10,10),(20,10)], [(20,10),(30,0)], [(30,0),(30,10)], [(30,10),(10,20)], [(10,20),(0,20)], [(0,20),(0,0)], [(3,14),(10,14)], [(10,14),(10,16)], [(10,16),(3,16)], [(3,16),(3,14)]]]

pdes30b = [(4,5), [(28,3),(29,3)],
    [[(0,0),(10,0)], [(10,0),(10,10)], [(10,10),(20,10)], [(20,10),(30,0)], [(30,0),(30,10)], [(30,10),(10,20)], [(10,20),(0,20)], [(0,20),(0,0)], [(3,14),(10,14)], [(10,14),(10,16)], [(10,16),(3,16)], [(3,16),(3,14)]]]

# the finish line is behind a wall that's connected to a rectangular obstacle

rectwall8 = [(3,1), [(5,1),(6,1)],
    [[(0,0),(8,0)], [(8,0),(8,8)], [(8,8),(0,8)], [(0,8),(0,0)], [(4,0),(4,2)], [(3,2),(5,2)], [(5,2),(5,6)], [(5,6),(3,6)], [(3,6),(3,2)]]]

rectwall16 = [(6,2), [(10,2),(12,2)],
    [[(0,0),(16,0)], [(16,0),(16,16)], [(16,16),(0,16)], [(0,16),(0,0)], [(8,0),(8,4)], [(6,4),(10,4)], [(10,4),(10,12)], [(10,12),(6,12)], [(6,12),(6,4)]]]

rectwall32 = [(12,4), [(20,4),(24,4)],
    [[(0,0),(32,0)], [(32,0),(32,32)], [(32,32),(0,32)], [(0,32),(0,0)], [(16,0),(16,8)], [(12,8),(20,8)], [(20,8),(20,24)], [(20,24),(12,24)], [(12,24),(12,8)]]]

rectwall32a = [(12,4), [(20,4),(24,4)],
    [[(0,0),(32,0)], [(32,0),(32,32)], [(32,32),(0,32)], [(0,32),(0,0)], [(16,0),(16,8)], [(12,8),(20,8)], [(20,8),(20,22)], [(20,22),(12,22)], [(12,22),(12,8)], [(16,32),(16,24)]]]

# Warning: the next one is *very* hard

twisty0 = [(60, 58), [(2, 4), (7, 4)], [[(6, 1), (10, 7)], [(10, 7), (14, 8)], [(14, 8), (16, 8)], [(16, 8), (20, 9)], [(20, 9), (27, 12)], [(27, 12), (28, 12)], [(28, 12), (28, 10)], [(28, 10), (26, 4)], [(26, 4), (27, 2)], [(27, 2), (29, 0)], [(29, 0), (34, 0)], [(34, 0), (43, 3)], [(43, 3), (47, 3)], [(47, 3), (52, 4)], [(52, 4), (56, 4)], [(56, 4), (57, 6)], [(57, 6), (57, 10)], [(57, 10), (55, 12)], [(55, 12), (52, 16)], [(52, 16), (50, 18)], [(50, 18), (53, 19)], [(53, 19), (58, 21)], [(58, 21), (62, 24)], [(62, 24), (62, 26)], [(62, 26), (62, 30)], [(62, 30), (61, 34)], [(61, 34), (57, 35)], [(57, 35), (51, 35)], [(51, 35), (45, 35)], [(45, 35), (42, 29)], [(42, 29), (39, 26)], [(39, 26), (37, 24)], [(37, 24), (34, 22)], [(34, 22), (32, 25)], [(32, 25), (30, 29)], [(30, 29), (28, 32)], [(28, 32), (26, 34)], [(26, 34), (22, 34)], [(22, 34), (19, 30)], [(19, 30), (17, 27)], [(17, 27), (15, 24)], [(15, 24), (14, 22)], [(14, 22), (12, 24)], [(12, 24), (9, 26)], [(9, 26), (7, 29)], [(7, 29), (6, 33)], [(6, 33), (8, 36)], [(8, 36), (11, 38)], [(11, 38), (16, 39)], [(16, 39), (18, 43)], [(18, 43), (19, 46)], [(19, 46), (19, 50)], [(19, 50), (16, 53)], [(16, 53), (12, 54)], [(12, 54), (9, 55)], [(9, 55), (10, 57)], [(10, 57), (15, 57)], [(15, 57), (27, 54)], [(27, 54), (29, 54)], [(29, 54), (33, 48)], [(33, 48), (38, 40)], [(38, 40), (39, 38)], [(39, 38), (44, 52)], [(44, 52), (46, 55)], [(46, 55), (48, 53)], [(48, 53), (54, 42)], [(54, 42), (62, 58)], [(62, 58), (60, 60)], [(60, 60), (55, 54)], [(55, 54), (54, 48)], [(54, 48), (53, 54)], [(53, 54), (53, 57)], [(53, 57), (52, 61)], [(52, 61), (50, 62)], [(50, 62), (45, 62)], [(45, 62), (43, 61)], [(43, 61), (42, 58)], [(42, 58), (39, 46)], [(39, 46), (38, 45)], [(38, 45), (36, 52)], [(36, 52), (33, 57)], [(33, 57), (11, 62)], [(11, 62), (4, 62)], [(4, 62), (1, 61)], [(1, 61), (0, 58)], [(0, 58), (0, 53)], [(0, 53), (9, 51)], [(9, 51), (16, 46)], [(16, 46), (15, 45)], [(15, 45), (12, 43)], [(12, 43), (3, 42)], [(3, 42), (0, 35)], [(0, 35), (0, 32)], [(0, 32), (1, 26)], [(1, 26), (2, 22)], [(2, 22), (8, 19)], [(8, 19), (12, 17)], [(12, 17), (16, 20)], [(16, 20), (20, 26)], [(20, 26), (21, 28)], [(21, 28), (25, 30)], [(25, 30), (26, 28)], [(26, 28), (26, 26)], [(26, 26), (26, 21)], [(26, 21), (29, 20)], [(29, 20), (33, 18)], [(33, 18), (36, 18)], [(36, 18), (39, 20)], [(39, 20), (43, 24)], [(43, 24), (45, 26)], [(45, 26), (47, 29)], [(47, 29), (51, 29)], [(51, 29), (55, 29)], [(55, 29), (56, 28)], [(56, 28), (56, 26)], [(56, 26), (55, 24)], [(55, 24), (51, 21)], [(51, 21), (47, 20)], [(47, 20), (44, 18)], [(44, 18), (44, 16)], [(44, 16), (48, 14)], [(48, 14), (51, 11)], [(51, 11), (53, 9)], [(53, 9), (52, 8)], [(52, 8), (51, 7)], [(51, 7), (46, 6)], [(46, 6), (40, 8)], [(40, 8), (37, 8)], [(37, 8), (34, 6)], [(34, 6), (32, 3)], [(32, 3), (30, 4)], [(30, 4), (29, 7)], [(29, 7), (30, 8)], [(30, 8), (32, 11)], [(32, 11), (33, 14)], [(33, 14), (27, 16)], [(27, 16), (22, 16)], [(22, 16), (19, 12)], [(19, 12), (17, 11)], [(17, 11), (14, 12)], [(14, 12), (8, 12)], [(8, 12), (4, 9)], [(4, 9), (1, 4)], [(1, 4), (0, 3)], [(0, 3), (3, 2)], [(3, 2), (6, 1)], [(6, 1), (6, 1)], [(29, 22), (28, 24)], [(28, 24), (28, 25)], [(28, 25), (28, 26)], [(28, 26), (29, 25)], [(29, 25), (30, 24)], [(30, 24), (30, 22)], [(30, 22), (30, 22)], [(30, 22), (29, 22)], [(47, 57), (46, 57)], [(46, 57), (45, 58)], [(45, 58), (46, 60)], [(46, 60), (48, 60)], [(48, 60), (51, 58)], [(51, 58), (50, 57)], [(50, 57), (48, 57)], [(48, 57), (47, 57)], [(8, 58), (7, 57)], [(7, 57), (6, 57)], [(6, 57), (6, 57)], [(6, 57), (6, 58)], [(6, 58), (7, 59)], [(7, 59), (8, 59)], [(8, 59), (8, 59)], [(8, 59), (8, 58)], [(3, 57), (3, 56)], [(3, 56), (2, 55)], [(2, 55), (1, 56)], [(1, 56), (2, 58)], [(2, 58), (3, 60)], [(3, 60), (3, 58)], [(3, 58), (3, 57)], [(3, 57), (3, 56)], [(7, 37), (6, 35)], [(6, 35), (4, 34)], [(4, 34), (4, 35)], [(4, 35), (5, 36)], [(5, 36), (5, 37)], [(5, 37), (6, 37)], [(6, 37), (6, 37)], [(6, 37), (7, 37)]]]