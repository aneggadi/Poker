import poker2
import puntuacion
import color


valorcartasjugador=0
def escaleracolor():
    global valorcartasjugador
    if color.treborbot==5 or color.picasbot==5 or color.corazonesbot==5 or color.diamantesbot==5:
        if puntuacion.dosbot==1:
            if puntuacion.tresbot==1:
                if puntuacion.cuatrobot==1:
                    if puntuacion.cincobot==1:
                        if puntuacion.seisbot==1:
                            valorcartasjugador=326
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.tresbot==1:
            if puntuacion.cuatrobot==1:
                if puntuacion.cincobot==1:
                    if puntuacion.seisbot==1:
                        if puntuacion.sietebot==1:
                            valorcartasjugador=327
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.cuatrobot==1:
            if puntuacion.cincobot==1:
                if puntuacion.seisbot==1:
                    if puntuacion.sietebot==1:
                        if puntuacion.ochobot==1:
                            valorcartasjugador=328
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.cincobot==1:
            if puntuacion.seisbot==1:
                if puntuacion.sietebot==1:
                    if puntuacion.ochobot==1:
                        if puntuacion.nuevebot==1:
                            valorcartasjugador=329
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.seisbot==1:
            if puntuacion.sietebot==1:
                if puntuacion.ochobot==1:
                    if puntuacion.nuevebot==1:
                        if puntuacion.diezbot==1:
                            valorcartasjugador=330
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.sietebot==1:
            if puntuacion.ochobot==1:
                if puntuacion.nuevebot==1:
                    if puntuacion.diezbot==1:
                        if puntuacion.jotabot==1:
                            valorcartasjugador=331
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.ochobot==1:
            if puntuacion.nuevebot==1:
                if puntuacion.diezbot==1:
                    if puntuacion.jotabot==1:
                        if puntuacion.reinabot==1:
                            valorcartasjugador=332
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        elif puntuacion.nuevebot==1:
            if puntuacion.diezbot==1:
                if puntuacion.jotabot==1:
                    if puntuacion.reinabot==1:
                        if puntuacion.reybot==1:
                            valorcartasjugador=333
                        else:
                            valorcartasjugador=156
                    else:
                        valorcartasjugador=156
                else:
                    valorcartasjugador=156
            else:
                valorcartasjugador=156
        else:
            valorcartasjugador=334
    #poker
    elif puntuacion.assbot==4:
            valorcartasjugador=325
    elif puntuacion.reybot==4:
            valorcartasjugador=324
    elif puntuacion.reinabot==4:
            valorcartasjugador=323
    elif puntuacion.jotabot==4:
            valorcartasjugador=322
    elif puntuacion.diezbot==4:
            valorcartasjugador=321
    elif puntuacion.nuevebot==4:
            valorcartasjugador=320
    elif puntuacion.ochobot==4:
            valorcartasjugador=319
    elif puntuacion.sietebot==4:
            valorcartasjugador=318
    elif puntuacion.seisbot==4:
            valorcartasjugador=317
    elif puntuacion.cincobot==4:
            valorcartasjugador=316
    elif puntuacion.cuatrobot==4:
            valorcartasjugador=315
    elif puntuacion.tresbot==4:
            valorcartasjugador=314
    elif puntuacion.dosbot==4:
            valorcartasjugador=313
    #full house
    elif puntuacion.assbot==3:
        if puntuacion.reybot==2:
            valorcartasjugador=312
        elif puntuacion.reinabot==2:
            valorcartasjugador=311
        elif puntuacion.jotabot==2:
            valorcartasjugador=310
        elif puntuacion.diezbot==2:
            valorcartasjugador=309
        elif puntuacion.nuevebot==2:
            valorcartasjugador=308
        elif puntuacion.ochobot==2:
            valorcartasjugador=307
        elif puntuacion.sietebot==2:
            valorcartasjugador=306
        elif puntuacion.seisbot==2:
            valorcartasjugador=305
        elif puntuacion.cincobot==2:
            valorcartasjugador=304
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=303
        elif puntuacion.tresbot==2:
            valorcartasjugador=302
        elif puntuacion.dosbot==2:
            valorcartasjugador=301
    elif puntuacion.reybot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=300
        elif puntuacion.reinabot==2:
            valorcartasjugador=299
        elif puntuacion.jotabot==2:
            valorcartasjugador=298
        elif puntuacion.diezbot==2:
            valorcartasjugador=298
        elif puntuacion.nuevebot==2:
            valorcartasjugador=297
        elif puntuacion.ochobot==2:
            valorcartasjugador=295
        elif puntuacion.sietebot==2:
            valorcartasjugador=294
        elif puntuacion.seisbot==2:
            valorcartasjugador=293
        elif puntuacion.cincobot==2:
            valorcartasjugador=292
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=291
        elif puntuacion.tresbot==2:
            valorcartasjugador=290
        elif puntuacion.dosbot==2:
            valorcartasjugador=289
    elif puntuacion.reinabot==3:
        if puntuacion.assbot==2:
                valorcartasjugador=288
        elif puntuacion.reybot==2:
                valorcartasjugador=287
        elif puntuacion.jotabot==2:
                valorcartasjugador=286
        elif puntuacion.diezbot==2:
                valorcartasjugador=285
        elif puntuacion.nuevebot==2:
                valorcartasjugador=284
        elif puntuacion.ochobot==2:
                valorcartasjugador=283
        elif puntuacion.sietebot==2:
                valorcartasjugador=282
        elif puntuacion.seisbot==2:
                valorcartasjugador=281
        elif puntuacion.cincobot==2:
                valorcartasjugador=280
        elif puntuacion.cuatrobot==2:
                valorcartasjugador=279
        elif puntuacion.tresbot==2:
                valorcartasjugador=278
        elif puntuacion.dosbot==2:
                valorcartasjugador=277
    elif puntuacion.jotabot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=276
        elif puntuacion.reybot==2:
            valorcartasjugador=275
        elif puntuacion.reinabot==2:
            valorcartasjugador=274
        elif puntuacion.diezbot==2:
            valorcartasjugador=273
        elif puntuacion.nuevebot==2:
            valorcartasjugador=272
        elif puntuacion.ochobot==2:
            valorcartasjugador=271
        elif puntuacion.sietebot==2:
            valorcartasjugador=270
        elif puntuacion.seisbot==2:
            valorcartasjugador=269
        elif puntuacion.cincobot==2:
            valorcartasjugador=268
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=267
        elif puntuacion.tresbot==2:
            valorcartasjugador=266
        elif puntuacion.dosbot==2:
            valorcartasjugador=265
    elif puntuacion.diezbot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=264
        elif puntuacion.reybot==2:
            valorcartasjugador=263
        elif puntuacion.reinabot==2:
            valorcartasjugador=262
        elif puntuacion.jotabot==2:
            valorcartasjugador=261
        elif puntuacion.nuevebot==2:
            valorcartasjugador=260
        elif puntuacion.ochobot==2:
            valorcartasjugador=259
        elif puntuacion.sietebot==2:
            valorcartasjugador=258
        elif puntuacion.seisbot==2:
            valorcartasjugador=257
        elif puntuacion.cincobot==2:
            valorcartasjugador=256
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=255
        elif puntuacion.tresbot==2:
            valorcartasjugador=254
        elif puntuacion.dosbot==2:
             valorcartasjugador=253
    elif puntuacion.nuevebot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=252
        elif puntuacion.reybot==2:
            valorcartasjugador=251
        elif puntuacion.reinabot==2:
            valorcartasjugador=250
        elif puntuacion.jotabot==2:
            valorcartasjugador=249
        elif puntuacion.diezbot==2:
            valorcartasjugador=248
        elif puntuacion.ochobot==2:
            valorcartasjugador=247
        elif puntuacion.sietebot==2:
            valorcartasjugador=246
        elif puntuacion.seisbot==2:
            valorcartasjugador=245
        elif puntuacion.cincobot==2:
            valorcartasjugador=244
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=243
        elif puntuacion.tresbot==2:
            valorcartasjugador=242
        elif puntuacion.dosbot==2:
             valorcartasjugador=241
    elif puntuacion.ochobot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=240
        elif puntuacion.reybot==2:
            valorcartasjugador=239
        elif puntuacion.reinabot==2:
            valorcartasjugador=238
        elif puntuacion.jotabot==2:
            valorcartasjugador=237
        elif puntuacion.diezbot==2:
            valorcartasjugador=236
        elif puntuacion.nuevebot==2:
            valorcartasjugador=235
        elif puntuacion.sietebot==2:
            valorcartasjugador=234
        elif puntuacion.seisbot==2:
            valorcartasjugador=233
        elif puntuacion.cincobot==2:
            valorcartasjugador=232
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=231
        elif puntuacion.tresbot==2:
            valorcartasjugador=230
        elif puntuacion.dosbot==2:
             valorcartasjugador=229
    elif puntuacion.sietebot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=228
        elif puntuacion.reybot==2:
            valorcartasjugador=227
        elif puntuacion.reinabot==2:
            valorcartasjugador=226
        elif puntuacion.jotabot==2:
            valorcartasjugador=225
        elif puntuacion.diezbot==2:
            valorcartasjugador=224
        elif puntuacion.nuevebot==2:
            valorcartasjugador=223
        elif puntuacion.ochobot==2:
            valorcartasjugador=222
        elif puntuacion.seisbot==2:
            valorcartasjugador=221
        elif puntuacion.cincobot==2:
            valorcartasjugador=220
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=219
        elif puntuacion.tresbot==2:
            valorcartasjugador=218
        elif puntuacion.dosbot==2:
             valorcartasjugador=217
    elif puntuacion.seisbot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=216
        elif puntuacion.reybot==2:
            valorcartasjugador=215
        elif puntuacion.reinabot==2:
            valorcartasjugador=214
        elif puntuacion.jotabot==2:
            valorcartasjugador=213
        elif puntuacion.diezbot==2:
            valorcartasjugador=212
        elif puntuacion.nuevebot==2:
            valorcartasjugador=211
        elif puntuacion.ochobot==2:
            valorcartasjugador=210
        elif puntuacion.sietebot==2:
            valorcartasjugador=209
        elif puntuacion.cincobot==2:
            valorcartasjugador=208
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=207
        elif puntuacion.tresbot==2:
            valorcartasjugador=206
        elif puntuacion.dosbot==2:
             valorcartasjugador=205
    elif puntuacion.cincobot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=204
        elif puntuacion.reybot==2:
            valorcartasjugador=203
        elif puntuacion.reinabot==2:
            valorcartasjugador=202
        elif puntuacion.jotabot==2:
            valorcartasjugador=201
        elif puntuacion.diezbot==2:
            valorcartasjugador=200
        elif puntuacion.nuevebot==2:
            valorcartasjugador=199
        elif puntuacion.ochobot==2:
            valorcartasjugador=198
        elif puntuacion.sietebot==2:
            valorcartasjugador=197
        elif puntuacion.seisbot==2:
            valorcartasjugador=196
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=195
        elif puntuacion.tresbot==2:
            valorcartasjugador=194
        elif puntuacion.dosbot==2:
             valorcartasjugador=193
    elif puntuacion.cuatrobot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=192
        elif puntuacion.reybot==2:
            valorcartasjugador=191
        elif puntuacion.reinabot==2:
            valorcartasjugador=190
        elif puntuacion.jotabot==2:
            valorcartasjugador=189
        elif puntuacion.diezbot==2:
            valorcartasjugador=188
        elif puntuacion.nuevebot==2:
            valorcartasjugador=187
        elif puntuacion.ochobot==2:
            valorcartasjugador=186
        elif puntuacion.sietebot==2:
            valorcartasjugador=185
        elif puntuacion.seisbot==2:
            valorcartasjugador=184
        elif puntuacion.cincobot==2:
            valorcartasjugador=183
        elif puntuacion.tresbot==2:
            valorcartasjugador=182
        elif puntuacion.dosbot==2:
             valorcartasjugador=181
    elif puntuacion.tresbot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=180
        elif puntuacion.reybot==2:
            valorcartasjugador=179
        elif puntuacion.reinabot==2:
            valorcartasjugador=178
        elif puntuacion.jotabot==2:
            valorcartasjugador=177
        elif puntuacion.diezbot==2:
            valorcartasjugador=176
        elif puntuacion.nuevebot==2:
            valorcartasjugador=175
        elif puntuacion.ochobot==2:
            valorcartasjugador=174
        elif puntuacion.sietebot==2:
            valorcartasjugador=173
        elif puntuacion.seisbot==2:
            valorcartasjugador=172
        elif puntuacion.cincobot==2:
            valorcartasjugador=171
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=170
        elif puntuacion.dosbot==2:
             valorcartasjugador=169
    elif puntuacion.dosbot==3:
        if puntuacion.assbot==2:
            valorcartasjugador=168
        elif puntuacion.reybot==2:
            valorcartasjugador=167
        elif puntuacion.reinabot==2:
            valorcartasjugador=166
        elif puntuacion.jotabot==2:
            valorcartasjugador=165
        elif puntuacion.diezbot==2:
            valorcartasjugador=164
        elif puntuacion.nuevebot==2:
            valorcartasjugador=163
        elif puntuacion.ochobot==2:
            valorcartasjugador=162
        elif puntuacion.sietebot==2:
            valorcartasjugador=161
        elif puntuacion.seisbot==2:
            valorcartasjugador=160
        elif puntuacion.cincobot==2:
            valorcartasjugador=159
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=158
        elif puntuacion.tresbot==2:
            valorcartasjugador=157
#Escalera
    elif puntuacion.dosbot==1:
            if puntuacion.tresbot==1:
                if puntuacion.cuatrobot==1:
                    if puntuacion.cincobot==1:
                        if puntuacion.seisbot==1:
                            valorcartasjugador=147
    elif puntuacion.tresbot==1:
            if puntuacion.cuatrobot==1:
                if puntuacion.cincobot==1:
                    if puntuacion.seisbot==1:
                        if puntuacion.sietebot==1:
                            valorcartasjugador=148
    elif puntuacion.cuatrobot==1:
            if puntuacion.cincobot==1:
                if puntuacion.seisbot==1:
                    if puntuacion.sietebot==1:
                        if puntuacion.ochobot==1:
                            valorcartasjugador=149
    elif puntuacion.cincobot==1:
            if puntuacion.seisbot==1:
                if puntuacion.sietebot==1:
                    if puntuacion.ochobot==1:
                        if puntuacion.nuevebot==1:
                            valorcartasjugador=150
    elif puntuacion.seisbot==1:
            if puntuacion.sietebot==1:
                if puntuacion.ochobot==1:
                    if puntuacion.nuevebot==1:
                        if puntuacion.diezbot==1:
                            valorcartasjugador==151
    elif puntuacion.sietebot==1:
            if puntuacion.ochobot==1:
                if puntuacion.nuevebot==1:
                    if puntuacion.diezbot==1:
                        if puntuacion.jotabot==1:
                            valorcartasjugador=152
    elif puntuacion.ochobot==1:
            if puntuacion.nuevebot==1:
                if puntuacion.diezbot==1:
                    if puntuacion.jotabot==1:
                        if puntuacion.reinabot==1:
                            valorcartasjugador=153
    elif puntuacion.nuevebot==1:
            if puntuacion.diezbot==1:
                if puntuacion.jotabot==1:
                    if puntuacion.reinabot==1:
                        if puntuacion.reybot==1:
                            valorcartasjugador=154
    elif puntuacion.diezbot==1:
            if puntuacion.jotabot==1:
                if puntuacion.reinabot==1:
                    if puntuacion.reybot==1:
                        if puntuacion.assbot==1:
                            valorcartasjugador=155
#Trio
    elif puntuacion.assbot==3:
        valorcartasjugador=146
    elif puntuacion.reybot==3:
        valorcartasjugador=145
    elif puntuacion.reinabot==3:
        valorcartasjugador=144
    elif puntuacion.jotabot==3:
        valorcartasjugador=143
    elif puntuacion.diezbot==3:
        valorcartasjugador=142
    elif puntuacion.nuevebot==3:
        valorcartasjugador=141
    elif puntuacion.ochobot==3:
        valorcartasjugador=140
    elif puntuacion.sietebot==3:
        valorcartasjugador=139
    elif puntuacion.seisbot==3:
        valorcartasjugador=138
    elif puntuacion.cincobot==3:
        valorcartasjugador=137
    elif puntuacion.cuatrobot==3:
        valorcartasjugador=136
    elif puntuacion.tresbot==3:
        valorcartasjugador=135
    elif puntuacion.dosbot==3:
        valorcartasjugador=134
#Doble pareja
    elif puntuacion.assbot==2:
        if puntuacion.reybot==2:
            valorcartasjugador=133
        elif puntuacion.reinabot==2:
            valorcartasjugador=132
        elif puntuacion.jotabot==2:
            valorcartasjugador=131
        elif puntuacion.diezbot==2:
            valorcartasjugador=130
        elif puntuacion.nuevebot==2:
            valorcartasjugador=129
        elif puntuacion.ochobot==2:
            valorcartasjugador=128
        elif puntuacion.sietebot==2:
            valorcartasjugador=127
        elif puntuacion.seisbot==2:
            valorcartasjugador=126
        elif puntuacion.cincobot==2:
            valorcartasjugador=125
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=124
        elif puntuacion.tresbot==2:
            valorcartasjugador=123
        elif puntuacion.dosbot==2:
            valorcartasjugador=122
    elif puntuacion.reybot==2:
        if puntuacion.reinabot==2:
            valorcartasjugador=121
        elif puntuacion.jotabot==2:
            valorcartasjugador=120
        elif puntuacion.diezbot==2:
            valorcartasjugador=119
        elif puntuacion.nuevebot==2:
            valorcartasjugador=118
        elif puntuacion.ochobot==2:
            valorcartasjugador=117
        elif puntuacion.sietebot==2:
            valorcartasjugador=116
        elif puntuacion.seisbot==2:
            valorcartasjugador=115
        elif puntuacion.cincobot==2:
            valorcartasjugador=114
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=113
        elif puntuacion.tresbot==2:
            valorcartasjugador=112
        elif puntuacion.dosbot==2:
            valorcartasjugador=111
    elif puntuacion.reinabot==2:
        if puntuacion.jotabot==2:
                valorcartasjugador=110
        elif puntuacion.diezbot==2:
                valorcartasjugador=109
        elif puntuacion.nuevebot==2:
                valorcartasjugador=108
        elif puntuacion.ochobot==2:
                valorcartasjugador=107
        elif puntuacion.sietebot==2:
                valorcartasjugador=106
        elif puntuacion.seisbot==2:
                valorcartasjugador=105
        elif puntuacion.cincobot==2:
                valorcartasjugador=104
        elif puntuacion.cuatrobot==2:
                valorcartasjugador=103
        elif puntuacion.tresbot==2:
                valorcartasjugador=102
        elif puntuacion.dosbot==2:
                valorcartasjugador=101
    elif puntuacion.jotabot==2:
        if puntuacion.diezbot==2:
            valorcartasjugador=100
        elif puntuacion.nuevebot==2:
            valorcartasjugador=99
        elif puntuacion.ochobot==2:
            valorcartasjugador=98
        elif puntuacion.sietebot==2:
            valorcartasjugador=97
        elif puntuacion.seisbot==2:
            valorcartasjugador=96
        elif puntuacion.cincobot==2:
            valorcartasjugador=95
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=94
        elif puntuacion.tresbot==2:
            valorcartasjugador=93
        elif puntuacion.dosbot==2:
            valorcartasjugador=92
    elif puntuacion.diezbot==2:
        if puntuacion.nuevebot==2:
            valorcartasjugador=91
        elif puntuacion.ochobot==2:
            valorcartasjugador=90
        elif puntuacion.sietebot==2:
            valorcartasjugador=89
        elif puntuacion.seisbot==2:
            valorcartasjugador=88
        elif puntuacion.cincobot==2:
            valorcartasjugador=87
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=86
        elif puntuacion.tresbot==2:
            valorcartasjugador=85
        elif puntuacion.dosbot==2:
             valorcartasjugador=84
    elif puntuacion.nuevebot==2:
        if puntuacion.ochobot==2:
            valorcartasjugador=83
        elif puntuacion.sietebot==2:
            valorcartasjugador=82
        elif puntuacion.seisbot==2:
            valorcartasjugador=81
        elif puntuacion.cincobot==2:
            valorcartasjugador=80
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=79
        elif puntuacion.tresbot==2:
            valorcartasjugador=78
        elif puntuacion.dosbot==2:
             valorcartasjugador=77
    elif puntuacion.ochobot==2:
        if puntuacion.sietebot==2:
            valorcartasjugador=234
        elif puntuacion.seisbot==2:
            valorcartasjugador=233
        elif puntuacion.cincobot==2:
            valorcartasjugador=232
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=231
        elif puntuacion.tresbot==2:
            valorcartasjugador=230
        elif puntuacion.dosbot==2:
             valorcartasjugador=229
    elif puntuacion.sietebot==2:
        if puntuacion.seisbot==2:
            valorcartasjugador=221
        elif puntuacion.cincobot==2:
            valorcartasjugador=220
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=219
        elif puntuacion.tresbot==2:
            valorcartasjugador=218
        else:
            valorcartasjugador=301
    elif puntuacion.seisbot==2:
        if puntuacion.cincobot==2:
            valorcartasjugador=208
        elif puntuacion.cuatrobot==2:
            valorcartasjugador=207
        elif puntuacion.tresbot==2:
            valorcartasjugador=206
        elif puntuacion.dosbot==2:
             valorcartasjugador=205
    elif puntuacion.cincobot==2:
        if puntuacion.cuatrobot==2:
            valorcartasjugador=195
        elif puntuacion.tresbot==2:
            valorcartasjugador=194
        elif puntuacion.dosbot==2:
             valorcartasjugador=193
    elif puntuacion.cuatrobot==2:
        if puntuacion.tresbot==2:
            valorcartasjugador=182
        elif puntuacion.dosbot==2:
             valorcartasjugador=181
    elif puntuacion.tresbot==2:
        if puntuacion.dosbot==2:
             valorcartasjugador=169
#Pareja
    elif puntuacion.assbot==2:
        valorcartasjugador=146
    elif puntuacion.reybot==2:
        valorcartasjugador=145
    elif puntuacion.reinabot==2:
        valorcartasjugador=144
    elif puntuacion.jotabot==2:
        valorcartasjugador=143
    elif puntuacion.diezbot==2:
        valorcartasjugador=142
    elif puntuacion.nuevebot==2:
        valorcartasjugador=141
    elif puntuacion.ochobot==3:
        valorcartasjugador=140
    elif puntuacion.sietebot==3:
        valorcartasjugador=139
    elif puntuacion.seisbot==3:
        valorcartasjugador=138
    elif puntuacion.cincobot==3:
        valorcartasjugador=137
    elif puntuacion.cuatrobot==3:
        valorcartasjugador=136
    elif puntuacion.tresbot==3:
        valorcartasjugador=135
    elif puntuacion.dosbot==3:
        valorcartasjugador=134