	.data
str_nl: .asciz "\n"
j Lmain
L0:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L1:
#	<function Quad.toString at 0x7fbabff34c10>
li a7, 5
ecall
lw t0, -4(sp)
addi t0, t0, -12
sw a7, 0(t0)
L2:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L3:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L4:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
ble t0, t1, 6
L5:
#	<function Quad.toString at 0x7fbabff34c10>
j 11
L6:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
mul t0, t1, t0
sw t0, -24(sp)
L7:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L8:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
add t0, t1, t0
sw t0, -28(sp)
L9:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L10:
#	<function Quad.toString at 0x7fbabff34c10>
j 4
L11:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L12:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L13:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L14:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
ble t0, t1, 16
L15:
#	<function Quad.toString at 0x7fbabff34c10>
j 18
L16:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)
L17:
#	<function Quad.toString at 0x7fbabff34c10>
j 28
L18:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
sub t0, t1, t0
sw t0, -16(sp)
L19:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
lw t0, -16(sp)
sw t0, --12(fp)
L20:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L21:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
sw t0, -4(fp)
addi sp, sp, 36
jal 13
addi sp, sp, -36
L22:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 2
li t1, 2
sub t0, t1, t0
sw t0, -24(sp)
L23:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
lw t0, -24(sp)
sw t0, --12(fp)
L24:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L25:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
sw t0, -4(fp)
addi sp, sp, 36
jal 13
addi sp, sp, -36
L26:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -20(sp)
lw t1, -28(sp)
add t0, t1, t0
sw t0, -32(sp)
L27:
#	<function Quad.toString at 0x7fbabff34c10>
lw t1, -32(sp)
lw t0, -8(sp)
sw t1, 0(t0)
L28:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L29:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L30:
#	<function Quad.toString at 0x7fbabff34c10>
li a7, 5
ecall
lw t0, -4(sp)
addi t0, t0, -12
sw a7, 0(t0)
L31:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)
L32:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L33:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 36
jal 13
addi sp, sp, -36
L34:
#	<function Quad.toString at 0x7fbabff34c10>
lw a0, -16(sp)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L35:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L36:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L37:
#	<function Quad.toString at 0x7fbabff34c10>
li a7, 5
ecall
lw t0, -4(sp)
addi t0, t0, -12
sw a7, 0(t0)
L38:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L39:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 0
li t1, 0
bgt t0, t1, 41
L40:
#	<function Quad.toString at 0x7fbabff34c10>
j 46
L41:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 10
li t1, 10
div t0, t1, t0
sw t0, -20(sp)
L42:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L43:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
add t0, t1, t0
sw t0, -24(sp)
L44:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L45:
#	<function Quad.toString at 0x7fbabff34c10>
j 39
L46:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L47:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L48:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L49:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
div t0, t1, t0
sw t0, -20(sp)
L50:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -20(sp)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
mul t0, t1, t0
sw t0, -24(sp)
L51:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t1, -24(sp)
beq t0, t1, 53
L52:
#	<function Quad.toString at 0x7fbabff34c10>
j 55
L53:
#	<function Quad.toString at 0x7fbabff34c10>
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)
L54:
#	<function Quad.toString at 0x7fbabff34c10>
j 56
L55:
#	<function Quad.toString at 0x7fbabff34c10>
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)
L56:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L57:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L58:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L59:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
blt t0, t1, 61
L60:
#	<function Quad.toString at 0x7fbabff34c10>
j 72
L61:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)
L62:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)
L63:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L64:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 28
jal 48
addi sp, sp, -28
L65:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
beq t0, t1, 67
L66:
#	<function Quad.toString at 0x7fbabff34c10>
j 69
L67:
#	<function Quad.toString at 0x7fbabff34c10>
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)
L68:
#	<function Quad.toString at 0x7fbabff34c10>
j _
L69:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
add t0, t1, t0
sw t0, -24(sp)
L70:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L71:
#	<function Quad.toString at 0x7fbabff34c10>
j 59
L72:
#	<function Quad.toString at 0x7fbabff34c10>
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)
L73:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L74:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L75:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L76:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 30
li t1, 30
ble t0, t1, 78
L77:
#	<function Quad.toString at 0x7fbabff34c10>
j 88
L78:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)
L79:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L80:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 28
jal 57
addi sp, sp, -28
L81:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
beq t0, t1, 83
L82:
#	<function Quad.toString at 0x7fbabff34c10>
j 85
L83:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L84:
#	<function Quad.toString at 0x7fbabff34c10>
j _
L85:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
add t0, t1, t0
sw t0, -20(sp)
L86:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L87:
#	<function Quad.toString at 0x7fbabff34c10>
j 76
L88:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L89:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L90:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
bgt t0, t1, 92
L91:
#	<function Quad.toString at 0x7fbabff34c10>
j 94
L92:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)
L93:
#	<function Quad.toString at 0x7fbabff34c10>
j 95
L94:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)
L95:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L96:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L97:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
li t0, 5
sw t0, --12(fp)
L98:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
li t0, 7
sw t0, --12(fp)
L99:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L100:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 20
jal 89
addi sp, sp, -20
L101:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, 20
lw t0, -16(sp)
sw t0, --12(fp)
L102:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
li t0, 8
sw t0, --12(fp)
L103:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, None
li t0, 9
sw t0, --12(fp)
L104:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -None
sw t0, -8(fp)
L105:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 20
jal 89
addi sp, sp, -20
L106:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, 20
lw t0, -20(sp)
sw t0, --12(fp)
L107:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -20
sw t0, -8(fp)
L108:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 20
jal 89
addi sp, sp, -20
L109:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L110:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L111:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L112:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L113:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L114:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L115:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -24
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -24
sw t0, 0(t0)
L116:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
lw t1, 0(t0)
add t0, t1, t0
sw t0, -28(sp)
L117:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
blt t0, t1, 121
L118:
#	<function Quad.toString at 0x7fbabff34c10>
j 141
L119:
#	<function Quad.toString at 0x7fbabff34c10>
L120:
#	<function Quad.toString at 0x7fbabff34c10>
j 141
L121:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
beq t0, t1, 123
L122:
#	<function Quad.toString at 0x7fbabff34c10>
j 125
L123:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L124:
#	<function Quad.toString at 0x7fbabff34c10>
j 130
L125:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 2
li t1, 2
beq t0, t1, 127
L126:
#	<function Quad.toString at 0x7fbabff34c10>
j 129
L127:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L128:
#	<function Quad.toString at 0x7fbabff34c10>
j 130
L129:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L130:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
blt t0, t1, 132
L131:
#	<function Quad.toString at 0x7fbabff34c10>
j 140
L132:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 2
li t1, 2
beq t0, t1, 134
L133:
#	<function Quad.toString at 0x7fbabff34c10>
j 139
L134:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
beq t0, t1, 136
L135:
#	<function Quad.toString at 0x7fbabff34c10>
j 138
L136:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L137:
#	<function Quad.toString at 0x7fbabff34c10>
j 134
L138:
#	<function Quad.toString at 0x7fbabff34c10>
j _
L139:
#	<function Quad.toString at 0x7fbabff34c10>
j 130
L140:
#	<function Quad.toString at 0x7fbabff34c10>
j 116
L141:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L142:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L143:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L144:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L145:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -24
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -24
sw t0, 0(t0)
L146:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)
L147:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L148:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L149:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L150:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, 20
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)
L151:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -20
sw t0, -8(fp)
L152:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 20
jal 142
addi sp, sp, -20
L153:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L154:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, 36
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)
L155:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, 36
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
sw t0, --12(fp)
L156:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -36
sw t0, -8(fp)
L157:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
sw t0, -4(fp)
addi sp, sp, 36
jal 148
addi sp, sp, -36
L158:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L159:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L160:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)
L161:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
L162:
#	<function Quad.toString at 0x7fbabff34c10>
sw ra, 0(sp)
L163:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)
L164:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L165:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)
L166:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
bgt t0, t1, 170
L167:
#	<function Quad.toString at 0x7fbabff34c10>
j 174
L168:
#	<function Quad.toString at 0x7fbabff34c10>
L169:
#	<function Quad.toString at 0x7fbabff34c10>
j 174
L170:
#	<function Quad.toString at 0x7fbabff34c10>
li t0, 1
li t1, 1
add t0, t1, t0
sw t0, -24(sp)
L171:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
add t0, t1, t0
sw t0, -28(sp)
L172:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -24(sp)
lw t1, -28(sp)
blt t0, t1, 174
L173:
#	<function Quad.toString at 0x7fbabff34c10>
j 179
L174:
#	<function Quad.toString at 0x7fbabff34c10>
addi fp, sp, 36
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
sw t0, --12(fp)
L175:
#	<function Quad.toString at 0x7fbabff34c10>
addi t0, sp, -36
sw t0, -8(fp)
L176:
#	<function Quad.toString at 0x7fbabff34c10>
sw sp, -4(fp)
addi sp, sp, 36
jal 148
addi sp, sp, -36
L177:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L178:
#	<function Quad.toString at 0x7fbabff34c10>
j 180
L179:
#	<function Quad.toString at 0x7fbabff34c10>
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)
L180:
#	<function Quad.toString at 0x7fbabff34c10>
lw ra, 0(sp)
jr ra
Lmain:
sw sp, -4(fp)
addi sp, sp, 32
jal 0
addi sp, sp, -32
sw sp, -4(fp)
addi sp, sp, 20
jal 29
addi sp, sp, -20
sw sp, -4(fp)
addi sp, sp, 28
jal 36
addi sp, sp, -28
sw sp, -4(fp)
addi sp, sp, 24
jal 74
addi sp, sp, -24
sw sp, -4(fp)
addi sp, sp, 28
jal 96
addi sp, sp, -28
li a0, 0
li a7, 93
ecall
