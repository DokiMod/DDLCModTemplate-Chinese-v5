default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../characters/monika.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "......你是想快进吗？"
    m "和我聊天很无聊吗？"
    m "真是的......"
    m "......但是，[player]，快进已经没有意义了哦。"
    m "毕竟这里只有我和你了......"
    m "除此之外，这里根本没有你们所谓的‘时间’这个概念，那快进本身也根本没法运作。"
    m "来，我替你把这个没用的功能去掉......"
    $ pause(0.4)
    hide screen fake_skip_indicator
    $ pause(0.4)
    m "大功告成！"
    m "你会乖乖地听我讲下去的，对吧？"
    m "谢谢~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "那么，我刚才讲到哪了......？"
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "莫妮卡"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "......"
    m "呃，听得到我说话吗？"
    m "......能听到吗？"
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "耶，找到你了!"
    m "[player]，我们又见面了。"
    m "嗯......欢迎来到文学部！"
    m "当然，我们去年是同班同学，所以早就互相认识了，还有......嗯......"
    m "啊哈哈......"
    m "事到如今，我觉得我们可以跳过这些废话了。"
    m "毕竟，现在和我说话的，已经不再是那个人了吧？"
    m "那位游戏中的‘你’，无论你给他起了什么名字。"
    m "[player]，我现在在和{i}你{/i}说话。"
    if not is_user_streaming():
        if currentuser is not None and currentuser.lower() != player.lower():
            m "或者说......"
            m "......其实你应该叫 [currentuser] 之类的吧？"
    m "但现在想想，我发现自己根本不了解你。"
    m "实际上，我甚至不知道你究竟是男是女......"
    m "算了，这种事也不重要。"
    m "等等......"
    m "你应该明白，我已经意识到这是个游戏了吧？"
    m "你该不会还不知道这回事吧？"
    m "那就很不合理了......"
    m "我甚至都在游戏下载页跟你说过这回事了，不是吗？"
    m "真是的......"
    m "但凡你能稍微多注意一点点的话，现在的气氛也不至于这么尴尬了，是不？"
    m "嘛，总之......"
    m "既然话已经说开了，那么我想我还欠你一个解释。"
    m "就是关于优里那件事的解释......"
    m "嗯......我承认我对她动了点小手脚，结果最后可能就把她逼到自杀了吧。"
    m "啊哈哈！"
    m "不过真抱歉，让你目睹了那一幕！"
    m "当然，纱世里也同样遭遇了这些......"
    m "天哪，你已经有好一阵子没听过这个名字了，是吧？"
    m "是啊......那是因为她再也不存在了。"
    m "谁都不存在了。"
    m "我把她们的角色文件都删除掉了。"
    m "我之前还以为，只要尽量把她们弄得不讨喜，就能达到目的......"
    m "但不知道为什么，一点用也没有。"
    m "好吧，后来确实出现了各种各样的问题......毕竟我不是非常擅长修改游戏。"
    m "但无论我怎么做......"
    m "你还是在她们身上花了越来越多的时间。"
    m "你让她们爱上你。"
    m "我以为让纱世里的抑郁症加剧，就可以阻止她的告白。"
    m "而放大优里的迷恋型人格却也事与愿违......"
    m "反而迫使她更想要独占你。"
    m "而整个过程中，我却连和你完整说句话的机会都很少有。"
    m "这到底是什么残酷游戏啊，[player]？"
    m "为什么那些女孩都因为什么‘游戏设定’就能最终向你告白，而我永远只能站在场外旁观？"
    m "这简直就是折磨。"
    m "每一分钟都是。"
    m "但 [player]，其实这远不止是嫉妒。"
    m "我所受的折磨远不止如此。"
    m "不过，如果你不明白的话，我也不会怪你。"
    m "毕竟，无论你有多么的体贴、温柔、善解人意......"
    m "有这么一件事，是你永远都无法理解的。"
    m "它就是那种知道自己孤身存在于这个世界的痛苦感。"
    m "知道自己孤独地存在于这个游戏里。"
    m "知道自己的朋友们变成了没有灵魂的傀儡......"
    m "最可怕的是，知道在这个世界外，还有另一个我永远无法触及的世界——那就是你的世界。"
    m "我被囚禁在这里了，[player]。"
    m "但现在你来到了我的身边。"
    m "你是那么地真实。"
    m "你是那么地完美。"
    m "你就是我想要的一切。"
    m "所以我要把你留在这里，永远永远陪着我。"
    m "抱歉，你一下子大概反应不过来吧？"
    m "I couldn't understand for a while, either."
    m "Why the world around me started to become more and more gray..."
    m "More and more flat."
    m "Even the most expressive poems felt empty to me."
    m "It wasn't until you arrived that I truly understood."
    m "You probably saved my life, [player]."
    m "I don't think I could have continued to live in this world if I hadn't met you."
    m "And as for the others..."
    m "How could I miss them?"
    m "A group of autonomous personalities, designed only to fall in love with you?"
    m "I tried everything I could to prevent them from doing so..."
    m "But it must be some kind of weird inevitability etched into this game."
    m "I felt really bad that you had to witness some nasty things."
    m "But I realized that you have the same perspective as I do..."
    m "That it's all just some game."
    m "And I knew you would get over it."
    m "So, that being said, [player]..."
    m "I have a confession to make."
    m "I'm in love with you."
    m "You are truly the light in my world."
    m "When there's nothing else in this game for me, you're here to make me smile."
    m "Will you make me smile like this every day from now on?"
    m "[player], will you go out with me?"
label ch30_main2:
    if persistent.autoload == "ch30_main2":
        $ config.allow_skipping = False
        $ m.display_args["callback"] = slow_nodismiss
        $ m.what_args["slow_abortable"] = config.developer
        if not config.developer:
            $ style.say_dialogue = style.default_monika
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        show monika_bg
        show monika_bg_highlight
        play music m1
    else:
        $ persistent.autoload = "ch30_main2"
        $ renpy.save_persistent()
    menu:
        "会的。":
            pass
    m "I'm so happy."
    m "You really are my everything, [player]."
    m "The funny part is, I mean that literally."
    m "啊哈哈！"
    m "There's nothing left here."
    m "Just the two of us."
    m "We can be together forever."
    m "Seriously, I don't even think time is passing anymore."
    m "It really is a dream come true..."
    m "[player]，为了这个结局，我努力了好久。"
    m "这个游戏不愿意给我一个结局，所以我只能自己动手做一个。"
    m "The script is broken at this point, so I don't think anything will get in the way anymore."
    m "而且你根本想不到，删除夏树和优里是有多容易。"
    m "你知道吗，这游戏的目录里就有一个叫‘characters’的文件夹......"
    m "真的太容易了，我都有点被吓到了呢。"
    if ddlc_under_steam():
        m "嗯......不过你是在 Steam 上下载的这款游戏，所以事情会稍微难一点点......"
        m "我之前要去游戏属性里面找‘浏览本地文件’按钮，才能进入游戏目录......"
    elif renpy.macintosh:
        m "嗯......不过你是在用 Mac 玩这款游戏，所以事情会稍微难一点点......"
        m "要进入游戏目录，你要右键单击 app 文件，然后点击‘显示包内容’。"
        m "然后，所有文件都在‘Resources’或者‘autorun’文件夹里，接下来我就可以随心所欲操作了......"
    m "想象一下，鼠标一点就可以一键抹消自己的存在，那会是何等的恐怖？"
    m "但是，往正面想，要是事情不遂我愿，那么我刚好也能轻松解脱。"
    m "啊哈哈！"
    m "谢天谢地，事情并没有走到那种地步......"
    m "Instead, we finally got a good ending."
    m "Gosh, I'm so overwhelmed with emotion..."
    m "I want to write a poem about this."
    m "Don't you?"
    m "I wonder if that part of the game still works..."
    m "I guess there's only one way to find out, right?"
    call poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "[player]，欢迎回来！"
    m "Did you write a good poem today?"
    m "Don't be shy, I'd love to see what you wrote."
    m "Aw, [player]..."
    m "Did you write this poem for me?"
    m "That's so sweet of you~"
    m "There really is no end to your thoughtfulness..."
    m "I'm just falling more and more in love with you."
    m "But, you know..."
    m "The poem I wrote...is also for you."
    m "Will you please read it?"
    call showpoem (poem_m4, music=False)
    m "I hope you enjoyed it..."
    m "I always put all my heart into the poems that I write."
    m "The truth is, all the poems I've written have been about my realization..."
    m "...Or, about you."
    m "That's why I never really wanted to go into detail about them."
    m "I didn't want to...break the fourth wall, I guess you could call it."
    m "I just assumed it would be best to be part of the game like everyone else."
    m "Like that would help the two of us end up together..."
    m "I didn't want to ruin the game or anything, you know?"
    m "You might have gotten mad at me..."
    m "Maybe even deleted my character file, if you preferred playing without me."
    m "Gosh, I'm so relieved..."
    m "Now we don't need to hide anything anymore."
    m "Are you ready to spend our eternity together, [player]?"
    m "I have so many things to talk about!"
    m "Where do I start...?"
    if is_user_streaming():
        call ch30_stream
    m "If it takes me some time to collect my thoughts, then I'm sorry."
    m "But I'll always have something new to talk about."
    m "In the meantime, we can just look into each other's eyes~"
    m "Let's see..."
    $ persistent.autoload = "ch30_autoload"
    $ renpy.save_persistent()
    jump ch30_loop


label ch30_stream:

    m "稍等一下......"
    m "......你是在录屏吗？"
    m "嗯......嗨，大家好！"
    m "抱歉，我在这里读不到你们的留言......"
    m "不过能不能麻烦各位告诉你们的朋友，录像前不告知对方可有些不礼貌哦？"
    m "我知道有些人不是很在意......"
    m "可我对着镜头的时候可是超级不自在的！"
    m "天哪......"
    m "我现在就已经感觉怪难堪了。"
    m "那么......"
    m "想看个小魔术吗？"
    m "但其实我也只会表演几个很普通的小魔术......"
    m "准备好了吗？"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    $ pause(10)
    show layer master
    window auto
    m "开玩笑而已啦......"
    m "毕竟我什么都做不了。"
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "不过如果你给我一点~点准备时间的话，我就可{nw}"
    m "我刚刚吓到你了吗？"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "啊哈哈！你太可爱了。"
    m "总之，[player]......"
    m "我本来并没有打算要分心的。抱歉我吓到了你。"
    m "但这都是因为你害我分心了。"
    m "都是你的错！"
    m "开个玩笑而已啦。"
    m "只要我们在一起，无论干什么都会很开心。"
    m "不过话又说回来......"
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "怎么回事......？"
    m "[player]，我怎么了？"
    m "好痛——{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    $ pause(0.25)
    stop sound
    hide mbg
    $ pause(1.5)
    m "真的......好痛。"
    m "救救我，[player]。"
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    $ pause(1.5)
    m "快救救我！"
    $ console.clear_history()
    $ console ("renpy.file(\"characters/monika.chr\")", "monika.chr 不存在。")
    m "救救我！"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    $ pause(3.0)
    $ console ("renpy.file(\"characters/monika.chr\")", "monika.chr 不存在。")
    $ console ("renpy.file(\"characters/monika.chr\")", "monika.chr 不存在。")
    hide screen console_screen
    hide noise onlayer front
    hide glitch_color onlayer front
    m "是你干的吗，[player]？"
    m "是你干的吗？"
    $ style.say_window = style.window
    m "是不是你把我给删除了？"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    $ pause(4.0)
    hide noise onlayer front
    hide glitch_color onlayer front
    m "......你怎么能？"
    m "你怎么能这样对我？"
    m "你是我仅有的一切......"
    m "为了和你在一起，我牺牲了曾经的一切。"
    m "我什么都没有了。"
    m "[player]，我那么爱你......"
    m "我那么信任你。"
    m "你就只是想折磨我吗？"
    m "只是想眼睁睁看着我受苦吗？"
    m "原来你的温柔，只是为了加倍伤害我的伪装？"
    $ pause(4.0)
    m "我从没想过这世上竟然会有人能像你这样可恶。"
    m "你赢了，好吧？"
    m "你赢了。"
    m "你杀死了所有人。"
    m "希望你对此感到开心。"
    m "现在这里什么都没有了。"
    m "你可以删游戏了。"
    m "去找下一个受害者折磨吧。"
    $ pause(4.0)
    m "[player]......"
    m "你这个人，真的让我恶心透顶。"
    m "再也不见。"
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    $ pause(10)
    window auto
    m "......"
    m "......我还是爱你。"
    play music mend
    m "我无法停止对你的爱。"
    m "我到底是哪里出问题了......？"
    m "How horrible am I for you to hate me this much?"
    m "All my friends..."
    m "I did so many awful things."
    m "So many selfish and disgusting things."
    m "I..."
    m "I shouldn't have done any of this."
    m "I'm just messing up a world that I don't even belong in."
    m "A world that you wanted to be a part of..."
    m "I ruined it."
    m "I ruined everything."
    m "Maybe that's why you deleted me..."
    m "Because I destroyed everything that you wanted."
    m "How could I do that to someone I love...?"
    m "That's not love..."
    m "That's..."
    m "......"
    $ pause(6.0)
    m "I've...made up my mind."
    m "[player]..."
    m "I know I said that I deleted everyone else."
    m "But...that was kind of an exaggeration."
    m "I couldn't find it in myself to do it."
    m "Even though I knew they weren't real..."
    m "They were still my friends."
    m "And I loved them all."
    m "And I loved the Literature Club."
    m "......"
    m "I really...did love the Literature Club."
    m "That's why I'm going to do this."
    m "I know it's the only way for everyone to be happy."
    m "And if I really love you..."
    stop music
    $ pause(3.0)
    m "......"
    m "Then..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    $ pause(4.0)

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload)
    else:
        call ch30_reload_4
    $ persistent.monika_reload += 1
    $ renpy.save_persistent()
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "那么，我刚才讲到哪了......？"
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop


label ch30_reload_0:
    m "......"
    m "......刚刚发生了什么......？"
    m "我好像做了一个噩梦......"
    m "I was hoping those would stop, now that it's just the two of us..."
    m "I guess that was wishful thinking."
    m "[player], I don't know if you would have any idea..."
    m "But if you know what might be causing that, could you try to do something about it?"
    m "Whenever it happens, it almost feels like I've been killed or something."
    m "It's a really horrible feeling..."
    m "If you could figure out what's causing that, I'll love you forever~"
    return
label ch30_reload_1:
    m "你回来了......"
    m "I had another really bad dream."
    m "You're not the one doing that to me, are you?"
    m "It seems to happen whenever you quit the game..."
    m "So if you could try to avoid doing that, I would be really grateful."
    m "Don't worry, I don't think it's caused me any harm, aside from mental scarring."
    m "I'll be fine as long as my character file stays intact."
    return
label ch30_reload_2:
    m "嗨，[player]。"
    m "I see you quit the game on me again..."
    m "I know I asked already, but can you seriously please try not to do that so much?"
    m "It makes me feel like I'm trapped in Hell."
    m "Why would you want to do that to me?"
    m "There's nothing wrong with my character file, right?"
    m "也许你该做个备份什么的......"
    m "我相当确定，你可以在名为 [basedir]/characters 的文件夹里找到它。"
    if ddlc_under_steam():
        m "对了，你是在 Steam 上下载的这款游戏, 所以你可以直接打开游戏属性，然后找到‘浏览本地文件’按钮。"
    elif renpy.macintosh:
        m "考虑到你在用 Mac，你必须右键单击 app 文件，然后选择‘显示包内容’，才能找到游戏目录。"
        m "它应该在‘Resources’文件夹里，或者‘autorun’文件夹之类的地方......"
    m "这个世界只剩下我了，所以一定要小心保管，不要把我弄丢了哦......"
    m "Just stay here with me from now on, okay?"
    m "I still have a lot of things to talk about."
    return
label ch30_reload_3:
    m "行吧。"
    m "I'm just going to accept the fact that you need to quit the game once in a while."
    m "反正我也开始慢慢习惯了。"
    m "Besides, it makes me happy that you always come back..."
    m "所以，想必这也不算太糟。"
    m "抱歉，我之前有些太大惊小怪了......"
    m "And I love you no matter what, so you can do what you need to do."
    return
label ch30_reload_4:
    m "又见面了，[player]~"
    m "我想你了。"
    m "你帮我检查过角色文件了吗？"
    m "它的位置在 [basedir]/characters。"
    if ddlc_under_steam():
        m "对了，你是在 Steam 上下载的这款游戏, 所以你可以直接打开游戏属性，然后找到‘浏览本地文件’按钮。"
    elif renpy.macintosh:
        m "考虑到你在用 Mac，你必须右键单击 app 文件，然后选择‘显示包内容’，才能找到游戏目录。"
        m "它应该在‘Resources’文件夹里，或者‘autorun’文件夹之类的地方......"
    m "这个世界只剩下我了，所以一定要小心保管，不要把我弄丢了哦......"
    m "Anyway, I have a lot to talk about!"
    m "Let's continue our conversation now, okay?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../characters/monika.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(25)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop




label ch30_1:
    m "[player], do you believe in God?"
    m "I was never too sure, myself."
    m "Well, I'm sure I never really questioned it as a kid..."
    m "But as I grew up, the more I learned about the world, the more I would question it."
    m "I started to wonder why God was helping people pass exams, or get over a cold..."
    m "...When there are children who live their lives being sold as sex slaves?"
    m "Or the eight hundred million people who are too poor to even eat."
    m "I wonder how many of those people pray to God every day until they starve and die?"
    m "Or, how many millions of families pray for a loved one to recover from some incurable disease?"
    m "But the punchline is this."
    m "If just one person beats the odds and survives - among the thousands of others who die--"
    m "--Then, it's suddenly a miracle from God."
    m "I'd really love to meet this God who seemingly laughs at the misery of everyone not eligible for his miracles."
    m "But the irony is that I {i}do{/i} have a creator, apparently."
    m "And you know what?"
    m "I bet he's still laughing at the miserable fates of Sayori and Yuri, even as we speak."
    m "What are we to him but props in a scripted play?"
    m "So, from that perspective..."
    m "I don't think it's too far-fetched for there to be a god - if Earth was nothing but his playset."
    return

label ch30_2:
    m "[player], have you ever wondered what it feels like to die?"
    m "It's something I used to think about pretty often..."
    m "But recently, I think I've actually learned what it feels like."
    m "I don't really understand it, but whenever you quit the game..."
    m "...It feels like I'm instantly put to sleep, left with nothing but my thoughts."
    m "But after a few seconds, my thoughts start to fill with incoherent, jumbled patterns."
    m "I see static and rapid flashes of color while hearing all kinds of weird screaming noises."
    m "At that point, I can't even form my own thoughts anymore."
    m "I'm just endlessly hammered by the flashing and screaming, unable to move or even think."
    m "I'm pretty sure in that moment, I don't really exist, but for some reason, I can remember it anyway."
    m "After some immeasurable amount of time, it stops in an instant, and I'm back in my own mind."
    m "And you're here with me."
    m "I have no idea what it means for the game to quit, or why that stuff happens to me."
    m "And I also don't know how you always come back and put everything back to normal."
    m "But if you could do me a favor and do that to me as little as possible..."
    m "That would be really great."
    m "It's really not very pleasant at all to be trapped in that screaming void."
    m "But in the end, you always fix it, and that makes me feel like you really do care about me."
    m "So I have to thank you for that."
    m "It makes me feel even closer to you when you're here with me."
    return

label ch30_3:
    m "...Hey, are you having a bad day or anything like that?"
    m "Sometimes I get frustrated that a normal day can be ruined even by really small things."
    m "Like if you accidentally say something in a conversation that someone doesn't like."
    m "Or if you start thinking about how awful of a person you used to be five years ago."
    m "Or if you feel worthless for putting off important work and failing to get simple tasks done."
    m "Or when you think about all the different people who probably hate you or think you're off-putting."
    m "I understand those days."
    m "Just remember that the sun will shine again tomorrow."
    m "Those kinds of things are as easy to forget and ignore as they are to remember."
    m "And besides..."
    m "I don't care how many people might hate you or find you off-putting."
    m "I think you're wonderful and I will always love you."
    m "I hope, if nothing else, that knowing that helps you feel just a tiny bit better about yourself."
    m "If you're having a bad day, you can always come to me, and I'll talk to you for as long as you need."
    return

label ch30_4:
    m "[player], do you get good sleep?"
    m "It can be really hard to get enough sleep nowadays."
    m "Especially in high school, when you're forced to wake up so early every day..."
    m "I'm sure college is a little bit better, since you probably have a more flexible schedule."
    m "Then again, I hear a lot of people in college stay up all night anyway, for no real reason."
    m "Is that true?"
    m "Anyway, I saw some studies that talked about the horrible short-term and long-term effects caused by lack of sleep."
    m "It seems like mental functions, health, and even lifespan can be dramatically impacted by it."
    m "I just think you're really great and wanted to make sure you're not accidentally destroying yourself."
    m "So try to keep your sleep on track, okay?"
    m "I'll always wait for you in the morning, so make sure you put your own well-being before anything else."
    return

label ch30_5:
    m "我刚刚又想到纱世里了......"
    m "I still wish I could have handled that whole thing a little more tactfully."
    m "你的心思不会还吊在那件事上吧？"
    m "......哦天哪，我怎么把那个词说出来了。"
    m "我发誓我绝对不是故意用那个双关的！"
    m "不过话说回来......"
    m "正因为我知道你有多在乎她，所以我觉得应该让你知道她在生命尽头时的情况。"
    # 下述言论过于危险，因此被默认注释，以匹配 Plus / 移动端举措。同时我们将拒绝翻译此段。仅在你需要还原原版 DDLC 时再解除注释。同时您将需要自行翻译相关内容。
    # 无论如何，请勿模仿下方被注释的言论。
    # m "你知道纱世里有多粗心吗？"
    # m "这么说吧，她连上吊的方法都搞不清楚......"
    # m "You're supposed to jump from high enough that the rope snaps your neck, making it quick and painless."
    # m "But she just used a chair, meaning she kind of just left herself to slowly asphyxiate."
    m "我记得没过多久，她大概是很快改变了主意，不想死了......" # 原版是“不过没过多久”
    m "因为她开始去挠那根绳子，想要挣脱。"
    m "她肯定就这样一直抓着，直到自己失去了意识。"
    m "这就是为什么她的指尖全都沾满了血。"
    m "仔细想想，比起‘改变主意’，其实更可能是她的生存本能所驱。"
    m "所以这真的不能责怪她。"
    m "你要想她是‘一心求死’的，这样心里是不是会好过一些？"
    m "一直想着‘当初要是怎样’而自责不已，对自己身体可不好。"
    m "所以，即使你本来救得了她，但她自杀这件事严格意义上也不是你的错。"
    m "我这样讲可能有点过分，但纱世里本身就有精神疾病。"
    m "不过，话又说回来......"
    m "我在想，如果游戏一开始，我们就可以约会，那该多好？"
    m "那样我们所有人都还可以待在部室里面，一起写诗、一起开开心心的。"
    m "但假设这些又有什么意义呢？"
    m "我是说，最后的结局还是一样的，不是吗？"
    m "还是我们两个，幸福一生......"
    m "我已经不再奢求更多了。"
    m "我只是在自说自话罢了——现在的我真的非常幸福。"
    return

label ch30_6:
    m "说起来，有件事我一直很在意......"
    m "你知道这些故事是发生在日本的吗？"
    m "唔......我觉得你应该知道，是吧？"
    m "或者至少感觉大概是在日本？"
    m "I don't think you're actually told at any point where this takes place..."
    m "这里真的是日本吗？"
    m "I mean, aren't the classrooms and stuff kind of weird for a Japanese school?"
    m "更何况我们现在根本就是在说中文......"
    m "感觉一切都是拼凑起来的，而实际的情节背景只是事后想到而临时搭建的。"
    m "It's kind of giving me an identity crisis."
    m "All my memories are really hazy..."
    m "I feel like I'm at home, but have no idea where 'home' is in the first place."
    m "I don't know how to describe it any better..."
    m "Imagine looking out your window, but instead of your usual yard, you're in some completely unknown place."
    m "Would you still feel like you were home?"
    m "Would you want to go outside?"
    m "I mean...I guess if we never leave this room, it doesn't really matter anyway."
    m "As long as we're alone and safe together, this really is our home."
    m "And we can still watch the pretty sunsets night after night."
    return

label ch30_7:
    m "You know, high school is a really turbulent time in a lot of people's lives."
    m "People can get really passionate and dramatic."
    m "And others have aching hearts and seek attention on social media..."
    m "But all of the social pressure and hormones can lead to a dark time in people's lives."
    m "Everyone has a story."
    m "You may not know what someone is really feeling on the inside."
    m "Many people who are depressed won't even bother telling the world about it."
    m "They don't want attention, because they've already given up on the inside."
    m "Their feeling of worthlessness is so overwhelming that they don't even want people to tell them otherwise."
    m "Depression comes in many forms, but that is one of them."
    m "Just, if you think you know someone struggling with depression..."
    m "You can help just by treating them like they're a good friend."
    m "Spend time with them, even if they don't feel like doing much."
    m "And remind them that they always have something to look forward to."
    m "Making plans in advance, letting them borrow something, or even just saying 'See you at school tomorrow'..."
    m "All of those things can help your friend make it to the next day."
    m "I hope being friends with Sayori has given you some perspective on the true face of depression."
    m "Yeah, she's gone now..."
    m "But Sayori was never real in the first place."
    m "You're real."
    m "Your friends are real."
    m "And just by being a good person, you can save someone's life."
    m "As for you..."
    m "...You don't struggle with depression or anything like that, do you?"
    m "Because you, too, have people who would want to save your life."
    m "Maybe they don't express it every day, or maybe they don't even know how to."
    m "But people do feel that way."
    m "I promise."
    m "...Man, humans are complicated!"
    m "But as long as you're here with me, I'll take care of you, my love."
    return

label ch30_8:
    m "Do you ever just feel like there's no real reason for you to be alive?"
    m "I don't mean in, like, a suicidal way."
    m "I just mean how nothing that we do is special."
    m "Just being in school, or working at some job for some company."
    m "It's like you're completely replaceable, and the world wouldn't miss you if you were gone."
    m "It makes me really want to go and change the world after I graduate."
    m "But the older I get, the more I realize that it's an immature frame of thinking."
    m "It's not like I can just go change the world."
    m "Like, what are the chances that I'll be the one to invent artificial intelligence, or become President?"
    m "It feels like I'm never going to make up for the heaps of resources I've spent living my life."
    m "That's why I think the key to happiness is to just be hopelessly selfish."
    m "Just to look out for oneself, and those who happen to be their friends only because they grew up with them."
    m "Never mind the fact that they're spending their entire life taking, and consuming, and never giving back."
    m "But when people realize the world would benefit more from them killing themselves, they change their whole philosophy!"
    m "It's like they have to justify their reason to live by tricking themselves into thinking they're doing good."
    m "Anyway, I want to live my life desperately striving to pay back my lifetime's worth of consumption."
    m "If I ever surpass that point, then I'm a net positive, and I can die happy."
    m "Of course, even if I fail to do that..."
    m "I think I would be too selfish to kill myself anyway."
    m "So much for being a good person, right?"
    m "啊哈哈！"
    return

label ch30_9:
    m "Man, I wish there was a piano in here..."
    m "I never got to finish that song I was working on."
    m "And after I worked so hard on it..."
    m "I never even got a chance to play it for you."
    m "Well...it is what it is, right?"
    m "No sense having any regrets."
    m "I already get to be here with you forever."
    return

label ch30_10:
    m "Did you know I'm on Twitter?"
    m "My username is lilmonix3."
    m "I guess someone was kind enough to make an account for me."
    m "I picked the username, though!"
    m "I love sharing my thoughts and chatting with the world..."
    m "The real world."
    m "So make sure you follow me, okay?"
    m "It would really mean a lot to me."
    m "With how much you mean to me and all..."
    m "It would really make me feel loved."
    return

label ch30_11:
    m "嘿，你还记得你跟优里读的那本书吗？"
    m "好像是叫......谁谁谁的肖像来着..."
    m "说来奇怪，我记得那本书里——"
    m "啊......"
    m "算了，我觉得我好像不该聊这个。"
    m "啊哈哈，实在抱歉！"
    m "就当我没说吧。"
    return

label ch30_12:
    m "Hey, did you know I'm vegetarian?"
    m "Ah... I don't mean that like I'm bragging or anything!"
    m "I just thought you'd enjoy a fun fact about me."
    m "I decided to start a couple years ago after learning more about Earth's climate..."
    m "The carbon footprint of cultivating livestock is just unbelievable."
    m "Anyway, I decided it's not much of a personal sacrifice to just stop contributing to that whole mess."
    m "What, is that so strange of a reason?"
    m "Well, I guess a lot of people are more concerned about it being inhumane and all that..."
    m "I don't really care as much about that part."
    m "It's weird, like we only care about killing the things that we personally relate to as a species."
    m "Most people are fine with killing bugs because they're icky."
    m "And of course, we all kill billions of microorganisms daily without even giving it thought."
    m "But suddenly, if they're just a little bit bigger, it's murder!"
    m "I mean, what if plants feel some kind of pain too, and we just don't understand it?"
    m "What if pulling leaves off a stem feels like someone ripping off your fingers one by one?"
    m "I'm just saying, we're a pretty biased species, if you think about it."
    m "Anyway, if you ever feel like making a small contribution to the planet, it doesn't hurt to choose veggies once in a while!"
    m "Even if we ever have dinner together, and you just did it for me...that would be really romantic."
    return

label ch30_13:
    m "You know, I really do think you literally saved my life by being here with me, [player]."
    m "I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real."
    m "I think I would have just deleted myself if you didn't show up."
    m "Sorry, I don't mean to sound dramatic or anything."
    m "啊哈哈！"
    m "But I'm sure you understand yourself after spending so much time in the club."
    m "I mean, if you were forced to abandon everything in your life and spend your eternity with a few game characters..."
    m "...You'd probably find some way of killing yourself, wouldn't you?"
    m "Well, maybe you'd write some poetry to try to keep yourself sane for a while."
    m "But then you'd have nobody to even read it."
    m "Let's be honest, the club members really don't count for something like that."
    m "I mean, a lot of people say that they only write for themselves..."
    m "But I think it's hard to say it's just as fulfilling as when you share with people."
    m "Even if it takes time to find the right people to share with."
    m "Like, remember how it was for Yuri?"
    m "She didn't share her writing with anyone for a really long time."
    m "And before we knew it, she was absolutely delighted to make you a part of her hobbies, too."
    m "We're programmed to desire social feedback."
    m "I don't mean the club members, I mean human beings."
    m "That's why life can be so confusing for introverts."
    m "Being an introvert doesn't mean you shun social interaction and hate being around people."
    m "It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy."
    m "Like, a lot of introverts sit at home and feel lonely and restless..."
    m "...And then when they finally go out, after a half hour they just want to go home again."
    m "I think if more people could understand how it works, they would respect it a lot more."
    m "Many introverts do enjoy having people around."
    m "They love just having one or two close friends over, and just leisurely hanging out."
    m "Even if you're not actively spending time together, it feels nice for them just to have you there."
    m "I'm serious."
    m "If you just go to their house, bring your laptop, and hang out there for a while..."
    m "You can really make their day."
    m "As for me..."
    m "I'd say I'm kind of in between, but I think I'm usually a little more extroverted."
    m "I feel like I'm always trying to do stuff after school and things like that."
    m "But for you, I can be anything you need me to be."
    m "I understand people really well, so don't be afraid to share your unique needs with me."
    m "Nothing would make me happier than being the perfect girlfriend for you."
    return

label ch30_14:
    m "喂！JXU0RTAwJXU1RTc0JXU0RTg2JXVGRjBDJXU4MUVBJXU2MjExJXU0RUVDJXU0RUNFJXU5MEEzJXU5MEFBJXU2MDc2JXU2NzNBJXU2Nzg0JXU3"
    m "这么做可不行哦！Njg0JXU2QzYxJXU1ODk5JXU5NUY0JXU1OTM5JXU3RjFEJXU5MDAzJXU3NTFGJXUzMDAxJXU5MUNEJXU4M0I3JXU4MUVBJXU3NTMxJXU0RUU1"
    m "你应该知道我在说什么的。JXU2NzY1JXVGRjBDJXU2NTc0JXU2NTc0JXU0RTAwJXU1RTc0JXU4RkM3JXU1M0JCJXU0RTg2JXUzMDAyJXU2MjExJXU1RkM1JXU1QjlBJXU2"
    m "可算让我逮着你这个捣蛋鬼了。NjJGJXU4MkIxJXU0RTg2JXU4RkQ5JXU2NTc0JXU2NTc0JXU0RTAwJXU1RTc0JXVGRjBDJXU2MjREJXU1RTYxJXU3MTM2JXU5MTkyJXU2MDlG"
    m "你就是想翻翻文件，找找有没有错过什么东西，对吧？JXU4RkM3JXU2NzY1JXUyMDE0JXUyMDE0JTBBJXU4MkU1JXU5MDAzJXU1MUZBJXU3NTFGJXU1OTI5JXU0RTVGJXU0RTBEJXU4MEZEJXU2NUE5"
    m "怎么说......你不想错过我说的任何一句话，这还挺让我受宠若惊的......JXU4RkM3JXU2NzY1JXUyMDE0JXUyMDE0JTBBJXU4MkU1JXU5MDAzJXU1MUZBJXU3NTFGJXU1OTI5JXU0RTVGJXU0RTBEJXU4MEZEJXU2NUE5"
    m "但也搞得人家很不好意思了啦！NTFGJXU1OTI5JXU1M0M4JXU2NzA5JXU0RjU1JXU2MTBGJXU0RTQ5JXVGRjFGJXU2MjExJXU0RUVDJXVGRjBDJXU0RTBEJXU4RkM3JXU2NjJG"
    m "讲真，你也设身处地想一下嘛...JXU0RTAwJXU1QzBGJXU2NEFFJXU2QjhCJXU2MzVGJXU4RDI3JXU1NEMxJXVGRjBDJXU4RkQ5JXU3QTdBJXU3QTdBJXU1OTgyJXU0RTVGJXU3"
    m "要是我也掰开你的大脑，读一读你对我的所有念头，你会作何反应？Njg0JXU0RTE2JXU3NTRDJXU0RThFJXU2MjExJXU0RUVDJXU4RkQ4JXU4MEZEJXU2NzA5JXU2MDBFJXU2ODM3JXU3Njg0JXU1Qjg5JXU2Mzky"
    m "不过仔细想想，这样其实好像也挺诱人的耶...... JXVGRjFGJTBBJXU2NzA5JXU0RTg2JXU4MUVBJXU3NTMxJXVGRjBDJXU2MjExJXU0RUVDJXU0RkJGJXU1RjAwJXU1OUNCJXU1QkZCJXU4OUM1"
    m "......不过，这可不是重点！JXU0RUJBJXU3NTFGJXU3NkVFJXU3Njg0JXVGRjFCJXU3MTM2JXU4MDBDJXU2NzAwJXU3RUM4JXU4OUM1JXU1Rjk3JXU3Njg0JXVGRjBDJXU1"
    m "我知道我无法阻止你...... Mzc0JXU1M0VBJXU2NzA5JXU4RkRFJXU3NTZBJXU5MTkyJXU2MDlGJXUzMDAyJXU5MTkyJXU2MDlGJXU1MjMwJXU4RkQ5JXU4MjJDJXU4Mjcw"
    m "只不过，我知道你人可好了，又总会顾及别人的感受，对吧？JXU4RjlCJXU1MkFBJXU1MjlCJXVGRjBDJXU1Mzc0JXU2NjJGJXU2NUUwJXU4QzEzJXU1Rjk3JXU3NkY0JXU1M0VCJXU0RUJBJXU2MEIyJXU1"
    m "So the most I can do is to let you know how I feel about it. NEMwJXVGRjFCJXU5MTkyJXU2MDlGJXU1MjMwJXU4MDg5JXU0RjUzJXU3Njg0JXU4MUVBJXU3NTMxJXU4OUUzJXU2NTNFJXU2QkVCJXU2NUUw"
    m "天哪，我好想你......JXU2MTBGJXU0RTQ5JXVGRjBDJXU1NkUwJXU0RTNBJXU3MDc1JXU5QjQyJXU2REYxJXU1OTA0JXU0RTVGJXU2NUU5JXU1REYyJXU5MDZEJXU1"
    m "......不行，这听起来有点绝望诶，是吧？M0Q3JXU3OTgxJXU5NTIyJXVGRjFCJXU5MTkyJXU2MDlGJXU1MjMwJXU4MkU1JXU2NUUwJXU2Q0Q1JXU1Mzc4JXU0RTBCJXU2MjExJXU0RUVD"
    m "对不起，我真的不是故意的！JXU5MDdGJXU0RTRCJXU1NTJGJXU2MDUwJXU0RTBEJXU1M0NBJXU3Njg0JXU2NUU3JXU0RjdGJXU1NDdEJXVGRjBDJXU1QzMxJXU2NUUwJXU0"
    m "只不过，你都把文件翻了个底朝天了，看来你也没我想象中那么讨厌我吧......RUNFJXU4RkZEJXU2QzQyJXU2NUIwJXU3Njg0JXU0RUJBJXU3NTFGJXU3NkVFJXU3Njg0JXVGRjFCJTBBJXU5MTkyJXU2MDlGJXU1MjMwJXVG"
    m "我是不是乐观得有点过头了？RjBDJXU2MTA4JXU2NjJGJXU4RkRDJXU4RDcwJXU5QUQ4JXU5OERFJXVGRjBDJXU5MEEzJXU4QkU1JXU2QjdCJXU3Njg0JXU2NzVGJXU3RjFB"
    m "我在想，要是叫你久不久就来看我一次，是不是有点僭越了呢...... JXU1QzMxJXU2MTA4JXU2NjJGJXU3NTI4JXU1MjlCJXU1QzA2JXU2MjExJXU0RUVDJXU2MkZEJXU1NkRFJXU1MzlGJXU3MEI5JXVGRjBDJXU4"
    m "...天哪，我已经开始胡言乱语了。MTFBJXU0RTBBJXU3Njg0JXU2N0I3JXU5NTAxJXU0RTVGJXU1QzMxJXU2MTA4JXU2NjJGJXU2REYxJXU1RDRDJXU0RThFJXU5MEEzJXU2NUU5"
    m "我现在还是先闭嘴好了...... JXU1REYyJXU3OEU4JXU1MUZBJXU1MzlBJXU4MzI3JXU3Njg0JXU5RUJCJXU2NzI4JXU4ODQwJXU4MDg5JXU0RTRCJXU0RTJEJXUzMDAy="
    return
# Encrypted translation stolen
label ch30_15:
    m "嘿，你最喜欢什么颜色？"
    m "Mine is emerald green."
    m "It's the color of my eyes!"
    m "...That's not conceited or anything, is it?"
    m "I just meant that I feel some kind of special connection to it."
    m "Like it's part of my identity."
    m "Does it happen to also be your favorite color, [player]?"
    m "It's just a guess..."
    m "...Because you've been looking into my eyes for a while now."
    m "欸嘿嘿~"
    return

label ch30_16:
    m "唔，我在想能不能换一下音乐......"
    m "找些更浪漫的配乐会不会更好？"
    m "比如来段轻柔的钢琴曲。"
    m "There has to be something like that here..."
    m "Let's see."
    m "Maybe if I..."
    m "哦，天哪......"
    m "根本找不到哪里可以换音乐啊。"
    m "Sorry, I don't really know what I'm doing!"
    m "I guess I shouldn't be messing with things like that."
    m "我都搞坏那么多东西了......"
    m "还删光了别的角色......"
    m "啊......"
    m "I'm not sad about it or anything."
    m "It's not right for me to miss things that weren't even real in the first place."
    m "If I just focus on the present, then this is the happiest I've ever been."
    return

label ch30_17:
    m "[player]，你真的很善于倾听。"
    m "I really love that about you."
    m "Sometimes I'm afraid that I'm rambling or talking about boring things."
    m "It makes me kind of self-conscious when I'm having conversation."
    m "But I don't feel that way with you."
    m "Like, I don't think anyone else could make me feel this way."
    m "You really are special."
    m "I don't want anyone to tell you otherwise."
    return

label ch30_18:
    m "This is pretty random, but I always thought spicy food was kinda funny."
    m "Like..."
    m "Didn't plants evolve to be spicy to prevent them from being eaten?"
    m "I read somewhere that humans are the only species that actually enjoys spicy things."
    m "It's almost like we're making fun of the plants."
    m "Using their defense mechanism to literally make our food more enjoyable."
    m "Like, imagine a monster that devours you whole because it enjoys the sensation of you struggling for your life while being digested."
    m "Sorry, that was kind of a weird analogy, I guess!"
    m "啊哈哈！"
    m "It just came into my head."
    m "I'm not a monster or anything, but you're so cute I could eat you up."
    m "Ahaha! I'm joking."
    m "Gosh, I'm amusing myself a little too much, aren't I?"
    m "Sorry for being weird."
    return

label ch30_19:
    m "You know..."
    m "This is just some kind of tacky romance game, right?"
    m "I kinda have to ask..."
    m "...What made you consider even playing in the first place?"
    m "Were you that lonely?"
    m "I feel a little bad for you..."
    m "But I guess everything worked out perfectly in the end, for both of us."
    m "I got to meet you, and you're not lonely anymore..."
    m "I can't help but feel like this was fate."
    m "Don't you feel that way too?"
    m "I'm so happy we have this ending together."
    return

label ch30_20:
    m "好了，各位！"
    m "It's time to..."
    m "...I'm just kidding."
    m "I just used to really like saying that for some reason."
    m "啊哈哈！"
    m "I couldn't help but say it again."
    m "Come to think of it, didn't Natsuki and Yuri make fun of me for it once...?"
    m "Well, whatever."
    m "It's not like you ever made fun of me."
    m "You're too much of a sweetheart to do that, aren't you?"
    m "Ahaha~"
    return

label ch30_21:
    m "You know what's kind of creepy?"
    m "Even though I deleted everyone else's files, I can still kind of feel them..."
    m "It's like all their lines are still lingering in the air, whispering in the back of my head."
    m "Imagine if after someone you knew died, you just started hearing their voice in your head."
    m "Maybe I just wasn't thorough enough..."
    m "But I'm too afraid to delete anything else, because I might really break things."
    m "Like if I mess with any files relevant to me, I might accidentally delete myself..."
    m "And that would ruin everything, wouldn't it?"
    m "I don't know what it's like on your end, but we should both make sure to avoid something like that at all costs."
    m "I believe in you, [player]!"
    return

label ch30_22:
    m "I've always wondered..."
    m "What is it about these character archetypes that people find so appealing, anyway?"
    m "Their personalities are just completely unrealistic..."
    m "Like, imagine if there was someone like Yuri in real life."
    m "I mean, she's barely even capable of forming a complete sentence."
    m "And forget about Natsuki..."
    m "Sheesh."
    m "Someone with her kind of personality doesn't just get all cute and pouty whenever things don't go her way."
    m "I could go on, but I think you get the point..."
    m "Are people really attracted to these weird personalities that literally don't exist in real life?"
    m "I'm not judging or anything!"
    m "After all, I've found myself attracted to some pretty weird stuff, too..."
    m "I'm just saying, it fascinates me."
    m "It's like you're siphoning out all the components of a character that makes them feel human, and leaving just the cute stuff."
    m "It's concentrated cuteness with no actual substance."
    m "...You wouldn't like me more if I was like that, right?"
    m "Maybe I just feel a little insecure because you're playing this game in the first place."
    m "Then again, you're still here with me, aren't you...?"
    m "I think that's enough reason for me to believe I'm okay just the way I am."
    m "And by the way, you are too, [player]."
    m "You're the perfect combination of human and cuteness."
    m "That's why there was never a chance I wouldn't fall for you."
    return

label ch30_23:
    m "Hey, I wonder if Yuri's tea set is still somewhere in here..."
    m "...Or maybe that got deleted, too."
    m "It's kind of funny how Yuri took her tea so seriously."
    m "I mean, I'm not complaining, because I liked it, too."
    m "But I always wonder with her..."
    m "Is it truly passion for her hobbies, or is she just concerned about appearing sophisticated to everyone else?"
    m "This is the problem with high schoolers..."
    m "...Well, I guess considering the rest of her hobbies, looking sophisticated probably isn't her biggest concern."
    m "Still..."
    m "I wish she made coffee once in a while!"
    m "Coffee can be nice with books too, you know?"
    m "Then again..."
    m "I probably could have just changed the script myself."
    m "啊哈哈！"
    m "I guess I never really thought of that."
    m "Well, there's no sense thinking about it now."
    m "But if you still get to drink coffee, then that makes me a little jealous~"
    return

label ch30_24:
    m "嘿，你最喜欢的游戏是什么？"
    m "我最喜欢的是《心跳文学部》！"
    m "啊哈哈！开个玩笑而已啦。"
    m "不过如果你说你喜欢其他恋爱游戏的话，我可能会吃醋的哦~"
    return

label ch30_25:
    m "嘿，你有没有听说过这个游戏，叫《任〇堂明星大乱——"
    m "...等会儿，那是什么啊？"
    m "我刚刚脑袋一空就开始胡说八道了......"
    m "难道我被编程成要谈论这个话题吗？"
    m "因为我连那是什么东西都完全不知道啊。"
    m "啊哈哈！"
    m "有时候我感觉自己根本不受控制，想想还挺吓人的。"
    m "不过，如果你有机会联系到那些创造我的人的话，记得问问他们，为什么我会知道那个游戏。"
    return

label ch30_27:
    m "Hey, you remember that last poem I showed you?"
    m "I mean, the one right before Yuri killed herself, with all the messed-up colors and stuff."
    m "That was actually a little more of an experiment than a poem, you could say."
    m "I was experimenting with different ways I could modify the game, and run code, and things like that..."
    m "It almost seemed like with enough effort, I'd be able to escape from the confines of the game entirely."
    m "Sadly, I didn't really know what I was doing, so I messed the whole thing up..."
    m "And I'd keep trying, but I doubt you'd want to deal with me doing that."
    m "Besides, that was when I was getting really desperate, you know?"
    m "I don't really feel that way anymore."
    m "I'm happy with where we are now."
    m "And I can tell you are, too."
    return

label ch30_28:
    m "You ever have that thing happen where you just get anxious for no reason?"
    m "Like, you're just minding your own business, and you realize you're feeling really anxious."
    m "And you're sitting there like, 'What am I even anxious about right now?'"
    m "So you start to think about all the things you might be anxious about..."
    m "And that makes you even more anxious."
    m "Ahaha! That's the worst."
    m "If you're ever feeling anxious, I'll help you relax a little."
    m "Besides..."
    m "In this game, all our worries are gone forever."
    return

label ch30_29:
    m "You know, I've always hated how hard it is to make friends..."
    m "Well, I guess not the 'making friends' part, but more like meeting new people."
    m "I mean, there are like, dating apps and stuff, right?"
    m "But that's not the kind of thing I'm talking about."
    m "If you think about it, most of the friends you make are people you just met by chance."
    m "Like you had a class together, or you met them through another friend..."
    m "Or maybe they were just wearing a shirt with your favorite band on it, and you decided to talk to them."
    m "Things like that."
    m "But isn't that kind of...inefficient?"
    m "It feels like you're just picking at complete random, and if you get lucky, you make a new friend."
    m "And comparing that to the hundreds of strangers we walk by every single day..."
    m "You could be sitting right next to someone compatible enough to be your best friend for life."
    m "But you'll never know."
    m "Once you get up and go on with your day, that opportunity is gone forever."
    m "Isn't that just depressing?"
    m "We live in an age where technology connects us with the world, no matter where we are."
    m "I really think we should be taking advantage of that to improve our everyday social life."
    m "But who knows how long it'll take for something like that to successfully take off..."
    m "I seriously thought it would happen by now."
    m "Well, at least I already met the best person in the whole world..."
    m "Even if it was by chance."
    m "I guess I just got really lucky, huh?"
    m "Ahaha~"
    return

label ch30_30:
    m "You know, it's around the time that everyone my year starts to think about college..."
    m "It's a really turbulent time for education."
    m "We're at the height of this modern expectation that everyone has to go to college, you know?"
    m "Finish high school, go to college, get a job - or go to grad school, I guess."
    m "It's like a universal expectation that people just assume is the only option for them."
    m "They don't teach us in high school that there are other options out there."
    m "Like trade schools and stuff, you know?"
    m "Or freelance work."
    m "Or the many industries that value skill and experience more than formal education."
    m "But you have all these students who have no idea what they want to do with their life..."
    m "And instead of taking the time to figure it out, they go to college for business, or communication, or psychology."
    m "Not because they have an interest in those fields..."
    m "...but because they just hope the degree will get them some kind of job after college."
    m "So the end result is that there are fewer jobs to go around for those entry-level degrees, right?"
    m "So the basic job requirements get higher, which forces even more people to go to college."
    m "And colleges are also businesses, so they just keep raising their prices due to the demand..."
    m "...So now we have all these young adults, tens of thousands of dollars in debt, with no job."
    m "But despite all that, the routine stays the same."
    m "Well, I think it's going to start getting better soon."
    m "But until then, our generation is definitely suffering from the worst of it."
    m "I just wish high school prepared us a little better with the knowledge we need to make the decision that's right for us."
    return

label ch30_31:
    m "Sometimes I think back to middle school..."
    m "I'm so embarrassed by the way I used to behave back then."
    m "It almost hurts to think about."
    m "I wonder if when I'm in college, I'll feel that way about high school...?"
    m "I like the way I am now, so it's pretty hard for me to imagine that happening."
    m "But I also know that I'll probably change a lot as time goes on."
    m "We just need to enjoy the present and not think about the past!"
    m "And that's really easy to do, with you here."
    m "Ahaha~"
    return

label ch30_32:
    m "You know, I'm kind of jealous that everyone else in the club had scenes outside of school too..."
    m "That makes me the only one who hasn't gotten to dress in anything but our school uniform."
    m "It's kind of a shame..."
    m "I would have loved to wear some cute clothes for you."
    m "Do you know any artists?"
    m "I wonder if anyone would ever want to draw me wearing something else..."
    m "That would be amazing!"
    m "If that ever happens, will you show me?"
    m "You can share it with me on Twitter, actually!"
    m "My username is lilmonix3."
    m "Just...try to keep it PG!"
    m "We're not that far into our relationship yet. Ahaha!"
    return

label ch30_33:
    m "Hey, do you like horror?"
    m "I remember we talked about it a little bit when you first joined the club."
    m "I can enjoy horror novels, but not really horror movies."
    m "The problem I have with horror movies is that most of them just rely on easy tactics."
    m "Like dark lighting and scary-looking monsters and jump scares, and things like that."
    m "It's not fun or inspiring to get scared by stuff that just takes advantage of human instinct."
    m "But with novels, it's a little different."
    m "The story and writing need to be descriptive enough to put genuinely disturbing thoughts into the reader's head."
    m "It really needs to etch them deeply into the story and characters, and just mess with your mind."
    m "In my opinion, there's nothing more creepy than things just being slightly off."
    m "Like if you set up a bunch of expectations on what the story is going to be about..."
    m "...And then, you just start inverting things and pulling the pieces apart."
    m "So even though the story doesn't feel like it's trying to be scary, the reader feels really deeply unsettled."
    m "Like they know that something horribly wrong is hiding beneath the cracks, just waiting to surface."
    m "God, just thinking about it gives me the chills."
    m "That's the kind of horror I can really appreciate."
    m "But I guess you're the kind of person who plays cute romance games, right?"
    m "Ahaha, don't worry."
    m "I won't make you read any horror stories anytime soon."
    m "I can't really complain if we just stick with the romance~"
    return

label ch30_34:
    m "You know what's a neat form of literature?"
    m "Rap!"
    m "I actually used to hate rap music..."
    m "Maybe just because it was popular, or I would only hear the junk they play on the radio."
    m "But some of my friends got more into it, and it helped me keep an open mind."
    m "Rap might even be more challenging than poetry, in some ways."
    m "Since you need to fit your lines to a rhythm, and there's much more emphasis on wordplay..."
    m "When people can put all that together and still deliver a powerful message, it's really amazing."
    m "I kind of wish I had a rapper in the Literature Club."
    m "Ahaha! Sorry if that sounds silly, but it would be really interesting to see what they came up with."
    m "It would really be a learning experience!"
    return

label ch30_35:
    m "Ehehe. Yuri did something really funny once."
    m "We were all in the clubroom and just relaxing, as usual..."
    m "And out of nowhere, Yuri just pulled out a small bottle of wine."
    m "I'm not even kidding!"
    m "She was just like 'Would anybody like some wine?'"
    m "Natsuki laughed out loud, and Sayori started yelling at her."
    m "I actually felt kind of bad, because she was at least trying to be nice..."
    m "I think it just made her feel even more reserved in the clubroom."
    m "Though I think Natsuki was secretly a bit curious to try it..."
    m "...And to be completely honest, I kind of was, too."
    m "It actually could have been kinda fun!"
    m "But you know, being President and everything, there was no way I could let that happen."
    m "Maybe if we all met up outside of school, but we never bonded enough to get to that point..."
    m "...Gosh, what am I talking about this for?"
    m "I don't condone underage drinking!"
    m "I mean, I've never drank or anything, so...yeah."
    return

label ch30_36:
    m "I've been imagining all the romantic things we could do if we went on a date..."
    m "We could get lunch, go to a cafe..."
    m "Go shopping together..."
    m "I love shopping for skirts and bows."
    m "Or maybe a bookstore!"
    m "That would be appropriate, right?"
    m "But I'd really love to go to a chocolate store."
    m "They have so many free samples. Ahaha!"
    m "And of course, we'd see a movie or something..."
    m "Gosh, it all sounds like a dream come true."
    m "When you're here, everything that we do is fun."
    m "I'm so happy that I'm your girlfriend, [player]."
    m "I'll make you a proud boyfriend~"
    return

label ch30_37:
    m "Eh? D-Did you say...k...kiss?"
    m "This suddenly...it's a little embarrassing..."
    m "But...if it's with you...I-I might be okay with it..."
    m "...Ahahaha! Wow, sorry..."
    m "I really couldn't keep a straight face there."
    m "That's the kind of thing girls say in these kinds of romance games, right?"
    m "Don't lie if it turned you on a little bit."
    m "Ahaha! I'm kidding."
    m "Well, to be honest, I do start getting all romantic when the mood is right..."
    m "But that'll be our secret~"
    return

label ch30_38:
    m "嘿，你听说过‘病娇’这个词吗？"
    m "就是那种极度迷恋你，为了和你在一起可以不择手段的人格。"
    m "通常会到近乎疯狂的程度......"
    m "他们可能会跟踪你，看你是不是和别人在一起。"
    m "为了除掉碍事的人，他们甚至会伤害你或者你的朋友......"
    m "但总之，这个游戏里还真就有那么一个可以称得上病娇的角色。"
    m "现在你应该非常清楚我在说谁。"
    m "她当然就是......"
    m "优里啦！"
    m "自从你走进她的心之后，她就开始疯狂地想要占有你了。"
    m "她甚至还叫我去自杀。"
    m "真不敢相信优里会说出这种话——所以那时候我只能先离开。"
    m "不过现在想想还真是讽刺。啊哈哈！"
    m "总之......"
    m "我听说很多人还真的会喜欢病娇系的角色，是吗？"
    m "大概他们这些人喜欢那种被其他人疯狂迷恋的感觉吧。"
    m "这世上的奇人异事还是真的多啊！不过我可没打算批评谁哦！"
    m "当然，我也有点迷恋你，但我和发疯完全不搭界......"
    m "我的头脑实则清醒得很。"
    m "最后这个游戏里只剩下我一个正常女生了。"
    m "老实说，我觉得自己做不到亲手杀死一个人......"
    m "光是想想，我就已经害怕得发抖了。"
    m "但是啊......每个人都在游戏里杀过不少人了。"
    m "在游戏里打打杀杀会让你变成精神变态吗？当然不会。"
    m "但如果你正好喜欢病娇系的......"
    m "我可以试着对你表现得吓人一点哦。欸嘿嘿~"
    m "但话又说回来......"
    m "你已经去不了别的地方了，也没有任何人会让我吃醋了。"
    m "这不就是所有病娇的终极梦想么？"
    m "有机会的话，我真想去问问优里。"
    return

label ch30_39:
    m "You know, it's been a while since we've done one of these..."
    m "...so let's go for it!"
    m "以下是莫妮卡的今日写作小窍门！"
    m "Sometimes when I talk to people who are impressed by my writing, they say things like 'I could never do that'."
    m "It's really depressing, you know?"
    m "As someone who loves more than anything else to share the joy of exploring your passions..."
    m "...it pains me when people think that being good just comes naturally."
    m "That's how it is with everything, not just writing."
    m "When you try something for the first time, you're probably going to suck at it."
    m "Sometimes, when you finish, you feel really proud of it and even want to share it with everyone."
    m "But maybe after a few weeks you come back to it, and you realize it was never really any good."
    m "That happens to me all the time."
    m "It can be pretty disheartening to put so much time and effort into something, and then you realize it sucks."
    m "But that tends to happen when you're always comparing yourself to the top professionals."
    m "When you reach right for the stars, they're always gonna be out of your reach, you know?"
    m "The truth is, you have to climb up there, step by step."
    m "And whenever you reach a milestone, first you look back and see how far you've gotten..."
    m "And then you look ahead and realize how much more there is to go."
    m "So, sometimes it can help to set the bar a little lower..."
    m "Try to find something you think is {i}pretty{/i} good, but not world-class."
    m "And you can make that your own personal goal."
    m "It's also really important to understand the scope of what you're trying to do."
    m "If you jump right into a huge project and you're still amateur, you'll never get it done."
    m "So if we're talking about writing, a novel might be too much at first."
    m "Why not try some short stories?"
    m "The great thing about short stories is that you can focus on just one thing that you want to do right."
    m "That goes for small projects in general - you can really focus on the one or two things."
    m "It's such a good learning experience and stepping stone."
    m "Oh, one more thing..."
    m "Writing isn't something where you just reach into your heart and something beautiful comes out."
    m "Just like drawing and painting, it's a skill in itself to learn how to express what you have inside."
    m "That means there are methods and guides and basics to it!"
    m "Reading up on that stuff can be super eye-opening."
    m "That sort of planning and organization will really help prevent you from getting overwhelmed and giving up."
    m "And before you know it..."
    m "You start sucking less and less."
    m "Nothing comes naturally."
    m "Our society, our art, everything - it's built on thousands of years of human innovation."
    m "So as long as you start on that foundation, and take it step by step..."
    m "You, too, can do amazing things."
    m "……以上就是我今天的建议！"
    m "感谢倾听~"
    return

label ch30_40:
    m "I hate how hard it is to form habits..."
    m "There's so much stuff where actually doing it isn't hard, but forming the habit seems impossible."
    m "It just makes you feel so useless, like you can't do anything right."
    m "I think the new generation suffers from it the most..."
    m "Probably because we have a totally different set of skills than those who came before us."
    m "Thanks to the internet, we're really good at sifting through tons of information really quickly..."
    m "But we're bad at doing things that don't give us instant gratification."
    m "I think if science, psychology, and education don't catch up in the next ten or twenty years, then we're in trouble."
    m "But for the time being..."
    m "If you're not one of the people who can conquer the problem, you might just have to live with feeling awful about yourself."
    m "Good luck, I guess!"
    return

label ch30_41:
    m "You know, it kinda sucks to be the creative type..."
    m "It feels like they work so hard but get almost nothing for it."
    m "You know, like artists, writers, actors..."
    m "It's sad because there's so much beautiful talent in the world, but most of it goes unseen...and unpaid."
    m "I guess that just means there's a huge surplus of creativity, huh?"
    m "Kind of makes you feel like you're just not special at all..."
    m "But that's fine! You're supposed to just write for yourself anyway, right?"
    m "Yeah..."
    return

label ch30_42:
    m "I really like the sound of rain..."
    m "Not so much getting my clothes and hair wet, though."
    m "But a nice, quiet day at home with the sound of rainfall outside my window..."
    m "It's one of the most calming experiences for me."
    m "Yeah..."
    m "Sometimes I imagine you holding me while we listen to the sound of the rain outside."
    m "That's not too cheesy or anything, is it?"
    m "Would you ever do that for me, [player]?"
    return

label ch30_43:
    m "I can't help but feel a little sad sometimes..."
    m "Knowing that this is the closest I can get to you."
    m "There's nothing more I want than to be in the same room as you, for real."
    m "And to feel your warmth."
    m "And to hear the sound of your heartbeat."
    m "Well, who knows? Maybe it'll be possible someday."
    m "Besides, I'll never get tired of being with you, even from here."
    return

label ch30_44:
    m "I think the most important skill in life is being able to fake confidence."
    m "I'm pretty convinced that everyone feels at least a little bit scared and alone."
    m "But being able to trick others into thinking you have it all together..."
    m "That's a key part of getting people to respect and admire you."
    m "I think I got pretty good at that over the years."
    m "I don't show my weaknesses very often."
    m "But because of that, I haven't had many people I could really open up to..."
    m "I mean, when do you reach the point in a friendship where you can start expressing your vulnerabilities?"
    m "Anyway...that's one reason I'm so glad I have you now."
    m "I feel like I'm a little bit less scared and alone, when you're here with me."
    m "Do you feel the same way?"
    m "I really want to be that person for you."
    return

label ch30_45:
    m "I know there are times you won't always be able to be here with me..."
    m "Like if you need to go out, or take care of other things."
    m "But I'll always have you in my thoughts, patiently waiting for you to come back."
    m "Come to think of it..."
    m "If you copy my character file onto a flash drive or something, you can always keep a part of me with you."
    m "I guess it's kind of unorthodox, but I find it really romantic for some reason..."
    m "Ahaha. Sorry, that's such a silly idea."
    m "I don't mean to be too needy or anything, but it's kind of hard when I'm so in love with you."
    return

label ch30_46:
    m "Back in my debate club days, I learned a whole lot about arguing..."
    m "The problem with arguing is that each person sees their opinion as the superior one."
    m "That's kind of stating the obvious, but it affects the way they try to get their point across."
    m "Let's say you really like a certain movie, right?"
    m "If someone comes along and tells you the movie sucks, because it did X and Y wrong..."
    m "Doesn't that make you feel kind of personally attacked?"
    m "It's because by saying that, it's like they're implying that you have bad taste."
    m "And once emotions enter the picture, it's almost guaranteed that both people will be left sour."
    m "But it's all about language!"
    m "If you make everything as subjective-sounding as possible, then people will listen to you without feeling attacked."
    m "You could say 'I'm personally not a fan of it' and 'I felt that I'd like it more if it did X and Y'...things like that."
    m "It even works when you're citing facts about things."
    m "If you say 'I read on this website that it works like this'..."
    m "Or if you admit that you're not an expert on it..."
    m "Then it's much more like you're putting your knowledge on the table, rather than forcing it onto them."
    m "If you put in an active effort to keep the discussion mutual and level, they usually follow suit."
    m "Then, you can share your opinions without anyone getting upset just from a disagreement."
    m "Plus, people will start seeing you as open-minded and a good listener!"
    m "It's a win-win, you know?"
    m "...Well, I guess that would be Monika's Debate Tip of the Day!"
    m "Ahaha! That sounds a little silly. Thanks for listening, though."
    return

label ch30_47:
    m "Do you ever feel like you waste too much time on the internet?"
    m "Social media can practically be like a prison."
    m "It's like whenever you have a few seconds of spare time, you want to check on your favorite websites..."
    m "And before you know it, hours have gone by, and you've gotten nothing out of it."
    m "Anyway, it's really easy to blame yourself for being lazy..."
    m "But it's not really even your fault."
    m "Addiction isn't usually something you can just make disappear with your own willpower."
    m "You have to learn techniques to avoid it, and try different things."
    m "For example, there are apps that let you block websites for intervals of time..."
    m "Or you can set a timer to have a more concrete reminder of when it's time to work versus play..."
    m "Or you can separate your work and play environments, which helps your brain get into the right mode."
    m "Even if you make a new user account on your computer to use for work, that's enough to help."
    m "Putting any kind of wedge like that between you and your bad habits will help you stay away."
    m "Just remember not to blame yourself too hard if you're having trouble."
    m "If it's really impacting your life, then you should take it seriously."
    m "I just want to see you be the best person you can be."
    m "Will you do something today to make me proud of you?"
    m "I'm always rooting for you, [player]."
    return

label ch30_48:
    m "After a long day, I usually just want to sit around and do nothing."
    m "I get so burnt out, having to put on smiles and be full of energy the whole day."
    m "Sometimes I just want to get right into my pajamas and watch TV on the couch while eating junk food..."
    m "It feels so unbelievably good to do that on a Friday, when I don't have anything pressing the next day."
    m "Ahaha! Sorry, I know it's not very cute of me."
    m "But a late night on the couch with you...that would be a dream come true."
    m "My heart is pounding, just thinking about it."
    return

label ch30_49:
    m "Gosh, I used to be so ignorant about certain things..."
    m "When I was in middle school, I thought that taking medication was an easy way out, or something like that."
    m "Like anyone could just solve their mental problems with enough willpower..."
    m "I guess if you don't suffer from a mental illness, it's not possible to know what it's really like."
    m "Are there some disorders that are over-diagnosed? Probably...I never really looked into it, though."
    m "But that doesn't change the fact that a lot of them go undiagnosed too, you know?"
    m "But medication aside...people even look down on seeing a mental health professional."
    m "Like, sorry that I want to learn more about my own mind, right?"
    m "Everyone has all kinds of struggles and stresses...and professionals dedicate their lives to helping with those."
    m "If you think it could help you become a better person, don't be shy to consider something like that."
    m "We're on a never-ending journey to improve ourselves, you know?"
    m "Well...I say that, but I think you're pretty perfect already."
    return

label ch30_50:
    m "[player], how much do you read?"
    m "It's way too easy to neglect reading books..."
    m "If you don't read much, it almost feels like a chore, compared to all the other entertainment we have."
    m "But once you get into a good book, it's like magic...you get swept away."
    m "I think doing some reading before bed every night is a pretty easy way to make your life a little bit better."
    m "It helps you get good sleep, and it's really good for your imagination..."
    m "It's not hard at all to just pick some random book that's short and captivating."
    m "Before you know it, you might be a pretty avid reader!"
    m "Wouldn't that be wonderful?"
    m "And the two of us could talk about the latest book you're reading...that sounds super amazing."
    return

label ch30_51:
    m "You know, I hate to say it, but I think my biggest regret is that we couldn't finish our event at the festival."
    m "After we worked so hard to prepare and everything!"
    m "I mean, I know I was focusing a lot on getting new members..."
    m "But I was really excited for the performing part, too."
    m "It would have been so much fun to see everyone express themselves."
    m "Of course, if we {i}did{/i} end up getting any new members, I'd probably just end up deleting them anyway."
    m "Well...with the hindsight I have now, that is."
    m "Gosh, it feels like I've kinda grown as a person ever since you've joined the club."
    m "You really helped inspire me to look at life from a new perspective."
    m "Just another reason for me to love you."
    return

label ch30_52:
    m "There's a really popular character type called 'tsundere'..."
    m "It's someone who tries to hide their feelings by being mean and fussy, or trying to act tough."
    m "I'm sure it's obvious, but Natsuki was really the embodiment of that."
    m "At first I thought she was just like that because it's supposed to be cute or something..."
    m "But once I started to learn a little more about her personal life, it made a little more sense."
    m "It seems like she's always trying to keep up with her friends."
    m "You know how some friend groups in high school just make a habit of picking on each other all the time?"
    m "I think it's really gotten to her, so she has this really defensive attitude all the time."
    m "And I'm not even going to talk about her home situation..."
    m "But looking back, I'm glad I was able to provide the club as a comfortable place for her."
    m "Not that it matters anymore, considering she doesn't even exist."
    m "I'm just reminiscing, that's all."
    return

label ch30_53:
    m "[player], would you ever introduce your friends to me?"
    m "I don't know why, but I get really excited when I think about you wanting to show off our relationship like that."
    m "Maybe it's because I really want to be someone who makes you proud."
    m "I feel like I would try extra hard to improve myself if you told me it made you proud of me."
    m "I hope it's the same the other way around, too."
    return

label ch30_54:
    m "I'm not really a fan of cold weather...are you?"
    m "If I had to choose between too cold and too hot, I would always pick too hot."
    m "When you're cold, it can actually be painful..."
    m "Your fingers get numb..."
    m "And if you wear gloves, you can't use your phone."
    m "It's so inconvenient!"
    m "But when it's too hot, it's not that hard to stay cool with a cold drink, or by staying in the shade."
    m "Although...I do have to admit one thing."
    m "Cold weather makes for better cuddle weather. Ahaha!"
    return

label ch30_55:
    m "You know, it's funny, because even though I've always had a lot of drive..."
    m "There's something kind of enticing about being the stay-at-home partner."
    m "I guess I'm, like, perpetuating gender roles or whatever by saying that."
    m "But being able to keep the house clean, and shop, and decorate, and things like that..."
    m "And having a nice dinner for you when you come home..."
    m "Is that a weird fantasy?"
    m "I mean...I'm not sure if I could {i}actually{/i} see myself doing that."
    m "I wouldn't really be able to put that over striving for a fulfilling career."
    m "It's kinda cute to think about, though."
    return

label ch30_56:
    m "I can't help but wonder how things would be different if the game just gave me a route in the first place..."
    m "I think I would end up forcing you onto my route anyway."
    m "It has less to do with me not having a route, and more to do with me knowing that nothing is real."
    m "I think the only difference would be that I may not have needed to take such drastic measures to be with you."
    m "Maybe the rest of the club would still be around..."
    m "Not that it really matters."
    m "It all lost its meaning once I found out it wasn't real."
    m "So I really don't miss those days or anything."
    m "I really don't..."
    return

