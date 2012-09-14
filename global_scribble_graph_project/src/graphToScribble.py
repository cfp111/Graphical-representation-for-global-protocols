'''
Created on 17 juil. 12

@author: Charlotte
'''

# This file allows to get the Scribble global protocol from the specification of a graph
# using the graphic tools defined in the extensions file.

import sys
from ext import extensions
import graphCreation

def main(args):
    # define a name for the protocol
    name = "TestG1"
    
    # create a new graph
    graph = extensions.SGraph(name)
    
    # execute the graph's commands like add_Snode, add_Sedge, etc.
    # these commands are specified in a method test(graph), defined in graphCreation
    graphCreation.test(graph)
    
    # draw the built graph in a 'png' file
    graph.write_png(name+".png")
    
    # write the corresponding Scribble global protocol in a text file
    # define first the name of the file
    filename = "test1"
    f = open(filename+".spr","w")
    f.write(graph.toScribble())
    f.close()

if __name__ == "__main__":
    sys.exit (main (sys.argv))