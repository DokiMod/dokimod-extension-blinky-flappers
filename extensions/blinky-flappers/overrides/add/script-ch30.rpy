# 本 rpy 仅适用于三周目
# defining blinking
image Act3_eye:
    "mod_assets/m_animation/Act3_eye_1.png"
    choice:
        8.0
    choice:
        5.5
    choice:
        2.5
    "mod_assets/m_animation/Act3_eye_0.png"
    0.1
    repeat

# defining mouth-flapping
image Act3_mouth_0:
    "mod_assets/m_animation/Act3_mouth0_1.png"
    0.12
    "mod_assets/m_animation/Act3_mouth0_2.png"
    0.1
    "mod_assets/m_animation/Act3_mouth0_0.png"
    0.12
    "mod_assets/m_animation/Act3_mouth0_2.png"
    0.1
    repeat

image Act3_mouth_1:
    "mod_assets/m_animation/Act3_mouth1_1.png"
    0.12
    "mod_assets/m_animation/Act3_mouth1_2.png"
    0.1
    "mod_assets/m_animation/Act3_mouth1_0.png"
    0.12
    "mod_assets/m_animation/Act3_mouth1_2.png"
    0.1
    repeat

# setting face animations to Just Monika CG
image monika_bg = LiveComposite((1280,720),(0,0),"images/cg/monika/monika_bg.png",(0,0),"Act3_eye",(0,0),WhileSpeaking("monika","Act3_mouth_0","mod_assets/m_animation/Act3_mouth0_0.png"))
image monika_bg_highlight:
    LiveComposite((1280,720),(0,0),"images/cg/monika/monika_bg_highlight.png",(0,0),"Act3_eye",(0,0),WhileSpeaking("monika","Act3_mouth_0","mod_assets/m_animation/Act3_mouth0_0.png"))
    function monika_alpha