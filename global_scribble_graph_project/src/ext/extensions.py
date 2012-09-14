'''
Created on 16 juil. 12

@author: Charlotte
'''
import pydot


class SGraph(pydot.Dot):
    
    # extends the class Dot, a derived class of Graph with a new method: get_edge_src
    
    def __init__(self, graph_name = '', graph_type = 'digraph', splines ='polyline', obj_dict=None,*args1, **argsd):
        pydot.Dot.__init__(self, graph_name = graph_name, graph_type = graph_type, splines = splines,obj_dic = obj_dict,*args1, **argsd)
        
        if obj_dict is None:
            self.obj_dict['roles']=[]
            #self.obj_dict['type']= graph_type
            #self.obj_dict['splines']='polyline'
            #if name is not None:
                #self.set_name(name)
        
        
    def get_edge_src(self, src):
        """Get the list of Edge instances which source is src.
        """
        edge_objs = list()
                           
        for edge, obj_dict_list in self.obj_dict['edges'].iteritems():
            if edge[0] == src:
                edge_objs.extend( [ SEdge( obj_dict = obj_d ) for obj_d in obj_dict_list ] )
        
        return edge_objs
    
    def add_Snode(self,snode):
        """Adds a SNode object to the graph and store the roles.

        It takes a node object as its only argument and returns
        None.
        """
        
        if isinstance(snode, Message):

            self.add_role(snode.get_role1())
            self.add_role(snode.get_role2())
            
        if isinstance(snode, Choice):
            self.add_role(snode.get_role())
        
        self.add_node(snode)
        
    def add_role(self, role):
        
        if isinstance(role,str):
            roles_list = self.obj_dict['roles']
            if role not in roles_list:
                self.obj_dict['roles']= roles_list+[role]
            
        
    def get_Snode(self, name):
        """Retrieve a node from the graph.
        
        Given a node's name the corresponding Node
        instance will be returned.
        
        If one or more nodes exist with that name a list of
        Node instances is returned.
        An empty list is returned otherwise.
        """
        
        match = list()
        
        if self.obj_dict['nodes'].has_key(name):
            
            for obj_dict in self.obj_dict['nodes'][name]:
                if obj_dict['activity']=='start':
                    match.append( Start( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='end':
                    match.append( End( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='choice':
                    match.append( Choice( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='merge':
                    match.append( Merge( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='fork':
                    match.append( Fork( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='join':
                    match.append( Join( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='msg':
                    match.append( Message( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='rec':
                    match.append( Rec( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='interrupt':
                    match.append( Interrupt( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='slot':
                    match.append( TimeSlot( obj_dict = obj_dict ) )
                elif obj_dict['activity']=='delay':
                    match.append( Delay( obj_dict = obj_dict ) )
                    
        subgraphs = self.get_Ssubgraph_list()
        for s in subgraphs:
            match.extend(s.get_Snode(name))
        return match
    
    def add_Sedge(self,edge):
        
        source = self.get_Snode(edge.get_source())[0]
        
        destination = self.get_Snode(edge.get_destination())[0]
        
        if source.get_activity() == 'rec':
            edge.set_tailport('s')
        elif source.get_activity() == 'msg':
            edge.set_tailport('s')
        elif source.get_activity() == 'merge':
            edge.set_tailport('s')
        elif source.get_activity() == 'join':
            edge.set_tailport('s')
        elif source.get_activity() == 'interrupt':
            edge.set_tailport('s')
        elif source.get_activity() == 'start':
            edge.set_tailport('s')
        elif source.get_activity() == 'slot':
            edge.set_tailport('s')
        elif source.get_activity() == 'delay':
            edge.set_tailport('s')
            
            
        if destination.get_activity() == 'rec':
            if destination.get_port_flag():
                edge.set_headport('e')
                destination.set_port_flag(False)
            else:
                edge.set_headport('n')
        elif destination.get_activity() == 'msg':
            edge.set_headport('n')
        elif destination.get_activity() == 'choice':
            edge.set_headport('n')
        elif destination.get_activity() == 'fork':
            edge.set_headport('n')
        elif destination.get_activity() == 'interrupt':
            edge.set_headport('n')
        elif destination.get_activity() == 'slot':
            edge.set_headport('n')
        elif destination.get_activity() == 'end':
            edge.set_headport('n')
        elif destination.get_activity() == 'delay':
            edge.set_headport('n')
        
        self.add_edge(edge)
        
    def add_Sedge_with_ports(self, edge, h, t):
        
        edge.set_headport(h)
        edge.set_tailport(t)
        
        self.add_edge(edge)
    
    def add_Sedge_with_label(self, edge, label):
        
        edge.set_label(label)
        
        self.add_Sedge(edge)
    
    def get_Ssubgraph_list(self):
        """Get the list of Subgraph instances.
        
        This method returns the list of Subgraph instances
        in the graph.
        """
        
        sgraph_objs = list()
        
        for sgraph, obj_dict_list in self.obj_dict['subgraphs'].iteritems():
                sgraph_objs.extend( [ SSubgraph( obj_dict = obj_d ) for obj_d in obj_dict_list ] )
        
        return sgraph_objs
    
    def toScribble(self):
        protocoldcl = "global protocol "+self.get_name()+"("
        roles_list = self.obj_dict['roles']
        for i in range(0 ,len(roles_list)):
            protocoldcl = protocoldcl+"role "+roles_list[i]
            if i<len(roles_list)-1:
                protocoldcl = protocoldcl+", "
        protocoldcl=protocoldcl+")"
        
        # assumption: there is only one start node
        start = self.get_Snode('start')[0]
        
        return protocoldcl+start.toScribble(self)
    
class SSubgraph(SGraph, pydot.Subgraph):
    
    def __init__(self, graph_name='', obj_dict=None, suppress_disconnected=False,
        simplify=False, **attrs):
        
        SGraph.__init__(self, graph_name=graph_name, obj_dict=obj_dict,
            suppress_disconnected=suppress_disconnected, simplify=simplify, **attrs)
        pydot.Subgraph.__init__(self, graph_name=graph_name, obj_dict=obj_dict,
            suppress_disconnected=suppress_disconnected, simplify=simplify, **attrs)

        if obj_dict is None:

            self.obj_dict['type'] = 'subgraph'
    
class SEdge(pydot.Edge):
    
    def __init__(self, src='', dst='', obj_dict=None, **attrs):
        pydot.Edge.__init__(self, src=src, dst=dst, obj_dict=obj_dict, **attrs)
        
        #if obj_dict is None:
            #self.obj_dict['style']='solid'
        
    def set_tailport(self,value):
        
        self.obj_dict['attributes']['tailport'] = value
        
    def set_headport(self,value):
        
        self.obj_dict['attributes']['headport'] = value
        
    def set_minlen(self, value):
        
        self.obj_dict['minlen'] = value
        
    def set_label(self,label):
        
        self.obj_dict['attributes']['label']=label

    
class SNode(pydot.Node):
    
    def __init__(self, name = '', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, obj_dict = None, **attrs)
        
    
    def get_activity(self):
        
        return self.obj_dict['activity']
        
    def addIndent(self,indent):
        code = "\n"
        for i in range(0,indent+1):
            code = code + "   "
        return code
    
    def next_nodes(self, graph):
        edges =graph.get_edge_src(self.get_name())
        names =[]
        next_nodes = []
        for e in edges:
            names = names+[e.get_destination()]
        for n in names:
            next_nodes = next_nodes + graph.get_Snode(n)
        return next_nodes
    
    def toScribble(self, graph, indent):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
        
    
class Start(SNode):
    
    def __init__(self, name = 'start', label = " ", shape = 'circle', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label = label, shape = shape, obj_dict = obj_dict, **attrs)

        if obj_dict is None:
            self.obj_dict['activity']='start'
        
    def toScribble(self,graph):
        # assumption: there is only one edge and one node linked to the start node
        next_node = self.next_nodes(graph)[0]
        c = next_node.toScribble(graph, 0)[0]
        code = "{" + c +"\n}"
        return code
    
        
        
class End(SNode):
    
    def __init__(self, name = 'end', label=" ", style="bold", shape="circle", penwidth = 4.0, obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label= label, style = style, shape = shape, penwidth = penwidth, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='end'
        
    def toScribble(self,graph,indent):
        
        return " ",None

class Choice(SNode):
    
    def __init__(self, name = '', role = '', label ="+", shape='diamond', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label = label, shape = shape, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='choice'
            self.obj_dict['role']=role
            
    def get_role(self):
        """Get the node's role."""
        
        return self.obj_dict['role']
        
    def toScribble(self,graph,indent):
        flag = False
        node = None
        next_nodes = self.next_nodes(graph)
        code = self.addIndent(indent)
        code = code + "choice at "+ self.get_role() + " {"
        c0, n0 = next_nodes[0].toScribble(graph, indent+1)
        if n0 is None:
            flag = True
        else:
            node = n0
        code = code + c0
        code = code +self.addIndent(indent)+"}"
        for i in range(1,len(next_nodes)):
            c, n = next_nodes[i].toScribble(graph, indent+1)
            if not flag and n is None:
                flag = True
                node = None                
            code = code +self.addIndent(indent)+ "or{"
            code = code + c
            code = code +self.addIndent(indent)+ "}"
        if node is None:
            return code,None
        else:
            co, no = node.toScribble(graph, indent)
            return code + co , no
    
    
        
class Merge(SNode):
    
    def __init__(self, name = '', label="+", style='bold', shape='diamond', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label = label, style = style, shape = shape, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='merge'
            
    def toScribble(self, graph, indent):
        next_node = self.next_nodes(graph)[0]
        
        return " ", next_node
            
            
class Fork(SNode):
    
    def __init__(self, name = '', label = "|", shape = 'diamond', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label = label, shape = shape, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='fork'
            
    def toScribble(self, graph, indent):
        flag = False
        node = None
        next_nodes = self.next_nodes(graph)
        code = self.addIndent(indent)
        code = code + "par{"
        c0, n0 = next_nodes[0].toScribble(graph, indent+1)
        if n0 is None:
            flag = True
        else:
            node = n0
        code = code + c0
        code = code + self.addIndent(indent)+"}"
        for i in range(1,len(next_nodes)):
            c, n = next_nodes[i].toScribble(graph, indent+1)
            if not flag and n is None:
                flag = True
                node = None 
            code = code +self.addIndent(indent)+ "and{"
            code = code + c
            code = code +self.addIndent(indent)+ "}"
        if node is None:
            return code, None
        else:
            co,no = node.toScribble(graph, indent)
            return code +co , no
            
            
class Join(SNode):
    
    def __init__(self, name = '', label = "|", style = 'bold', shape = 'diamond', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label = label, style = style, shape = shape, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='join'
            
    def toScribble(self, graph, indent):
        next_node = self.next_nodes(graph)[0]
        
        return " ", next_node
            
            
class Rec(SNode):
    
    def __init__(self, name = '', identifier ='', label = " ", shape = 'diamond', obj_dict = None, **attrs):
        pydot.Node.__init__(self, name = name, label = label, shape = shape, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='rec'
            self.obj_dict['identifier']= identifier
            self.obj_dict['flag']= False
            self.obj_dict['port_flag']= True
            
    def get_port_flag(self):
        
        return self.obj_dict['port_flag']
    
    
    def set_port_flag(self, value):
        
        self.obj_dict['port_flag'] = value
    
    
    def get_flag(self):
        
        return self.obj_dict['flag']
    
    
    def set_flag(self, value):
        
        self.obj_dict['flag'] = value
        
        
    def get_identifier(self):
        """Get the node's identifier."""
        
        return self.obj_dict['identifier']
    
        
    def toScribble(self, graph, indent):
        if not self.get_flag():
            self.set_flag(True)
            next_node = self.next_nodes(graph)[0]
            code = self.addIndent(indent)
            code = code + "rec "+self.get_identifier()+" {"
            c,n = next_node.toScribble(graph, indent+1)
            code = code + c
            code = code +self.addIndent(indent)+"}"
            return code, n
        else:
            code = self.addIndent(indent)
            code = code + "continue " + self.get_identifier()+";" 
            return code, None
        
            
            
class Message(SNode):
    
    def __init__(self, name = '', role1 = '', role2 = '', msg = '', time = '', label = " ", shape = 'box', obj_dict = None, **attrs):
        msgLabel = role1+" -> "+role2+": "+msg + "\n within "+str(time)
        pydot.Node.__init__(self, name = name, label = msgLabel, shape = shape, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['role1']=role1
            self.obj_dict['role2']=role2
            self.obj_dict['msg']=msg
            self.obj_dict['time'] = str(time)
            self.obj_dict['activity']='msg'
    
    def get_role1(self):
        """Get the node's role1."""
        
        return self.obj_dict['role1']
    
    def get_role2(self):
        """Get the node's role2."""
        
        return self.obj_dict['role2']
    
    def get_msg(self):
        """Get the node's msg."""
        
        return self.obj_dict['msg']
    
    def get_time(self):
        """Get the node's time."""
        
        return self.obj_dict['time']
        
    def toScribble(self,graph,indent):
        next_node = self.next_nodes(graph)[0]
        code = self.addIndent(indent)
        code = code + self.get_msg()
        code = code +" from "+self.get_role1()+" "
        code = code +"to "+self.get_role2()+" "
        code = code + "within "+self.get_time()+";"
        c, n = next_node.toScribble(graph,indent)
        return code + c, n

        

class Interrupt(SNode):
    
    def __init__(self, name = '', withLabel ='', shape = 'oval', fontcolor='red', obj_dict = None, **attrs):
        interruptLabel = "Interruptible "+withLabel
        pydot.Node.__init__(self, name = name, label = interruptLabel, shape = shape, fontcolor= fontcolor, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='interrupt'
            self.obj_dict['withLabel'] = withLabel
            
            
    def get_withLabel(self):
        """Get the node's withLabel."""
        
        return self.obj_dict['withLabel']
    
    
    def toScribble(self,graph, indent):
        next_node = self.next_nodes(graph)[0]
        code = self.addIndent(indent)
        c,n = next_node.toScribble(graph,indent+1)
        code = code+"interruptible{"+c+"\n"+self.addIndent(indent)+"} "+self.get_withLabel()
        return code, n
    
    
class TimeSlot(SNode):
    # this class was needed in a previous version to represent deadline for blocks.
    # the node was situated at the beginning of the block,
    # this means all the underneath nodes were constraint by the deadline.
    # the deadline has the form after time1 before time2.
    
    def __init__(self, name = '', time1 ='', time2 = '', shape = 'circle', orientation = 180, width = 0.5, height = 0.5, fixedsize = True, fontcolor='red', peripheries = 3, obj_dict = None, **attrs):
        timeLabel = " "
        if time1 is not 0:
            timeLabel = str(time1)+" < "
        timeLabel = timeLabel +"t < "+str(time2)
        deadlineLabel = timeLabel+"\n \n   |_\n \n \n \n"
        pydot.Node.__init__(self, name = name, label = deadlineLabel, shape = shape, orientation = orientation, width = width, height = height, fixedsize = fixedsize, fontcolor= fontcolor, peripheries = peripheries, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='slot'
            self.obj_dict['time1'] = str(time1)
            self.obj_dict['time2'] = str(time2)
            
    
    def get_time1(self):
        """Get the node's time1."""
        
        return self.obj_dict['time1']
    
    def get_time2(self):
        """Get the node's time2."""
        
        return self.obj_dict['time2']
    
    
    def toScribble(self,graph, indent):
        next_node = self.next_nodes(graph)[0]
        code = self.addIndent(indent)
        c,n = next_node.toScribble(graph,indent)
        if self.get_time1() is not 0:
            code = code+"after "+ self.get_time1()
        code = code+" before "+ self.get_time2()+ ";"
        return code + c, n
     
class Delay(SNode):
    
    def __init__(self, name = '', time1 ='', shape = 'circle', width = 0.5, height = 0.5, fixedsize = True, fontcolor='red', peripheries = 3, obj_dict = None, **attrs):
        
        deadlineLabel = "\n                   "+time1+"\n     |_   \n \n \n \n"
        # "\n \n   |_\n \n \n"
        pydot.Node.__init__(self, name = name, label = deadlineLabel, shape = shape, width = width, height = height, fixedsize = fixedsize, fontcolor= fontcolor, peripheries = peripheries, obj_dict = obj_dict, **attrs)
        
        if obj_dict is None:
            self.obj_dict['activity']='delay'
            self.obj_dict['time1'] = time1
            
    
    def get_time1(self):
        """Get the node's time1."""
        
        return self.obj_dict['time1']
    
        
    def toScribble(self,graph, indent):
        next_node = self.next_nodes(graph)[0]
        code = self.addIndent(indent)
        c,n = next_node.toScribble(graph,indent)
        code = code+"wait for "+ self.get_time1()+ ";"
        return code + c, n
     
            