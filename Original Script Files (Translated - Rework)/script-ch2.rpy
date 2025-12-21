

label ch2_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "又一天过去了，已经到了社团活动的时间。"
    "几天下来，我对文学部已经相当适应了。"
    "走进部室，迎接我的又是那熟悉的一幕。"
    show sayori 2x zorder 2 at t11
    s "嗨，[player]~"
    mc "哟，这不纱世里嘛。"
    mc "你今天看起来心情很不错嘛。"
    s 1q "欸嘿嘿~"
    s "我只是还不太习惯看见你出现在社团里，没别的意思。"
    mc "这样啊......"
    mc "...这么小一件事都能让你这么高兴啊。"
    mc "不过似乎你也总是为这种小事开心呢。"
    s 1d "说起来......"
    s "我有点饿了......"
    s "要和我一起去买零食吗？"
    mc "不了，谢谢。"
    s 4h "诶？？"
    s "这、这一点也不像你！！"
    mc "我有我的理由。"
    mc "要不检查下你的钱包吧，纱世里？"
    s 4l "诶、诶？"
    show sayori at s11
    s "为什么......突然要看啊？"
    mc "没有啥原因，真的。"
    mc "我只是想看看。"
    s 1l "啊、啊......"
    show sayori zorder 2 at t11
    "纱世里紧张地拿出了她的零钱包。"
    "她笨拙地摸索着扣子，将钱包打开。"
    "然后，她把钱包倒过来，将里面的东西都倒在桌面上。"
    "掉出来的只有两枚小硬币。"
    s 5a "啊、啊哈哈......"
    mc "我就知道......"
    mc "纱世里，我早就看穿你了。"
    s 5c "这不公平！"
    s "你怎么知道的？"
    mc "很简单。"
    mc "如果你一开始就有足够的钱，来部室之前你肯定就买好零食了。"
    mc "所以，要么就是你不饿，只是想找个借口出去走走......"
    mc "要么就是，你早就花光了所有的钱，然后试图装健忘骗我借钱给你！"
    mc "不过，还有一点......"
    mc "......你就没有不饿的时候！"
    mc "这么一来，就只剩下最后一种可能了！"
    s 4p "呜哇啊啊~！"
    s "我投降好吧！"
    s "别搞得我那么内疚好吧！"
    mc "你要是觉得内疚的话，那就说明你确实应该感到内疚......"
    show yuri 1c zorder 2 at t33
    y "啊哈哈。"
    "优里突然咯咯地笑了起来。"
    show sayori 4g
    mc "诶？"
    "我都没注意到她在听我们说话。"
    "她把脸埋在书里，就跟往常一样。"
    show yuri 3n at h33
    y "啊、啊！"
    y "我刚刚没有在听——！"
    y 3o "只不过是......书里的东西......"
    show sayori zorder 3 at f32
    s 1h "优——里——......"
    s "快让 [player] 借我点钱......"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "这......！"
    y "纱世里，别这样把我牵扯进来啊......"
    y "更何况......"
    y 1k "你应该根据自己的经济能力来买东西......"
    y "而且坦白说，耍这么个小把戏，你的痛苦也算是受到点报应了。"
    show sayori 1b
    mc "......"
    y 3n "啊——！"
    y "我刚刚是不是......"
    y 4c "我、我不是那个意思！！"
    y "我看这本书看得太入迷了......"
    y "唔......"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1r "啊哈哈！"
    s 3x "我真的很挺喜欢你有话直说的样子，优里......"
    s "虽说很少见，但那也是你有趣的一面哦！"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3v "这......"
    y "你怎么会那样想......"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1x "你说的倒也没错啦......"
    s "我做了错事，所以就得接受抱怨。"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "是‘报应’啦......"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1l "反正就那个词啦！"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "难得你会这么说，纱世里......"
    y 1a "我想，我们每个人心中都有只小恶魔，对吧？"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1q "欸嘿嘿......"
    show sayori zorder 2 at t32
    mc "别听她瞎说。"
    mc "纱世里知道她在做什么。"
    mc "别忘了，她在跟我说之前，就已经告诉你们她会把我带到社团来......"
    show sayori zorder 3 at f32
    s 1h "但、但是......！"
    s "你要不是为了小蛋糕，也不会来嘛......"
    s "所以我只好耍点小诡计，骗夏树去做蛋糕了！"
    show sayori zorder 2 at t32
    mc "拜托，对我有点信心好嘛，纱世里。"
    show sayori zorder 3 at f32
    s 1l "欸嘿嘿......"
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p zorder 3 at hf32
    "{i}啪！{/i}"
    hide white
    s 4p "噫呀——！"
    "不知道从哪里冒出来的某个东西冷不丁地打到了纱世里脸上，然后滚到了桌子上。"
    s 4j "嗷......"
    s "什么东西——"
    s 4n "诶？？"
    s "是、是曲奇诶！"
    "真的诶，是一块塑料包装的超大曲奇。"
    "纱世里环顾了一下四周。"
    s 4m "这、这就是奇迹吗？"
    s "一定是因为我受到了报复！"
    show sayori zorder 2 at t32
    mc "是‘报应’啦......"
    show sayori 4n
    show yuri zorder 3 at f33
    y 1u "其实你这个词差不多算是用对了......"
    show yuri zorder 2 at t33
    show natsuki 3z zorder 3 at f31
    n "啊哈哈哈！"
    n "这曲奇{i}本来{/i}就是我打算给你的。"
    n 3d "但我接着又听到你把小蛋糕的事情给说漏嘴了。"
    n "不过能看到你那反应，倒也算是扯平了吧。啊哈哈！"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 4m "夏、夏树！"
    s "你人好好哦！"
    s 4s "我超开心的......"
    "纱世里抱住了曲奇。"
    show sayori zorder 2 at t32
    mc "天哪，你赶紧吃就是了......"
    "纱世里一下子就拆开了包装，大口咬了下去。"
    show sayori zorder 3 at f32
    s 4q "尊好次......"
    show sayori zorder 3 at hf32
    s 4o "唔——！"
    "纱世里突然捂住了嘴。"
    s 4p "我咬到舌头了......"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3a "欸嘿嘿。"
    n "你吃个曲奇还挺一波三折的嘛。"
    "夏树咬了一口自己的曲奇。"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1c "啊，夏树，你这个看上去也很好吃嘛！"
    s "我能尝尝吗？"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "拜托......"
    n "蹭吃的还带挑三拣四啊！"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1h "但你的是巧克力味的......"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4c "是啊，不然你觉得我为啥要给你那块？"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "好吧......"
    s 1q "不过你能把这块分享给我，还是让我很开心。"
    s "诶嘿嘿~"
    show sayori behind natsuki zorder 2 at t21
    "纱世里起身走到夏树身后，伸出双臂搂住了她。"
    n 12c "啊——真是的......"
    n "行啦行啦。"
    "夏树手里还拿着曲奇，便用手肘把纱世里轻轻推开。"
    show sayori 1n at h21
    s "......{i}啊呜。{/i}"
    "纱世里突然弯下身，咬了一口夏树的曲奇。"
    n 1p "{i}喂、喂！！{/i}"
    n "你还真就上嘴抢啊？！"
    s 1q "唔呼呼呼！"
    show sayori at lhide
    hide sayori
    "嘴巴塞得满满的纱世里，快步跑到了安全的地方。"
    show yuri 1c
    "优里和我也笑了起来。"
    show yuri 1a
    show natsuki zorder 3 at f31
    n 1w "天哪！你有时简直跟一小孩差不多诶！"
    n 1h "莫妮卡！你能不能说说纱世里——"
    n 1c "——诶？"
    "夏树看了看四周。"
    "莫妮卡并不在部室。"
    n 4q "呃......"
    n "所以说，莫妮卡去哪了？"
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "好问题......"
    y "她有和你们说今天会晚点来之类的吗？"
    show sayori 1b zorder 3 at f32
    show yuri zorder 2 at t33
    s "没有......"
    show sayori zorder 2 at t32
    mc "啊，我也不知道。"
    show yuri zorder 3 at f33
    y 2l "唔......"
    y "那可有点反常。"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "希望她没事......"
    show sayori zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "她肯定不会有事的。"
    n "她也许只是今天刚好有事要做。"
    n 3t "毕竟她还是蛮受欢迎的......"
    show natsuki zorder 2 at t31
    show sayori 4m zorder 3 at f32
    s "诶？"
    s "你该不会觉得她......"
    s "她交了一个......！"
    show sayori zorder 2 at t32
    show yuri 1a zorder 3 at f33
    y "啊哈哈，那也不奇怪嘛。"
    y "她可能比我们所有人加起来都更有魅力。"
    show yuri zorder 2 at t33
    show sayori 1r zorder 3 at f32
    s "诶嘿嘿，确实是这样......"
    show sayori zorder 2 at t32
    show natsuki 1p zorder 3 at f31
    n "这又是哪跟哪啊喂？！"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "突然，门猛地打开了。"
    show monika 1g at l41
    m "抱歉抱歉！非常抱歉！"
    mc "啊，你终于到了......"
    m "我真不是故意要迟到的......"
    m "希望你们没有在担心我之类的！"
    show sayori 4n zorder 3 at f42
    s "诶？？"
    s "所以莫妮卡最终在社团和男朋友之间选择了社团！"
    s "你的意志力真的很强诶！"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m 1l "什、什么男朋友......？"
    m "你们到底在说什么啊？"
    "莫妮卡疑惑地看向我。"
    show monika zorder 2 at t41
    mc "啊，就当无事发生吧......"
    mc "话说，你是被什么事情耽误了吗？"
    show monika zorder 3 at f41
    m 1e "啊......"
    m "嗯，我今天最后一节课是自习课。"
    m "说实话，我忘了注意时间......"
    m "啊哈哈......"
    show monika zorder 2 at t41
    show natsuki 2c zorder 3 at f43
    n "那也不合理啊。"
    n "你至少应该有听到下课铃吧。"
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1m "那想必是被我练钢琴的声音盖过去了吧......"
    show monika zorder 2 at t41
    show yuri 1e zorder 3 at f44
    y "钢琴......？"
    y "我都不知道你会弹钢琴耶，莫妮卡。"
    show yuri zorder 2 at t44
    show monika zorder 3 at f41
    m 1l "啊，其实也不算会弹......！"
    m "我最近才开始学。"
    m 1m "我一直都蛮想学钢琴的。"
    show monika zorder 2 at t41
    show sayori 4x zorder 3 at f42
    s "很酷诶！"
    s "莫妮卡，弹几首曲子给我们听听吧！"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "这......"
    "莫妮卡看着我说道。"
    m 1a "大概还是等我弹得稍微好点了，再弹给大家听吧。"
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 4q "好耶~！"
    show sayori zorder 2 at t42
    mc "听起来好厉害。"
    mc "我也很期待哦。"
    show monika zorder 3 at f41
    m 1b "是吗？"
    m "这样的话......"
    m "我不会让你失望的，[player]。"
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    show monika 5 zorder 2 at t11
    hide sayori
    hide natsuki
    hide yuri
    "莫妮卡冲我甜甜地笑着。"
    mc "啊......"
    mc "我不是想给你压力什么的！"
    m 1a "啊哈哈，不用担心。"
    m "我最近练习得蛮多的。"
    m "等我准备好之后，有机会的话我会很乐意分享的。"
    mc "这样啊......"
    mc "那么，就祝你好运吧。"
    m 1j "谢谢~！"
    m 1a "话说，我没有错过什么吧？"
    mc "呃......其实没错过什么。"
    show monika zorder 1 at thide
    hide monika
    "我选择不提纱世里的调皮恶作剧。"
    "不过我敢肯定，夏树最后还是会跟她抱怨的。"
    "看起来大家都已经安定下来了。"
    "纱世里竟然已经吃完了整块曲奇。"
    "优里回到了书本前，而夏树也消失在储藏间里了。"



    $ nextscene = get_exclusive_scene(1)
    call expression nextscene



    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "好了，各位！"
    m "我们都已经读完彼此的诗了，对吧？"
    m "我们今天需要商量点别的事，请大家都坐到房间的前面来..."
    show natsuki 3c zorder 3 at f31
    n "是关于学园祭吗？"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "嗯，差不多~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "呃。我们真的非要准备学园祭不可吗？"
    n "我们好像也没办法在短短几天内，拼凑出什么像样的东西来啊。"
    n "可能到头来不仅没办法吸引到新成员，还会让我们自己出丑。"
    show yuri 2g zorder 3 at f33
    show natsuki zorder 2 at t31
    y "我也有这种担心呢。"
    y "临时抱佛脚什么的，我真的不擅长......"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "别想那么多嘛！"
    m "我们就弄得简单点，好吗？"
    m 1a "做一点小装饰，其实也差不多了。"
    m "纱世里已经在做海报了，我也设计了一些能在赏诗会期间分发的诗册。"
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "好吧，这些都很不错......"
    n "但你还是没说清楚，我们到底要在赏诗会上做什么啊。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1d "啊，抱歉！我还以为你已经知道了。"
    m 1b "我们要上台表演！"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3h "表演？"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "表......"
    y 3o "呃，莫妮卡......"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1k "没错！我们要举办一场诗朗诵表演。"
    m 1b "我们每个人都要选一首诗，在赏诗会上朗诵。"
    m "不过最棒的部分是，其他人也有机会上台进行诗朗诵！"
    m 1a "纱世里会在海报上写明这一点，以便有意者提前做好准备。"
    show yuri zorder 2 at t44
    show monika zorder 2 at t43
    show natsuki zorder 2 at t42
    show sayori 4q at l41
    s "诶嘿嘿~"
    "紗世里一直在给海报上色，她把它拿起来给我们看了看。"
    show natsuki 4w zorder 3 at f42
    n "你是在开玩笑吗，莫妮卡？"
    n "你不会......你不会已经把这些海报贴出去了吧？"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1d "诶？是的，我已经贴了......"
    m "你真的觉得这个主意有那么糟吗......？"
    show monika zorder 2 at t43
    show natsuki 1s zorder 3 at f42
    n "好吧，倒也没有。"
    n "这个主意也不算糟。"
    n 1w "但是我可不想参加这个哦！"
    n 1x "我{i}绝不{/i}可能像你说的那样，在一大群人面前表演的！"
    show natsuki zorder 2 at t42
    show yuri zorder 3 at f44
    y 3r "我...我同意夏树！"
    y 3w "我这辈子......也不会......做那样的事情的......"
    "想到这里，优里害怕地摇了摇头。"
    show yuri zorder 2 at t44
    show sayori 1g zorder 3 at f41
    s "各位......"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 1g "纱世里，先别说了......"
    m "我明白她们心里在想什么。"
    m "要知道几天前，夏树和优里还从来没有跟别人分享过她们的诗......"
    m "让她们当着一屋子的人大声朗诵自己的诗，确实要求太高了。"
    m 1r "我好像确实忽略了这一点。"
    m "唉，实在对不起。"
    show monika zorder 2 at t43
    show natsuki 5g zorder 3 at f42
    n "......"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1i "......但是！"
    m "我觉得我们还是应该竭尽全力！"
    m 1d "毕竟这个社团的命运只能靠我们自己。"
    m "如果我们成功举办了赏诗会，并且演出效果不错的话......"
    m 3a "那就会激励别人也这么做！"
    m "表演的人越多，我们就能更好地告诉大家，文学到底是什么！"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "是的!"
    s 1x "文学就是表达出你们的感情......"
    s "挖掘自己的内心......"
    s "发现新的视界......"
    s "然后玩得开心就行了！"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 4b "没错！"
    m "正因如此，我们今天才会相聚在社团里。"
    m 4e "你们难道不想和他人分享吗？"
    m "难道就不想鼓舞其他人，让他们体会到当初引领各位来到这里的那些感受吗？"
    m 1e "我知道你们想的。"
    m "我知道我们都很想。"
    m 1b "而如果我们只需要花上两分钟，站在房间前朗诵一首诗的话......"
    m "......那我相信大家一定可以做到的！"
    show monika 1a zorder 2 at t43
    show natsuki 5s zorder 3 at f42
    n "......"
    show natsuki zorder 2 at t42
    show yuri 4b zorder 3 at f44
    y "......"
    show yuri zorder 2 at t44
    show sayori 1g
    "夏树和优里沉默不语。"
    "纱世里看起来则有些担心。"
    "那想必我是别无选择了......"
    mc "我同意......"
    mc "我不觉得这样的要求很过分。"
    mc "纱世里和莫妮卡一直努力地想吸引新成员。"
    mc "我觉得我们至少该帮她们分担一点。"
    show natsuki zorder 3 at f42
    n 5h "好吧......或许你说的没错，但是......"
    n "......"
    "夏树似乎也没什么可反驳的了。"
    n "唔......"
    n 1q "......那，行吧！"
    n "看来我也只能忍一下了。"
    show natsuki zorder 2 at t42
    show sayori zorder 3 at f41
    s 4r "太好了~！"
    show sayori 4a zorder 2 at t41
    show monika zorder 3 at f43
    m 1e "呼......"
    m "谢谢你，夏树。"
    m "那你呢，优里......？"
    show monika zorder 2 at t43
    show yuri zorder 3 at f44
    y "......"
    "优里郁闷地看着周围其他人满怀期待的脸。"
    y "唉......"
    y "那、那我也别无选择了啊......"
    show yuri zorder 2 at t44
    show sayori zorder 3 at f41
    s 4r "啊哈哈！那就是全员参加咯！"
    s "你最好了，优里~"
    show sayori 4a zorder 2 at t41
    show yuri zorder 3 at f44
    y "这个社团迟早会要了我的命啊......"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 1l "哦，天哪......"
    m 1n "没事的，优里。"
    m "不过话说回来......"
    m 1b "我们还是开始准备赏诗会吧！"
    m "我希望你们每个人都选一首自己的诗。"
    m "我们会在彼此面前进行朗诵练习。"
    show monika 1a zorder 2 at t43
    show natsuki zorder 3 at f42
    n 1p "不、不、不行！！"
    show natsuki zorder 2 at t42
    show yuri 3n zorder 3 at f44
    y "莫妮卡......！"
    y "这太突然了吧......！"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "呃，要是连在社团成员面前朗诵都不敢，又怎么能指望在陌生人面前朗诵呢？"
    show monika zorder 2 at t43
    show yuri 4c zorder 3 at f44
    show natsuki 1o
    y "哦不……"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "别担心。"
    m "我会打头阵，让大家更自在一些。"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "那我能当下一位吗？？"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m "啊哈哈，当然可以。"
    m 2d "这样的话，我看看……"
    "莫妮卡快速翻动笔记本，寻找着她心里想着的那一首诗。"
    "接着她便站在了讲台后面。"
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri
    m 1a "这首诗题为《飞翔的方式》。"
    m 1r "咳咳……"
    show monika 1a
    "莫妮卡开始朗诵她的诗。"
    "她那清晰又自信的声音在整间房内回荡。"
    "不仅如此，她那抑扬顿挫的语调也很质朴清新。"
    "她十分清楚如何将感情投入到自己朗诵的每一行诗句中，给文字带来生气。"
    "她是之前就朗诵过诗篇，还是说她天生就如此在行？"
    "我朝周围看了看。"
    "所有人的视线都放在莫妮卡身上。"
    "纱世里一脸惊讶。"
    "优里脸上带着我不能理解的紧张表情。"
    show monika 1j
    "终于，莫妮卡完成了朗诵。"
    "我们四个都鼓起了掌。"
    "莫妮卡深吸了一口气，微笑了起来。"
    show monika 1a
    show sayori 4m zorder 3 at f33
    s "莫妮卡，你……你的表现好棒啊！"
    show sayori zorder 2 at t33
    show monika zorder 3 at f32
    m 1j "Ahaha, thank you very much."
    m 1a "I was just hoping to set a good example."
    m "Are you ready to go next, Sayori?"
    show monika zorder 2 at t32
    show yuri 2r at l31
    y "I...I'll go next!!"
    show sayori at h33
    s 1n "Uwah! Yuri's fired up all of a sudden!"
    "Yuri clutches a sheet of paper between her hands and stands up."
    "Keeping her head down, she walks quickly over to the podium."
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    show yuri zorder 2 at t11
    hide monika
    hide sayori
    y 2v "This poem is called--!"
    "Yuri anxiously glances at each of us."
    s "You can do it, Yuri..."
    y "It...It's called...{i}Afterimage of a Crimson Eye{/i}."
    "Yuri's voice shakes as she starts reading the poem."
    "Just a moment ago, she practically refused to do this."
    "Why is she suddenly putting in so much effort?"
    show yuri 2l
    "As Yuri gets past the first couple of lines, her voice changes."
    "It's almost like what happens when Yuri gets absorbed into her books."
    "Her quivering words transform into the sharp syllables of a fierce and confident woman."
    "The poem is full of twists and turns in its structure that she enunciates with perfect timing."
    "This must be a rare glimpse into the whirling fire Yuri keeps concealed inside her head...!"
    show yuri 2t
    "Suddenly, she's finished."
    "Everyone is stunned."
    "Yuri snaps back into reality and glances around her, as if she bewildered even herself."
    y 3o "I..."
    "...It's up to me to save this situation."
    "I'm the first to start applauding."
    "Everyone joins me afterward, and we give Yuri the recognition she deserves."
    "It's not that we didn't want to applaud for her."
    "But we were caught so off-guard that we must have forgotten."
    "As we applaud, Yuri holds the poem to her chest and rushes back into her seat."
    show yuri at lhide
    hide yuri
    show monika 1a zorder 2 at t11
    m "Yuri, that was really good."
    m "Thank you for sharing."
    y "..."
    "Looks like Yuri is down for the count..."
    show sayori 1q zorder 2 at t31
    s "Okaay~"
    s "I guess I'm next, then!"
    "Sayori hops out of her chair and cheerfully walks to the podium."
    show sayori zorder 2 at t11
    show monika zorder 1 at thide
    hide monika
    s 1x "This one's called...{i}My Meadow{/i}."
    s "Ah..."
    s 1s "...Ahaha!"
    s 4s "Sorry, I giggled..."
    s 4q "Ehehe..."
    mc "Sayori..."
    s 1l "It's a lot harder than I thought!"
    s "How did you guys do it so easily?"
    show monika 3a zorder 2 at t31
    show sayori 1b
    m "Ah..."
    m "Try not to think of it like you're reciting to other people."
    m "Imagine you're reciting it to yourself, like in front of a mirror, or in your own head."
    m "It's your poem, so it'll come out the best that way."
    show sayori 1i
    s "I see, I see..."
    s "Okay, then..."
    show monika zorder 1 at thide
    hide monika
    show sayori 1c
    "Sayori begins her poem."
    "Somehow, it feels like her soft voice was made as a perfect match."
    "The poem isn't aimlessly cheery like Sayori is."
    "It's serene and bittersweet."
    "If I were to read this on paper, I probably wouldn't think much of it..."
    "But hearing it come from Sayori's voice almost gives it a whole new meaning."
    "Maybe this is what Sayori meant when she said she likes my poems."
    "It's like I get to reach more deeply into someone I thought I knew through and through."
    "Sayori finishes, and we applaud."
    s 3q "I did it~!"
    mc "Good job, Sayori."
    s "Ehehe, even [player] liked it."
    s "I guess that's a good sign~"
    mc "What does that even mean...?"
    show monika 2b zorder 3 at f31
    m "It came out nicely, Sayori."
    m "The atmosphere of the poem fits you really nicely."
    m "But it might be that other poems wouldn't work quite as well with that kind of delivery..."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "Eh? I don't really understand..."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "In other words, I've seen poems of yours where that sort of gentle delivery wouldn't work as well."
    m "They might need a little more force behind them, depending on what you're reading..."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1x "Oh, I know what you mean!"
    s "That's...well, I've been practicing that kind of thing..."
    s 5 "It's just embarrassing to do in front of everyone..."
    s "Ehehe..."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 4a "Then next time, I'm going to make you pick a poem that challenges you a little more."
    m "We don't have much time before the festival, you know?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "Okaaaaay."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Now, who's next...?"
    m "Natsuki?"
    show natsuki 5s zorder 3 at f33
    show monika zorder 2 at t31
    n "Hmph."
    n "Don't make me go before [player]."
    n "It's not like I can compare to you guys, anyway..."
    n "Might as well let [player] lower everyone's standards a little before I have to do it."
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "Natsuki..."
    show sayori zorder 2 at t32
    mc "It's fine, it's fine."
    mc "I might as well get it over with."
    mc "But it's not like I have much of a selection of what to read..."
    mc "I'll just have to go with what I wrote for today."
    "I stand up and step in front of the podium."
    show natsuki 2c zorder 2 at t44
    show sayori 1a zorder 2 at t43
    show monika 1a zorder 2 at t42
    show yuri 1e zorder 2 at t41
    "Everyone has their eyes on me, making me feel terribly awkward."
    "I recite my poem."
    "Since I'm not exactly confident in my own writing, it's hard to put energy into it."
    "Despite that, once I finish, I receive applause anyway."
    mc "Sorry I'm not really as good as everyone else..."
    show monika zorder 3 at f42
    m 1a "Don't worry about it so much."
    m "I think it's less about your abilities, and more about your lack of confidence in your writing."
    m "That's something that'll improve over time, though."
    show monika zorder 2 at t42
    mc "Yeah... Maybe."
    show monika zorder 3 at f42
    m 1j "Alright, then!"
    m 1a "That just leaves you, Natsuki."
    show monika zorder 2 at t42
    show natsuki zorder 3 at f44
    n 2g "Yeah, yeah."
    n "I'm going."
    "Natsuki begrudgingly gets out of her seat and makes her way to the podium."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 2 at t11
    hide sayori
    hide monika
    hide yuri
    n 2c "The poem is called..."
    n 2q "It's called..."
    n 1x "W-Why are you all looking at me?!"
    m "Because you're presenting..."
    n 2x "Hmph..."
    n 2h "Anyway...the poem is called {i}Jump{/i}."
    "Natsuki takes a breath."
    show natsuki 2c
    "Once she starts reciting the poem, her sour attitude disappears a little."
    "While she's still a little unenthused, her poem has a rhythm and rhyme to it."
    "It's Natsuki's trademark style, and it works surprisingly well when spoken aloud."
    "The words feel like they bounce up and down, as if giving life to the poem."
    show natsuki 2s
    "Natsuki finishes, and everyone applauds."
    "She huffs back to her seat."
    show monika 2a zorder 3 at f31
    m "That wasn't so bad, was it?"
    show monika zorder 2 at t31
    show natsuki 5w zorder 3 at f32
    n "Easy for you to say..."
    n "You'd better not make me do that again."
    show natsuki zorder 2 at t32
    show monika 1d zorder 3 at f31
    m "Ah, well..."
    m "Do you at least feel prepared enough to recite a poem in front of other people?"
    show monika zorder 2 at t31
    show natsuki 2c zorder 3 at f32
    n "I mean, doing it in front of other people will be way easier!"
    n "I can put on whatever face I want for other people."
    n 2q "But when it's just my friends..."
    n "It's just...embarrassing."
    show natsuki zorder 2 at t32
    show sayori 1b zorder 3 at f33
    s "That's a surprise, Natsuki..."
    s "I think it would be the other way around for me."
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f32
    n "Well, that's just how it is, so..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Well, I guess in that case..."
    m "You won't have much to worry about for the festival."
    m 2b "That said, I want to thank everyone for coming through."
    m "It might be hard, but I hope that you all have an idea of what it's like now."
    m 4b "Make sure you pick a poem and get enough practice before the festival, okay?"
    m "I'll be making pamphlets, so let me know ahead of time what you'll be reciting."
    show monika zorder 2 at t31
    mc "Jeez..."
    mc "I should probably find some other poem to recite instead."
    show monika zorder 3 at f31
    m 1j "That's fine, too!"
    m 1a "It doesn't have to be your own."
    m "I'm already pleasantly surprised that you're putting in all this effort for the club."
    m 5 "It makes me really happy."
    show monika zorder 2 at t31
    mc "Ah... Yeah, no problem..."
    play music t8 fadeout 1.0
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    hide sayori
    hide natsuki
    m 4b "Okay, everyone!"
    m "I think that's about it for today."
    m "I know the festival is coming up, but let's try to write poems for tomorrow, as well."
    m "It's been working out really nicely so far, so I'd like to continue that."
    m "As for the festival, we'll finish planning tomorrow, and then we'll have the weekend to prepare."
    m "Monday's the big day!"
    show sayori 4r zorder 2 at t31
    s "I can't wait~!"
    show yuri 4b zorder 2 at t33
    y "I can do this... I can do this..."
    mc "Alright--"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "I stand up."
    "There's no way I'll be able to find the same enthusiasm as Sayori and Monika, but I'll do my best to get through it."
    "If it's for the sake of the club..."
    "And impressing Monika..."
    "Then I'll have to do my best."
    show sayori 1a zorder 2 at t32
    mc "Ready to go, Sayori?"
    show sayori at h32
    s 1x "Yep!"
    show natsuki 2d zorder 3 at f33
    n "Look at you two, always going home together like that."
    show monika 5 zorder 3 at f31
    show natsuki zorder 2 at t33
    m "It's kind of adorable, isn't it?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "Ehehe~"
    show sayori zorder 2 at t32
    mc "Jeez, guys..."
    mc "Don't make such a big deal out of it."
    show natsuki zorder 2 at t44
    show sayori zorder 2 at t43
    show monika zorder 2 at t42
    show yuri 1u zorder 3 at f41
    y "It must be a little nice, though..."
    show yuri zorder 2 at t41
    mc "Well..."
    mc "Ah..."
    "How am I supposed to respond to that?"
    show sayori zorder 3 at f43
    s 1d "It's okay, [player], you don't have to say it."
    show sayori zorder 2 at t43
    mc "...Whatever. Let's go already."
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori" or ch2_winner == "Yuri":
        $ ch2_winner = "优里"
    elif ch2_winner == "Natsuki":
        $ ch2_winner = "夏树"

    "I walk home with Sayori once more."
    "Even though it's only been a few days, a lot of things have already changed."
    "But today, Sayori is being a little quieter than usual on the way home."
    mc "Hey, Sayori..."
    show sayori 1k at t11
    s "..."
    s 1n "...Sorry! I was spacing out!"
    mc "Ah, no wonder..."
    s 1d "Um..."
    s "I was...thinking about something from earlier."
    s "I like how we get to..."
    s 1y "I-I mean..."
    "Sayori fumbles with her words."
    s 1a "So...let's just say that one day, [ch2_winner] asked to walk home with you..."
    mc "Huh?!"
    s "What would you do?"
    mc "What kind of question is that...?"
    mc "You're kind of putting me on the spot here..."
    s 1y "Ehehe..."
    menu:
        "Well..."
        "I would walk home with [ch2_winner].":
            if ch2_winner == "夏树":
                call ch2_end_natsuki
            else:
                call ch2_end_yuri
        "I would still walk home with Sayori.":
            call ch2_end_sayori

    "Then again, the festival is only a few days away..."
    "Who knows what will happen in that time?"
    return
label ch2_end_sayori:
    mc "Sayori..."
    mc "You really think I would ditch you for [ch2_winner]?"
    s 1e "Eh?!"
    s "B-But..."
    if ch2_winner == "夏树":
        s "She's so cute and fun to be around..."
    else:
        s "She's so beautiful and smart..."
    mc "Jeez..."
    mc "I already see her in the club every day."
    mc "Besides, you always seem to really like going home together..."
    mc "I wouldn't just ruin that for you."
    s 1y "You're so silly, [player]..."
    s "You think about me too much sometimes."
    s "[ch2_winner] would deserve it if she wanted it, so..."
    mc "Sayori, I've already made up my mind."
    mc "I really can't figure you out sometimes..."
    s "Sorry..."
    mc "Besides, what's the point in speculating something that's never going to happen?"
    s 1k "Hm..."
    show sayori at thide
    hide sayori
    "The conversation trails off."
    "It's kind of a weird thing for Sayori to care so much about..."
    "But I want to respect her and keep her happy, too."
    return

label ch2_end_natsuki:
    mc "Walking home with Natsuki, huh..."
    "Why does the thought of that make my heart pound...?"
    mc "I mean..."
    mc "I think I would be afraid of what she'd do to me if I turned her down..."
    s 1x "Isn't she so cute and fun to be around?"
    jump ch2_end_shared

label ch2_end_yuri:
    mc "Walking home with Yuri, huh..."
    "Why does the thought of that make my heart pound...?"
    mc "I mean..."
    mc "Given how hard it is for her to socialize, I would feel awful turning her down, so..."
    s 1x "Isn't she so beautiful and smart?"
    jump ch2_end_shared

label ch2_end_shared:
    mc "That has nothing to do with what I just said!"
    s 4s "Ahaha! You admitted it!"
    mc "Jeez..."
    mc "There's not even any point in speculating something that's never going to happen."
    s 1d "Well, maybe..."
    s "But I just like to think about it."
    s 1y "It's not long before you won't need me anymore, you know?"
    mc "Need you...?"
    mc "Sayori..."
    mc "I can't figure out how you're seeing things in your head right now."
    s "Sorry..."
    mc "Everyone is different..."
    mc "Nobody in the club is a replacement for you."
    s 1k "Hmm..."
    s "If you say so..."
    show sayori at thide
    hide sayori
    "The conversation trails off, and I'm left feeling awkward."
    "But it was kind of her fault for trapping me with such a weird question..."
    "I can't just lie to her."
    "But if there's something that makes her happy, I would hate to take that away from her."
    "That's why I said there's no point in speculating."
    return

