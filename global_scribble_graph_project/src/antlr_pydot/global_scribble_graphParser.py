# $ANTLR 3.1.1 C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g 2012-08-30 15:31:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
Before=21
After=22
ID=26
EOF=-1
PROTOCOL=17
ActivityList=6
Parallel=9
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




class global_scribble_graphParser(Parser):
    grammarFileName = "C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


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






                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class protocolDef_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "protocolDef"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:38:1: protocolDef : PROTOCOL protocolName ( '<' parameters '>' )? rolesDef protocolBody -> ^( PROTOCOL protocolName rolesDef protocolBody ) ;
    def protocolDef(self, ):

        retval = self.protocolDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PROTOCOL1 = None
        char_literal3 = None
        char_literal5 = None
        protocolName2 = None

        parameters4 = None

        rolesDef6 = None

        protocolBody7 = None


        PROTOCOL1_tree = None
        char_literal3_tree = None
        char_literal5_tree = None
        stream_30 = RewriteRuleTokenStream(self._adaptor, "token 30")
        stream_31 = RewriteRuleTokenStream(self._adaptor, "token 31")
        stream_PROTOCOL = RewriteRuleTokenStream(self._adaptor, "token PROTOCOL")
        stream_rolesDef = RewriteRuleSubtreeStream(self._adaptor, "rule rolesDef")
        stream_protocolName = RewriteRuleSubtreeStream(self._adaptor, "rule protocolName")
        stream_parameters = RewriteRuleSubtreeStream(self._adaptor, "rule parameters")
        stream_protocolBody = RewriteRuleSubtreeStream(self._adaptor, "rule protocolBody")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:39:2: ( PROTOCOL protocolName ( '<' parameters '>' )? rolesDef protocolBody -> ^( PROTOCOL protocolName rolesDef protocolBody ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:39:4: PROTOCOL protocolName ( '<' parameters '>' )? rolesDef protocolBody
                pass 
                PROTOCOL1=self.match(self.input, PROTOCOL, self.FOLLOW_PROTOCOL_in_protocolDef161) 
                if self._state.backtracking == 0:
                    stream_PROTOCOL.add(PROTOCOL1)
                self._state.following.append(self.FOLLOW_protocolName_in_protocolDef163)
                protocolName2 = self.protocolName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_protocolName.add(protocolName2.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:39:26: ( '<' parameters '>' )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 30) :
                    alt1 = 1
                if alt1 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:39:27: '<' parameters '>'
                    pass 
                    char_literal3=self.match(self.input, 30, self.FOLLOW_30_in_protocolDef166) 
                    if self._state.backtracking == 0:
                        stream_30.add(char_literal3)
                    self._state.following.append(self.FOLLOW_parameters_in_protocolDef168)
                    parameters4 = self.parameters()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameters.add(parameters4.tree)
                    char_literal5=self.match(self.input, 31, self.FOLLOW_31_in_protocolDef170) 
                    if self._state.backtracking == 0:
                        stream_31.add(char_literal5)



                self._state.following.append(self.FOLLOW_rolesDef_in_protocolDef175)
                rolesDef6 = self.rolesDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolesDef.add(rolesDef6.tree)
                self._state.following.append(self.FOLLOW_protocolBody_in_protocolDef178)
                protocolBody7 = self.protocolBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_protocolBody.add(protocolBody7.tree)

                # AST Rewrite
                # elements: PROTOCOL, protocolBody, rolesDef, protocolName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 39:72: -> ^( PROTOCOL protocolName rolesDef protocolBody )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:39:75: ^( PROTOCOL protocolName rolesDef protocolBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PROTOCOL.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_protocolName.nextTree())
                    self._adaptor.addChild(root_1, stream_rolesDef.nextTree())
                    self._adaptor.addChild(root_1, stream_protocolBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "protocolDef"

    class protocolName_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "protocolName"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:41:1: protocolName : ID ;
    def protocolName(self, ):

        retval = self.protocolName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID8 = None

        ID8_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:42:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:42:4: ID
                pass 
                root_0 = self._adaptor.nil()

                ID8=self.match(self.input, ID, self.FOLLOW_ID_in_protocolName201)
                if self._state.backtracking == 0:

                    ID8_tree = self._adaptor.createWithPayload(ID8)
                    self._adaptor.addChild(root_0, ID8_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "protocolName"

    class parameters_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "parameters"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:44:1: parameters : SIG identifier ( ',' SIG identifier )* ;
    def parameters(self, ):

        retval = self.parameters_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SIG9 = None
        char_literal11 = None
        SIG12 = None
        identifier10 = None

        identifier13 = None


        SIG9_tree = None
        char_literal11_tree = None
        SIG12_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:45:2: ( SIG identifier ( ',' SIG identifier )* )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:45:4: SIG identifier ( ',' SIG identifier )*
                pass 
                root_0 = self._adaptor.nil()

                SIG9=self.match(self.input, SIG, self.FOLLOW_SIG_in_parameters211)
                if self._state.backtracking == 0:

                    SIG9_tree = self._adaptor.createWithPayload(SIG9)
                    self._adaptor.addChild(root_0, SIG9_tree)

                self._state.following.append(self.FOLLOW_identifier_in_parameters213)
                identifier10 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier10.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:45:20: ( ',' SIG identifier )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 32) :
                        alt2 = 1


                    if alt2 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:45:22: ',' SIG identifier
                        pass 
                        char_literal11=self.match(self.input, 32, self.FOLLOW_32_in_parameters218)
                        if self._state.backtracking == 0:

                            char_literal11_tree = self._adaptor.createWithPayload(char_literal11)
                            self._adaptor.addChild(root_0, char_literal11_tree)

                        SIG12=self.match(self.input, SIG, self.FOLLOW_SIG_in_parameters220)
                        if self._state.backtracking == 0:

                            SIG12_tree = self._adaptor.createWithPayload(SIG12)
                            self._adaptor.addChild(root_0, SIG12_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_parameters222)
                        identifier13 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier13.tree)


                    else:
                        break #loop2





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "parameters"

    class rolesDef_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "rolesDef"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:1: rolesDef : '(' roleDef ( ',' roleDef )* ')' -> ^( Roles ( roleDef )+ ) ;
    def rolesDef(self, ):

        retval = self.rolesDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal14 = None
        char_literal16 = None
        char_literal18 = None
        roleDef15 = None

        roleDef17 = None


        char_literal14_tree = None
        char_literal16_tree = None
        char_literal18_tree = None
        stream_32 = RewriteRuleTokenStream(self._adaptor, "token 32")
        stream_33 = RewriteRuleTokenStream(self._adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_roleDef = RewriteRuleSubtreeStream(self._adaptor, "rule roleDef")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:9: ( '(' roleDef ( ',' roleDef )* ')' -> ^( Roles ( roleDef )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:11: '(' roleDef ( ',' roleDef )* ')'
                pass 
                char_literal14=self.match(self.input, 33, self.FOLLOW_33_in_rolesDef233) 
                if self._state.backtracking == 0:
                    stream_33.add(char_literal14)
                self._state.following.append(self.FOLLOW_roleDef_in_rolesDef235)
                roleDef15 = self.roleDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleDef.add(roleDef15.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:23: ( ',' roleDef )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 32) :
                        alt3 = 1


                    if alt3 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:24: ',' roleDef
                        pass 
                        char_literal16=self.match(self.input, 32, self.FOLLOW_32_in_rolesDef238) 
                        if self._state.backtracking == 0:
                            stream_32.add(char_literal16)
                        self._state.following.append(self.FOLLOW_roleDef_in_rolesDef240)
                        roleDef17 = self.roleDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roleDef.add(roleDef17.tree)


                    else:
                        break #loop3


                char_literal18=self.match(self.input, 34, self.FOLLOW_34_in_rolesDef244) 
                if self._state.backtracking == 0:
                    stream_34.add(char_literal18)

                # AST Rewrite
                # elements: roleDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 47:42: -> ^( Roles ( roleDef )+ )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:45: ^( Roles ( roleDef )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Roles, "Roles"), root_1)

                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:47:53: ( roleDef )+
                    if not (stream_roleDef.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roleDef.hasNext():
                        self._adaptor.addChild(root_1, stream_roleDef.nextTree())


                    stream_roleDef.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "rolesDef"

    class roleDef_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "roleDef"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:49:1: roleDef : 'role' roleName -> ^( ROLE roleName ) ;
    def roleDef(self, ):

        retval = self.roleDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal19 = None
        roleName20 = None


        string_literal19_tree = None
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:49:9: ( 'role' roleName -> ^( ROLE roleName ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:49:11: 'role' roleName
                pass 
                string_literal19=self.match(self.input, 35, self.FOLLOW_35_in_roleDef263) 
                if self._state.backtracking == 0:
                    stream_35.add(string_literal19)
                self._state.following.append(self.FOLLOW_roleName_in_roleDef265)
                roleName20 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName20.tree)

                # AST Rewrite
                # elements: roleName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 49:27: -> ^( ROLE roleName )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:49:30: ^( ROLE roleName )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLE, "ROLE"), root_1)

                    self._adaptor.addChild(root_1, stream_roleName.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "roleDef"

    class roleName_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "roleName"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:51:1: roleName : ID ;
    def roleName(self, ):

        retval = self.roleName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID21 = None

        ID21_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:51:9: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:51:11: ID
                pass 
                root_0 = self._adaptor.nil()

                ID21=self.match(self.input, ID, self.FOLLOW_ID_in_roleName280)
                if self._state.backtracking == 0:

                    ID21_tree = self._adaptor.createWithPayload(ID21)
                    self._adaptor.addChild(root_0, ID21_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "roleName"

    class protocolBody_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "protocolBody"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:53:1: protocolBody : block ;
    def protocolBody(self, ):

        retval = self.protocolBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        block22 = None



        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:54:2: ( block )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:54:4: block
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_block_in_protocolBody289)
                block22 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block22.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "protocolBody"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "block"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:56:1: block : '{' activityList '}' -> ^( Block activityList ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal23 = None
        char_literal25 = None
        activityList24 = None


        char_literal23_tree = None
        char_literal25_tree = None
        stream_36 = RewriteRuleTokenStream(self._adaptor, "token 36")
        stream_37 = RewriteRuleTokenStream(self._adaptor, "token 37")
        stream_activityList = RewriteRuleSubtreeStream(self._adaptor, "rule activityList")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:56:7: ( '{' activityList '}' -> ^( Block activityList ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:56:9: '{' activityList '}'
                pass 
                char_literal23=self.match(self.input, 36, self.FOLLOW_36_in_block297) 
                if self._state.backtracking == 0:
                    stream_36.add(char_literal23)
                self._state.following.append(self.FOLLOW_activityList_in_block299)
                activityList24 = self.activityList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_activityList.add(activityList24.tree)
                char_literal25=self.match(self.input, 37, self.FOLLOW_37_in_block301) 
                if self._state.backtracking == 0:
                    stream_37.add(char_literal25)

                # AST Rewrite
                # elements: activityList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 56:30: -> ^( Block activityList )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:56:33: ^( Block activityList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Block, "Block"), root_1)

                    self._adaptor.addChild(root_1, stream_activityList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "block"

    class timeConstraints_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "timeConstraints"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:58:1: timeConstraints : timeConstraint ( 'and' timeConstraint )* -> ^( Constraint ( timeConstraint )+ ) ;
    def timeConstraints(self, ):

        retval = self.timeConstraints_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal27 = None
        timeConstraint26 = None

        timeConstraint28 = None


        string_literal27_tree = None
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
        stream_timeConstraint = RewriteRuleSubtreeStream(self._adaptor, "rule timeConstraint")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:59:2: ( timeConstraint ( 'and' timeConstraint )* -> ^( Constraint ( timeConstraint )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:59:5: timeConstraint ( 'and' timeConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_timeConstraint_in_timeConstraints319)
                timeConstraint26 = self.timeConstraint()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_timeConstraint.add(timeConstraint26.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:59:20: ( 'and' timeConstraint )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 38) :
                        alt4 = 1


                    if alt4 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:59:21: 'and' timeConstraint
                        pass 
                        string_literal27=self.match(self.input, 38, self.FOLLOW_38_in_timeConstraints322) 
                        if self._state.backtracking == 0:
                            stream_38.add(string_literal27)
                        self._state.following.append(self.FOLLOW_timeConstraint_in_timeConstraints324)
                        timeConstraint28 = self.timeConstraint()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraint.add(timeConstraint28.tree)


                    else:
                        break #loop4



                # AST Rewrite
                # elements: timeConstraint
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 59:45: -> ^( Constraint ( timeConstraint )+ )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:59:47: ^( Constraint ( timeConstraint )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Constraint, "Constraint"), root_1)

                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:59:60: ( timeConstraint )+
                    if not (stream_timeConstraint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_timeConstraint.hasNext():
                        self._adaptor.addChild(root_1, stream_timeConstraint.nextTree())


                    stream_timeConstraint.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "timeConstraints"

    class timeConstraint_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "timeConstraint"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:62:1: timeConstraint : ( timeIdentifier After time -> ^( After timeIdentifier time ) | timeIdentifier Before time -> ^( Before timeIdentifier time ) | timeIdentifier Is time -> ^( Is timeIdentifier time ) );
    def timeConstraint(self, ):

        retval = self.timeConstraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        After30 = None
        Before33 = None
        Is36 = None
        timeIdentifier29 = None

        time31 = None

        timeIdentifier32 = None

        time34 = None

        timeIdentifier35 = None

        time37 = None


        After30_tree = None
        Before33_tree = None
        Is36_tree = None
        stream_Before = RewriteRuleTokenStream(self._adaptor, "token Before")
        stream_Is = RewriteRuleTokenStream(self._adaptor, "token Is")
        stream_After = RewriteRuleTokenStream(self._adaptor, "token After")
        stream_time = RewriteRuleSubtreeStream(self._adaptor, "rule time")
        stream_timeIdentifier = RewriteRuleSubtreeStream(self._adaptor, "rule timeIdentifier")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:62:15: ( timeIdentifier After time -> ^( After timeIdentifier time ) | timeIdentifier Before time -> ^( Before timeIdentifier time ) | timeIdentifier Is time -> ^( Is timeIdentifier time ) )
                alt5 = 3
                LA5_0 = self.input.LA(1)

                if (LA5_0 == ID) :
                    LA5 = self.input.LA(2)
                    if LA5 == After:
                        alt5 = 1
                    elif LA5 == Is:
                        alt5 = 3
                    elif LA5 == Before:
                        alt5 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:62:17: timeIdentifier After time
                    pass 
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_timeConstraint348)
                    timeIdentifier29 = self.timeIdentifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_timeIdentifier.add(timeIdentifier29.tree)
                    After30=self.match(self.input, After, self.FOLLOW_After_in_timeConstraint350) 
                    if self._state.backtracking == 0:
                        stream_After.add(After30)
                    self._state.following.append(self.FOLLOW_time_in_timeConstraint352)
                    time31 = self.time()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_time.add(time31.tree)

                    # AST Rewrite
                    # elements: After, time, timeIdentifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 62:44: -> ^( After timeIdentifier time )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:62:47: ^( After timeIdentifier time )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_After.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_timeIdentifier.nextTree())
                        self._adaptor.addChild(root_1, stream_time.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:63:5: timeIdentifier Before time
                    pass 
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_timeConstraint369)
                    timeIdentifier32 = self.timeIdentifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_timeIdentifier.add(timeIdentifier32.tree)
                    Before33=self.match(self.input, Before, self.FOLLOW_Before_in_timeConstraint371) 
                    if self._state.backtracking == 0:
                        stream_Before.add(Before33)
                    self._state.following.append(self.FOLLOW_time_in_timeConstraint373)
                    time34 = self.time()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_time.add(time34.tree)

                    # AST Rewrite
                    # elements: time, Before, timeIdentifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 63:33: -> ^( Before timeIdentifier time )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:63:36: ^( Before timeIdentifier time )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_Before.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_timeIdentifier.nextTree())
                        self._adaptor.addChild(root_1, stream_time.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 3:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:64:5: timeIdentifier Is time
                    pass 
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_timeConstraint390)
                    timeIdentifier35 = self.timeIdentifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_timeIdentifier.add(timeIdentifier35.tree)
                    Is36=self.match(self.input, Is, self.FOLLOW_Is_in_timeConstraint392) 
                    if self._state.backtracking == 0:
                        stream_Is.add(Is36)
                    self._state.following.append(self.FOLLOW_time_in_timeConstraint394)
                    time37 = self.time()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_time.add(time37.tree)

                    # AST Rewrite
                    # elements: Is, time, timeIdentifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 64:29: -> ^( Is timeIdentifier time )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:64:32: ^( Is timeIdentifier time )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_Is.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_timeIdentifier.nextTree())
                        self._adaptor.addChild(root_1, stream_time.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "timeConstraint"

    class timeIdentifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "timeIdentifier"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:66:1: timeIdentifier : ID ;
    def timeIdentifier(self, ):

        retval = self.timeIdentifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID38 = None

        ID38_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:67:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:67:4: ID
                pass 
                root_0 = self._adaptor.nil()

                ID38=self.match(self.input, ID, self.FOLLOW_ID_in_timeIdentifier416)
                if self._state.backtracking == 0:

                    ID38_tree = self._adaptor.createWithPayload(ID38)
                    self._adaptor.addChild(root_0, ID38_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "timeIdentifier"

    class time_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "time"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:69:1: time : NO ID -> ^( Time NO ID ) ;
    def time(self, ):

        retval = self.time_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NO39 = None
        ID40 = None

        NO39_tree = None
        ID40_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_NO = RewriteRuleTokenStream(self._adaptor, "token NO")

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:69:7: ( NO ID -> ^( Time NO ID ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:69:10: NO ID
                pass 
                NO39=self.match(self.input, NO, self.FOLLOW_NO_in_time426) 
                if self._state.backtracking == 0:
                    stream_NO.add(NO39)
                ID40=self.match(self.input, ID, self.FOLLOW_ID_in_time428) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID40)

                # AST Rewrite
                # elements: ID, NO
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 69:16: -> ^( Time NO ID )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:69:18: ^( Time NO ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Time, "Time"), root_1)

                    self._adaptor.addChild(root_1, stream_NO.nextNode())
                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "time"

    class activityList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "activityList"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:71:1: activityList : ( activity )* -> ^( ActivityList ( activity )* ) ;
    def activityList(self, ):

        retval = self.activityList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        activity41 = None


        stream_activity = RewriteRuleSubtreeStream(self._adaptor, "rule activity")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:72:2: ( ( activity )* -> ^( ActivityList ( activity )* ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:72:4: ( activity )*
                pass 
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:72:4: ( activity )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((Parallel <= LA6_0 <= Rec) or LA6_0 == Wait or LA6_0 == ID or (45 <= LA6_0 <= 46)) :
                        alt6 = 1


                    if alt6 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:72:6: activity
                        pass 
                        self._state.following.append(self.FOLLOW_activity_in_activityList448)
                        activity41 = self.activity()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_activity.add(activity41.tree)


                    else:
                        break #loop6



                # AST Rewrite
                # elements: activity
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 72:16: -> ^( ActivityList ( activity )* )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:72:18: ^( ActivityList ( activity )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ActivityList, "ActivityList"), root_1)

                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:72:33: ( activity )*
                    while stream_activity.hasNext():
                        self._adaptor.addChild(root_1, stream_activity.nextTree())


                    stream_activity.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "activityList"

    class activity_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "activity"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:1: activity : ( ( timeConstraints )? interaction -> ^( Activity interaction ( timeConstraints )? ) | ( timeConstraints )? choice -> ^( Activity choice ( timeConstraints )? ) | ( timeConstraints )? parallel -> ^( Activity parallel ( timeConstraints )? ) | ( timeConstraints )? recursion -> ^( Activity recursion ( timeConstraints )? ) | ( timeConstraints )? cont -> ^( Activity cont ( timeConstraints )? ) | ( timeConstraints )? interruptible -> ^( Activity interruptible ( timeConstraints )? ) | ( timeConstraints )? delay -> ^( Activity delay ( timeConstraints )? ) );
    def activity(self, ):

        retval = self.activity_return()
        retval.start = self.input.LT(1)

        root_0 = None

        timeConstraints42 = None

        interaction43 = None

        timeConstraints44 = None

        choice45 = None

        timeConstraints46 = None

        parallel47 = None

        timeConstraints48 = None

        recursion49 = None

        timeConstraints50 = None

        cont51 = None

        timeConstraints52 = None

        interruptible53 = None

        timeConstraints54 = None

        delay55 = None


        stream_parallel = RewriteRuleSubtreeStream(self._adaptor, "rule parallel")
        stream_choice = RewriteRuleSubtreeStream(self._adaptor, "rule choice")
        stream_timeConstraints = RewriteRuleSubtreeStream(self._adaptor, "rule timeConstraints")
        stream_interaction = RewriteRuleSubtreeStream(self._adaptor, "rule interaction")
        stream_delay = RewriteRuleSubtreeStream(self._adaptor, "rule delay")
        stream_cont = RewriteRuleSubtreeStream(self._adaptor, "rule cont")
        stream_interruptible = RewriteRuleSubtreeStream(self._adaptor, "rule interruptible")
        stream_recursion = RewriteRuleSubtreeStream(self._adaptor, "rule recursion")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:9: ( ( timeConstraints )? interaction -> ^( Activity interaction ( timeConstraints )? ) | ( timeConstraints )? choice -> ^( Activity choice ( timeConstraints )? ) | ( timeConstraints )? parallel -> ^( Activity parallel ( timeConstraints )? ) | ( timeConstraints )? recursion -> ^( Activity recursion ( timeConstraints )? ) | ( timeConstraints )? cont -> ^( Activity cont ( timeConstraints )? ) | ( timeConstraints )? interruptible -> ^( Activity interruptible ( timeConstraints )? ) | ( timeConstraints )? delay -> ^( Activity delay ( timeConstraints )? ) )
                alt14 = 7
                alt14 = self.dfa14.predict(self.input)
                if alt14 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:11: ( timeConstraints )? interaction
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:11: ( timeConstraints )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == ID) :
                        LA7_1 = self.input.LA(2)

                        if ((Before <= LA7_1 <= Is)) :
                            alt7 = 1
                    if alt7 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:12: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity467)
                        timeConstraints42 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints42.tree)



                    self._state.following.append(self.FOLLOW_interaction_in_activity471)
                    interaction43 = self.interaction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interaction.add(interaction43.tree)

                    # AST Rewrite
                    # elements: timeConstraints, interaction
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 74:41: -> ^( Activity interaction ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:44: ^( Activity interaction ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_interaction.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:74:67: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:75:5: ( timeConstraints )? choice
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:75:5: ( timeConstraints )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == ID) :
                        alt8 = 1
                    if alt8 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:0:0: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity487)
                        timeConstraints44 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints44.tree)



                    self._state.following.append(self.FOLLOW_choice_in_activity490)
                    choice45 = self.choice()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_choice.add(choice45.tree)

                    # AST Rewrite
                    # elements: timeConstraints, choice
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 75:28: -> ^( Activity choice ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:75:31: ^( Activity choice ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_choice.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:75:49: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 3:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:76:5: ( timeConstraints )? parallel
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:76:5: ( timeConstraints )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == ID) :
                        alt9 = 1
                    if alt9 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:0:0: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity508)
                        timeConstraints46 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints46.tree)



                    self._state.following.append(self.FOLLOW_parallel_in_activity511)
                    parallel47 = self.parallel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parallel.add(parallel47.tree)

                    # AST Rewrite
                    # elements: parallel, timeConstraints
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 76:30: -> ^( Activity parallel ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:76:33: ^( Activity parallel ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_parallel.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:76:53: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 4:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:77:5: ( timeConstraints )? recursion
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:77:5: ( timeConstraints )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ID) :
                        alt10 = 1
                    if alt10 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:0:0: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity527)
                        timeConstraints48 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints48.tree)



                    self._state.following.append(self.FOLLOW_recursion_in_activity530)
                    recursion49 = self.recursion()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_recursion.add(recursion49.tree)

                    # AST Rewrite
                    # elements: recursion, timeConstraints
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 77:31: -> ^( Activity recursion ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:77:34: ^( Activity recursion ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_recursion.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:77:55: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 5:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:78:5: ( timeConstraints )? cont
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:78:5: ( timeConstraints )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID) :
                        alt11 = 1
                    if alt11 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:0:0: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity546)
                        timeConstraints50 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints50.tree)



                    self._state.following.append(self.FOLLOW_cont_in_activity549)
                    cont51 = self.cont()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_cont.add(cont51.tree)

                    # AST Rewrite
                    # elements: timeConstraints, cont
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 78:26: -> ^( Activity cont ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:78:29: ^( Activity cont ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_cont.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:78:45: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 6:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:79:5: ( timeConstraints )? interruptible
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:79:5: ( timeConstraints )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == ID) :
                        alt12 = 1
                    if alt12 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:0:0: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity565)
                        timeConstraints52 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints52.tree)



                    self._state.following.append(self.FOLLOW_interruptible_in_activity568)
                    interruptible53 = self.interruptible()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interruptible.add(interruptible53.tree)

                    # AST Rewrite
                    # elements: timeConstraints, interruptible
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 79:35: -> ^( Activity interruptible ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:79:37: ^( Activity interruptible ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_interruptible.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:79:62: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 7:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:80:5: ( timeConstraints )? delay
                    pass 
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:80:5: ( timeConstraints )?
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ID) :
                        alt13 = 1
                    if alt13 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:0:0: timeConstraints
                        pass 
                        self._state.following.append(self.FOLLOW_timeConstraints_in_activity583)
                        timeConstraints54 = self.timeConstraints()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_timeConstraints.add(timeConstraints54.tree)



                    self._state.following.append(self.FOLLOW_delay_in_activity586)
                    delay55 = self.delay()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_delay.add(delay55.tree)

                    # AST Rewrite
                    # elements: delay, timeConstraints
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 80:28: -> ^( Activity delay ( timeConstraints )? )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:80:31: ^( Activity delay ( timeConstraints )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Activity, "Activity"), root_1)

                        self._adaptor.addChild(root_1, stream_delay.nextTree())
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:80:48: ( timeConstraints )?
                        if stream_timeConstraints.hasNext():
                            self._adaptor.addChild(root_1, stream_timeConstraints.nextTree())


                        stream_timeConstraints.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "activity"

    class delay_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "delay"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:82:1: delay : ( Wait timeIdentifier Symbol time -> ^( Wait timeIdentifier Symbol time ) | Wait timeIdentifier Is time -> ^( Wait timeIdentifier time ) );
    def delay(self, ):

        retval = self.delay_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Wait56 = None
        Symbol58 = None
        Wait60 = None
        Is62 = None
        timeIdentifier57 = None

        time59 = None

        timeIdentifier61 = None

        time63 = None


        Wait56_tree = None
        Symbol58_tree = None
        Wait60_tree = None
        Is62_tree = None
        stream_Symbol = RewriteRuleTokenStream(self._adaptor, "token Symbol")
        stream_Wait = RewriteRuleTokenStream(self._adaptor, "token Wait")
        stream_Is = RewriteRuleTokenStream(self._adaptor, "token Is")
        stream_time = RewriteRuleSubtreeStream(self._adaptor, "rule time")
        stream_timeIdentifier = RewriteRuleSubtreeStream(self._adaptor, "rule timeIdentifier")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:82:7: ( Wait timeIdentifier Symbol time -> ^( Wait timeIdentifier Symbol time ) | Wait timeIdentifier Is time -> ^( Wait timeIdentifier time ) )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == Wait) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == ID) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == Is) :
                            alt15 = 2
                        elif (LA15_2 == Symbol) :
                            alt15 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:82:9: Wait timeIdentifier Symbol time
                    pass 
                    Wait56=self.match(self.input, Wait, self.FOLLOW_Wait_in_delay608) 
                    if self._state.backtracking == 0:
                        stream_Wait.add(Wait56)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_delay610)
                    timeIdentifier57 = self.timeIdentifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_timeIdentifier.add(timeIdentifier57.tree)
                    Symbol58=self.match(self.input, Symbol, self.FOLLOW_Symbol_in_delay612) 
                    if self._state.backtracking == 0:
                        stream_Symbol.add(Symbol58)
                    self._state.following.append(self.FOLLOW_time_in_delay614)
                    time59 = self.time()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_time.add(time59.tree)

                    # AST Rewrite
                    # elements: timeIdentifier, time, Wait, Symbol
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 82:41: -> ^( Wait timeIdentifier Symbol time )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:82:44: ^( Wait timeIdentifier Symbol time )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_Wait.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_timeIdentifier.nextTree())
                        self._adaptor.addChild(root_1, stream_Symbol.nextNode())
                        self._adaptor.addChild(root_1, stream_time.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt15 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:83:5: Wait timeIdentifier Is time
                    pass 
                    Wait60=self.match(self.input, Wait, self.FOLLOW_Wait_in_delay632) 
                    if self._state.backtracking == 0:
                        stream_Wait.add(Wait60)
                    self._state.following.append(self.FOLLOW_timeIdentifier_in_delay634)
                    timeIdentifier61 = self.timeIdentifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_timeIdentifier.add(timeIdentifier61.tree)
                    Is62=self.match(self.input, Is, self.FOLLOW_Is_in_delay636) 
                    if self._state.backtracking == 0:
                        stream_Is.add(Is62)
                    self._state.following.append(self.FOLLOW_time_in_delay638)
                    time63 = self.time()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_time.add(time63.tree)

                    # AST Rewrite
                    # elements: time, Wait, timeIdentifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 83:33: -> ^( Wait timeIdentifier time )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:83:36: ^( Wait timeIdentifier time )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_Wait.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_timeIdentifier.nextTree())
                        self._adaptor.addChild(root_1, stream_time.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "delay"

    class interaction_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interaction"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:85:1: interaction : message 'from' roleName 'to' roleName 'within' time ';' -> ^( Message message roleName roleName time ) ;
    def interaction(self, ):

        retval = self.interaction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal65 = None
        string_literal67 = None
        string_literal69 = None
        char_literal71 = None
        message64 = None

        roleName66 = None

        roleName68 = None

        time70 = None


        string_literal65_tree = None
        string_literal67_tree = None
        string_literal69_tree = None
        char_literal71_tree = None
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_time = RewriteRuleSubtreeStream(self._adaptor, "rule time")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:86:2: ( message 'from' roleName 'to' roleName 'within' time ';' -> ^( Message message roleName roleName time ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:86:4: message 'from' roleName 'to' roleName 'within' time ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_interaction657)
                message64 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message64.tree)
                string_literal65=self.match(self.input, 39, self.FOLLOW_39_in_interaction659) 
                if self._state.backtracking == 0:
                    stream_39.add(string_literal65)
                self._state.following.append(self.FOLLOW_roleName_in_interaction661)
                roleName66 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName66.tree)
                string_literal67=self.match(self.input, 40, self.FOLLOW_40_in_interaction663) 
                if self._state.backtracking == 0:
                    stream_40.add(string_literal67)
                self._state.following.append(self.FOLLOW_roleName_in_interaction665)
                roleName68 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName68.tree)
                string_literal69=self.match(self.input, 41, self.FOLLOW_41_in_interaction667) 
                if self._state.backtracking == 0:
                    stream_41.add(string_literal69)
                self._state.following.append(self.FOLLOW_time_in_interaction669)
                time70 = self.time()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_time.add(time70.tree)
                char_literal71=self.match(self.input, 42, self.FOLLOW_42_in_interaction671) 
                if self._state.backtracking == 0:
                    stream_42.add(char_literal71)

                # AST Rewrite
                # elements: roleName, time, roleName, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 86:60: -> ^( Message message roleName roleName time )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:86:63: ^( Message message roleName roleName time )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Message, "Message"), root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())
                    self._adaptor.addChild(root_1, stream_roleName.nextTree())
                    self._adaptor.addChild(root_1, stream_roleName.nextTree())
                    self._adaptor.addChild(root_1, stream_time.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "interaction"

    class choice_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "choice"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:88:1: choice : Choice 'at' roleName block ( 'or' block )* -> ^( Choice roleName ( block )+ ) ;
    def choice(self, ):

        retval = self.choice_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Choice72 = None
        string_literal73 = None
        string_literal76 = None
        roleName74 = None

        block75 = None

        block77 = None


        Choice72_tree = None
        string_literal73_tree = None
        string_literal76_tree = None
        stream_Choice = RewriteRuleTokenStream(self._adaptor, "token Choice")
        stream_43 = RewriteRuleTokenStream(self._adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self._adaptor, "token 44")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:89:2: ( Choice 'at' roleName block ( 'or' block )* -> ^( Choice roleName ( block )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:89:4: Choice 'at' roleName block ( 'or' block )*
                pass 
                Choice72=self.match(self.input, Choice, self.FOLLOW_Choice_in_choice694) 
                if self._state.backtracking == 0:
                    stream_Choice.add(Choice72)
                string_literal73=self.match(self.input, 43, self.FOLLOW_43_in_choice696) 
                if self._state.backtracking == 0:
                    stream_43.add(string_literal73)
                self._state.following.append(self.FOLLOW_roleName_in_choice698)
                roleName74 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName74.tree)
                self._state.following.append(self.FOLLOW_block_in_choice700)
                block75 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block75.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:89:31: ( 'or' block )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 44) :
                        alt16 = 1


                    if alt16 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:89:33: 'or' block
                        pass 
                        string_literal76=self.match(self.input, 44, self.FOLLOW_44_in_choice704) 
                        if self._state.backtracking == 0:
                            stream_44.add(string_literal76)
                        self._state.following.append(self.FOLLOW_block_in_choice707)
                        block77 = self.block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_block.add(block77.tree)


                    else:
                        break #loop16



                # AST Rewrite
                # elements: Choice, block, roleName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 89:48: -> ^( Choice roleName ( block )+ )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:89:51: ^( Choice roleName ( block )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_Choice.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_roleName.nextTree())
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:89:69: ( block )+
                    if not (stream_block.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_block.hasNext():
                        self._adaptor.addChild(root_1, stream_block.nextTree())


                    stream_block.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "choice"

    class parallel_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "parallel"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:91:1: parallel : Parallel block ( 'and' block )+ -> ^( Parallel block ( block )+ ) ;
    def parallel(self, ):

        retval = self.parallel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Parallel78 = None
        string_literal80 = None
        block79 = None

        block81 = None


        Parallel78_tree = None
        string_literal80_tree = None
        stream_Parallel = RewriteRuleTokenStream(self._adaptor, "token Parallel")
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:91:9: ( Parallel block ( 'and' block )+ -> ^( Parallel block ( block )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:92:3: Parallel block ( 'and' block )+
                pass 
                Parallel78=self.match(self.input, Parallel, self.FOLLOW_Parallel_in_parallel733) 
                if self._state.backtracking == 0:
                    stream_Parallel.add(Parallel78)
                self._state.following.append(self.FOLLOW_block_in_parallel735)
                block79 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block79.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:92:18: ( 'and' block )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == 38) :
                        alt17 = 1


                    if alt17 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:92:20: 'and' block
                        pass 
                        string_literal80=self.match(self.input, 38, self.FOLLOW_38_in_parallel739) 
                        if self._state.backtracking == 0:
                            stream_38.add(string_literal80)
                        self._state.following.append(self.FOLLOW_block_in_parallel742)
                        block81 = self.block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_block.add(block81.tree)


                    else:
                        if cnt17 >= 1:
                            break #loop17

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1



                # AST Rewrite
                # elements: Parallel, block, block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 92:37: -> ^( Parallel block ( block )+ )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:92:40: ^( Parallel block ( block )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_Parallel.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_block.nextTree())
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:92:57: ( block )+
                    if not (stream_block.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_block.hasNext():
                        self._adaptor.addChild(root_1, stream_block.nextTree())


                    stream_block.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "parallel"

    class recursion_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "recursion"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:94:1: recursion : Rec identifier block -> ^( Rec identifier block ) ;
    def recursion(self, ):

        retval = self.recursion_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Rec82 = None
        identifier83 = None

        block84 = None


        Rec82_tree = None
        stream_Rec = RewriteRuleTokenStream(self._adaptor, "token Rec")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:95:2: ( Rec identifier block -> ^( Rec identifier block ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:95:4: Rec identifier block
                pass 
                Rec82=self.match(self.input, Rec, self.FOLLOW_Rec_in_recursion768) 
                if self._state.backtracking == 0:
                    stream_Rec.add(Rec82)
                self._state.following.append(self.FOLLOW_identifier_in_recursion770)
                identifier83 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier83.tree)
                self._state.following.append(self.FOLLOW_block_in_recursion772)
                block84 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block84.tree)

                # AST Rewrite
                # elements: identifier, block, Rec
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 95:24: -> ^( Rec identifier block )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:95:27: ^( Rec identifier block )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_Rec.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_identifier.nextTree())
                    self._adaptor.addChild(root_1, stream_block.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "recursion"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "identifier"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:97:1: identifier : ID ;
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID85 = None

        ID85_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:98:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:98:4: ID
                pass 
                root_0 = self._adaptor.nil()

                ID85=self.match(self.input, ID, self.FOLLOW_ID_in_identifier791)
                if self._state.backtracking == 0:

                    ID85_tree = self._adaptor.createWithPayload(ID85)
                    self._adaptor.addChild(root_0, ID85_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "identifier"

    class cont_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "cont"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:100:1: cont : 'continue' identifier ';' -> ^( Continue identifier ) ;
    def cont(self, ):

        retval = self.cont_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal86 = None
        char_literal88 = None
        identifier87 = None


        string_literal86_tree = None
        char_literal88_tree = None
        stream_45 = RewriteRuleTokenStream(self._adaptor, "token 45")
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:100:6: ( 'continue' identifier ';' -> ^( Continue identifier ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:100:8: 'continue' identifier ';'
                pass 
                string_literal86=self.match(self.input, 45, self.FOLLOW_45_in_cont800) 
                if self._state.backtracking == 0:
                    stream_45.add(string_literal86)
                self._state.following.append(self.FOLLOW_identifier_in_cont802)
                identifier87 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier87.tree)
                char_literal88=self.match(self.input, 42, self.FOLLOW_42_in_cont804) 
                if self._state.backtracking == 0:
                    stream_42.add(char_literal88)

                # AST Rewrite
                # elements: identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 100:33: -> ^( Continue identifier )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:100:36: ^( Continue identifier )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Continue, "Continue"), root_1)

                    self._adaptor.addChild(root_1, stream_identifier.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "cont"

    class interruptible_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "interruptible"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:102:1: interruptible : 'interruptible' block withMessage -> ^( Interrupt block withMessage ) ;
    def interruptible(self, ):

        retval = self.interruptible_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal89 = None
        block90 = None

        withMessage91 = None


        string_literal89_tree = None
        stream_46 = RewriteRuleTokenStream(self._adaptor, "token 46")
        stream_withMessage = RewriteRuleSubtreeStream(self._adaptor, "rule withMessage")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:103:2: ( 'interruptible' block withMessage -> ^( Interrupt block withMessage ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:103:4: 'interruptible' block withMessage
                pass 
                string_literal89=self.match(self.input, 46, self.FOLLOW_46_in_interruptible820) 
                if self._state.backtracking == 0:
                    stream_46.add(string_literal89)
                self._state.following.append(self.FOLLOW_block_in_interruptible822)
                block90 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block90.tree)
                self._state.following.append(self.FOLLOW_withMessage_in_interruptible824)
                withMessage91 = self.withMessage()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_withMessage.add(withMessage91.tree)

                # AST Rewrite
                # elements: withMessage, block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 103:37: -> ^( Interrupt block withMessage )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:103:40: ^( Interrupt block withMessage )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Interrupt, "Interrupt"), root_1)

                    self._adaptor.addChild(root_1, stream_block.nextTree())
                    self._adaptor.addChild(root_1, stream_withMessage.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "interruptible"

    class withMessage_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "withMessage"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:105:1: withMessage : 'by' roleName 'with' message ( ',' 'by' roleName 'with' message )* -> ^( With ( roleName message )+ ) ;
    def withMessage(self, ):

        retval = self.withMessage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal92 = None
        string_literal94 = None
        char_literal96 = None
        string_literal97 = None
        string_literal99 = None
        roleName93 = None

        message95 = None

        roleName98 = None

        message100 = None


        string_literal92_tree = None
        string_literal94_tree = None
        char_literal96_tree = None
        string_literal97_tree = None
        string_literal99_tree = None
        stream_48 = RewriteRuleTokenStream(self._adaptor, "token 48")
        stream_47 = RewriteRuleTokenStream(self._adaptor, "token 47")
        stream_32 = RewriteRuleTokenStream(self._adaptor, "token 32")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:106:2: ( 'by' roleName 'with' message ( ',' 'by' roleName 'with' message )* -> ^( With ( roleName message )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:106:4: 'by' roleName 'with' message ( ',' 'by' roleName 'with' message )*
                pass 
                string_literal92=self.match(self.input, 47, self.FOLLOW_47_in_withMessage843) 
                if self._state.backtracking == 0:
                    stream_47.add(string_literal92)
                self._state.following.append(self.FOLLOW_roleName_in_withMessage845)
                roleName93 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName93.tree)
                string_literal94=self.match(self.input, 48, self.FOLLOW_48_in_withMessage847) 
                if self._state.backtracking == 0:
                    stream_48.add(string_literal94)
                self._state.following.append(self.FOLLOW_message_in_withMessage849)
                message95 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message95.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:106:33: ( ',' 'by' roleName 'with' message )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 32) :
                        alt18 = 1


                    if alt18 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:106:34: ',' 'by' roleName 'with' message
                        pass 
                        char_literal96=self.match(self.input, 32, self.FOLLOW_32_in_withMessage852) 
                        if self._state.backtracking == 0:
                            stream_32.add(char_literal96)
                        string_literal97=self.match(self.input, 47, self.FOLLOW_47_in_withMessage853) 
                        if self._state.backtracking == 0:
                            stream_47.add(string_literal97)
                        self._state.following.append(self.FOLLOW_roleName_in_withMessage855)
                        roleName98 = self.roleName()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roleName.add(roleName98.tree)
                        string_literal99=self.match(self.input, 48, self.FOLLOW_48_in_withMessage857) 
                        if self._state.backtracking == 0:
                            stream_48.add(string_literal99)
                        self._state.following.append(self.FOLLOW_message_in_withMessage859)
                        message100 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message100.tree)


                    else:
                        break #loop18



                # AST Rewrite
                # elements: roleName, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 106:68: -> ^( With ( roleName message )+ )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:106:71: ^( With ( roleName message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(With, "With"), root_1)

                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:106:78: ( roleName message )+
                    if not (stream_roleName.hasNext() or stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roleName.hasNext() or stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_roleName.nextTree())
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_roleName.reset()
                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "withMessage"

    class message_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "message"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:108:1: message : ( ID -> ^( Msg ID ) | messageSignature -> ^( Msg messageSignature ) );
    def message(self, ):

        retval = self.message_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID101 = None
        messageSignature102 = None


        ID101_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_messageSignature = RewriteRuleSubtreeStream(self._adaptor, "rule messageSignature")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:108:9: ( ID -> ^( Msg ID ) | messageSignature -> ^( Msg messageSignature ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == ID) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == EOF or (Parallel <= LA19_1 <= Rec) or LA19_1 == Wait or LA19_1 == ID or LA19_1 == 32 or LA19_1 == 37 or LA19_1 == 39 or (45 <= LA19_1 <= 46)) :
                        alt19 = 1
                    elif (LA19_1 == 33) :
                        alt19 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 19, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:108:11: ID
                    pass 
                    ID101=self.match(self.input, ID, self.FOLLOW_ID_in_message883) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID101)

                    # AST Rewrite
                    # elements: ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 108:14: -> ^( Msg ID )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:108:17: ^( Msg ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Msg, "Msg"), root_1)

                        self._adaptor.addChild(root_1, stream_ID.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt19 == 2:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:109:5: messageSignature
                    pass 
                    self._state.following.append(self.FOLLOW_messageSignature_in_message897)
                    messageSignature102 = self.messageSignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_messageSignature.add(messageSignature102.tree)

                    # AST Rewrite
                    # elements: messageSignature
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 109:22: -> ^( Msg messageSignature )
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:109:25: ^( Msg messageSignature )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(Msg, "Msg"), root_1)

                        self._adaptor.addChild(root_1, stream_messageSignature.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "message"

    class messageSignature_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "messageSignature"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:111:1: messageSignature : messageOperator '(' payloadType ( ',' payloadType )* ')' -> ^( MsgSig messageOperator ( payloadType )+ ) ;
    def messageSignature(self, ):

        retval = self.messageSignature_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal104 = None
        char_literal106 = None
        char_literal108 = None
        messageOperator103 = None

        payloadType105 = None

        payloadType107 = None


        char_literal104_tree = None
        char_literal106_tree = None
        char_literal108_tree = None
        stream_32 = RewriteRuleTokenStream(self._adaptor, "token 32")
        stream_33 = RewriteRuleTokenStream(self._adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_payloadType = RewriteRuleSubtreeStream(self._adaptor, "rule payloadType")
        stream_messageOperator = RewriteRuleSubtreeStream(self._adaptor, "rule messageOperator")
        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:112:2: ( messageOperator '(' payloadType ( ',' payloadType )* ')' -> ^( MsgSig messageOperator ( payloadType )+ ) )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:112:4: messageOperator '(' payloadType ( ',' payloadType )* ')'
                pass 
                self._state.following.append(self.FOLLOW_messageOperator_in_messageSignature916)
                messageOperator103 = self.messageOperator()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_messageOperator.add(messageOperator103.tree)
                char_literal104=self.match(self.input, 33, self.FOLLOW_33_in_messageSignature919) 
                if self._state.backtracking == 0:
                    stream_33.add(char_literal104)
                self._state.following.append(self.FOLLOW_payloadType_in_messageSignature922)
                payloadType105 = self.payloadType()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_payloadType.add(payloadType105.tree)
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:112:38: ( ',' payloadType )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == 32) :
                        alt20 = 1


                    if alt20 == 1:
                        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:112:40: ',' payloadType
                        pass 
                        char_literal106=self.match(self.input, 32, self.FOLLOW_32_in_messageSignature926) 
                        if self._state.backtracking == 0:
                            stream_32.add(char_literal106)
                        self._state.following.append(self.FOLLOW_payloadType_in_messageSignature928)
                        payloadType107 = self.payloadType()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_payloadType.add(payloadType107.tree)


                    else:
                        break #loop20


                char_literal108=self.match(self.input, 34, self.FOLLOW_34_in_messageSignature934) 
                if self._state.backtracking == 0:
                    stream_34.add(char_literal108)

                # AST Rewrite
                # elements: payloadType, messageOperator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 112:64: -> ^( MsgSig messageOperator ( payloadType )+ )
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:112:67: ^( MsgSig messageOperator ( payloadType )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MsgSig, "MsgSig"), root_1)

                    self._adaptor.addChild(root_1, stream_messageOperator.nextTree())
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:112:92: ( payloadType )+
                    if not (stream_payloadType.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_payloadType.hasNext():
                        self._adaptor.addChild(root_1, stream_payloadType.nextTree())


                    stream_payloadType.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "messageSignature"

    class messageOperator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "messageOperator"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:114:1: messageOperator : ID ;
    def messageOperator(self, ):

        retval = self.messageOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID109 = None

        ID109_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:115:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:115:4: ID
                pass 
                root_0 = self._adaptor.nil()

                ID109=self.match(self.input, ID, self.FOLLOW_ID_in_messageOperator958)
                if self._state.backtracking == 0:

                    ID109_tree = self._adaptor.createWithPayload(ID109)
                    self._adaptor.addChild(root_0, ID109_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "messageOperator"

    class payloadType_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "payloadType"
    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:117:1: payloadType : ID ;
    def payloadType(self, ):

        retval = self.payloadType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID110 = None

        ID110_tree = None

        try:
            try:
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:118:2: ( ID )
                # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:118:4: ID
                pass 
                root_0 = self._adaptor.nil()

                ID110=self.match(self.input, ID, self.FOLLOW_ID_in_payloadType968)
                if self._state.backtracking == 0:

                    ID110_tree = self._adaptor.createWithPayload(ID110)
                    self._adaptor.addChild(root_0, ID110_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "payloadType"


    # Delegated rules


    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\35\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\35\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\11\1\25\6\uffff\2\33\1\uffff\1\33\3\32\3\11\1\32\1\25\3\33"
        u"\3\32\3\11"
        )

    DFA14_max = DFA.unpack(
        u"\1\56\1\47\6\uffff\2\33\1\uffff\1\33\3\32\3\56\1\32\1\27\3\33"
        u"\3\32\3\56"
        )

    DFA14_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\5\1\6\1\7\2\uffff\1\1\22\uffff"
        )

    DFA14_special = DFA.unpack(
        u"\35\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\1\22\uffff\1\5"
        u"\1\6"),
        DFA.unpack(u"\1\13\1\11\1\10\11\uffff\1\12\5\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\12\13\uffff\1"
        u"\22\6\uffff\1\5\1\6"),
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\12\13\uffff\1"
        u"\22\6\uffff\1\5\1\6"),
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\12\13\uffff\1"
        u"\22\6\uffff\1\5\1\6"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\25\1\24\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\12\13\uffff\1"
        u"\22\6\uffff\1\5\1\6"),
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\12\13\uffff\1"
        u"\22\6\uffff\1\5\1\6"),
        DFA.unpack(u"\1\3\1\2\1\4\14\uffff\1\7\1\uffff\1\12\13\uffff\1"
        u"\22\6\uffff\1\5\1\6")
    ]

    # class definition for DFA #14

    DFA14 = DFA
 

    FOLLOW_PROTOCOL_in_protocolDef161 = frozenset([26])
    FOLLOW_protocolName_in_protocolDef163 = frozenset([30, 33])
    FOLLOW_30_in_protocolDef166 = frozenset([18])
    FOLLOW_parameters_in_protocolDef168 = frozenset([31])
    FOLLOW_31_in_protocolDef170 = frozenset([30, 33])
    FOLLOW_rolesDef_in_protocolDef175 = frozenset([36])
    FOLLOW_protocolBody_in_protocolDef178 = frozenset([1])
    FOLLOW_ID_in_protocolName201 = frozenset([1])
    FOLLOW_SIG_in_parameters211 = frozenset([26])
    FOLLOW_identifier_in_parameters213 = frozenset([1, 32])
    FOLLOW_32_in_parameters218 = frozenset([18])
    FOLLOW_SIG_in_parameters220 = frozenset([26])
    FOLLOW_identifier_in_parameters222 = frozenset([1, 32])
    FOLLOW_33_in_rolesDef233 = frozenset([35])
    FOLLOW_roleDef_in_rolesDef235 = frozenset([32, 34])
    FOLLOW_32_in_rolesDef238 = frozenset([35])
    FOLLOW_roleDef_in_rolesDef240 = frozenset([32, 34])
    FOLLOW_34_in_rolesDef244 = frozenset([1])
    FOLLOW_35_in_roleDef263 = frozenset([26])
    FOLLOW_roleName_in_roleDef265 = frozenset([1])
    FOLLOW_ID_in_roleName280 = frozenset([1])
    FOLLOW_block_in_protocolBody289 = frozenset([1])
    FOLLOW_36_in_block297 = frozenset([9, 10, 11, 24, 26, 37, 45, 46])
    FOLLOW_activityList_in_block299 = frozenset([37])
    FOLLOW_37_in_block301 = frozenset([1])
    FOLLOW_timeConstraint_in_timeConstraints319 = frozenset([1, 38])
    FOLLOW_38_in_timeConstraints322 = frozenset([26])
    FOLLOW_timeConstraint_in_timeConstraints324 = frozenset([1, 38])
    FOLLOW_timeIdentifier_in_timeConstraint348 = frozenset([22])
    FOLLOW_After_in_timeConstraint350 = frozenset([27])
    FOLLOW_time_in_timeConstraint352 = frozenset([1])
    FOLLOW_timeIdentifier_in_timeConstraint369 = frozenset([21])
    FOLLOW_Before_in_timeConstraint371 = frozenset([27])
    FOLLOW_time_in_timeConstraint373 = frozenset([1])
    FOLLOW_timeIdentifier_in_timeConstraint390 = frozenset([23])
    FOLLOW_Is_in_timeConstraint392 = frozenset([27])
    FOLLOW_time_in_timeConstraint394 = frozenset([1])
    FOLLOW_ID_in_timeIdentifier416 = frozenset([1])
    FOLLOW_NO_in_time426 = frozenset([26])
    FOLLOW_ID_in_time428 = frozenset([1])
    FOLLOW_activity_in_activityList448 = frozenset([1, 9, 10, 11, 24, 26, 45, 46])
    FOLLOW_timeConstraints_in_activity467 = frozenset([26])
    FOLLOW_interaction_in_activity471 = frozenset([1])
    FOLLOW_timeConstraints_in_activity487 = frozenset([10, 26])
    FOLLOW_choice_in_activity490 = frozenset([1])
    FOLLOW_timeConstraints_in_activity508 = frozenset([9, 26])
    FOLLOW_parallel_in_activity511 = frozenset([1])
    FOLLOW_timeConstraints_in_activity527 = frozenset([11, 26])
    FOLLOW_recursion_in_activity530 = frozenset([1])
    FOLLOW_timeConstraints_in_activity546 = frozenset([26, 45])
    FOLLOW_cont_in_activity549 = frozenset([1])
    FOLLOW_timeConstraints_in_activity565 = frozenset([26, 46])
    FOLLOW_interruptible_in_activity568 = frozenset([1])
    FOLLOW_timeConstraints_in_activity583 = frozenset([9, 10, 11, 24, 26, 45, 46])
    FOLLOW_delay_in_activity586 = frozenset([1])
    FOLLOW_Wait_in_delay608 = frozenset([26])
    FOLLOW_timeIdentifier_in_delay610 = frozenset([28])
    FOLLOW_Symbol_in_delay612 = frozenset([27])
    FOLLOW_time_in_delay614 = frozenset([1])
    FOLLOW_Wait_in_delay632 = frozenset([26])
    FOLLOW_timeIdentifier_in_delay634 = frozenset([23])
    FOLLOW_Is_in_delay636 = frozenset([27])
    FOLLOW_time_in_delay638 = frozenset([1])
    FOLLOW_message_in_interaction657 = frozenset([39])
    FOLLOW_39_in_interaction659 = frozenset([26])
    FOLLOW_roleName_in_interaction661 = frozenset([40])
    FOLLOW_40_in_interaction663 = frozenset([26])
    FOLLOW_roleName_in_interaction665 = frozenset([41])
    FOLLOW_41_in_interaction667 = frozenset([27])
    FOLLOW_time_in_interaction669 = frozenset([42])
    FOLLOW_42_in_interaction671 = frozenset([1])
    FOLLOW_Choice_in_choice694 = frozenset([43])
    FOLLOW_43_in_choice696 = frozenset([26])
    FOLLOW_roleName_in_choice698 = frozenset([36])
    FOLLOW_block_in_choice700 = frozenset([1, 44])
    FOLLOW_44_in_choice704 = frozenset([36])
    FOLLOW_block_in_choice707 = frozenset([1, 44])
    FOLLOW_Parallel_in_parallel733 = frozenset([36])
    FOLLOW_block_in_parallel735 = frozenset([38])
    FOLLOW_38_in_parallel739 = frozenset([36])
    FOLLOW_block_in_parallel742 = frozenset([1, 38])
    FOLLOW_Rec_in_recursion768 = frozenset([26])
    FOLLOW_identifier_in_recursion770 = frozenset([36])
    FOLLOW_block_in_recursion772 = frozenset([1])
    FOLLOW_ID_in_identifier791 = frozenset([1])
    FOLLOW_45_in_cont800 = frozenset([26])
    FOLLOW_identifier_in_cont802 = frozenset([42])
    FOLLOW_42_in_cont804 = frozenset([1])
    FOLLOW_46_in_interruptible820 = frozenset([36])
    FOLLOW_block_in_interruptible822 = frozenset([47])
    FOLLOW_withMessage_in_interruptible824 = frozenset([1])
    FOLLOW_47_in_withMessage843 = frozenset([26])
    FOLLOW_roleName_in_withMessage845 = frozenset([48])
    FOLLOW_48_in_withMessage847 = frozenset([26])
    FOLLOW_message_in_withMessage849 = frozenset([1, 32])
    FOLLOW_32_in_withMessage852 = frozenset([47])
    FOLLOW_47_in_withMessage853 = frozenset([26])
    FOLLOW_roleName_in_withMessage855 = frozenset([48])
    FOLLOW_48_in_withMessage857 = frozenset([26])
    FOLLOW_message_in_withMessage859 = frozenset([1, 32])
    FOLLOW_ID_in_message883 = frozenset([1])
    FOLLOW_messageSignature_in_message897 = frozenset([1])
    FOLLOW_messageOperator_in_messageSignature916 = frozenset([33])
    FOLLOW_33_in_messageSignature919 = frozenset([26])
    FOLLOW_payloadType_in_messageSignature922 = frozenset([32, 34])
    FOLLOW_32_in_messageSignature926 = frozenset([26])
    FOLLOW_payloadType_in_messageSignature928 = frozenset([32, 34])
    FOLLOW_34_in_messageSignature934 = frozenset([1])
    FOLLOW_ID_in_messageOperator958 = frozenset([1])
    FOLLOW_ID_in_payloadType968 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("global_scribble_graphLexer", global_scribble_graphParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
