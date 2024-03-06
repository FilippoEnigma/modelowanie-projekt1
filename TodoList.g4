grammar TodoList;

task        : 'task' STRING ';';
priority    : 'priority' STRING NUMBER ';';
deadline    : 'deadline' STRING DATE ';';
dependency  : 'depends' STRING 'on' STRING ';';

STRING      : '"' ( 'a'..'z' | 'A'..'Z' | '0'..'9' | ' ' )+ '"';
NUMBER      : '0'..'9'+;
DATE        : '0'..'9' {2} '-' '0'..'9' {2} '-' '0'..'9' {4};

WS          : [ \t\r\n]+ -> skip;
