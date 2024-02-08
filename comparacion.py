import poker2
import puntuacion
import color

valorcartasjugador=0
def escaleracolor():
    global valorcartasjugador
    if color.treborjugador==5 or color.picasjugador==5 or color.corazonesjugador==5 or color.diamantesjugador==5:
        if puntuacion.dos==1:
            if puntuacion.tres==1:
                if puntuacion.cuatro==1:
                    if puntuacion.cinco==1:
                        if puntuacion.seis==1:
                            valorcartasjugador=1
                        else:
                            valorcartasjugador==326
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.tres==1:
            if puntuacion.cuatro==1:
                if puntuacion.cinco==1:
                    if puntuacion.seis==1:
                        if puntuacion.siete==1:
                            valorcartasjugador=327
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.cuatro==1:
            if puntuacion.cinco==1:
                if puntuacion.seis==1:
                    if puntuacion.siete==1:
                        if puntuacion.ocho==1:
                            valorcartasjugador=327
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.cinco==1:
            if puntuacion.seis==1:
                if puntuacion.siete==1:
                    if puntuacion.ocho==1:
                        if puntuacion.nueve==1:
                            valorcartasjugador=328
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.seis==1:
            if puntuacion.siete==1:
                if puntuacion.ocho==1:
                    if puntuacion.nueve==1:
                        if puntuacion.diez==1:
                            valorcartasjugador==329
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.siete==1:
            if puntuacion.ocho==1:
                if puntuacion.nueve==1:
                    if puntuacion.diez==1:
                        if puntuacion.jota==1:
                            valorcartasjugador=330
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.ocho==1:
            if puntuacion.nueve==1:
                if puntuacion.diez==1:
                    if puntuacion.jota==1:
                        if puntuacion.reina==1:
                            valorcartasjugador=331
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        elif puntuacion.nueve==1:
            if puntuacion.diez==1:
                if puntuacion.jota==1:
                    if puntuacion.reina==1:
                        if puntuacion.rey==1:
                            valorcartasjugador=332
                        else:
                            valorcartasjugador==100
                    else:
                        valorcartasjugador
                else:
                    valorcartasjugador==100
            else:
                valorcartasjugador=100
        else:
            valorcartasjugador=333
    #poker
    if puntuacion.ass==4:
            valorcartasjugador=325
    elif puntuacion.rey==4:
            valorcartasjugador=324
    elif puntuacion.reina==4:
            valorcartasjugador=323
    elif puntuacion.jota==4:
            valorcartasjugador=322
    elif puntuacion.diez==4:
            valorcartasjugador=321
    elif puntuacion.nueve==4:
            valorcartasjugador=320
    elif puntuacion.ocho==4:
            valorcartasjugador=319
    elif puntuacion.siete==4:
            valorcartasjugador=318
    elif puntuacion.seis==4:
            valorcartasjugador=317
    elif puntuacion.cinco==4:
            valorcartasjugador=316
    elif puntuacion.cuatro==4:
            valorcartasjugador=315
    elif puntuacion.tres==4:
            valorcartasjugador=314
    elif puntuacion.dos==4:
            valorcartasjugador=313
    #full house
    if puntuacion.ass==3:
        if puntuacion.rey==2:
            valorcartasjugador=312
        elif puntuacion.reina==2:
            valorcartasjugador=311
        elif puntuacion.jota==2:
            valorcartasjugador=310
        elif puntuacion.diez==2:
            valorcartasjugador=309
        elif puntuacion.nueve==2:
            valorcartasjugador=308
        elif puntuacion.ocho==2:
            valorcartasjugador=307
        elif puntuacion.siete==2:
            valorcartasjugador=306
        elif puntuacion.seis==2:
            valorcartasjugador=305
        elif puntuacion.cinco==2:
            valorcartasjugador=304
        elif puntuacion.cuatro==2:
            valorcartasjugador=303
        elif puntuacion.tres==2:
            valorcartasjugador=302
        elif puntuacion.dos==2:
            valorcartasjugador=301
    elif puntuacion.rey==3:
        if puntuacion.ass==2:
            valorcartasjugador=300
        elif puntuacion.reina==2:
            valorcartasjugador=299
        elif puntuacion.jota==2:
            valorcartasjugador=298
        elif puntuacion.diez==2:
            valorcartasjugador=298
        elif puntuacion.nueve==2:
            valorcartasjugador=297
        elif puntuacion.ocho==2:
            valorcartasjugador=295
        elif puntuacion.siete==2:
            valorcartasjugador=294
        elif puntuacion.seis==2:
            valorcartasjugador=293
        elif puntuacion.cinco==2:
            valorcartasjugador=292
        elif puntuacion.cuatro==2:
            valorcartasjugador=291
        elif puntuacion.tres==2:
            valorcartasjugador=290
        elif puntuacion.dos==2:
            valorcartasjugador=289
    elif puntuacion.reina==3:
        if puntuacion.ass==2:
                valorcartasjugador=288
        elif puntuacion.rey==2:
                valorcartasjugador=287
        elif puntuacion.jota==2:
                valorcartasjugador=286
        elif puntuacion.diez==2:
                valorcartasjugador=285
        elif puntuacion.nueve==2:
                valorcartasjugador=284
        elif puntuacion.ocho==2:
                valorcartasjugador=283
        elif puntuacion.siete==2:
                valorcartasjugador=282
        elif puntuacion.seis==2:
                valorcartasjugador=281
        elif puntuacion.cinco==2:
                valorcartasjugador=280
        elif puntuacion.cuatro==2:
                valorcartasjugador=279
        elif puntuacion.tres==2:
                valorcartasjugador=278
        elif puntuacion.dos==2:
                valorcartasjugador=277
    elif puntuacion.jota==3:
        if puntuacion.ass==2:
            valorcartasjugador=276
        elif puntuacion.rey==2:
            valorcartasjugador=275
        elif puntuacion.reina==2:
            valorcartasjugador=274
        elif puntuacion.diez==2:
            valorcartasjugador=273
        elif puntuacion.nueve==2:
            valorcartasjugador=272
        elif puntuacion.ocho==2:
            valorcartasjugador=271
        elif puntuacion.siete==2:
            valorcartasjugador=270
        elif puntuacion.seis==2:
            valorcartasjugador=269
        elif puntuacion.cinco==2:
            valorcartasjugador=268
        elif puntuacion.cuatro==2:
            valorcartasjugador=267
        elif puntuacion.tres==2:
            valorcartasjugador=266
        elif puntuacion.dos==2:
            valorcartasjugador=265
    elif puntuacion.diez==3:
        if puntuacion.ass==2:
            valorcartasjugador=264
        elif puntuacion.rey==2:
            valorcartasjugador=263
        elif puntuacion.reina==2:
            valorcartasjugador=262
        elif puntuacion.jota==2:
            valorcartasjugador=261
        elif puntuacion.nueve==2:
            valorcartasjugador=260
        elif puntuacion.ocho==2:
            valorcartasjugador=259
        elif puntuacion.siete==2:
            valorcartasjugador=258
        elif puntuacion.seis==2:
            valorcartasjugador=257
        elif puntuacion.cinco==2:
            valorcartasjugador=256
        elif puntuacion.cuatro==2:
            valorcartasjugador=255
        elif puntuacion.tres==2:
            valorcartasjugador=254
        elif puntuacion.dos==2:
             valorcartasjugador=253
    elif puntuacion.nueve==3:
        if puntuacion.ass==2:
            valorcartasjugador=252
        elif puntuacion.rey==2:
            valorcartasjugador=251
        elif puntuacion.reina==2:
            valorcartasjugador=250
        elif puntuacion.jota==2:
            valorcartasjugador=249
        elif puntuacion.diez==2:
            valorcartasjugador=248
        elif puntuacion.ocho==2:
            valorcartasjugador=247
        elif puntuacion.siete==2:
            valorcartasjugador=246
        elif puntuacion.seis==2:
            valorcartasjugador=245
        elif puntuacion.cinco==2:
            valorcartasjugador=244
        elif puntuacion.cuatro==2:
            valorcartasjugador=243
        elif puntuacion.tres==2:
            valorcartasjugador=242
        elif puntuacion.dos==2:
             valorcartasjugador=241
    elif puntuacion.ocho==3:
        if puntuacion.ass==2:
            valorcartasjugador=240
        elif puntuacion.rey==2:
            valorcartasjugador=239
        elif puntuacion.reina==2:
            valorcartasjugador=238
        elif puntuacion.jota==2:
            valorcartasjugador=237
        elif puntuacion.diez==2:
            valorcartasjugador=236
        elif puntuacion.nueve==2:
            valorcartasjugador=235
        elif puntuacion.siete==2:
            valorcartasjugador=234
        elif puntuacion.seis==2:
            valorcartasjugador=233
        elif puntuacion.cinco==2:
            valorcartasjugador=232
        elif puntuacion.cuatro==2:
            valorcartasjugador=231
        elif puntuacion.tres==2:
            valorcartasjugador=230
        elif puntuacion.dos==2:
             valorcartasjugador=229
    elif puntuacion.siete==3:
        if puntuacion.ass==2:
            valorcartasjugador=228
        elif puntuacion.rey==2:
            valorcartasjugador=227
        elif puntuacion.reina==2:
            valorcartasjugador=226
        elif puntuacion.jota==2:
            valorcartasjugador=225
        elif puntuacion.diez==2:
            valorcartasjugador=224
        elif puntuacion.nueve==2:
            valorcartasjugador=223
        elif puntuacion.ocho==2:
            valorcartasjugador=222
        elif puntuacion.seis==2:
            valorcartasjugador=221
        elif puntuacion.cinco==2:
            valorcartasjugador=220
        elif puntuacion.cuatro==2:
            valorcartasjugador=219
        elif puntuacion.tres==2:
            valorcartasjugador=218
        elif puntuacion.dos==2:
             valorcartasjugador=217
    elif puntuacion.seis==3:
        if puntuacion.ass==2:
            valorcartasjugador=216
        elif puntuacion.rey==2:
            valorcartasjugador=215
        elif puntuacion.reina==2:
            valorcartasjugador=214
        elif puntuacion.jota==2:
            valorcartasjugador=213
        elif puntuacion.diez==2:
            valorcartasjugador=212
        elif puntuacion.nueve==2:
            valorcartasjugador=211
        elif puntuacion.ocho==2:
            valorcartasjugador=210
        elif puntuacion.siete==2:
            valorcartasjugador=209
        elif puntuacion.cinco==2:
            valorcartasjugador=208
        elif puntuacion.cuatro==2:
            valorcartasjugador=207
        elif puntuacion.tres==2:
            valorcartasjugador=206
        elif puntuacion.dos==2:
             valorcartasjugador=205
    elif puntuacion.cinco==3:
        if puntuacion.ass==2:
            valorcartasjugador=204
        elif puntuacion.rey==2:
            valorcartasjugador=203
        elif puntuacion.reina==2:
            valorcartasjugador=202
        elif puntuacion.jota==2:
            valorcartasjugador=201
        elif puntuacion.diez==2:
            valorcartasjugador=200
        elif puntuacion.nueve==2:
            valorcartasjugador=199
        elif puntuacion.ocho==2:
            valorcartasjugador=198
        elif puntuacion.siete==2:
            valorcartasjugador=197
        elif puntuacion.seis==2:
            valorcartasjugador=196
        elif puntuacion.cuatro==2:
            valorcartasjugador=195
        elif puntuacion.tres==2:
            valorcartasjugador=194
        elif puntuacion.dos==2:
             valorcartasjugador=193
    elif puntuacion.cuatro==3:
        if puntuacion.ass==2:
            valorcartasjugador=192
        elif puntuacion.rey==2:
            valorcartasjugador=191
        elif puntuacion.reina==2:
            valorcartasjugador=190
        elif puntuacion.jota==2:
            valorcartasjugador=189
        elif puntuacion.diez==2:
            valorcartasjugador=188
        elif puntuacion.nueve==2:
            valorcartasjugador=187
        elif puntuacion.ocho==2:
            valorcartasjugador=186
        elif puntuacion.siete==2:
            valorcartasjugador=185
        elif puntuacion.seis==2:
            valorcartasjugador=184
        elif puntuacion.cinco==2:
            valorcartasjugador=183
        elif puntuacion.tres==2:
            valorcartasjugador=182
        elif puntuacion.dos==2:
             valorcartasjugador=181
    elif puntuacion.tres==3:
        if puntuacion.ass==2:
            valorcartasjugador=180
        elif puntuacion.rey==2:
            valorcartasjugador=179
        elif puntuacion.reina==2:
            valorcartasjugador=178
        elif puntuacion.jota==2:
            valorcartasjugador=177
        elif puntuacion.diez==2:
            valorcartasjugador=176
        elif puntuacion.nueve==2:
            valorcartasjugador=175
        elif puntuacion.ocho==2:
            valorcartasjugador=174
        elif puntuacion.siete==2:
            valorcartasjugador=173
        elif puntuacion.seis==2:
            valorcartasjugador=172
        elif puntuacion.cinco==2:
            valorcartasjugador=171
        elif puntuacion.cuatro==2:
            valorcartasjugador=170
        elif puntuacion.dos==2:
             valorcartasjugador=169
    elif puntuacion.dos==3:
        if puntuacion.ass==2:
            valorcartasjugador=168
        elif puntuacion.rey==2:
            valorcartasjugador=167
        elif puntuacion.reina==2:
            valorcartasjugador=166
        elif puntuacion.jota==2:
            valorcartasjugador=165
        elif puntuacion.diez==2:
            valorcartasjugador=164
        elif puntuacion.nueve==2:
            valorcartasjugador=163
        elif puntuacion.ocho==2:
            valorcartasjugador=162
        elif puntuacion.siete==2:
            valorcartasjugador=161
        elif puntuacion.seis==2:
            valorcartasjugador=160
        elif puntuacion.cinco==2:
            valorcartasjugador=159
        elif puntuacion.cuatro==2:
            valorcartasjugador=158
        elif puntuacion.tres==2:
            valorcartasjugador=157
    