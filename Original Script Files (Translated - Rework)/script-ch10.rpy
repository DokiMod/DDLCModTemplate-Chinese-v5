label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)
    "我看见一个吵吵闹闹的女孩从远处朝我跑来，一边猛挥着手，仿佛完全意识不到这样会引来全世界的注意。"
    "她叫[s_name]，我的邻居，也是我的儿时玩伴。"
    "怎么说，换做现在，我大概不会想跟她交朋友。但是，因为和她相识太久，我们就自然而然地合拍了。"
    "我们以前经常这样结伴上学，但上了高中以后，她睡过头的频率就越来越高，我也就有点懒得等她了。"
    "每当她像这样狂追不舍的时候，我还真的有点想一走了之。"
    "然而我也别无选择，只是叹了口气，在路口等着，好让[s_name]赶上我。"

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat
    $ renpy.save_persistent()

    jump ch20_from_ch10

