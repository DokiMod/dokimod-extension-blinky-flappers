# Defining blinking
image menu_art_y_eye:
    "mod_assets/y_animation/menu_art_y_eye_1.png"
    choice:
        6.0
    choice:
        3.5
    choice:
        2.5
    "mod_assets/y_animation/menu_art_y_eye_0.png"
    0.1
    repeat
image menu_art_y_blink = LiveComposite((481,1080),(0,0),"gui/menu_art_y.png",(0,0),"menu_art_y_eye")

image menu_art_n_eye:
    "mod_assets/n_animation/menu_art_n_eye_1.png"
    choice:
        5.0
    choice:
        3.5
    choice:
        1.5
    "mod_assets/n_animation/menu_art_n_eye_0.png"
    0.1
    repeat
image menu_art_n_blink = LiveComposite((400,1080),(0,0),"gui/menu_art_n.png",(0,0),"menu_art_n_eye")

image menu_art_s_eye:
    "mod_assets/s_animation/menu_art_s_eye_1.png"
    choice:
        5.5
    choice:
        3.5
    choice:
        1.0
    "mod_assets/s_animation/menu_art_s_eye_0.png"
    0.1
    repeat
image menu_art_s_blink = LiveComposite((411,1080),(0,0),"gui/menu_art_s.png",(0,0),"menu_art_s_eye")

image menu_art_m_eye:
    "mod_assets/m_animation/menu_art_m_eye_1.png"
    choice:
        5.0
    choice:
        4.0
    choice:
        2.0
    "mod_assets/m_animation/menu_art_m_eye_0.png"
    0.1
    repeat
image menu_art_m_blink = LiveComposite((602,1080),(0,0),"gui/menu_art_m.png",(0,0),"menu_art_m_eye")

# defining blurring of ghost sprites
image menu_art_m_ghost_move:
    "gui/menu_art_m_ghost.png"
    choice:
        7.0
    choice:
        5.0
    choice:
        2.0
    "mod_assets/m_animation/menu_art_m_ghost_move.png"
    0.08
    repeat

image menu_art_n_ghost_move:
    "gui/menu_art_n_ghost.png"
    choice:
        6.5
    choice:
        4.5
    choice:
        2.5
    "mod_assets/n_animation/menu_art_n_ghost_move.png"
    0.08
    repeat

image menu_art_s_ghost_move:
    "gui/menu_art_s_ghost.png"
    choice:
        7.5
    choice:
        5.0
    choice:
        3.0
    "mod_assets/s_animation/menu_art_s_ghost_move.png"
    0.08
    repeat

image menu_art_y_ghost_move:
    "gui/menu_art_y_ghost.png"
    choice:
        8.0
    choice:
        6.0
    choice:
        3.0
    "mod_assets/y_animation/menu_art_y_ghost_move.png"
    0.08
    repeat

image menu_art_s_glitch_move:
    "gui/menu_art_s_break.png"
    choice:
        7.0
    choice:
        5.0
    choice:
        2.0
    "mod_assets/s_animation/menu_art_s_break_move.png"
    0.1
    repeat

image menu_art_y:
    subpixel True
    "menu_art_y_blink"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "menu_art_n_blink"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "menu_art_s_blink"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "menu_art_m_blink"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "menu_art_y_ghost_move"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "menu_art_n_ghost_move"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "menu_art_s_ghost_move"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "menu_art_m_ghost_move"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "menu_art_s_glitch_move"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)