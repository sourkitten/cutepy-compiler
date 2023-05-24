.data
str_nl: .asciz "\n"
j Lmain

L0:
#0 begin_block main_factorial _ _
sw ra, 0(sp)

L1:
#1 in x _ _
li a7, 5
ecall
lw t0, -4(sp)
addi t0, t0, -12
sw a7, 0(t0)

L2:
#2 = fact _ 1
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L3:
#3 = i _ 1
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L4:
#4 <= i x 6
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
ble t0, t1, 6

L5:
#5 jump _ _ 11
j L11

L6:
#6 * fact i T%0
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
mul t0, t1, t0
sw t0, -24(sp)

L7:
#7 = fact _ T%0
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L8:
#8 + i 1 T%1
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
li t1, 1
add t0, t1, t0
sw t0, -28(sp)

L9:
#9 = i _ T%1
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L10:
#10 jump _ _ 4
j L4

L11:
#11 out fact _ _
lw t0, -4(sp)
addi t0, t0, -20
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall

L12:
#12 end_block main_factorial _ _
lw ra, 0(sp)
jr ra

L13:
#13 begin_block fibonacci _ _
sw ra, 0(sp)

L14:
#14 <= x 1 16
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 1
ble t0, t1, 16

L15:
#15 jump _ _ 18
j L18

L16:
#16 ret _ _ x
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)

L17:
#17 jump _ _ 28
j L28

L18:
#18 - x 1 T%2
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 1
sub t0, t1, t0
sw t0, -16(sp)

L19:
#19 par T%2 cv _
addi fp, sp, None
lw t0, -16(sp)
sw t0, --12(fp)

L20:
#20 par T%3 ret _
addi t0, sp, -None
sw t0, -8(fp)

L21:
#21 call fibonacci _ _
lw t0, -4(sp)
sw t0, -4(fp)
addi sp, sp, 36
jal L13
addi sp, sp, -36

L22:
#22 - x 2 T%4
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 2
sub t0, t1, t0
sw t0, -24(sp)

L23:
#23 par T%4 cv _
addi fp, sp, None
lw t0, -24(sp)
sw t0, --12(fp)

L24:
#24 par T%5 ret _
addi t0, sp, -None
sw t0, -8(fp)

L25:
#25 call fibonacci _ _
lw t0, -4(sp)
sw t0, -4(fp)
addi sp, sp, 36
jal L13
addi sp, sp, -36

L26:
#26 + T%3 T%5 T%6
lw t0, -20(sp)
lw t1, -28(sp)
add t0, t1, t0
sw t0, -32(sp)

L27:
#27 ret _ _ T%6
lw t1, -32(sp)
lw t0, -8(sp)
sw t1, 0(t0)

L28:
#28 end_block fibonacci _ _
lw ra, 0(sp)
jr ra

L29:
#29 begin_block main_fibonacci _ _
sw ra, 0(sp)

L30:
#30 in x _ _
li a7, 5
ecall
lw t0, -4(sp)
addi t0, t0, -12
sw a7, 0(t0)

L31:
#31 par x cv _
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)

L32:
#32 par T%7 ret _
addi t0, sp, -None
sw t0, -8(fp)

L33:
#33 call fibonacci _ _
sw sp, -4(fp)
addi sp, sp, 36
jal L13
addi sp, sp, -36

L34:
#34 out T%7 _ _
lw a0, -16(sp)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall

L35:
#35 end_block main_fibonacci _ _
lw ra, 0(sp)
jr ra

L36:
#36 begin_block main_countdigits _ _
sw ra, 0(sp)

L37:
#37 in x _ _
li a7, 5
ecall
lw t0, -4(sp)
addi t0, t0, -12
sw a7, 0(t0)

L38:
#38 = count _ 0
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L39:
#39 > x 0 41
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 0
bgt t0, t1, 41

L40:
#40 jump _ _ 46
j L46

L41:
#41 // x 10 T%8
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 10
div t0, t1, t0
sw t0, -20(sp)

L42:
#42 = x _ T%8
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L43:
#43 + count 1 T%9
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
li t1, 1
add t0, t1, t0
sw t0, -24(sp)

L44:
#44 = count _ T%9
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L45:
#45 jump _ _ 39
j L39

L46:
#46 out count _ _
lw t0, -4(sp)
addi t0, t0, -16
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall

L47:
#47 end_block main_countdigits _ _
lw ra, 0(sp)
jr ra

L48:
#48 begin_block divides _ _
sw ra, 0(sp)

L49:
#49 // y x T%10
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
div t0, t1, t0
sw t0, -20(sp)

L50:
#50 * T%10 x T%11
lw t0, -20(sp)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
mul t0, t1, t0
sw t0, -24(sp)

L51:
#51 == y T%11 53
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t1, -24(sp)
beq t0, t1, 53

L52:
#52 jump _ _ 55
j L55

L53:
#53 ret _ _ 1
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)

L54:
#54 jump _ _ 56
j L56

L55:
#55 ret _ _ 0
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)

L56:
#56 end_block divides _ _
lw ra, 0(sp)
jr ra

L57:
#57 begin_block isPrime _ _
sw ra, 0(sp)

L58:
#58 = i _ 2
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L59:
#59 < i x 61
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
blt t0, t1, 61

L60:
#60 jump _ _ 72
j L72

L61:
#61 par i cv _
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)

L62:
#62 par x cv _
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)

L63:
#63 par T%12 ret _
addi t0, sp, -None
sw t0, -8(fp)

L64:
#64 call divides _ _
sw sp, -4(fp)
addi sp, sp, 28
jal L48
addi sp, sp, -28

L65:
#65 == T%12 1 67
lw t0, -20(sp)
li t1, 1
beq t0, t1, 67

L66:
#66 jump _ _ 69
j L69

L67:
#67 ret _ _ 0
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)

L68:
#68 jump _ _ _
j L_

L69:
#69 + i 1 T%13
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 1
add t0, t1, t0
sw t0, -24(sp)

L70:
#70 = i _ T%13
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L71:
#71 jump _ _ 59
j L59

L72:
#72 ret _ _ 1
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)

L73:
#73 end_block isPrime _ _
lw ra, 0(sp)
jr ra

L74:
#74 begin_block main_primes _ _
sw ra, 0(sp)

L75:
#75 = i _ 2
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L76:
#76 <= i 30 78
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 30
ble t0, t1, 78

L77:
#77 jump _ _ 88
j L88

L78:
#78 par i cv _
addi fp, sp, None
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)

L79:
#79 par T%14 ret _
addi t0, sp, -None
sw t0, -8(fp)

L80:
#80 call isPrime _ _
sw sp, -4(fp)
addi sp, sp, 28
jal L57
addi sp, sp, -28

L81:
#81 == T%14 1 83
lw t0, -16(sp)
li t1, 1
beq t0, t1, 83

L82:
#82 jump _ _ 85
j L85

L83:
#83 out i _ _
lw t0, -4(sp)
addi t0, t0, -12
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall

L84:
#84 jump _ _ _
j L_

L85:
#85 + i 1 T%15
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 1
add t0, t1, t0
sw t0, -20(sp)

L86:
#86 = i _ T%15
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L87:
#87 jump _ _ 76
j L76

L88:
#88 end_block main_primes _ _
lw ra, 0(sp)
jr ra

L89:
#89 begin_block max _ _
sw ra, 0(sp)

L90:
#90 > a b 92
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
bgt t0, t1, 92

L91:
#91 jump _ _ 94
j L94

L92:
#92 ret _ _ a
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)

L93:
#93 jump _ _ 95
j L95

L94:
#94 ret _ _ b
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)

L95:
#95 end_block max _ _
lw ra, 0(sp)
jr ra

L96:
#96 begin_block main_test _ _
sw ra, 0(sp)

L97:
#97 par 5 cv _
addi fp, sp, None
li t0, 5
sw t0, --12(fp)

L98:
#98 par 7 cv _
addi fp, sp, None
li t0, 7
sw t0, --12(fp)

L99:
#99 par T%16 ret _
addi t0, sp, -None
sw t0, -8(fp)

L100:
#100 call max _ _
sw sp, -4(fp)
addi sp, sp, 20
jal L89
addi sp, sp, -20

L101:
#101 par T%16 cv max
addi fp, sp, 20
lw t0, -16(sp)
sw t0, --12(fp)

L102:
#102 par 8 cv _
addi fp, sp, None
li t0, 8
sw t0, --12(fp)

L103:
#103 par 9 cv _
addi fp, sp, None
li t0, 9
sw t0, --12(fp)

L104:
#104 par T%17 ret _
addi t0, sp, -None
sw t0, -8(fp)

L105:
#105 call max _ _
sw sp, -4(fp)
addi sp, sp, 20
jal L89
addi sp, sp, -20

L106:
#106 par T%17 cv max
addi fp, sp, 20
lw t0, -20(sp)
sw t0, --12(fp)

L107:
#107 par T%18 ret max
addi t0, sp, -20
sw t0, -8(fp)

L108:
#108 call max _ _
sw sp, -4(fp)
addi sp, sp, 20
jal L89
addi sp, sp, -20

L109:
#109 = x _ T%18
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L110:
#110 out x _ _
lw t0, -4(sp)
addi t0, t0, -12
lw a0, 0(t0)
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall

L111:
#111 end_block main_test _ _
lw ra, 0(sp)
jr ra

L112:
#112 begin_block main_ifWhile _ _
sw ra, 0(sp)

L113:
#113 = a _ 1
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L114:
#114 = b _ 0
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L115:
#115 = t _ 0
lw t0, -4(sp)
addi t0, t0, -24
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -24
sw t0, 0(t0)

L116:
#116 + a b T%19
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
lw t1, 0(t0)
add t0, t1, t0
sw t0, -28(sp)

L117:
#117 < T%19 1 121
lw t0, -28(sp)
li t1, 1
blt t0, t1, 121

L118:
#118 jump _ _ 141
j L141

L119:
#119 5 < ] 121

L120:
#120 jump _ _ 141
j L141

L121:
#121 == t 1 123
lw t0, -4(sp)
addi t0, t0, -24
lw t0, 0(t0)
li t1, 1
beq t0, t1, 123

L122:
#122 jump _ _ 125
j L125

L123:
#123 = c _ 2
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L124:
#124 jump _ _ 130
j L130

L125:
#125 == t 2 127
lw t0, -4(sp)
addi t0, t0, -24
lw t0, 0(t0)
li t1, 2
beq t0, t1, 127

L126:
#126 jump _ _ 129
j L129

L127:
#127 = c _ 4
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L128:
#128 jump _ _ 130
j L130

L129:
#129 = c _ 0
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L130:
#130 < a 1 132
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
li t1, 1
blt t0, t1, 132

L131:
#131 jump _ _ 140
j L140

L132:
#132 == a 2 134
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
li t1, 2
beq t0, t1, 134

L133:
#133 jump _ _ 139
j L139

L134:
#134 == b 1 136
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
li t1, 1
beq t0, t1, 136

L135:
#135 jump _ _ 138
j L138

L136:
#136 = c _ 2
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L137:
#137 jump _ _ 134
j L134

L138:
#138 jump _ _ _
j L_

L139:
#139 jump _ _ 130
j L130

L140:
#140 jump _ _ 116
j L116

L141:
#141 end_block main_ifWhile _ _
lw ra, 0(sp)
jr ra

L142:
#142 begin_block P11 _ _
sw ra, 0(sp)

L143:
#143 = e _ 1
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L144:
#144 = X _ Y
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L145:
#145 = f _ b
lw t0, -4(sp)
addi t0, t0, -24
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -24
sw t0, 0(t0)

L146:
#146 ret _ _ e
lw t0, -4(sp)
addi t0, t0, -16
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)

L147:
#147 end_block P11 _ _
lw ra, 0(sp)
jr ra

L148:
#148 begin_block P1 _ _
sw ra, 0(sp)

L149:
#149 = b _ X
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L150:
#150 par X cv P11
addi fp, sp, 20
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)

L151:
#151 par T%20 ret P11
addi t0, sp, -20
sw t0, -8(fp)

L152:
#152 call P11 _ _
sw sp, -4(fp)
addi sp, sp, 20
jal L142
addi sp, sp, -20

L153:
#153 = e _ T%20
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L154:
#154 par X cv P1
addi fp, sp, 36
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
sw t0, --12(fp)

L155:
#155 par Y cv P1
addi fp, sp, 36
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
sw t0, --12(fp)

L156:
#156 par T%21 ret P1
addi t0, sp, -36
sw t0, -8(fp)

L157:
#157 call P1 _ _
lw t0, -4(sp)
sw t0, -4(fp)
addi sp, sp, 36
jal L148
addi sp, sp, -36

L158:
#158 = e _ T%21
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L159:
#159 = X _ b
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L160:
#160 ret _ _ e
lw t0, -4(sp)
addi t0, t0, -20
lw t1, 0(t0)
lw t0, -8(sp)
sw t1, 0(t0)

L161:
#161 end_block P1 _ _
lw ra, 0(sp)
jr ra

L162:
#162 begin_block main_small _ _
sw ra, 0(sp)

L163:
#163 = b _ 0
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
sw t0, 0(t0)

L164:
#164 = f _ 0
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L165:
#165 = g _ 0
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -16
sw t0, 0(t0)

L166:
#166 > b 1 170
lw t0, -4(sp)
addi t0, t0, -12
lw t0, 0(t0)
li t1, 1
bgt t0, t1, 170

L167:
#167 jump _ _ 174
j L174

L168:
#168 2 < or 174

L169:
#169 jump _ _ 174
j L174

L170:
#170 + g 1 T%22
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
li t1, 1
add t0, t1, t0
sw t0, -24(sp)

L171:
#171 + f b T%23
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -12
lw t1, 0(t0)
add t0, t1, t0
sw t0, -28(sp)

L172:
#172 < T%22 T%23 174
lw t0, -24(sp)
lw t1, -28(sp)
blt t0, t1, 174

L173:
#173 jump _ _ 179
j L179

L174:
#174 par g cv P1
addi fp, sp, 36
lw t0, -4(sp)
addi t0, t0, -16
lw t0, 0(t0)
sw t0, --12(fp)

L175:
#175 par T%24 ret P1
addi t0, sp, -36
sw t0, -8(fp)

L176:
#176 call P1 _ _
sw sp, -4(fp)
addi sp, sp, 36
jal L148
addi sp, sp, -36

L177:
#177 = f _ T%24
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L178:
#178 jump _ _ 180
j L180

L179:
#179 = f _ 1
lw t0, -4(sp)
addi t0, t0, -20
lw t0, 0(t0)
lw t0, -4(sp)
addi t0, t0, -20
sw t0, 0(t0)

L180:
#180 end_block main_small _ _
lw ra, 0(sp)
jr ra

Lmain:
sw sp, -4(fp)
addi sp, sp, 32
jal L0
addi sp, sp, -32
sw sp, -4(fp)
addi sp, sp, 20
jal L29
addi sp, sp, -20
sw sp, -4(fp)
addi sp, sp, 28
jal L36
addi sp, sp, -28
sw sp, -4(fp)
addi sp, sp, 24
jal L74
addi sp, sp, -24
sw sp, -4(fp)
addi sp, sp, 28
jal L96
addi sp, sp, -28
li a0, 0
li a7, 93
ecall
