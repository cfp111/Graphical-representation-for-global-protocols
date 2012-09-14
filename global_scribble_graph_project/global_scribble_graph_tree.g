tree grammar global_scribble_graph_tree;

options {
	tokenVocab=global_scribble_graph; // reuse token types
	ASTLabelType=CommonTree;
	language=Python;
	}


protocolDef
	:	^(PROTOCOL protocolName rolesDef protocolBody){print "The walk through the protocol has been performed: The graph will now be printed."
# The png file output has the name of the global protocol
name=$PROTOCOL.getChild(0).getText()+".png"
graph.write_png(name)} ;
	
protocolBody
	:	block {# the last node to be created, if it exists, is the end node.
# it may not exist in case of recursion
if end is not None :
	final = extensions.End()
        graph.add_Snode(final)
        edge = extensions.SEdge(end, final)
        graph.add_Sedge(edge)};
	
protocolName
	:	ID { print "The protocol is called: "+$ID.getText()};

rolesDef:	^(Roles (roleDef)+) {print "The roles that are involved in this protocol are",
k=$Roles.getChildCount()
for i in range (0, k):
	print $Roles.getChild(i).getChild(0).getText(),
print "."};

roleDef	:	^(ROLE roleName) {};

roleName:	ID {};

message	:	^(Msg ID) {node = "ID"}
		| ^(Msg  messageSignature ){node = "MsgSig"};

messageSignature
	:	^(MsgSig messageOperator (payloadType)+ ){};
	
messageOperator
	:	ID {};
	
payloadType
	:	ID {};
	

block	:	^(Block activityList){};

timeConstraints
	:	 ^(Constraint (timeConstraint)+){};


timeConstraint:	^(After timeIdentifier time){}
		| ^(Before timeIdentifier time){}
		| ^(Is timeIdentifier time){};
		
timeIdentifier
	:	ID{};

time 	:	 ^(Time NO ID){};

activityList
	:	^(ActivityList activity+){};

activity:	^(Activity interaction timeConstraints? ){}
		| ^(Activity choice timeConstraints? ){} 
		| ^(Activity parallel timeConstraints? ) {}
		| ^(Activity recursion timeConstraints? ){} 
		| ^(Activity cont timeConstraints? ){}
		| ^(Activity interruptible timeConstraints? ){}
		| ^(Activity delay timeConstraints? ){};
		
delay	:	^(Wait timeIdentifier Symbol time)
		| ^(Wait timeIdentifier time);
		
interaction
	:	^(Message message roleName roleName time){if (node == "ID") :
	sort = 1
elif (node == "MsgSig") :
        sort = 2
if (sort == 1):
        msgLabel = $Message.getChild(0).getChild(0).getText()
elif (sort == 2):
        n = $Message.getChild(0).getChild(0).getChildCount()
        msgLabel = $Message.getChild(0).getChild(0).getChild(0).getText()+" < "+$Message.getChild(0).getChild(0).getChild(1).getText()
        for i in range(2,n):
                msgLabel = msgLabel+", "+$Message.getChild(0).getChild(0).getChild(i).getText()
        msgLabel = msgLabel +" >"
                
nodeName = self.index
self.index += 1
msg = extensions.Message(nodeName,$Message.getChild(1).getText(),$Message.getChild(2).getText(),msgLabel,$Message.getChild(3).getText())
graph.add_Snode(msg)};

choice
	:	^(Choice roleName block+){};
	
parallel:	
		^(Parallel block (block)+){if createJoin is True:
nodeName = self.index
self.index += 1
join = extensions.Join(nodeName)
graph.add_Snode(join)
n = len(endList)
for i in range (0,n):
        edge = extensions.SEdge(endList[i],join)
	graph.add_Sedge(edge)};

recursion
	:	^(Rec identifier block){graph.add_subgraph(sgraph)};
	
cont:	^(Continue identifier){name = $Continue.getChild(0).getText()
rec = sgraph.get_Snode(self.recIndex)[0]};

interruptible
	:	^(Interrupt block withMessage){};
	
withMessage
	:	^(With (roleName message)+){};

identifier
	:	ID {};
