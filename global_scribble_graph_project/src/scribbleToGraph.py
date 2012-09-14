'''
Created on 10 juil. 12

@author: Charlotte
'''
import sys
import antlr3
from ext import extensions
from antlr_pydot.global_scribble_graphLexer import global_scribble_graphLexer
from antlr_pydot.global_scribble_graphParser import global_scribble_graphParser
from antlr_pydot.global_scribble_graph_tree import global_scribble_graph_tree

def main (argv):
    # first step: parse the global protocol into a tree
    filename = "C:/Users/Charlotte/Documents/Imperial/course/IndividualProject/workspaceProject/global_scribble_graph_project/protocols/TestDoubleRecursion.spr"
    input = antlr3.FileStream (filename)
    lexer = global_scribble_graphLexer (input)
    tokens = antlr3.CommonTokenStream (lexer)
    parser = global_scribble_graphParser (tokens)
    res = parser.protocolDef ()
    root = res.tree

    # second step: walk through the tree
    nodes = antlr3.tree.CommonTreeNodeStream(root)
    nodes.setTokenStream(tokens)
    result = global_scribble_graph_tree(nodes)
    
    # third step: create the graph
    graph = extensions.SGraph("G")
    result.protocolDef(graph)
    

if __name__ == "__main__":
    sys.exit (main (sys.argv))