grammar global_scribble_graph;

options {
	output=AST;
	backtrack=true;
	language=Java;
	}
	
tokens {
	Message;
	Block;
	ActivityList;
	Activity;
	Constraint='constraint';
	Parallel='parallel';
	Choice='choice';
	Rec='rec';
	Continue;
	Interrupt;
	With;
	Roles;
	ROLE;
	PROTOCOL='global protocol';
	SIG = 'sig';
	MsgSig;
	Msg;
	Before = 'before';
	After = 'after';
	Is = 'is';
	Wait='wait for';
	Time;
	}

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/

protocolDef
	:	PROTOCOL protocolName ('<' parameters '>' )? rolesDef  protocolBody -> ^(PROTOCOL protocolName rolesDef protocolBody) ;
	
protocolName
	:	ID;
	
parameters
	:	SIG identifier  ( ',' SIG identifier )* ;

rolesDef:	'(' roleDef (',' roleDef)* ')' -> ^(Roles (roleDef)+);

roleDef	:	'role' roleName -> ^(ROLE roleName);

roleName:	ID;

protocolBody
	:	block;

block	:	'{' activityList '}' -> ^(Block activityList);

timeConstraints
	:	 timeConstraint ('and' timeConstraint)*  ->^(Constraint (timeConstraint)+);
		
	
timeConstraint:	timeIdentifier After time  -> ^(After timeIdentifier time)
		| timeIdentifier Before time  -> ^(Before timeIdentifier time)
		| timeIdentifier Is time  -> ^(Is timeIdentifier time);
		
timeIdentifier
	:	ID;

time 	:	 NO ID ->^(Time NO ID);

activityList
	:	( activity)*->^(ActivityList activity* );
	
activity:	(timeConstraints)? interaction-> ^(Activity interaction timeConstraints?)
		| timeConstraints? choice-> ^(Activity choice timeConstraints? ) 
		| timeConstraints? parallel-> ^(Activity parallel timeConstraints?)
		| timeConstraints? recursion-> ^(Activity recursion timeConstraints?)
		| timeConstraints? cont-> ^(Activity cont timeConstraints?)
		| timeConstraints? interruptible->^(Activity interruptible timeConstraints?)
		| timeConstraints? delay -> ^(Activity delay timeConstraints?); 
		
delay	:	Wait timeIdentifier Symbol time -> ^(Wait timeIdentifier Symbol time)
		| Wait timeIdentifier Is time -> ^(Wait timeIdentifier time);

interaction
	:	message 'from' roleName 'to' roleName 'within' time ';' -> ^(Message message roleName roleName time);

choice
	:	Choice 'at' roleName block ( 'or'  block )* -> ^(Choice roleName block+ );
	
parallel:	
		Parallel block ( 'and'  block )+  -> ^(Parallel block (block)+);

recursion
	:	Rec identifier block-> ^(Rec identifier block) ;

identifier
	:	ID;
	
cont	:	'continue' identifier ';'-> ^(Continue identifier);

interruptible
	:	'interruptible' block withMessage-> ^(Interrupt block withMessage);
	
withMessage
	:	'by' roleName 'with' message (',''by' roleName 'with' message )*-> ^(With (roleName message)+);
	
message	:	ID -> ^(Msg ID)
		| messageSignature -> ^(Msg  messageSignature );

messageSignature
	:	messageOperator  '('  payloadType ( ',' payloadType )*  ')' -> ^(MsgSig messageOperator (payloadType)+ );
	
messageOperator
	:	ID;
	
payloadType
	:	ID;


	
/*------------------------------------------------------------------
 * LEXER RULES
 *------------------------------------------------------------------*/

ID : ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;

NO 	:	('0'..'9')*;

Symbol	:	('+'|'-'|'*'|'/');

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ 	{ $channel = HIDDEN; } ;


