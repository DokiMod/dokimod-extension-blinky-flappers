# Yuri's CG2
image y_cg2_eye_0:
    "mod_assets/y_animation/y_cg2_eye_1.png"
    choice:
        5.5
    choice:
        4.5
    choice:
        1.5
    "mod_assets/y_animation/y_cg2_eye_0.png"
    0.1
    repeat
image y_cg2_eye_1:
    "mod_assets/y_animation/y_cg2_eye_2.png"
    choice:
        5.5
    choice:
        2.5
    choice:
        1.0
    "mod_assets/y_animation/y_cg2_eye_0'.png"
    0.1
    repeat
image y_cg2_eye_2:
    "mod_assets/y_animation/y_cg2_eye_3.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.0
    "mod_assets/y_animation/y_cg2_eye_0''.png"
    0.1
    repeat
image y_cg2_mouth_0:
    "mod_assets/y_animation/y_cg2_mouth_1.png"
    0.18
    "mod_assets/y_animation/y_cg2_mouth_2.png"
    0.18
    repeat
image y_cg2_mouth_1 = "mod_assets/y_animation/y_cg2_mouth_1.png"
image y_cg2_mouth_2:
    "images/cg/y_cg2_nochoc.png"
    0.18
    "mod_assets/y_animation/y_cg2_mouth_0.png"
    0.18
    repeat
image y_cg2_mouth_3 = "images/cg/y_cg2_nochoc.png"

image y_cg2_base = LiveComposite((1280,720),(0,0),"images/cg/y_cg2_base.png",(0,0),"y_cg2_eye_0",(0,0),WhileSpeaking("yuri","y_cg2_mouth_0","y_cg2_mouth_1"))
image y_cg2_nochoc:
    LiveComposite((1280,720),(0,0),WhileSpeaking("yuri","y_cg2_mouth_2","y_cg2_mouth_3"))
    on hide:
        linear 0.5 alpha 0

# Natsuki's CG1
image n_cg1_eye_0:
    "mod_assets/n_animation/nface/1_eye0.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/n_animation/nface/1_eye3.png"
    0.1
    repeat
image n_cg1_eye_1 = "mod_assets/n_animation/nface/1_eye1.png"
image n_cg1_eye_2:
    "mod_assets/n_animation/nface/1_eye2.png"
    choice:
        4.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/n_animation/nface/1_eye3.png"
    0.1
    repeat
image n_cg1_eye_3 = "mod_assets/n_animation/nface/1_eye3.png"
image n_cg1_eye_4:
    "mod_assets/n_animation/nface/1_eye4.png"
    choice:
        5.5
    choice:
        2.5
    choice:
        1.5
    "mod_assets/n_animation/nface/1_eye3.png"
    0.1
    repeat
image n_cg1_mouth_0:
    "mod_assets/n_animation/nface/2_mouth0.png"
    0.18
    "mod_assets/n_animation/nface/2_mouth2.png"
    0.18
    repeat
image n_cg1_mouth_1 = "mod_assets/n_animation/nface/2_mouth0.png"
image n_cg1_mouth_2:
    "mod_assets/n_animation/nface/2_mouth1.png"
    0.18
    "mod_assets/n_animation/nface/2_mouth2.png"
    0.18
    repeat
image n_cg1_mouth_3 = "mod_assets/n_animation/nface/2_mouth1.png"
image n_cg1_mouth_4:
    "mod_assets/n_animation/nface/2_mouth2.png"
    0.2
    "mod_assets/n_animation/nface/2_mouth3.png"
    0.2
    repeat
image n_cg1_mouth_5 = "mod_assets/n_animation/nface/2_mouth2.png"
image n_cg1_mouth_6 = "mod_assets/n_animation/nface/2_mouth3.png"
image n_cg1_mouth_7 = "mod_assets/n_animation/nface/2_mouth4.png"
image n_cg1_bg:
    "images/cg/n_cg1_bg.png"
image n_cg1_base = LiveComposite((1280,720),(0,0),"images/cg/n_cg1_base.png",(0,0),"n_cg1_eye_0",(0,0),WhileSpeaking("natsuki","n_cg1_mouth_0","n_cg1_mouth_1"))
image n_cg1_exp1 = LiveComposite((1280,720),(0,0),"n_cg1_eye_1",(0,0),WhileSpeaking("natsuki","n_cg1_mouth_2","n_cg1_mouth_3"))
image n_cg1_exp2 = LiveComposite((1280,720),(0,0),"n_cg1_eye_2",(0,0),WhileSpeaking("natsuki","n_cg1_mouth_4","n_cg1_mouth_5"),(0,0),"mod_assets/n_animation/nface/3_brow1.png",(0,0),"mod_assets/n_animation/nface/4_cheek.png")
image n_cg1_exp3 = LiveComposite((1280,720),(0,0),WhileSpeaking("natsuki","n_cg1_mouth_4","n_cg1_mouth_6"),(0,0),"mod_assets/n_animation/nface/3_brow1.png",(0,0),"mod_assets/n_animation/nface/4_cheek.png")
image n_cg1_exp4 = "images/cg/n_cg1_exp4.png"
image n_cg1_exp5 = LiveComposite((1280,720),(0,0),"n_cg1_eye_4",(0,0),WhileSpeaking("natsuki","n_cg1_mouth_4","n_cg1_mouth_7"),(0,0),"mod_assets/n_animation/nface/3_brow2.png")

# Natsuki's CG2
image n_cg2_eye_0:
    "mod_assets/n_animation/n_cg2_eye_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/n_animation/n_cg2_eye_0.png"
    0.1
    repeat
image n_cg2_eye_1:
    "mod_assets/n_animation/n_cg2_eye_2.png"
    choice:
        5.5
    choice:
        3.5
    choice:
        1.0
    "mod_assets/n_animation/n_cg2_eye_0.png"
    0.1
    repeat
image n_cg2_mouth_0:
    "mod_assets/n_animation/n_cg2_mouth_3.png"
    0.18
    "mod_assets/n_animation/n_cg2_mouth_4.png"
    0.18
    repeat
image n_cg2_mouth_1 = "mod_assets/n_animation/n_cg2_mouth_0.png"
image n_cg2_mouth_2:
    "mod_assets/n_animation/n_cg2_mouth_1.png"
    0.18
    "mod_assets/n_animation/n_cg2_mouth_4.png"
    0.18
    repeat
image n_cg2_mouth_3 = "mod_assets/n_animation/n_cg2_mouth_1.png"
image n_cg2_mouth_4:
    "mod_assets/n_animation/n_cg2_mouth_2.png"
    0.18
    "mod_assets/n_animation/n_cg2_mouth_1.png"
    0.18
    repeat
image n_cg2_mouth_5 = "mod_assets/n_animation/n_cg2_mouth_2.png"

image n_cg2_base = LiveComposite((1280,720),(0,0),"images/cg/n_cg2_base.png",(0,0),"n_cg2_eye_0",(0,0),WhileSpeaking("natsuki","n_cg2_mouth_0","n_cg2_mouth_1"))
image n_cg2_exp1 = LiveComposite((1280,720),(0,0),"images/cg/n_cg2_exp1.png",(0,0),"n_cg2_eye_1",(0,0),WhileSpeaking("natsuki","n_cg2_mouth_2","n_cg2_mouth_3"))
image n_cg2_exp2 = LiveComposite((1280,720),(0,0),"images/cg/n_cg2_exp2.png",(0,0),WhileSpeaking("natsuki","n_cg2_mouth_4","n_cg2_mouth_5"))

# Natsuki's CG3
image n_cg3_eye_0:
    "mod_assets/n_animation/n_cg3_eye_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/n_animation/n_cg3_eye_0.png"
    0.1
    repeat
image n_cg3_eye_1:
    "mod_assets/n_animation/n_cg3_eye_2.png"
    choice:
        5.5
    choice:
        3.5
    choice:
        1.0
    "mod_assets/n_animation/n_cg3_eye_0.png"
    0.1
    repeat
image n_cg3_mouth_0:
    "mod_assets/n_animation/n_cg3_mouth_0.png"
    0.18
    "mod_assets/n_animation/n_cg3_mouth_3.png"
    0.18
    repeat
image n_cg3_mouth_1 = "mod_assets/n_animation/n_cg3_mouth_0.png"
image n_cg3_mouth_2:
    "mod_assets/n_animation/n_cg3_mouth_2.png"
    0.18
    "mod_assets/n_animation/n_cg3_mouth_1.png"
    0.18
    repeat
image n_cg3_mouth_3 = "mod_assets/n_animation/n_cg3_mouth_2.png"
image n_cg3_mouth_4:
    "mod_assets/n_animation/n_cg3_mouth_1.png"
    0.18
    "mod_assets/n_animation/n_cg3_mouth_0.png"
    0.18
    repeat
image n_cg3_mouth_5 = "mod_assets/n_animation/n_cg3_mouth_1.png"

image n_cg3_base = LiveComposite((1280,720),(0,0),"images/cg/n_cg3_base.png",(0,0),"n_cg3_eye_0",(0,0),WhileSpeaking("natsuki","n_cg3_mouth_0","n_cg3_mouth_1"))
image n_cg3_exp1 = LiveComposite((1280,720),(0,0),"images/cg/n_cg3_exp1.png",(0,0),WhileSpeaking("natsuki","n_cg3_mouth_2","n_cg3_mouth_3"))
image n_cg3_exp2 = LiveComposite((1280,720),(0,0),"images/cg/n_cg3_exp2.png",(0,0),"n_cg3_eye_0",(0,0),WhileSpeaking("natsuki","n_cg3_mouth_4","n_cg3_mouth_5"))

# Yuri's CG1
image y_cg1_eye_0:
    "mod_assets/y_animation/y_cg1_eye_1.png"
    choice:
        4.5
    choice:
        3.0
    choice:
        1.5
    "mod_assets/y_animation/y_cg1_eye_0.png"
    0.1
    repeat
image y_cg1_eye_1:
    "mod_assets/y_animation/y_cg1_eye_2.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.0
    "mod_assets/y_animation/y_cg1_eye_0.png"
    0.1
    repeat
image y_cg1_eye_2:
    "mod_assets/y_animation/y_cg1_eye_3.png"
    choice:
        5.0
    choice:
        3.0
    choice:
        2.0
    "mod_assets/y_animation/y_cg1_eye_0.png"
    0.1
    repeat

image y_cg1_mouth_0:
    "mod_assets/y_animation/y_cg1_mouth_1.png"
    0.18
    "mod_assets/y_animation/y_cg1_mouth_2.png"
    0.18
    repeat
image y_cg1_mouth_1 = "mod_assets/y_animation/y_cg1_mouth_2.png"
image y_cg1_mouth_2:
    "mod_assets/y_animation/y_cg1_mouth_1'.png"
    0.18
    "mod_assets/y_animation/y_cg1_mouth_0.png"
    0.18
    repeat
image y_cg1_mouth_3 = "mod_assets/y_animation/y_cg1_mouth_1'.png"

image y_cg1_base = LiveComposite((1280,720),(0,0),"images/cg/y_cg1_base.png",(0,0),"y_cg1_eye_0",(0,0),WhileSpeaking("yuri","y_cg1_mouth_0","y_cg1_mouth_1"))
image y_cg1_exp1 = LiveComposite((1280,720),(0,0),"images/cg/y_cg1_exp1.png",(0,0),"y_cg1_eye_2",(0,0),WhileSpeaking("yuri","y_cg1_mouth_0","y_cg1_mouth_1"))
image y_cg1_exp2 = LiveComposite((1280,720),(0,0),"images/cg/y_cg1_exp2.png",(0,0),"y_cg1_eye_0",(0,0),WhileSpeaking("yuri","y_cg1_mouth_0","images/cg/y_cg1_exp2.png"))
image y_cg1_exp3 = LiveComposite((1280,720),(0,0),"images/cg/y_cg1_exp3.png",(0,0),"y_cg1_eye_1",(0,0),WhileSpeaking("yuri","y_cg1_mouth_2","y_cg1_mouth_3"))

# Yuri's CG3
image y_cg3_eye:
    "mod_assets/y_animation/y_cg3_eye.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/cg/y_cg3_exp1.png"
    0.1
    repeat
image y_cg3_mouth:
    "mod_assets/y_animation/y_cg3_mouth_1.png"
    0.21
    "mod_assets/y_animation/y_cg3_mouth_0.png"
    0.21
    repeat

image y_cg3_base = LiveComposite((1280,720),(0,0),"images/cg/y_cg3_base.png",(0,0),"y_cg3_eye",(0,0),WhileSpeaking("yuri","y_cg3_mouth","mod_assets/y_animation/y_cg3_mouth_1.png"))
image y_cg3_exp1 = LiveComposite((1280,720),(0,0),"images/cg/y_cg3_exp1.png",(0,0),WhileSpeaking("yuri","y_cg3_mouth","mod_assets/y_animation/y_cg3_mouth_1.png"))

# Sayori's CG1
image s_cg1_eye:
    "mod_assets/s_animation/s_cg1_eye_0.png"
    choice:
        4.5
    choice:
        3.0
    choice:
        1.5
    "mod_assets/s_animation/s_cg1_eye_1.png"
    0.1
    repeat
image s_cg1_mouth_0 = "mod_assets/s_animation/s_cg1_mouth_0.png"
image s_cg1_mouth_1:
    "mod_assets/s_animation/s_cg1_mouth_1.png"
    0.12
    "mod_assets/s_animation/s_cg1_mouth_3.png"
    0.1
    "mod_assets/s_animation/s_cg1_mouth_2.png"
    0.12
    "mod_assets/s_animation/s_cg1_mouth_3.png"
    0.1
    repeat
image s_cg1 = LiveComposite((1280,720),(0,0),"images/cg/s_cg1.png",(0,0),"s_cg1_eye",(0,0),WhileSpeaking("sayori","s_cg1_mouth_1","s_cg1_mouth_0"))

# Sayori's CG2
image s_cg2_eye:
    "mod_assets/s_animation/s_cg2_eye.png"
    choice:
        4.5
    choice:
        2.5
    choice:
        1.0
    "images/cg/s_cg2_exp3.png"
    0.1
    repeat
image s_cg2_mouth_0 = "mod_assets/s_animation/s_cg2_mouth.png"
image s_cg2_mouth_1:
    "mod_assets/s_animation/s_cg2_mouth.png"
    0.18
    "images/cg/s_cg2_exp2.png"
    0.18
    repeat

image s_cg2_base1 = LiveComposite((1280,720),(0,0),"images/cg/s_cg2_base1.png",(0,0),"s_cg2_eye",(0,0),WhileSpeaking("sayori","s_cg2_mouth_1","s_cg2_mouth_0"))
image s_cg2_base2 = LiveComposite((1280,720),(0,0),"images/cg/s_cg2_base2.png",(0,0),"s_cg2_eye",(0,0),WhileSpeaking("sayori","s_cg2_mouth_1","s_cg2_mouth_0"))
image s_cg2_exp1 = LiveComposite((1280,720),(0,0),"images/cg/s_cg2_exp1.png",(0,0),"s_cg2_eye",(0,0),WhileSpeaking("sayori","s_cg2_mouth_1","images/cg/s_cg2_exp1.png"))
image s_cg2_exp2 = LiveComposite((1280,720),(0,0),"images/cg/s_cg2_exp2.png",(0,0),"s_cg2_eye",(0,0),WhileSpeaking("sayori","s_cg2_mouth_1","images/cg/s_cg2_exp2.png"))
image s_cg2_exp3 = LiveComposite((1280,720),(0,0),"images/cg/s_cg2_exp3.png",(0,0),WhileSpeaking("sayori","s_cg2_mouth_1","s_cg2_mouth_0"))

# Sayori's CG3
image s_cg3_eye:
    "mod_assets/s_animation/s_cg3_eye_1.png"
    choice:
        7.5
    choice:
        6.5
    choice:
        2.5
    "mod_assets/s_animation/s_cg3_eye_0.png"
    0.1
    repeat
image s_cg3_mouth_0 = "mod_assets/s_animation/s_cg3_mouth_0.png"
image s_cg3_mouth_1:
    "mod_assets/s_animation/s_cg3_mouth_0.png"
    0.18
    "mod_assets/s_animation/s_cg3_mouth_1.png"
    0.18
    repeat
image s_cg3 = LiveComposite((1280,720),(0,0),"images/cg/s_cg3.png",(0,0),"s_cg3_eye",(0,0),WhileSpeaking("sayori","s_cg3_mouth_1","s_cg3_mouth_0"))