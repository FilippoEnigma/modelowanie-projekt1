grammar TodoList;

task        : 'task' STRING ';';
priority    : 'priority' STRING NUMBER ';';
deadline    : 'deadline' STRING DATE ';';
dependency  : 'dependency' STRING 'on' STRING ';';
tag         : 'tag' STRING STRING ';';
status      : 'status' STRING STATUS ';';
note        : 'note' STRING STRING ';';
groupDeadline : 'groupDeadline' DATE STRING+ ';';
start      : 'start' STRING DATE ';';
duration    : 'duration' STRING NUMBER ';';
resource    : 'resource' STRING STRING+ ';';
file        : (task | priority | deadline | start | duration | dependency | tag | status | note | groupDeadline | resource)+ EOF;

STRING      : '"' ( 'a'..'z' | 'A'..'Z' | '0'..'9' | ' ' )+ '"';
NUMBER      : '0'..'9'+;
DATE        : [0-9][0-9][0-9][0-9]'-'[0-9][0-9]'-'[0-9][0-9];
WS          : [ \t\r\n]+ -> skip;
STATUS      : 'todo' | 'in_progress' | 'done';