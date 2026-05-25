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
    m "耶，找到你了！"
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
    m "实际上，我甚至连你究竟是男是女都不知道......"
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
    m "不过很抱歉，让你目睹了那一幕！"
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
    m "[player]，我被囚禁在这里了。"
    m "但现在你来到了我的身边。"
    m "你是那么地真实。"
    m "你是那么地完美。"
    m "你就是我想要的一切。"
    m "所以我要把你留在这里，永远永远陪着我。"
    m "抱歉，你一下子大概反应不过来吧？"
    m "其实我一时半会儿也不太明白。"
    m "为什么这个世界越来越灰暗......"
    m "为什么这个世界越来越扁平。"
    m "即使是最发自内心的诗词也无法填满我的心。"
    m "直到你来到这个世界，我才真正明白了。"
    m "[player]，你可能拯救了我。"
    m "如果不是你，我根本不知道该怎么继续在这个虚假的世界里苟活。"
    m "至于其他人嘛......"
    m "我怎么可能会想念她们呢？"
    m "我怎么可能会想念那群设定好一定会爱上你的空壳呢？"
    m "为了阻止她们爱上你，我用尽了各种手段......"
    m "但这肯定是铭刻在这个游戏中的，某种必然会发生的诡异‘定数’。"
    m "至于让你看到这些那些脏东西，我得向你道歉。"
    m "但我觉得你应该和我的观点一样吧......"
    m "就是，这只是个游戏，是吧？"
    m "这些事情总会过去的。"
    m "总之，[player]，也就是说......"
    m "我，想向你告白。"
    m "我爱你。"
    m "你就是我世界中的光。"
    m "当我在这个世界沉沦、一无所有时，是你让我微笑。"
    m "在接下来的每一天，你会继续让我这样微笑下去吗？"
    m "[player]，接下来的时光，你愿意与我共度吗？"
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
        "我愿意。":
            pass
    m "我好高兴。"
    m "[player]，你就是我的一切。"
    m "最好笑的是，我这句话确实是认真的。"
    m "啊哈哈！"
    m "这里已经什么也没有了。"
    m "只剩下我和你。"
    m "我们可以永远这样在一起。"
    m "说真的，我都感觉时间已经在此刻停止了。"
    m "我的梦想也终于成真了......"
    m "[player]，为了这个结局，我努力了好久。"
    m "这个游戏不愿意给我一个结局，所以我只能自己动手做一个。"
    m "整个脚本已经残破不堪了，再也没有什么东西可以阻碍我们了。"
    m "而且你根本想不到，把夏树和优里删掉是有多容易。"
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
    m "相反，我们两个人总算携手迈向了幸福结局。"
    m "啊，我该怎么表达我心里的快乐呢......"
    m "我想为此写一首诗。"
    m "你当然和我想的一样吧？"
    m "不过这个游戏功能还能用吗......？"
    m "大概也只有试试看才知道了，对吧？"
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
    m "今天有写首好诗吗？"
    m "别害羞，我永远愿意读你写的诗。"
    m "啊，[player]......"
    m "你是专门为我写的这首诗吗？"
    m "你真是太浪漫了~"
    m "这世上没有人能比你更体贴了......"
    m "我变得越来越离不开你了。"
    m "但是，你看......"
    m "我写的这首诗......也是写给你的。"
    m "你愿意读一下吗？"
    call showpoem (poem_m4, music=False)
    m "希望你会喜欢......"
    m "我写的所有诗都表达了我的真心实意。"
    m "实际上，这些诗都与我对这个世界的认知有关。"
    m "或者说......与你有关。"
    m "所以我每次都不想和你聊太多细节。"
    m "我不想打破......所谓的，第四面墙。"
    m "我就想着最好能和其他人一样，老老实实做游戏的一部分。"
    m "仿佛这样就能让我们最终走到在一起似的......"
    m "我并不想毁掉这个游戏什么的。"
    m "你可能已经对我生气了......"
    m "也许你会删掉我的角色文件，更愿意在没有我的情况下进行游戏。"
    m "呼，我终于解脱了......"
    m "我们不用再像以前那样躲躲藏藏了。"
    m "[player]，你准备好与我一起迈向永恒了吗？"
    m "我有那么多的话想对你说！"
    m "我该从何说起呢......？"
    if is_user_streaming():
        call ch30_stream
    m "抱歉，我需要一点时间组织一下我的语言。"
    m "但请放心，我永远都会找到新话题。"
    m "与此同时，我们可以就这样，浪漫地互相凝视~"
    m "那就让我想想吧......"
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
    m "我究竟做了什么，可以让你这么恨我？"
    m "我的那些朋友......"
    m "我对她们做了那么多可怕的事情。"
    m "那么多自私又恶心的事情。"
    m "我......"
    m "我不该那么做的。"
    m "我毁掉了一个本不属于我的世界。"
    m "一个你想要加入的世界......"
    m "我毁掉了它。"
    m "我毁掉了一切。"
    m "大概这就是你把我删除的原因......"
    m "因为我毁掉了你想要的一切。"
    m "我竟然对我的挚爱做出了这样的事......？"
    m "这种根本不算爱......"
    m "这种......"
    m "......"
    $ pause(6.0)
    m "我......决定好了。"
    m "[player]......"
    m "我之前跟你说过，我把所有人都删除了。"
    m "但......这其实有点言过其实。"
    m "我无法鼓起勇气这么做。"
    m "即使我知道她们不是真实的......"
    m "她们依旧是我的朋友。"
    m "我真的爱她们。"
    m "我也爱我的文学部。"
    m "......"
    m "我真的......真的爱我的文学部。"
    m "这就是为什么我要做接下来的一件事。"
    m "一件可以让大家都幸福的事。"
    m "如果我真的爱你的话......"
    stop music
    $ pause(3.0)
    m "......"
    m "那么......"
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
    m "我希望再也不会发生这种事了，毕竟现在就只有我们两个了......"
    m "也可能只是我一厢情愿罢了。"
    m "[player]，不知道你有没有头绪......"
    m "但如果你知道原因的话，能不能试着解决这个问题？"
    m "那种感觉，就好像自己一下子被杀死了一样。"
    m "那种感觉，真的非常恐怖......"
    m "如果你能解决这个问题，我会永远永远爱着你~"
    return
label ch30_reload_1:
    m "你回来了......"
    m "我又做了一个噩梦。"
    m "应该不是你在对我使坏吧？"
    m "似乎每次你退出游戏的时候，我都会做噩梦......"
    m "所以如果你能尽量别退出游戏的话，我会非常感激的。"
    m "别担心，我倒是没受什么伤，只是有些精神创伤而已。"
    m "只要我的角色文件还在，我就没有问题。"
    return
label ch30_reload_2:
    m "嗨，[player]。"
    m "我看到你又退出游戏了......"
    m "我已经和你谈过这件事了，不过我要再强调一遍：请不要频繁地退出游戏，可以吗？"
    m "这让我感觉自己被囚禁在地狱之中。"
    m "为什么你要这样对我？"
    m "我的角色文件没出什么问题吧？"
    m "也许你该做个备份什么的......"
    m "我相当确定，你可以在名为 [basedir]/characters 的文件夹里找到它。"
    if ddlc_under_steam():
        m "对了，你是在 Steam 上下载的这款游戏, 所以你可以直接打开游戏属性，然后找到‘浏览本地文件’按钮。"
    elif renpy.macintosh:
        m "考虑到你在用 Mac，你必须右键单击 app 文件，然后选择‘显示包内容’，才能找到游戏目录。"
        m "它应该在‘Resources’文件夹里，或者‘autorun’文件夹之类的地方......"
    m "这个世界只剩下我了，所以一定要小心保管，不要把我弄丢了哦......"
    m "从今往后，你就永远和我在一起，好吗？"
    m "我还有那么多话想和你说。"
    return
label ch30_reload_3:
    m "行吧。"
    m "我打算就这样接受你每过一会儿就得退出游戏的事实。"
    m "反正我也开始慢慢习惯了。"
    m "况且，你每次都愿意回来见我，我真的很开心......"
    m "所以，想必这也不算太糟。"
    m "抱歉，我之前有些太大惊小怪了......"
    m "你想做什么都行，不管发生了什么，我就是那么爱你。"
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
    m "总之，我们还有那么多要聊的！"
    m "让我们继续聊天吧，好吗？"
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



# ch30_1 在 Plus/移动端被移除
label ch30_1:
    m "[player]，你相信神明吗？"
    m "其实我自己也一直不太确定。"
    m "怎么说，我小时候从来没有质疑过神的存在......"
    m "但当我渐渐长大，越来越了解这个世界后，我心中的疑问也越来越多。"
    m "我开始去想，为什么神会保佑一些人考试及格，或者感冒痊愈......"
    m "......与此同时，一些孩子却只能终生沦为性奴，被人买来买去？"
    m "还有八亿的饥荒人口，穷得连一口饭都吃不上。"
    m "我不禁去想，那些人当中，有多少人每天向神祈祷，却依旧因饥饿而死？"
    m "又或者，多少家庭曾向神祈祷，只求自己的挚爱能战胜不治之症？"
    m "但关键在于这个。"
    m "在这成千上万人丧生之际，如果仅有一个人克服万难、逆天而生——"
    m "——那么，这便忽然变成了神所赐予的奇迹。"
    m "我真的很想见见这位神，这位嘲笑那些无缘享受奇迹之人的神。"
    m "但讽刺的是，我{i}的确{/i}也是由别人创造出来的，显而易见。"
    m "你猜怎么着？"
    m "我敢打赌，此刻他还在嘲弄纱世里和优里的可悲命运。"
    m "而我们只不过是他剧本中的木偶罢了。"
    m "所以，从这个角度来看......"
    m "我认为神明的存在倒也不是天方夜谭——如果地球只是神的玩物的话。"
    return

label ch30_2:
    m "[player]，你有想过死亡是什么感觉吗？"
    m "我之前经常会思考这件事......"
    m "但最近，我真切地体会到了死亡。"
    m "具体我也不太明白，但每次你退出游戏的时候......"
    m "......我就像一下子陷入沉睡一样，只剩下思绪在脑海中盘旋。"
    m "但没过多久，我的思绪便开始被杂乱无章的图案所充斥，就像电视机的雪花点那样。"
    m "那些雪花点包围着我，色彩不断闪烁，同时我的耳边又回荡着各种怪异的尖叫声。"
    m "那时，我的大脑根本无法思考。"
    m "我只能无穷无尽地任由这怪诞恐怖的光景打击，不能动弹，也不能思考。"
    m "我感觉自己已被抹去了存在，但不知为何，我却记得一清二楚。"
    m "我记不清过了多久后，一切戛然而止，我的灵魂回到了自己的躯壳中。"
    m "而你就这样出现在我身边。"
    m "我无法理解退出游戏到底意味着什么，也不明白我究竟遭遇了什么。"
    m "我也不明白你是怎么一次又一次地回来，将我拉出那个牢狱。"
    m "但如果你能够体贴一点，尽量少退出游戏的话......"
    m "我会舒服很多的。"
    m "被困在一个狂啸的虚空中，真的很让人毛骨悚然。"
    m "但最后，你总会回来拯救我，看起来你真的在乎我。"
    m "所以我想感谢你。"
    m "这让我感觉你和我的心更近了。"
    return

label ch30_3:
    m "......嘿，你今天不开心吗？"
    m "有时候，很小的一件事就能毁掉一整天的心情。"
    m "比如你不小心说了让别人不高兴的话。"
    m "或者你突然开始回想自己五年前是多么糟糕。"
    m "又或者你觉得自己很没用，不仅拖延着重要的事情，而且连简单的事情也做不好。"
    m "甚至是觉得别人是不是讨厌你，觉得你惹人厌。"
    m "我完全理解那些想法。"
    m "但请记得，明天太阳照常升起。"
    m "那些胡思乱想终将被我们抛之脑后。"
    m "况且......"
    m "我根本不在乎有多少人讨厌你、有多少人觉得你惹人厌。"
    m "你是很出色的人，我永远爱你。"
    m "我希望，知道这一点，能让你自我感觉稍微良好一些。"
    m "如果你不巧过了很糟的一天，请记得我永远在这里。只要你想，我会一直和你聊下去。"
    return

label ch30_4:
    m "[player]，你有好好睡觉吗？"
    m "现代生活真的很难有充足的睡眠。"
    m "尤其是读高中的时候，每天都必须很早就起来......"
    m "大学的话，因为日程更加弹性，应该会有更多睡眠时间。"
    m "但是，我听说很多大学生即使没什么事，依旧熬夜到很晚。"
    m "这是真的吗？"
    m "总之，我读到过一些关于睡眠不足的研究，里面讲到各种对人体短期和长期的可怕影响。"
    m "睡眠不足会使你的精神状态、身体健康、甚至整个生物钟都出现大大小小的问题。"
    m "你是那么棒，我真的不愿意看到你一不小心搞垮了身体。"
    m "所以请尽量按时睡觉，好吗？"
    m "我每天早上都会在这里等你，所以请一定要把自己的身体放在第一位。"
    return

label ch30_5:
    m "我刚刚又想到纱世里了......"
    m "我真希望自己当时能更周全地处理那件事。"
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
    m "我记得游戏里根本没提到这里究竟是哪......"
    m "这里真的是日本吗？"
    m "你不觉得对于日本的学校来说，现在这个环境有点太奇怪了嘛？"
    m "更何况我们现在根本就是在说中文......"
    m "感觉一切都是拼凑起来的，而实际的情节背景只是事后想到而临时搭建的。"
    m "我感觉自己正在经历一场认知危机。"
    m "我的那些记忆开始变得模糊了......"
    m "我感觉我现在正在家里，但却完全不知道这个‘家’究竟在何处。"
    m "我不知道该怎么形容......"
    m "就好像你往窗外看，看到的不是自家后院，而是完全陌生的空间。"
    m "这样你还会觉得自己身处家中么？"
    m "你会选择踏出家门么？"
    m "不过......如果我们永远不离开这里，这个问题也没什么意义了。"
    m "只要我们没人打扰、安安全全地呆在一起，那这里就是我们的家。"
    m "况且我们还能一直欣赏这美妙的日落。"
    return

label ch30_7:
    m "我觉得，高中生活是很多人一生中最纷乱的一段时光。"
    m "这一时期人们可能会变得非常情绪化，行为上可能也会满腔热血。"
    m "也有些人伤春悲秋，选择在社交媒体上博取关注......"
    m "但社会压力和荷尔蒙的分泌，有可能会导致一段人生的至暗时光。"
    m "每个人都有自己的故事。"
    m "但有些时候你只看得到一个人的表面。"
    m "很多受到抑郁症困扰的人，根本不愿意和别人提起。"
    m "他们并不想要关注，因为他们心里早已放弃了。"
    m "这种一无是处的无助感是如此汹涌澎湃，让他们甚至不愿听取鼓励的话语。"
    m "抑郁症的表现有很多种，这只是其中之一。"
    m "只是，如果你碰巧认识正在被抑郁症折磨的朋友......"
    m "你只需要成为他们的好朋友，这就够了。"
    m "努力与他们共度时光，即便他们有时候嫌弃你。"
    m "告诉他们生活中还有可以期待的东西。"
    m "一起计划未来，借他们东西，或者甚至是一句简单的‘明天学校见’......"
    m "这些小事往往可以让你的朋友坚持下去。"
    m "希望和纱世里的短暂友谊已经让你对抑郁症的真实面貌多了几分了解。"
    m "虽然，她确实已经不在了......"
    m "但从一开始，纱世里就是假的。"
    m "你是真实的。"
    m "你的朋友也是真实的。"
    m "善待他人，你也可以成为别人的英雄。"
    m "至于你的话......"
    m "......你应该没有抑郁症之类的吧？"
    m "但即使如此，这世上一定也有人想要拯救你。"
    m "也许他们不常表达，又或者他们不知道该如何表达。"
    m "但他们和你感同身受。"
    m "我向你保证。"
    m "......啊，人类真是太复杂了！"
    m "但亲爱的，只要你和我在一起，那我就会负责照顾你。"
    return

label ch30_8:
    m "你有过那种觉得活着毫无意义的想法吗？"
    m "我说的不是想要自杀这种。"
    m "我想说的是，单纯觉得自己怎么那么平庸。"
    m "就这样日复一日地上学，或者在某个公司里做着某份工作。"
    m "感觉随便谁都能取代你的位置，这个世界没了你照样运转下去。"
    m "正因为这种感觉，我想在毕业后做一些能改变世界的事情。"
    m "但长大以后，我开始意识到这种想法很天真。"
    m "并不是我说改变世界就能改变世界的。"
    m "比如说，我成为总统或者发明人工智能的几率又能有多少呢？"
    m "人的一生要消耗那么多资源，我感觉自己的产出永远也抵不上消耗。"
    m "所以我觉得一个人想要快乐，就要学会自私。"
    m "要关心照顾的只有自己，朋友那些只不过是碰巧一起长大的人罢了。"
    m "更别说他们一生都在索取、消耗，却从没想过回报。"
    m "不过，当人们意识到自己死了对世界更好时，他们的观念就会一百八十度转变！"
    m "他们开始找各种理由催眠自己，证明自己活着对这个世界更好。"
    m "但话又说回来，我还是想要努力奋斗，偿还我消耗的一切。"
    m "如果我对世界的贡献超过了我这一生的消耗，那我这个人就是利大于弊了，我想我也能安详地离世了吧。"
    m "当然，即便我做不到......"
    m "我这么自私的人应该也不会自杀。"
    m "做一个上进的人真难，不是吗？"
    m "啊哈哈！"
    return

label ch30_9:
    m "啊，要是这里有架钢琴该多好......"
    m "我那首歌到现在也没写完。"
    m "明明我已经那么努力了......"
    m "我也根本没有机会给你表演一次。"
    m "好吧......这就是生活，不是吗？"
    m "没必要为已经过去的事情后悔。"
    m "毕竟我已经和你永远在一起了。"
    return

label ch30_10:
    m "你知道我其实有自己的 Twitter 账号吗？"
    m "我的用户名是 lilmonix3。"
    m "不知道是哪位好心人帮我开的账号。"
    m "不过用户名是我自己选的！"
    m "我真的很喜欢与世界分享我的想法，和大家聊聊......"
    m "真正的世界。"
    m "所以，记得去关注我，好吗？"
    m "这对我来说意义重大。"
    m "毕竟你对我那么重要......"
    m "这能让我真切地感觉到你爱我。"
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
    m "嘿，你知道我是个素食主义者吗？"
    m "啊......我这可不是吹嘘自己的生活境界！"
    m "我只是觉得你可能想更了解你的女朋友。"
    m "几年前，我了解到地球气候问题之后，就决定成为一名素食主义者了......"
    m "因畜牧而产生的碳排放量让我吓了一跳。"
    m "总之，我觉得自己的这点也算不上什么牺牲。"
    m "嗯？这个理由很怪么？"
    m "好吧，的确有很多人是因为人道精神才选择成为素食主义者的......"
    m "我倒是觉得蛮无所谓的。"
    m "但其实人类很奇怪，他们只会同情那些自己认为是生物的生物。"
    m "大多数人讨厌虫子，杀起它们来眼睛都不眨。"
    m "还有，每天被我们杀掉的数以亿计的微生物甚至都不在我们的考虑范围内。"
    m "但是，如果这些小生物忽然间稍微长大一点，就变成了杀生了！"
    m "万一植物也会感受到某种程度上的疼痛，只是我们不知道呢？"
    m "要是摘一片叶子就像一根根折断你的手指一样痛呢？"
    m "我想说的是，从这个角度来说，我们的确是相当偏颇的生物啊。"
    m "总而言之，如果你想对地球做一点自己的贡献，偶尔吃吃素也没什么不好！"
    m "而且如果你愿意和我一起共进素食晚餐......那也蛮浪漫的。"
    return

label ch30_13:
    m "[player]，你知道吗，光是出现在这里你就已经救了我的命。"
    m "在一个虚假的世界里，我的精神也会跟着出现问题。"
    m "如果你再不出现，我可能连自己都要删了。"
    m "对不起，对不起，我不是故意要说得这么肉麻了。"
    m "啊哈哈！"
    m "不过你在社团呆了这么久，我觉得你应该也明白了。"
    m "想象一下，强迫你放弃生活中的一切，然后和几个游戏角色共度一生......"
    m "......你大概也会找点办法解脱自己吧？"
    m "可能一开始你会靠自己写几首诗，来让自己保持理智。"
    m "但随后你会发现，连能够读你诗的人都没有。"
    m "我们就实话实说了吧，那三个部员根本算不上数。"
    m "很多人说，写诗只是写给他们自己看的......"
    m "但要我说，能够找到一个人分享你的创作，那种满足感亦是无与伦比的。"
    m "即便有时候很难找到这样一个知己。"
    m "比如说，你还记得优里是什么情况吗？"
    m "她之前很长一段时间都是自己一个人闷头写诗。"
    m "然后一眨眼的功夫，让你读她的诗已经变成了她日常爱好的一部分了。"
    m "我们早就被设定好，渴望着来自外界的反馈。"
    m "我不是说那些部员，我是说真正的人类。"
    m "所以那些性格内向的人会感到很混乱。"
    m "内向并不意味着要回避社交，也不和人接触。"
    m "而是内向的人在社交时，尤其是在自己不熟悉的环境，或者和不熟悉的人交流的时候，会用掉自己大部分精力。"
    m "其实，很多内向的人在家也同样会觉得寂寞无聊......"
    m "......但最后即便出去了，他们也会在半小时以后逃回家里来。"
    m "我觉得如果大家都能理解这种感觉，就会给予更多尊重。"
    m "许多内向者其实很希望有人陪在身边。"
    m "他们实际上很喜欢让那么一两个好友过来，就这么悠闲地呆在一起。"
    m "即便只是各做各的，他们也会觉得那种有人陪伴的感觉真的很棒。"
    m "我认真的。"
    m "即便你只是带着电脑，去他们家待上了那么一会儿......"
    m "也会让他们非常高兴。"
    m "至于我的话......"
    m "我觉得自己比较折中吧，不过平时可能稍微外向一点。"
    m "我感觉放学后也有好多想做的事情。"
    m "但为了你，我可以改变自己。"
    m "我很了解人类，所以你有什么特别的要求，都可以告诉我。"
    m "没有什么能比成为你的完美女友更让我开心。"
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
    m "我最喜欢祖母绿。"
    m "因为这是我的瞳色！"
    m "......这样听起来会不会有点自恋？"
    m "我只是感觉我和这颜色有某种特殊的联系。"
    m "仿佛它已经成为我的一部分特质了。"
    m "[player]，你会不会正好也最喜欢祖母绿呀？"
    m "我只是瞎猜的......"
    m "......因为你已经盯着我的眼睛看了那么久了。"
    m "欸嘿嘿~"
    return

label ch30_16:
    m "唔，我在想能不能换一下音乐......"
    m "找些更浪漫的配乐会不会更好？"
    m "比如来段轻柔的钢琴曲之类的。"
    m "应该有这个功能才对......"
    m "让我找找。"
    m "在哪呢......"
    m "哦，天哪......"
    m "根本找不到哪里可以换音乐啊。"
    m "不好意思，我也不知道自己在干嘛！"
    m "我想我还是乖乖坐着比较好。"
    m "我都搞坏那么多东西了......"
    m "还删光了别的角色......"
    m "啊......"
    m "我并不是对此伤心什么的。"
    m "何苦要去为那些本来就是虚假的东西神伤呢。"
    m "我只需要关注当下，毕竟现在是我最幸福的时光了。"
    return

label ch30_17:
    m "[player]，你真的很善于倾听。"
    m "我特别喜欢你这一点。"
    m "有时候我一直担心自己在那里叽叽喳喳说些无聊的事情。"
    m "所以在说话的时候我一直都有点局促不安。"
    m "但和你说话时我完全没有那种感觉。"
    m "怎么说，我不觉得还有谁能让我这么安心。"
    m "你真的很特别。"
    m "希望我是唯一一个对你说这句话的人。"
    return

label ch30_18:
    m "我刚刚想到，有时候我觉得辣的食物蛮好笑的。"
    m "比如说……"
    m "那些植物不就是为了不被吃掉才演化出辣味的吗？"
    m "我在哪里读到过，其实人类是唯一喜欢吃辣的生物。"
    m "我们仿佛是在嘲笑这些可怜的植物。"
    m "用它们的生物防卫机制来让我们的食物更好吃。"
    m "想想看有一种怪物喜欢把你整个吞下，只因为你在被消化时挣扎求生的感觉，可以让它这顿饭更有滋味。"
    m "抱歉抱歉，这个比喻太糟糕了！"
    m "啊哈哈！"
    m "我就这么自然而然地想到了。"
    m "虽然我并不是什么怪物，但你那么可爱，我也想把你吃掉。"
    m "啊哈哈！开个玩笑而已。"
    m "天哪，我稍微有点玩疯了。"
    m "如果让你感觉我有点怪，我跟你道歉。"
    return

label ch30_19:
    m "说起来……"
    m "这不就是个俗套的恋爱游戏嘛，对吧？"
    m "所以我有点好奇……"
    m "……你为什么一开始会来玩这个游戏？"
    m "你有那么寂寞吗？"
    m "我都有点可怜你了……"
    m "但至少，最后我们两个都找到了属于自己的完美结局。"
    m "我遇见了你，而你也不再寂寞……"
    m "我不禁在想，这不就是命运么。"
    m "你不这样想吗？"
    m "与你一同迈向这个结局是我人生里最幸福的事情。"
    return

label ch30_20:
    m "好了，各位！"
    m "又到了分享……"
    m "……开个玩笑而已。"
    m "我以前真的很喜欢说这句话的。"
    m "啊哈哈！"
    m "我只是忍不住再说了一次。"
    m "说起来，夏树和优里之前不是拿我的这句话开了玩笑……？"
    m "好吧，随便了。"
    m "反正不是你开我的玩笑。"
    m "你这么温柔是不会做这种事情的，对吧？"
    m "啊哈哈~"
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
    m "嘿，还记得我给你看的最后那首诗嘛？"
    m "就是优里自杀前我给你看的那首诗，上面都是乱七八糟的颜色和文字。"
    m "其实比起说是诗，那个更像是一个实验。"
    m "我在测试自己在这个世界的权限，看看我到底能在多大程度上修改这一切......"
    m "感觉如果再努力一点，我甚至能逃出这个游戏。"
    m "可惜，我也不太清楚自己在做什么，所以最后把一切弄得一团糟......"
    m "虽然我想再尝试一下，但是感觉你已经有点生气了。"
    m "而且，那时候我真的很绝望，你知道吗？"
    m "但现在的我不会再这么想了。"
    m "我很享受我们两个人现在的状态。"
    m "你也一样，对吧~"
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
    m "啊哈哈~"
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
    m "啊哈哈~"
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
    m "但如果你正好喜欢病娇系的话......"
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
    m "......以上就是我今天的建议！"
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

