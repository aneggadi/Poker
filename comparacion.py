import poker2
import puntuacion
import color

valorcartas=0
def escaleracolor():
    global valorcartas
    if color.trebor==5 or color.picas==5 or color.corazones==5 or color.diamantes==5:
        #Color, Escalera de color y Escalera real
        if puntuacion.dos==1:
            if puntuacion.tres==1:
                if puntuacion.cuatro==1:
                    if puntuacion.cinco==1:
                        if puntuacion.seis==1:
                            valorcartas=326
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.tres==1:
            if puntuacion.cuatro==1:
                if puntuacion.cinco==1:
                    if puntuacion.seis==1:
                        if puntuacion.siete==1:
                            valorcartas=327
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.cuatro==1:
            if puntuacion.cinco==1:
                if puntuacion.seis==1:
                    if puntuacion.siete==1:
                        if puntuacion.ocho==1:
                            valorcartas=328
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.cinco==1:
            if puntuacion.seis==1:
                if puntuacion.siete==1:
                    if puntuacion.ocho==1:
                        if puntuacion.nueve==1:
                            valorcartas=329
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.seis==1:
            if puntuacion.siete==1:
                if puntuacion.ocho==1:
                    if puntuacion.nueve==1:
                        if puntuacion.diez==1:
                            valorcartas=330
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.siete==1:
            if puntuacion.ocho==1:
                if puntuacion.nueve==1:
                    if puntuacion.diez==1:
                        if puntuacion.jota==1:
                            valorcartas=331
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.ocho==1:
            if puntuacion.nueve==1:
                if puntuacion.diez==1:
                    if puntuacion.jota==1:
                        if puntuacion.reina==1:
                            valorcartas=332
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        elif puntuacion.nueve==1:
            if puntuacion.diez==1:
                if puntuacion.jota==1:
                    if puntuacion.reina==1:
                        if puntuacion.rey==1:
                            valorcartas=333
                        else:
                            valorcartas=156
                    else:
                        valorcartas=156
                else:
                    valorcartas=156
            else:
                valorcartas=156
        else:
            valorcartas=334
    else:
        #Carta Alta
        if puntuacion.ass==1:
            valorcartas=42
        elif puntuacion.rey:
            valorcartas=41
        elif puntuacion.reina:
            valorcartas=40
        elif puntuacion.jota:
            valorcartas=39
        elif puntuacion.diez:
            valorcartas=38
        elif puntuacion.nueve:
            valorcartas=37
        elif puntuacion.ocho:
            valorcartas=36
        elif puntuacion.siete:
            valorcartas=35
        elif puntuacion.seis:
            valorcartas=34
        elif puntuacion.cinco:
            valorcartas=33
        elif puntuacion.cuatro:
            valorcartas=32
        elif puntuacion.tres:
            valorcartas=31
        elif puntuacion.dos:
            valorcartas=30
        #Doble pareja y Pareja
        if puntuacion.ass==2:
            if puntuacion.rey==2:
                valorcartas=133
            elif puntuacion.reina==2:
                valorcartas=132
            elif puntuacion.jota==2:
                valorcartas=131
            elif puntuacion.diez==2:
                valorcartas=130
            elif puntuacion.nueve==2:
                valorcartas=129
            elif puntuacion.ocho==2:
                valorcartas=128
            elif puntuacion.siete==2:
                valorcartas=127
            elif puntuacion.seis==2:
                valorcartas=126
            elif puntuacion.cinco==2:
                valorcartas=125
            elif puntuacion.cuatro==2:
                valorcartas=124
            elif puntuacion.tres==2:
                valorcartas=123
            elif puntuacion.dos==2:
                valorcartas=122
            else:
                valorcartas=55
        elif puntuacion.rey==2:
            if puntuacion.reina==2:
                valorcartas=121
            elif puntuacion.jota==2:
                valorcartas=120
            elif puntuacion.diez==2:
                valorcartas=119
            elif puntuacion.nueve==2:
                valorcartas=118
            elif puntuacion.ocho==2:
                valorcartas=117
            elif puntuacion.siete==2:
                valorcartas=116
            elif puntuacion.seis==2:
                valorcartas=115
            elif puntuacion.cinco==2:
                valorcartas=114
            elif puntuacion.cuatro==2:
                valorcartas=113
            elif puntuacion.tres==2:
                valorcartas=112
            elif puntuacion.dos==2:
                valorcartas=111
            else:
                valorcartas=54
        elif puntuacion.reina==2:
            if puntuacion.jota==2:
                    valorcartas=110
            elif puntuacion.diez==2:
                    valorcartas=109
            elif puntuacion.nueve==2:
                    valorcartas=108
            elif puntuacion.ocho==2:
                    valorcartas=107
            elif puntuacion.siete==2:
                    valorcartas=106
            elif puntuacion.seis==2:
                    valorcartas=105
            elif puntuacion.cinco==2:
                    valorcartas=104
            elif puntuacion.cuatro==2:
                    valorcartas=103
            elif puntuacion.tres==2:
                    valorcartas=102
            elif puntuacion.dos==2:
                    valorcartas=101
            else:
                valorcartas=53
        elif puntuacion.jota==2:
            if puntuacion.diez==2:
                valorcartas=100
            elif puntuacion.nueve==2:
                valorcartas=99
            elif puntuacion.ocho==2:
                valorcartas=98
            elif puntuacion.siete==2:
                valorcartas=97
            elif puntuacion.seis==2:
                valorcartas=96
            elif puntuacion.cinco==2:
                valorcartas=95
            elif puntuacion.cuatro==2:
                valorcartas=94
            elif puntuacion.tres==2:
                valorcartas=93
            elif puntuacion.dos==2:
                valorcartas=92
            else:
                valorcartas=52
        elif puntuacion.diez==2:
            if puntuacion.nueve==2:
                valorcartas=91
            elif puntuacion.ocho==2:
                valorcartas=90
            elif puntuacion.siete==2:
                valorcartas=89
            elif puntuacion.seis==2:
                valorcartas=88
            elif puntuacion.cinco==2:
                valorcartas=87
            elif puntuacion.cuatro==2:
                valorcartas=86
            elif puntuacion.tres==2:
                valorcartas=85
            elif puntuacion.dos==2:
                valorcartas=84
            else:
                valorcartas=51
        elif puntuacion.nueve==2:
            if puntuacion.ocho==2:
                valorcartas=83
            elif puntuacion.siete==2:
                valorcartas=82
            elif puntuacion.seis==2:
                valorcartas=81
            elif puntuacion.cinco==2:
                valorcartas=80
            elif puntuacion.cuatro==2:
                valorcartas=79
            elif puntuacion.tres==2:
                valorcartas=78
            elif puntuacion.dos==2:
                valorcartas=77
            else:
                valorcartas=50
        elif puntuacion.ocho==2:
            if puntuacion.siete==2:
                valorcartas=76
            elif puntuacion.seis==2:
                valorcartas=75
            elif puntuacion.cinco==2:
                valorcartas=74
            elif puntuacion.cuatro==2:
                valorcartas=73
            elif puntuacion.tres==2:
                valorcartas=72
            elif puntuacion.dos==2:
                valorcartas=71
            else:
                valorcartas=49
        elif puntuacion.siete==2:
            if puntuacion.seis==2:
                valorcartas=70
            elif puntuacion.cinco==2:
                valorcartas=69
            elif puntuacion.cuatro==2:
                valorcartas=68
            elif puntuacion.tres==2:
                valorcartas=67
            elif puntuacion.dos==2:
                valorcartas=66
            else:
                valorcartas=48
        elif puntuacion.seis==2:
            if puntuacion.cinco==2:
                valorcartas=65
            elif puntuacion.cuatro==2:
                valorcartas=64
            elif puntuacion.tres==2:
                valorcartas=63
            elif puntuacion.dos==2:
                valorcartas=62
            else:
                valorcartas=47
        elif puntuacion.cinco==2:
            if puntuacion.cuatro==2:
                valorcartas=61
            elif puntuacion.tres==2:
                valorcartas=60
            elif puntuacion.dos==2:
                valorcartas=59
            else:
                valorcartas=46
        elif puntuacion.cuatro==2:
            if puntuacion.tres==2:
                valorcartas=58
            elif puntuacion.dos==2:
                valorcartas=57
            else:
                valorcartas=45 
        elif puntuacion.tres==2:
            if puntuacion.dos==2:
                valorcartas=56
            else:
                valorcartas=44
        elif puntuacion.dos==2:
            valorcartas=43    
        #Escalera
        if puntuacion.dos==1:
                if puntuacion.tres==1:
                    if puntuacion.cuatro==1:
                        if puntuacion.cinco==1:
                            if puntuacion.seis==1:
                                valorcartas=147
        elif puntuacion.tres==1:
                if puntuacion.cuatro==1:
                    if puntuacion.cinco==1:
                        if puntuacion.seis==1:
                            if puntuacion.siete==1:
                                valorcartas=148
        elif puntuacion.cuatro==1:
                if puntuacion.cinco==1:
                    if puntuacion.seis==1:
                        if puntuacion.siete==1:
                            if puntuacion.ocho==1:
                                valorcartas=149
        elif puntuacion.cinco==1:
                if puntuacion.seis==1:
                    if puntuacion.siete==1:
                        if puntuacion.ocho==1:
                            if puntuacion.nueve==1:
                                valorcartas=150
        elif puntuacion.seis==1:
                if puntuacion.siete==1:
                    if puntuacion.ocho==1:
                        if puntuacion.nueve==1:
                            if puntuacion.diez==1:
                                valorcartas==151
        elif puntuacion.siete==1:
                if puntuacion.ocho==1:
                    if puntuacion.nueve==1:
                        if puntuacion.diez==1:
                            if puntuacion.jota==1:
                                valorcartas=152
        elif puntuacion.ocho==1:
                if puntuacion.nueve==1:
                    if puntuacion.diez==1:
                        if puntuacion.jota==1:
                            if puntuacion.reina==1:
                                valorcartas=153
        elif puntuacion.nueve==1:
                if puntuacion.diez==1:
                    if puntuacion.jota==1:
                        if puntuacion.reina==1:
                            if puntuacion.rey==1:
                                valorcartas=154
        elif puntuacion.diez==1:
                if puntuacion.jota==1:
                    if puntuacion.reina==1:
                        if puntuacion.rey==1:
                            if puntuacion.ass==1:
                                valorcartas=155
        #Full house y Trio
        if puntuacion.ass==3:
            if puntuacion.rey==2:
                valorcartas=312
            elif puntuacion.reina==2:
                valorcartas=311
            elif puntuacion.jota==2:
                valorcartas=310
            elif puntuacion.diez==2:
                valorcartas=309
            elif puntuacion.nueve==2:
                valorcartas=308
            elif puntuacion.ocho==2:
                valorcartas=307
            elif puntuacion.siete==2:
                valorcartas=306
            elif puntuacion.seis==2:
                valorcartas=305
            elif puntuacion.cinco==2:
                valorcartas=304
            elif puntuacion.cuatro==2:
                valorcartas=303
            elif puntuacion.tres==2:
                valorcartas=302
            elif puntuacion.dos==2:
                valorcartas=301
            else:
                valorcartas=146
        elif puntuacion.rey==3:
            if puntuacion.ass==2:
                valorcartas=300
            elif puntuacion.reina==2:
                valorcartas=299
            elif puntuacion.jota==2:
                valorcartas=298
            elif puntuacion.diez==2:
                valorcartas=298
            elif puntuacion.nueve==2:
                valorcartas=297
            elif puntuacion.ocho==2:
                valorcartas=295
            elif puntuacion.siete==2:
                valorcartas=294
            elif puntuacion.seis==2:
                valorcartas=293
            elif puntuacion.cinco==2:
                valorcartas=292
            elif puntuacion.cuatro==2:
                valorcartas=291
            elif puntuacion.tres==2:
                valorcartas=290
            elif puntuacion.dos==2:
                valorcartas=289
            else:
                valorcartas=145
        elif puntuacion.reina==3:
            if puntuacion.ass==2:
                    valorcartas=288
            elif puntuacion.rey==2:
                    valorcartas=287
            elif puntuacion.jota==2:
                    valorcartas=286
            elif puntuacion.diez==2:
                    valorcartas=285
            elif puntuacion.nueve==2:
                    valorcartas=284
            elif puntuacion.ocho==2:
                    valorcartas=283
            elif puntuacion.siete==2:
                    valorcartas=282
            elif puntuacion.seis==2:
                    valorcartas=281
            elif puntuacion.cinco==2:
                    valorcartas=280
            elif puntuacion.cuatro==2:
                    valorcartas=279
            elif puntuacion.tres==2:
                    valorcartas=278
            elif puntuacion.dos==2:
                    valorcartas=277
            else:
                valorcartas=144
        elif puntuacion.jota==3:
            if puntuacion.ass==2:
                valorcartas=276
            elif puntuacion.rey==2:
                valorcartas=275
            elif puntuacion.reina==2:
                valorcartas=274
            elif puntuacion.diez==2:
                valorcartas=273
            elif puntuacion.nueve==2:
                valorcartas=272
            elif puntuacion.ocho==2:
                valorcartas=271
            elif puntuacion.siete==2:
                valorcartas=270
            elif puntuacion.seis==2:
                valorcartas=269
            elif puntuacion.cinco==2:
                valorcartas=268
            elif puntuacion.cuatro==2:
                valorcartas=267
            elif puntuacion.tres==2:
                valorcartas=266
            elif puntuacion.dos==2:
                valorcartas=265
            else:
                valorcartas=143
        elif puntuacion.diez==3:
            if puntuacion.ass==2:
                valorcartas=264
            elif puntuacion.rey==2:
                valorcartas=263
            elif puntuacion.reina==2:
                valorcartas=262
            elif puntuacion.jota==2:
                valorcartas=261
            elif puntuacion.nueve==2:
                valorcartas=260
            elif puntuacion.ocho==2:
                valorcartas=259
            elif puntuacion.siete==2:
                valorcartas=258
            elif puntuacion.seis==2:
                valorcartas=257
            elif puntuacion.cinco==2:
                valorcartas=256
            elif puntuacion.cuatro==2:
                valorcartas=255
            elif puntuacion.tres==2:
                valorcartas=254
            elif puntuacion.dos==2:
                valorcartas=253
            else:
                valorcartas=142
        elif puntuacion.nueve==3:
            if puntuacion.ass==2:
                valorcartas=252
            elif puntuacion.rey==2:
                valorcartas=251
            elif puntuacion.reina==2:
                valorcartas=250
            elif puntuacion.jota==2:
                valorcartas=249
            elif puntuacion.diez==2:
                valorcartas=248
            elif puntuacion.ocho==2:
                valorcartas=247
            elif puntuacion.siete==2:
                valorcartas=246
            elif puntuacion.seis==2:
                valorcartas=245
            elif puntuacion.cinco==2:
                valorcartas=244
            elif puntuacion.cuatro==2:
                valorcartas=243
            elif puntuacion.tres==2:
                valorcartas=242
            elif puntuacion.dos==2:
                valorcartas=241
            else:
                valorcartas=141
        elif puntuacion.ocho==3:
            if puntuacion.ass==2:
                valorcartas=240
            elif puntuacion.rey==2:
                valorcartas=239
            elif puntuacion.reina==2:
                valorcartas=238
            elif puntuacion.jota==2:
                valorcartas=237
            elif puntuacion.diez==2:
                valorcartas=236
            elif puntuacion.nueve==2:
                valorcartas=235
            elif puntuacion.siete==2:
                valorcartas=234
            elif puntuacion.seis==2:
                valorcartas=233
            elif puntuacion.cinco==2:
                valorcartas=232
            elif puntuacion.cuatro==2:
                valorcartas=231
            elif puntuacion.tres==2:
                valorcartas=230
            elif puntuacion.dos==2:
                valorcartas=229
            else:
                valorcartas=140
        elif puntuacion.siete==3:
            if puntuacion.ass==2:
                valorcartas=228
            elif puntuacion.rey==2:
                valorcartas=227
            elif puntuacion.reina==2:
                valorcartas=226
            elif puntuacion.jota==2:
                valorcartas=225
            elif puntuacion.diez==2:
                valorcartas=224
            elif puntuacion.nueve==2:
                valorcartas=223
            elif puntuacion.ocho==2:
                valorcartas=222
            elif puntuacion.seis==2:
                valorcartas=221
            elif puntuacion.cinco==2:
                valorcartas=220
            elif puntuacion.cuatro==2:
                valorcartas=219
            elif puntuacion.tres==2:
                valorcartas=218
            elif puntuacion.dos==2:
                valorcartas=217
            else:
                valorcartas=139
        elif puntuacion.seis==3:
            if puntuacion.ass==2:
                valorcartas=216
            elif puntuacion.rey==2:
                valorcartas=215
            elif puntuacion.reina==2:
                valorcartas=214
            elif puntuacion.jota==2:
                valorcartas=213
            elif puntuacion.diez==2:
                valorcartas=212
            elif puntuacion.nueve==2:
                valorcartas=211
            elif puntuacion.ocho==2:
                valorcartas=210
            elif puntuacion.siete==2:
                valorcartas=209
            elif puntuacion.cinco==2:
                valorcartas=208
            elif puntuacion.cuatro==2:
                valorcartas=207
            elif puntuacion.tres==2:
                valorcartas=206
            elif puntuacion.dos==2:
                valorcartas=205
            else:
                valorcartas=138
        elif puntuacion.cinco==3:
            if puntuacion.ass==2:
                valorcartas=204
            elif puntuacion.rey==2:
                valorcartas=203
            elif puntuacion.reina==2:
                valorcartas=202
            elif puntuacion.jota==2:
                valorcartas=201
            elif puntuacion.diez==2:
                valorcartas=200
            elif puntuacion.nueve==2:
                valorcartas=199
            elif puntuacion.ocho==2:
                valorcartas=198
            elif puntuacion.siete==2:
                valorcartas=197
            elif puntuacion.seis==2:
                valorcartas=196
            elif puntuacion.cuatro==2:
                valorcartas=195
            elif puntuacion.tres==2:
                valorcartas=194
            elif puntuacion.dos==2:
                valorcartas=193
            else:
                valorcartas=137
        elif puntuacion.cuatro==3:
            if puntuacion.ass==2:
                valorcartas=192
            elif puntuacion.rey==2:
                valorcartas=191
            elif puntuacion.reina==2:
                valorcartas=190
            elif puntuacion.jota==2:
                valorcartas=189
            elif puntuacion.diez==2:
                valorcartas=188
            elif puntuacion.nueve==2:
                valorcartas=187
            elif puntuacion.ocho==2:
                valorcartas=186
            elif puntuacion.siete==2:
                valorcartas=185
            elif puntuacion.seis==2:
                valorcartas=184
            elif puntuacion.cinco==2:
                valorcartas=183
            elif puntuacion.tres==2:
                valorcartas=182
            elif puntuacion.dos==2:
                valorcartas=181
            else:
                valorcartas=136
        elif puntuacion.tres==3:
            if puntuacion.ass==2:
                valorcartas=180
            elif puntuacion.rey==2:
                valorcartas=179
            elif puntuacion.reina==2:
                valorcartas=178
            elif puntuacion.jota==2:
                valorcartas=177
            elif puntuacion.diez==2:
                valorcartas=176
            elif puntuacion.nueve==2:
                valorcartas=175
            elif puntuacion.ocho==2:
                valorcartas=174
            elif puntuacion.siete==2:
                valorcartas=173
            elif puntuacion.seis==2:
                valorcartas=172
            elif puntuacion.cinco==2:
                valorcartas=171
            elif puntuacion.cuatro==2:
                valorcartas=170
            elif puntuacion.dos==2:
                valorcartas=169
            else:
                valorcartas=135
        elif puntuacion.dos==3:
            if puntuacion.ass==2:
                valorcartas=168
            elif puntuacion.rey==2:
                valorcartas=167
            elif puntuacion.reina==2:
                valorcartas=166
            elif puntuacion.jota==2:
                valorcartas=165
            elif puntuacion.diez==2:
                valorcartas=164
            elif puntuacion.nueve==2:
                valorcartas=163
            elif puntuacion.ocho==2:
                valorcartas=162
            elif puntuacion.siete==2:
                valorcartas=161
            elif puntuacion.seis==2:
                valorcartas=160
            elif puntuacion.cinco==2:
                valorcartas=159
            elif puntuacion.cuatro==2:
                valorcartas=158
            elif puntuacion.tres==2:
                valorcartas=157
            else:
                valorcartas=134
        #Poker
        if puntuacion.ass==4:
                valorcartas=325
        elif puntuacion.rey==4:
                valorcartas=324
        elif puntuacion.reina==4:
                valorcartas=323
        elif puntuacion.jota==4:
                valorcartas=322
        elif puntuacion.diez==4:
                valorcartas=321
        elif puntuacion.nueve==4:
                valorcartas=320
        elif puntuacion.ocho==4:
                valorcartas=319
        elif puntuacion.siete==4:
                valorcartas=318
        elif puntuacion.seis==4:
                valorcartas=317
        elif puntuacion.cinco==4:
                valorcartas=316
        elif puntuacion.cuatro==4:
                valorcartas=315
        elif puntuacion.tres==4:
                valorcartas=314
        elif puntuacion.dos==4:
                valorcartas=313