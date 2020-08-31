# defining blinking
image s_sticker_eye:
    "mod_assets/s_animation/s_sticker_eye_1.png"
    choice:
        4.5
    choice:
        3.0
    choice:
        1.5
    "mod_assets/s_animation/s_sticker_eye_0.png"
    0.1
    repeat

image s_sticker:
    LiveComposite((122,173),(0,0),"gui/poemgame/s_sticker_1.png",(0,0),"s_sticker_eye")
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker_eye:
    "mod_assets/n_animation/n_sticker_eye_1.png"
    choice:
        4.0
    choice:
        2.5
    choice:
        1.0
    "mod_assets/n_animation/n_sticker_eye_0.png"
    0.1
    repeat

image n_sticker:
    LiveComposite((141,161),(0,0),"gui/poemgame/n_sticker_1.png",(0,0),"n_sticker_eye")
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker_eye:
    "mod_assets/y_animation/y_sticker_eye_1.png"
    choice:
        5.0
    choice:
        3.5
    choice:
        2.0
    "mod_assets/y_animation/y_sticker_eye_0.png"
    0.1
    repeat

image y_sticker:
    LiveComposite((112,161),(0,0),"gui/poemgame/y_sticker_1.png",(0,0),"y_sticker_eye")
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    LiveComposite((112,161),(0,0),"gui/poemgame/y_sticker_cut_1.png",(0,0),"y_sticker_eye")
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker_eye:
    "mod_assets/m_animation/m_sticker_eye_1.png"
    choice:
        5.0
    choice:
        4.0
    choice:
        2.0
    "mod_assets/m_animation/m_sticker_eye_0.png"
    0.1
    repeat

image m_sticker:
    LiveComposite((119,168),(0,0),"gui/poemgame/m_sticker_1.png",(0,0),"m_sticker_eye")
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image y_sticker_1_broken:
    "gui/poemgame/y_sticker_1_broken.png"
    choice:
        6.0
    choice:
        5.5
    choice:
        3.0
    "mod_assets/y_animation/y_sticker_1_broken_move.png"
    0.1
    repeat

image y_sticker glitch:
    "y_sticker_1_broken"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat
