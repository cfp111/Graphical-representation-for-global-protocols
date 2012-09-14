# $ANTLR 3.1.1 C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g 2012-08-30 15:31:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class global_scribble_graphLexer(Lexer):

    grammarFileName = "C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )






    # $ANTLR start "Constraint"
    def mConstraint(self, ):

        try:
            _type = Constraint
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:7:12: ( 'constraint' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:7:14: 'constraint'
            pass 
            self.match("constraint")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Constraint"



    # $ANTLR start "Parallel"
    def mParallel(self, ):

        try:
            _type = Parallel
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:8:10: ( 'parallel' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:8:12: 'parallel'
            pass 
            self.match("parallel")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Parallel"



    # $ANTLR start "Choice"
    def mChoice(self, ):

        try:
            _type = Choice
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:9:8: ( 'choice' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:9:10: 'choice'
            pass 
            self.match("choice")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Choice"



    # $ANTLR start "Rec"
    def mRec(self, ):

        try:
            _type = Rec
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:10:5: ( 'rec' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:10:7: 'rec'
            pass 
            self.match("rec")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Rec"



    # $ANTLR start "PROTOCOL"
    def mPROTOCOL(self, ):

        try:
            _type = PROTOCOL
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:11:10: ( 'global protocol' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:11:12: 'global protocol'
            pass 
            self.match("global protocol")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROTOCOL"



    # $ANTLR start "SIG"
    def mSIG(self, ):

        try:
            _type = SIG
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:12:5: ( 'sig' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:12:7: 'sig'
            pass 
            self.match("sig")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SIG"



    # $ANTLR start "Before"
    def mBefore(self, ):

        try:
            _type = Before
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:13:8: ( 'before' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:13:10: 'before'
            pass 
            self.match("before")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Before"



    # $ANTLR start "After"
    def mAfter(self, ):

        try:
            _type = After
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:14:7: ( 'after' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:14:9: 'after'
            pass 
            self.match("after")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "After"



    # $ANTLR start "Is"
    def mIs(self, ):

        try:
            _type = Is
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:15:4: ( 'is' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:15:6: 'is'
            pass 
            self.match("is")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Is"



    # $ANTLR start "Wait"
    def mWait(self, ):

        try:
            _type = Wait
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:16:6: ( 'wait for' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:16:8: 'wait for'
            pass 
            self.match("wait for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Wait"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:17:7: ( '<' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:17:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:18:7: ( '>' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:18:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:19:7: ( ',' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:19:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:20:7: ( '(' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:20:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:21:7: ( ')' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:21:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:22:7: ( 'role' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:22:9: 'role'
            pass 
            self.match("role")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:23:7: ( '{' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:23:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:24:7: ( '}' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:24:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:25:7: ( 'and' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:25:9: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:26:7: ( 'from' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:26:9: 'from'
            pass 
            self.match("from")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:27:7: ( 'to' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:27:9: 'to'
            pass 
            self.match("to")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:28:7: ( 'within' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:28:9: 'within'
            pass 
            self.match("within")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:29:7: ( ';' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:29:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:30:7: ( 'at' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:30:9: 'at'
            pass 
            self.match("at")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:31:7: ( 'or' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:31:9: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:32:7: ( 'continue' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:32:9: 'continue'
            pass 
            self.match("continue")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:33:7: ( 'interruptible' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:33:9: 'interruptible'
            pass 
            self.match("interruptible")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:34:7: ( 'by' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:34:9: 'by'
            pass 
            self.match("by")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:35:7: ( 'with' )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:35:9: 'with'
            pass 
            self.match("with")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__48"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:126:4: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:126:6: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:126:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "NO"
    def mNO(self, ):

        try:
            _type = NO
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:128:5: ( ( '0' .. '9' )* )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:128:7: ( '0' .. '9' )*
            pass 
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:128:7: ( '0' .. '9' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:128:8: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    break #loop2





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NO"



    # $ANTLR start "Symbol"
    def mSymbol(self, ):

        try:
            _type = Symbol
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:130:8: ( ( '+' | '-' | '*' | '/' ) )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:130:10: ( '+' | '-' | '*' | '/' )
            pass 
            if (42 <= self.input.LA(1) <= 43) or self.input.LA(1) == 45 or self.input.LA(1) == 47:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Symbol"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:132:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:132:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:132:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((9 <= LA3_0 <= 10) or (12 <= LA3_0 <= 13) or LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1


            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:8: ( Constraint | Parallel | Choice | Rec | PROTOCOL | SIG | Before | After | Is | Wait | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | ID | NO | Symbol | WHITESPACE )
        alt4 = 33
        alt4 = self.dfa4.predict(self.input)
        if alt4 == 1:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:10: Constraint
            pass 
            self.mConstraint()


        elif alt4 == 2:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:21: Parallel
            pass 
            self.mParallel()


        elif alt4 == 3:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:30: Choice
            pass 
            self.mChoice()


        elif alt4 == 4:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:37: Rec
            pass 
            self.mRec()


        elif alt4 == 5:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:41: PROTOCOL
            pass 
            self.mPROTOCOL()


        elif alt4 == 6:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:50: SIG
            pass 
            self.mSIG()


        elif alt4 == 7:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:54: Before
            pass 
            self.mBefore()


        elif alt4 == 8:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:61: After
            pass 
            self.mAfter()


        elif alt4 == 9:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:67: Is
            pass 
            self.mIs()


        elif alt4 == 10:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:70: Wait
            pass 
            self.mWait()


        elif alt4 == 11:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:75: T__30
            pass 
            self.mT__30()


        elif alt4 == 12:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:81: T__31
            pass 
            self.mT__31()


        elif alt4 == 13:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:87: T__32
            pass 
            self.mT__32()


        elif alt4 == 14:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:93: T__33
            pass 
            self.mT__33()


        elif alt4 == 15:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:99: T__34
            pass 
            self.mT__34()


        elif alt4 == 16:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:105: T__35
            pass 
            self.mT__35()


        elif alt4 == 17:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:111: T__36
            pass 
            self.mT__36()


        elif alt4 == 18:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:117: T__37
            pass 
            self.mT__37()


        elif alt4 == 19:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:123: T__38
            pass 
            self.mT__38()


        elif alt4 == 20:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:129: T__39
            pass 
            self.mT__39()


        elif alt4 == 21:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:135: T__40
            pass 
            self.mT__40()


        elif alt4 == 22:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:141: T__41
            pass 
            self.mT__41()


        elif alt4 == 23:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:147: T__42
            pass 
            self.mT__42()


        elif alt4 == 24:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:153: T__43
            pass 
            self.mT__43()


        elif alt4 == 25:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:159: T__44
            pass 
            self.mT__44()


        elif alt4 == 26:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:165: T__45
            pass 
            self.mT__45()


        elif alt4 == 27:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:171: T__46
            pass 
            self.mT__46()


        elif alt4 == 28:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:177: T__47
            pass 
            self.mT__47()


        elif alt4 == 29:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:183: T__48
            pass 
            self.mT__48()


        elif alt4 == 30:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:189: ID
            pass 
            self.mID()


        elif alt4 == 31:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:192: NO
            pass 
            self.mNO()


        elif alt4 == 32:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:195: Symbol
            pass 
            self.mSymbol()


        elif alt4 == 33:
            # C:\\Users\\Charlotte\\Documents\\Imperial\\course\\IndividualProject\\EssaiAntlr\\globalProtocolGraph\\global_scribble_graph.g:1:202: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\1\26\11\25\7\uffff\2\25\1\uffff\1\25\4\uffff\10\25\1\64\2\25"
        u"\1\67\1\70\4\25\1\75\1\76\3\25\1\103\2\25\1\106\1\25\1\uffff\1"
        u"\25\1\111\2\uffff\4\25\2\uffff\4\25\1\uffff\1\122\1\25\1\uffff"
        u"\2\25\1\uffff\2\25\1\131\1\132\4\25\1\uffff\2\25\1\141\1\25\1\uffff"
        u"\1\25\2\uffff\2\25\1\146\2\25\1\151\1\uffff\1\25\1\153\2\25\1\uffff"
        u"\1\25\2\uffff\1\25\1\uffff\1\25\1\161\1\162\2\25\2\uffff\1\25\1"
        u"\166\1\25\1\uffff\2\25\1\172\1\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\173\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\1\11\1\150\1\141\1\145\1\154\1\151\1\145\1\146\1\156\1\141\7"
        u"\uffff\1\162\1\157\1\uffff\1\162\4\uffff\1\156\1\157\1\162\1\143"
        u"\1\154\1\157\1\147\1\146\1\60\1\164\1\144\2\60\1\164\1\151\1\164"
        u"\1\157\2\60\1\163\1\151\1\141\1\60\1\145\1\142\1\60\1\157\1\uffff"
        u"\1\145\1\60\2\uffff\1\145\1\164\1\150\1\155\2\uffff\1\164\1\151"
        u"\1\143\1\154\1\uffff\1\60\1\141\1\uffff\2\162\1\uffff\1\162\1\40"
        u"\2\60\1\162\1\156\1\145\1\154\1\uffff\1\154\1\145\1\60\1\162\1"
        u"\uffff\1\156\2\uffff\1\141\1\165\1\60\1\145\1\40\1\60\1\uffff\1"
        u"\165\1\60\1\151\1\145\1\uffff\1\154\2\uffff\1\160\1\uffff\1\156"
        u"\2\60\2\164\2\uffff\1\151\1\60\1\142\1\uffff\1\154\1\145\1\60\1"
        u"\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\1\175\1\157\1\141\1\157\1\154\1\151\1\171\1\164\1\163\1\151\7"
        u"\uffff\1\162\1\157\1\uffff\1\162\4\uffff\1\156\1\157\1\162\1\143"
        u"\1\154\1\157\1\147\1\146\1\172\1\164\1\144\2\172\1\164\1\151\1"
        u"\164\1\157\2\172\1\164\1\151\1\141\1\172\1\145\1\142\1\172\1\157"
        u"\1\uffff\1\145\1\172\2\uffff\1\145\1\164\1\150\1\155\2\uffff\1"
        u"\164\1\151\1\143\1\154\1\uffff\1\172\1\141\1\uffff\2\162\1\uffff"
        u"\1\162\1\40\2\172\1\162\1\156\1\145\1\154\1\uffff\1\154\1\145\1"
        u"\172\1\162\1\uffff\1\156\2\uffff\1\141\1\165\1\172\1\145\1\40\1"
        u"\172\1\uffff\1\165\1\172\1\151\1\145\1\uffff\1\154\2\uffff\1\160"
        u"\1\uffff\1\156\2\172\2\164\2\uffff\1\151\1\172\1\142\1\uffff\1"
        u"\154\1\145\1\172\1\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\12\uffff\1\13\1\14\1\15\1\16\1\17\1\21\1\22\2\uffff\1\27\1\uffff"
        u"\1\36\1\37\1\40\1\41\33\uffff\1\34\2\uffff\1\30\1\11\4\uffff\1"
        u"\25\1\31\4\uffff\1\4\2\uffff\1\6\2\uffff\1\23\10\uffff\1\20\4\uffff"
        u"\1\12\1\uffff\1\35\1\24\6\uffff\1\10\4\uffff\1\3\1\uffff\1\5\1"
        u"\7\1\uffff\1\26\5\uffff\1\32\1\2\3\uffff\1\1\3\uffff\1\33"
        )

    DFA4_special = DFA.unpack(
        u"\173\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\2\30\1\uffff\2\30\22\uffff\1\30\7\uffff\1\15\1\16"
        u"\2\27\1\14\1\27\1\uffff\1\27\13\uffff\1\23\1\12\1\uffff\1\13\2"
        u"\uffff\32\25\4\uffff\1\25\1\uffff\1\7\1\6\1\1\2\25\1\21\1\4\1\25"
        u"\1\10\5\25\1\24\1\2\1\25\1\3\1\5\1\22\2\25\1\11\3\25\1\17\1\uffff"
        u"\1\20"),
        DFA.unpack(u"\1\32\6\uffff\1\31"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34\11\uffff\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40\23\uffff\1\41"),
        DFA.unpack(u"\1\42\7\uffff\1\43\5\uffff\1\44"),
        DFA.unpack(u"\1\46\4\uffff\1\45"),
        DFA.unpack(u"\1\47\7\uffff\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\77\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\10\25\1"
        u"\130\21\25"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    DFA4 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(global_scribble_graphLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
