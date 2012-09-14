# $ANTLR 3.1.1 C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g 2012-08-30 14:44:39

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
from ext import extensions

# This file was firstly generated with ANTLR 
# and then completed with commands to build the graph, separated with the comments:
# action start / action end.


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
Before=21
After=22
ID=26
EOF=-1
PROTOCOL=17
Parallel=9
ActivityList=6
SIG=18
Activity=7
Symbol=28
MsgSig=19
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
ROLE=16
T__45=45
Continue=12
Constraint=8
T__48=48
Is=23
NO=27
WHITESPACE=29
Time=25
Choice=10
Msg=20
With=14
Block=5
Roles=15
T__30=30
T__31=31
Rec=11
T__32=32
T__33=33
T__34=34
Message=4
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
Wait=24
Interrupt=13

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "Message", "Block", "ActivityList", "Activity", "Constraint", "Parallel", "Choice", "Rec", "Continue", "Interrupt", "With", "Roles", "ROLE", "PROTOCOL", "SIG", "MsgSig", "Msg", "Before", "After", "Is", "Wait", "Time", "ID", "NO", "Symbol", "WHITESPACE", "'<'", "'>'", "','", "'('", "')'", "'role'", "'{'", "'}'", "'and'", "'from'", "'to'", "'within'", "';'", "'at'", "'or'", "'continue'", "'interruptible'", "'by'", "'with'"
]




class global_scribble_graph_tree(TreeParser):
    grammarFileName = "C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames
    # We associate to each node a unique number: index
    index = 0
    


    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        TreeParser.__init__(self, input, state)


        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )






                


        



    # $ANTLR start "protocolDef"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:10:1: protocolDef : ^( PROTOCOL protocolName rolesDef protocolBody ) ;
    def protocolDef(self,graph ):

        PROTOCOL1 = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:11:2: ( ^( PROTOCOL protocolName rolesDef protocolBody ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:11:4: ^( PROTOCOL protocolName rolesDef protocolBody )
                pass 
                PROTOCOL1=self.match(self.input, PROTOCOL, self.FOLLOW_PROTOCOL_in_protocolDef40)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_protocolName_in_protocolDef42)
                self.protocolName()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_rolesDef_in_protocolDef44)
                self.rolesDef()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_protocolBody_in_protocolDef46)
                self.protocolBody(graph)

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                print "The walk through the protocol has been performed: The graph will now be printed."
                # The png file output has the name of the global protocol
                name=PROTOCOL1.getChild(0).getText()+".png"
                graph.write_png(name)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "protocolDef"


    # $ANTLR start "protocolBody"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:16:1: protocolBody : block ;
    def protocolBody(self,graph ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:17:2: ( block )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:17:4: block
                pass 
                # action start
                # the first node to be created is the start node:
                start = extensions.Start()
                graph.add_Snode(start)
                # action end
                self._state.following.append(self.FOLLOW_block_in_protocolBody59)
                end = self.block(graph, start)

                self._state.following.pop()
                #action start
                # the last node to be created, if it exists, is the end node.
                # it may not exist in case of recursion
                if end is not None :
                    final = extensions.End()
                    graph.add_Snode(final)
                    edge = extensions.SEdge(end, final)
                    graph.add_Sedge(edge)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "protocolBody"


    # $ANTLR start "protocolName"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:25:1: protocolName : ID ;
    def protocolName(self, ):

        ID2 = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:26:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:26:4: ID
                pass 
                ID2=self.match(self.input, ID, self.FOLLOW_ID_in_protocolName71)
                #action start
                print "The protocol is called: "+ID2.getText()
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "protocolName"


    # $ANTLR start "rolesDef"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:28:1: rolesDef : ^( Roles ( roleDef )+ ) ;
    def rolesDef(self, ):

        Roles3 = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:28:9: ( ^( Roles ( roleDef )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:28:11: ^( Roles ( roleDef )+ )
                pass 
                Roles3=self.match(self.input, Roles, self.FOLLOW_Roles_in_rolesDef81)

                self.match(self.input, DOWN, None)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:28:19: ( roleDef )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ROLE) :
                        alt1 = 1


                    if alt1 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:28:20: roleDef
                        pass 
                        self._state.following.append(self.FOLLOW_roleDef_in_rolesDef84)
                        self.roleDef()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1



                self.match(self.input, UP, None)
                #action start
                print "The roles that are involved in this protocol are",
                k=Roles3.getChildCount()
                for i in range (0, k):
                    print Roles3.getChild(i).getChild(0).getText(),
                print "."
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rolesDef"


    # $ANTLR start "roleDef"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:34:1: roleDef : ^( ROLE roleName ) ;
    def roleDef(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:34:9: ( ^( ROLE roleName ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:34:11: ^( ROLE roleName )
                pass 
                self.match(self.input, ROLE, self.FOLLOW_ROLE_in_roleDef98)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_roleName_in_roleDef100)
                self.roleName()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "roleDef"


    # $ANTLR start "roleName"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:36:1: roleName : ID ;
    def roleName(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:36:9: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:36:11: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_roleName110)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "roleName"


    # $ANTLR start "message"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:38:1: message : ( ^( Msg ID ) | ^( Msg messageSignature ) );
    def message(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:38:9: ( ^( Msg ID ) | ^( Msg messageSignature ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == Msg) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 2) :
                        LA2_2 = self.input.LA(3)

                        if (LA2_2 == ID) :
                            alt2 = 1
                        elif (LA2_2 == MsgSig) :
                            alt2 = 2
                        else:
                            nvae = NoViableAltException("", 2, 2, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 2, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:38:11: ^( Msg ID )
                    pass 
                    self.match(self.input, Msg, self.FOLLOW_Msg_in_message121)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, ID, self.FOLLOW_ID_in_message123)

                    self.match(self.input, UP, None)
                    #action start
                    node = "ID"
                    #action end


                elif alt2 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:39:5: ^( Msg messageSignature )
                    pass 
                    self.match(self.input, Msg, self.FOLLOW_Msg_in_message133)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_messageSignature_in_message136)
                    self.messageSignature()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    node = "MsgSig"
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end "message"


    # $ANTLR start "messageSignature"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:41:1: messageSignature : ^( MsgSig messageOperator ( payloadType )+ ) ;
    def messageSignature(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:42:2: ( ^( MsgSig messageOperator ( payloadType )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:42:4: ^( MsgSig messageOperator ( payloadType )+ )
                pass 
                self.match(self.input, MsgSig, self.FOLLOW_MsgSig_in_messageSignature149)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_messageOperator_in_messageSignature151)
                self.messageOperator()

                self._state.following.pop()
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:42:29: ( payloadType )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ID) :
                        alt3 = 1


                    if alt3 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:42:30: payloadType
                        pass 
                        self._state.following.append(self.FOLLOW_payloadType_in_messageSignature154)
                        self.payloadType()

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "messageSignature"


    # $ANTLR start "messageOperator"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:44:1: messageOperator : ID ;
    def messageOperator(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:45:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:45:4: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_messageOperator169)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "messageOperator"


    # $ANTLR start "payloadType"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:47:1: payloadType : ID ;
    def payloadType(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:48:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:48:4: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_payloadType181)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "payloadType"


    # $ANTLR start "block"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:51:1: block : ^( Block activityList ) ;
    def block(self,graph, start ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:51:7: ( ^( Block activityList ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:51:9: ^( Block activityList )
                pass 
                self.match(self.input, Block, self.FOLLOW_Block_in_block194)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_activityList_in_block196)
                end = self.activityList(graph, start)

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return end

    # $ANTLR end "block"


    # $ANTLR start "timeConstraints"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:53:1: timeConstraints : ^( Constraint ( timeConstraint )+ ) ;
    def timeConstraints(self, ):

        label = " "
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:54:2: ( ^( Constraint ( timeConstraint )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:54:5: ^( Constraint ( timeConstraint )+ )
                pass 
                self.match(self.input, Constraint, self.FOLLOW_Constraint_in_timeConstraints209)

                self.match(self.input, DOWN, None)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:54:18: ( timeConstraint )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((Before <= LA4_0 <= Is)) :
                        alt4 = 1


                    if alt4 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:54:19: timeConstraint
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraint_in_timeConstraints212)
                        # this label will be the one on the corresponding arrow of the graph
                        # each constraint is added on a new line
                        label = label +"\n"+ self.timeConstraint()

                        self._state.following.pop()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1



                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return label

    # $ANTLR end "timeConstraints"


    # $ANTLR start "timeConstraint"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:57:1: timeConstraint : ( ^( After timeIdentifier time ) | ^( Before timeIdentifier time ) | ^( Is timeIdentifier time ) );
    def timeConstraint(self, ):

        Time5 = None
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:57:15: ( ^( After timeIdentifier time ) | ^( Before timeIdentifier time ) | ^( Is timeIdentifier time ) )
                alt5 = 3
                LA5 = self.input.LA(1)
                if LA5 == After:
                    alt5 = 1
                elif LA5 == Before:
                    alt5 = 2
                elif LA5 == Is:
                    alt5 = 3
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:57:17: ^( After timeIdentifier time )
                    pass 
                    Time5 = self.match(self.input, After, self.FOLLOW_After_in_timeConstraint225)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_timeConstraint227)
                    self.timeIdentifier()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_time_in_timeConstraint229)
                    self.time()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    label = Time5.getChild(0).getText()+" > "+Time5.getChild(1).getChild(0).getText()+Time5.getChild(1).getChild(1).getText()
                    #action end


                elif alt5 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:58:5: ^( Before timeIdentifier time )
                    pass 
                    Time5 = self.match(self.input, Before, self.FOLLOW_Before_in_timeConstraint238)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_timeConstraint240)
                    self.timeIdentifier()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_time_in_timeConstraint242)
                    self.time()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    label = Time5.getChild(0).getText()+" < "+Time5.getChild(1).getChild(0).getText()+Time5.getChild(1).getChild(1).getText()
                    #action end


                elif alt5 == 3:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:59:5: ^( Is timeIdentifier time )
                    pass 
                    Time5 = self.match(self.input, Is, self.FOLLOW_Is_in_timeConstraint251)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_timeConstraint253)
                    self.timeIdentifier()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_time_in_timeConstraint255)
                    self.time()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    label = Time5.getChild(0).getText()+" = "+Time5.getChild(1).getChild(0).getText()+Time5.getChild(1).getChild(1).getText()
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return label

    # $ANTLR end "timeConstraint"


    # $ANTLR start "timeIdentifier"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:61:1: timeIdentifier : ID ;
    def timeIdentifier(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:62:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:62:4: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_timeIdentifier268)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "timeIdentifier"


    # $ANTLR start "time"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:64:1: time : ^( Time NO ID ) ;
    def time(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:64:7: ( ^( Time NO ID ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:64:10: ^( Time NO ID )
                pass 
                self.match(self.input, Time, self.FOLLOW_Time_in_time280)

                self.match(self.input, DOWN, None)
                self.match(self.input, NO, self.FOLLOW_NO_in_time282)
                self.match(self.input, ID, self.FOLLOW_ID_in_time284)

                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "time"


    # $ANTLR start "activityList"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:66:1: activityList : ^( ActivityList ( activity )+ ) ;
    def activityList(self,graph, start ):

        ActivityList4 = None
        currentNode = start

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:67:2: ( ^( ActivityList ( activity )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:67:4: ^( ActivityList ( activity )+ )
                pass 
                ActivityList4=self.match(self.input, ActivityList, self.FOLLOW_ActivityList_in_activityList296)

                self.match(self.input, DOWN, None)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:67:19: ( activity )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == Activity) :
                        alt6 = 1


                    if alt6 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:67:19: activity
                        pass 
                        self._state.following.append(self.FOLLOW_activity_in_activityList298)
                        begin, end, label = self.activity(graph)
                        # action start
                        # at this point, we make the connection between nodes
                        # the first connection links the node referred as start with the first node of the first activity 
                        # and so on with all the activities in the list
                        edge = extensions.SEdge(currentNode, begin)
                        if label is None:
                            graph.add_Sedge(edge)
                        else:
                            graph.add_Sedge_with_label(edge,label)
                        currentNode = end
                        # action end


                        self._state.following.pop()


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1



                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return currentNode

    # $ANTLR end "activityList"


    # $ANTLR start "activity"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:73:1: activity : ( ^( Activity interaction ( timeConstraints )? ) | ^( Activity choice ( timeConstraints )? ) | ^( Activity parallel ( timeConstraints )? ) | ^( Activity recursion ( timeConstraints )? ) | ^( Activity cont ( timeConstraints )? ) | ^( Activity interruptible ( timeConstraints )? ) | ^( Activity delay ( timeConstraints )? ) );
    def activity(self,graph ):

        label = None
        begin = None
        end = None
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:73:9: ( ^( Activity interaction ( timeConstraints )? ) | ^( Activity choice ( timeConstraints )? ) | ^( Activity parallel ( timeConstraints )? ) | ^( Activity recursion ( timeConstraints )? ) | ^( Activity cont ( timeConstraints )? ) | ^( Activity interruptible ( timeConstraints )? ) | ^( Activity delay ( timeConstraints )? ) )
                alt14 = 7
                alt14 = self.dfa14.predict(self.input)
                if alt14 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:73:11: ^( Activity interaction ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity309)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_interaction_in_activity311)
                    begin, end = self.interaction(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:73:34: ( timeConstraints )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == Constraint) :
                        alt7 = 1
                    if alt7 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:73:34: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity313)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end


                elif alt14 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:74:5: ^( Activity choice ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity324)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_choice_in_activity326)
                    begin, end = self.choice(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:74:23: ( timeConstraints )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == Constraint) :
                        alt8 = 1
                    if alt8 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:74:23: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity328)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end


                elif alt14 == 3:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:75:5: ^( Activity parallel ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity340)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_parallel_in_activity342)
                    begin, end = self.parallel(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:75:25: ( timeConstraints )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == Constraint) :
                        alt9 = 1
                    if alt9 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:75:25: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity344)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end


                elif alt14 == 4:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:76:5: ^( Activity recursion ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity356)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_recursion_in_activity358)
                    begin, end = self.recursion(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:76:26: ( timeConstraints )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == Constraint) :
                        alt10 = 1
                    if alt10 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:76:26: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity360)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end


                elif alt14 == 5:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:77:5: ^( Activity cont ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity372)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_cont_in_activity374)
                    begin, end = self.cont(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:77:21: ( timeConstraints )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == Constraint) :
                        alt11 = 1
                    if alt11 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:77:21: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity376)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end


                elif alt14 == 6:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:78:5: ^( Activity interruptible ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity387)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_interruptible_in_activity389)
                    begin, end = self.interruptible(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:78:30: ( timeConstraints )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == Constraint) :
                        alt12 = 1
                    if alt12 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:78:30: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity391)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end


                elif alt14 == 7:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:79:5: ^( Activity delay ( timeConstraints )? )
                    pass 
                    self.match(self.input, Activity, self.FOLLOW_Activity_in_activity402)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_delay_in_activity404)
                    begin, end = self.delay(graph)

                    self._state.following.pop()
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:79:22: ( timeConstraints )?
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == Constraint) :
                        alt13 = 1
                    if alt13 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:79:22: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity406)
                        label = self.timeConstraints()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    #action start
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return begin, end, label

    # $ANTLR end "activity"


    # $ANTLR start "delay"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:81:1: delay : ( ^( Wait timeIdentifier Symbol time ) | ^( Wait timeIdentifier time ) );
    def delay(self,graph ):

        Wait5 = None
        
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:81:7: ( ^( Wait timeIdentifier Symbol time ) | ^( Wait timeIdentifier time ) )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == Wait) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == 2) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == ID) :
                            LA15_3 = self.input.LA(4)

                            if (LA15_3 == Symbol) :
                                alt15 = 1
                            elif (LA15_3 == Time) :
                                alt15 = 2
                            else:
                                nvae = NoViableAltException("", 15, 3, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:81:9: ^( Wait timeIdentifier Symbol time )
                    pass 
                    Wait5 = self.match(self.input, Wait, self.FOLLOW_Wait_in_delay421)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_delay423)
                    self.timeIdentifier()

                    self._state.following.pop()
                    self.match(self.input, Symbol, self.FOLLOW_Symbol_in_delay425)
                    self._state.following.append(self.FOLLOW_time_in_delay427)
                    self.time()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    
                    # action start
                    label = Wait5.getChild(0).getText()+" "+Wait5.getChild(1).getText()+" "+Wait5.getChild(2).getChild(0).getText()+Wait5.getChild(2).getChild(1).getText()
                    nodeName = self.index
                    self.index += 1
                    delay = extensions.Delay(nodeName, label)
                    graph.add_Snode(delay)
                    # action end


                elif alt15 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:82:5: ^( Wait timeIdentifier time )
                    pass 
                    Wait5 = self.match(self.input, Wait, self.FOLLOW_Wait_in_delay435)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_delay437)
                    self.timeIdentifier()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_time_in_delay439)
                    self.time()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    
                    # action start
                    label = Wait5.getChild(0).getText()+" = "+Wait5.getChild(1).getChild(0).getText()+Wait5.getChild(1).getChild(1).getText()
                    nodeName = self.index
                    self.index += 1
                    delay = extensions.Delay(nodeName, label)
                    graph.add_Snode(delay)
                    # action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return delay, delay

    # $ANTLR end "delay"


    # $ANTLR start "interaction"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:84:1: interaction : ^( Message message roleName roleName time ) ;
    def interaction(self,graph ):

        Message5 = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:85:2: ( ^( Message message roleName roleName time ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:85:4: ^( Message message roleName roleName time )
                pass 
                Message5=self.match(self.input, Message, self.FOLLOW_Message_in_interaction452)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_message_in_interaction454)
                node = self.message()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_roleName_in_interaction456)
                self.roleName()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_roleName_in_interaction458)
                self.roleName()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_time_in_interaction460)
                self.time()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                if (node == "ID") :
                    sort = 1
                elif (node == "MsgSig") :
                    sort = 2
                if (sort == 1):
                    msgLabel = Message5.getChild(0).getChild(0).getText()
                elif (sort == 2):
                    n = Message5.getChild(0).getChild(0).getChildCount()
                    msgLabel = Message5.getChild(0).getChild(0).getChild(0).getText()+" < "+Message5.getChild(0).getChild(0).getChild(1).getText()
                    for i in range(2,n):
                        msgLabel = msgLabel+", "+Message5.getChild(0).getChild(0).getChild(i).getText()
                    msgLabel = msgLabel +" >"
                timeLabel = Message5.getChild(3).getChild(0).getText() + Message5.getChild(3).getChild(1).getText()              
                nodeName = self.index
                self.index += 1
                msg = extensions.Message(nodeName,Message5.getChild(1).getText(),Message5.getChild(2).getText(),msgLabel,timeLabel)
                graph.add_Snode(msg)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return msg,msg

    # $ANTLR end "interaction"


    # $ANTLR start "choice"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:103:1: choice : ^( Choice roleName ( block )+ ) ;
    def choice(self,graph ):

        Choice6 = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:104:2: ( ^( Choice roleName ( block )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:104:4: ^( Choice roleName ( block )+ )
                pass 
                Choice6=self.match(self.input, Choice, self.FOLLOW_Choice_in_choice472)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_roleName_in_choice474)
                self.roleName()
                #action start
                choiceLabel="Choice at "+Choice6.getChild(0).getText()
                nodeName = self.index
                self.index += 1
                choice = extensions.Choice(nodeName,Choice6.getChild(0).getText())
                graph.add_Snode(choice)
                
                merge = None
                mergeIsCreated = False
                #action end

                self._state.following.pop()
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:104:22: ( block )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == Block) :
                        alt16 = 1


                    if alt16 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:104:22: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_choice476)
                        end = self.block(graph, choice)
                        # action start
                        if end is not None:
                            if mergeIsCreated is False:
                                mergeLabel="Merge"
                                nodeName = self.index
                                self.index += 1
                                merge = extensions.Merge(nodeName)
                                graph.add_Snode(merge)
                                mergeIsCreated = True
                            edge = extensions.SEdge(end,merge)
                            graph.add_Sedge(edge)
                        # action end

                        self._state.following.pop()


                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1



                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return choice, merge

    # $ANTLR end "choice"


    # $ANTLR start "parallel"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:118:1: parallel : ^( Parallel block ( block )+ ) ;
    def parallel(self,graph ):

        Parallel7 = None
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:118:9: ( ^( Parallel block ( block )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:119:3: ^( Parallel block ( block )+ )
                pass 
                Parallel7 = self.match(self.input, Parallel, self.FOLLOW_Parallel_in_parallel491)
                #action start
                nodeName = self.index
                self.index += 1
                fork = extensions.Fork(nodeName)
                graph.add_Snode(fork)
                
                # the join node will be created only if all the parallel branches have an endpoint.
                join = None
                createJoin = False
                endList = []
                #action end


                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_block_in_parallel493)
                end = self.block(graph, fork)
                # action start
                if end is not None:
                    endList = endList+[end]
                    createJoin = True
                # action end

                self._state.following.pop()
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:119:20: ( block )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == Block) :
                        alt17 = 1


                    if alt17 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:119:21: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_parallel496)
                        end = self.block(graph,fork)
                        # action start
                        if end is not None and createJoin is True:
                            endList = endList + [end]
                        else:
                            createJoin = False
                        # action end

                        self._state.following.pop()


                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1



                self.match(self.input, UP, None)
                #action start
                if createJoin is True:
                    nodeName = self.index
                    self.index += 1
                    join = extensions.Join(nodeName)
                    graph.add_Snode(join)
                    n = len(endList)
                    for i in range (0,n):
                        edge = extensions.SEdge(endList[i],join)
                        graph.add_Sedge(edge)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return fork, join

    # $ANTLR end "parallel"


    # $ANTLR start "recursion"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:129:1: recursion : ^( Rec identifier block ) ;
    def recursion(self,graph ):

        Recursion8 = None
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:130:2: ( ^( Rec identifier block ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:130:4: ^( Rec identifier block )
                pass 
                Recursion8 = self.match(self.input, Rec, self.FOLLOW_Rec_in_recursion510)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_identifier_in_recursion512)
                self.identifier()
                #action start
                # create a subgraph for the recursion block
                sgraphName = Recursion8.getChild(0).getText()
                sgraph = extensions.SSubgraph(sgraphName)
                
                nodeName = sgraphName
                rec=extensions.Rec(nodeName,sgraphName)
                sgraph.add_Snode(rec)
                #action end

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_block_in_recursion514)
                end = self.block(sgraph, rec)

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                graph.add_subgraph(sgraph)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return rec, end

    # $ANTLR end "recursion"


    # $ANTLR start "cont"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:132:1: cont : ^( Continue identifier ) ;
    def cont(self,sgraph ):

        Continue7 = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:132:5: ( ^( Continue identifier ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:132:7: ^( Continue identifier )
                pass 
                Continue7=self.match(self.input, Continue, self.FOLLOW_Continue_in_cont525)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_identifier_in_cont527)
                self.identifier()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                name = Continue7.getChild(0).getText()
                rec = sgraph.get_Snode(name)[0]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return rec, None

    # $ANTLR end "cont"


    # $ANTLR start "interruptible"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:136:1: interruptible : ^( Interrupt block withMessage ) ;
    def interruptible(self,graph ):

        Interrupt8 = None
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:137:2: ( ^( Interrupt block withMessage ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:137:4: ^( Interrupt block withMessage )
                pass 
                Interrupt8 = self.match(self.input, Interrupt, self.FOLLOW_Interrupt_in_interruptible539)
                # action start
                k=Interrupt8.getChild(1).getChildCount()/2
                print Interrupt8.getChild(0)
                print Interrupt8.getChild(1)
                #print "here"+Interrupt8.getChild(1).getChild(0)
                #print "here again"+Interrupt8.getChild(1).getChild(1).getChild(0)
                withLabel = "by "+Interrupt8.getChild(1).getChild(0).getText()+" with "+Interrupt8.getChild(1).getChild(1).getChild(0).getText()
                for i in range (1, k):
                    withLabel = withLabel+", "+"by "+Interrupt8.getChild(1).getChild(2*i).getText()+" with "+Interrupt8.getChild(1).getChild(2*i+1).getChild(0).getText()
                nodeName = self.index
                self.index += 1
                interruptWith = extensions.Interrupt(nodeName, withLabel)
                graph.add_Snode(interruptWith)
                # action end


                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_block_in_interruptible541)
                end = self.block(graph, interruptWith)

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_withMessage_in_interruptible543)
                self.withMessage()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return interruptWith, end

    # $ANTLR end "interruptible"


    # $ANTLR start "withMessage"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:139:1: withMessage : ^( With ( roleName message )+ ) ;
    def withMessage(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:140:2: ( ^( With ( roleName message )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:140:4: ^( With ( roleName message )+ )
                pass 
                self.match(self.input, With, self.FOLLOW_With_in_withMessage556)

                self.match(self.input, DOWN, None)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:140:11: ( roleName message )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == ID) :
                        alt18 = 1


                    if alt18 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:140:12: roleName message
                        pass 
                        self._state.following.append(self.FOLLOW_roleName_in_withMessage559)
                        self.roleName()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_message_in_withMessage561)
                        self.message()

                        self._state.following.pop()


                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1



                self.match(self.input, UP, None)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "withMessage"


    # $ANTLR start "identifier"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:142:1: identifier : ID ;
    def identifier(self, ):

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:143:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph_tree.g:143:4: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_identifier574)
                #action start
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "identifier"


    # Delegated rules


    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\7\1\2\1\4\7\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\1\7\1\2\1\30\7\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\3\uffff\1\4\1\3\1\2\1\1\1\7\1\6\1\5"
        )

    DFA14_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\6\4\uffff\1\4\1\5\1\3\1\11\1\10\12\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #14

    DFA14 = DFA
 

    FOLLOW_PROTOCOL_in_protocolDef40 = frozenset([2])
    FOLLOW_protocolName_in_protocolDef42 = frozenset([15])
    FOLLOW_rolesDef_in_protocolDef44 = frozenset([5])
    FOLLOW_protocolBody_in_protocolDef46 = frozenset([3])
    FOLLOW_block_in_protocolBody59 = frozenset([1])
    FOLLOW_ID_in_protocolName71 = frozenset([1])
    FOLLOW_Roles_in_rolesDef81 = frozenset([2])
    FOLLOW_roleDef_in_rolesDef84 = frozenset([3, 16])
    FOLLOW_ROLE_in_roleDef98 = frozenset([2])
    FOLLOW_roleName_in_roleDef100 = frozenset([3])
    FOLLOW_ID_in_roleName110 = frozenset([1])
    FOLLOW_Msg_in_message121 = frozenset([2])
    FOLLOW_ID_in_message123 = frozenset([3])
    FOLLOW_Msg_in_message133 = frozenset([2])
    FOLLOW_messageSignature_in_message136 = frozenset([3])
    FOLLOW_MsgSig_in_messageSignature149 = frozenset([2])
    FOLLOW_messageOperator_in_messageSignature151 = frozenset([26])
    FOLLOW_payloadType_in_messageSignature154 = frozenset([3, 26])
    FOLLOW_ID_in_messageOperator169 = frozenset([1])
    FOLLOW_ID_in_payloadType181 = frozenset([1])
    FOLLOW_Block_in_block194 = frozenset([2])
    FOLLOW_activityList_in_block196 = frozenset([3])
    FOLLOW_Constraint_in_timeConstraints209 = frozenset([2])
    FOLLOW_timeConstraint_in_timeConstraints212 = frozenset([3, 21, 22, 23])
    FOLLOW_After_in_timeConstraint225 = frozenset([2])
    FOLLOW_timeIdentifier_in_timeConstraint227 = frozenset([25])
    FOLLOW_time_in_timeConstraint229 = frozenset([3])
    FOLLOW_Before_in_timeConstraint238 = frozenset([2])
    FOLLOW_timeIdentifier_in_timeConstraint240 = frozenset([25])
    FOLLOW_time_in_timeConstraint242 = frozenset([3])
    FOLLOW_Is_in_timeConstraint251 = frozenset([2])
    FOLLOW_timeIdentifier_in_timeConstraint253 = frozenset([25])
    FOLLOW_time_in_timeConstraint255 = frozenset([3])
    FOLLOW_ID_in_timeIdentifier268 = frozenset([1])
    FOLLOW_Time_in_time280 = frozenset([2])
    FOLLOW_NO_in_time282 = frozenset([26])
    FOLLOW_ID_in_time284 = frozenset([3])
    FOLLOW_ActivityList_in_activityList296 = frozenset([2])
    FOLLOW_activity_in_activityList298 = frozenset([3, 7])
    FOLLOW_Activity_in_activity309 = frozenset([2])
    FOLLOW_interaction_in_activity311 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity313 = frozenset([3])
    FOLLOW_Activity_in_activity324 = frozenset([2])
    FOLLOW_choice_in_activity326 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity328 = frozenset([3])
    FOLLOW_Activity_in_activity340 = frozenset([2])
    FOLLOW_parallel_in_activity342 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity344 = frozenset([3])
    FOLLOW_Activity_in_activity356 = frozenset([2])
    FOLLOW_recursion_in_activity358 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity360 = frozenset([3])
    FOLLOW_Activity_in_activity372 = frozenset([2])
    FOLLOW_cont_in_activity374 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity376 = frozenset([3])
    FOLLOW_Activity_in_activity387 = frozenset([2])
    FOLLOW_interruptible_in_activity389 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity391 = frozenset([3])
    FOLLOW_Activity_in_activity402 = frozenset([2])
    FOLLOW_delay_in_activity404 = frozenset([3, 8])
    FOLLOW_timeConstraints_in_activity406 = frozenset([3])
    FOLLOW_Wait_in_delay421 = frozenset([2])
    FOLLOW_timeIdentifier_in_delay423 = frozenset([28])
    FOLLOW_Symbol_in_delay425 = frozenset([25])
    FOLLOW_time_in_delay427 = frozenset([3])
    FOLLOW_Wait_in_delay435 = frozenset([2])
    FOLLOW_timeIdentifier_in_delay437 = frozenset([25])
    FOLLOW_time_in_delay439 = frozenset([3])
    FOLLOW_Message_in_interaction452 = frozenset([2])
    FOLLOW_message_in_interaction454 = frozenset([26])
    FOLLOW_roleName_in_interaction456 = frozenset([26])
    FOLLOW_roleName_in_interaction458 = frozenset([25])
    FOLLOW_time_in_interaction460 = frozenset([3])
    FOLLOW_Choice_in_choice472 = frozenset([2])
    FOLLOW_roleName_in_choice474 = frozenset([5])
    FOLLOW_block_in_choice476 = frozenset([3, 5])
    FOLLOW_Parallel_in_parallel491 = frozenset([2])
    FOLLOW_block_in_parallel493 = frozenset([5])
    FOLLOW_block_in_parallel496 = frozenset([3, 5])
    FOLLOW_Rec_in_recursion510 = frozenset([2])
    FOLLOW_identifier_in_recursion512 = frozenset([5])
    FOLLOW_block_in_recursion514 = frozenset([3])
    FOLLOW_Continue_in_cont525 = frozenset([2])
    FOLLOW_identifier_in_cont527 = frozenset([3])
    FOLLOW_Interrupt_in_interruptible539 = frozenset([2])
    FOLLOW_block_in_interruptible541 = frozenset([14])
    FOLLOW_withMessage_in_interruptible543 = frozenset([3])
    FOLLOW_With_in_withMessage556 = frozenset([2])
    FOLLOW_roleName_in_withMessage559 = frozenset([20])
    FOLLOW_message_in_withMessage561 = frozenset([3, 26])
    FOLLOW_ID_in_identifier574 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(global_scribble_graph_tree)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
