label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_characters()
    s "喂！！等等我！！！"
    "我看见一个吵吵闹闹的女孩挥着手从远处朝我跑来，仿佛完全意识不到这样会引来全世界的注意。"
    "她叫纱世里，我的邻居，也是我儿时的玩伴。"
    "怎么说，换做现在，我大概不会想跟她交朋友。但是你能理解那种，因为相识太久而不知怎的就逐渐生出友谊的感觉吗？"
    "我们以前经常这样结伴上学，但上了高中以后，她睡过头的频率就越来越高，我也就有点懒得等她了。"
    "但她要是像这样狂追不舍的话，我还真的有点想一走了之。"
    "然而我只是叹了口气，在路口等着，好让纱世里赶上我。"
    $ s_name = "纱世里"
    show sayori 4p zorder 2 at t11
    s 4p "哈啊......哈啊......"
    s "我怎么又睡过头了！"
    s "但是！这次我追上你了哦！"
    mc "也许如此，但这只是因为我决定停下来等你而已。"
    show sayori at s11
    s 5c "欸——？你这话说得好像是想抛下我的样子呢！"
    s "[player]，你好坏哦！"
    mc "毕竟我可不想让路人在看到你这番奇怪行为后，把我和你当成笨蛋情侣之类的。"
    show sayori zorder 2 at t11
    s 1a "好吧，好吧。"
    s "但你最后也确实等了我嘛。"
    s "想必，即使你心里想使坏，你本质上也还是个温柔的人嘛~"
    mc "随你吧，纱世里，你高兴就好......"
    s 1q "欸嘿嘿~"
    show sayori zorder 1 at thide
    hide sayori
    "我们穿过马路，继续向学校走去。"
    "逐渐接近学校，路上熙熙攘攘的学生也愈发挤满了街道。"
    show sayori 3a zorder 2 at t11
    s "话说回来，[player]......"
    s "你决定好加入什么社团了吗？"
    mc "社团？"
    mc "我早就跟你说过了，我对社团活动没兴趣。"
    mc "我更是连学校有什么社团都没找过。"
    show sayori at s11
    s 4h "欸？你骗人的吧？！"
    s "你跟我说过今年你要参加社团的！"
    mc "有吗......？"
    "也许我真有可能说过这话，不过大概是为了应付她不断跳跃的话题，然后就随口附和了。"
    "纱世里有点太过于担心我了，我倒是挺满足的。平平淡淡的生活，闲暇时间就沉浸在动画和游戏里。"
    s 4j "嗯哼？但是！"
    s "我刚刚还在说呢，我很担心你上大学前还搞不清楚怎么和人打交道，而且你没有什么特长。"
    s "我真的很在乎你过得开不开心啊！"
    s "我知道你现在这么过日子还挺开心的，但一想到过几年你就会变成一个完全融入不了社会的废宅，我害怕得连想死的心都有了！"
    s 4g "你会相信我的吧？"
    s "真别让我一直担心你啦......"
    mc "行吧，行吧......"
    mc "我会去一些社团转转，这样你大概会开心吧。"
    mc "当然，我可不保证我一定会加入什么社团。"
    s 1h "那你至少答应我去浅浅地试一下吧？"
    mc "好吧，这个我可以保证。"
    show sayori zorder 2 at t11
    s 4r "好耶~！"
    "我怎么就任由自己被这么一个无忧无虑的女孩给说教了呢？"
    "不仅如此，更吓人的是，在她面前我却一点也强硬不起来，只能乖乖听任她的安排。"
    "我猜是看到她这么担心后，最起码想让她轻松一点吧 —— 毕竟她肯定是过度紧张了。"

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "Sayori wants me to check out some clubs."
    "I guess I have no choice but to start with the anime club..."

    s "Hellooo?"
    show sayori 1b zorder 2 at t11
    mc "Sayori...?"
    "Sayori must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    s 1a "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    s 1y "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    s 1a "Well, that you could come to my club!"
    mc "Sayori..."
    s 4r "Yeah??"
    mc "...There is no way I'm going to your club."
    show sayori at s11
    s 5d "Eeeehhhhh?! Meanie!"
    "Sayori is vice president of the Literature Club."
    "Not that I was ever aware that she had any interest in literature."
    "In fact, I'm 99%% sure she only did it because she thought it would be fun to help start a new club."
    "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
    "That said, my interest in literature is guaranteed to be even less."
    mc "Yeah. I'm going to the anime club."
    show sayori zorder 2 at t11
    s 1g "C'mon, please?"
    mc "Why do you care so much, anyway?"
    s 5b "Well..."
    s "I kind of told the club yesterday I would bring in a new member..."
    s "And Natsuki made cupcakes and everything..."
    s "Ehehe..."
    mc "Don't make promises you can't keep!"
    "I can't tell if Sayori is really that much of an airhead, or if she's so cunning as to have planned all of this out."
    "I let out a long sigh."
    mc "Fine... I'll stop by for a cupcake, okay?"
    show sayori at h11
    s 4r "Yes! Let's go~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I sold my soul for a cupcake."
    "I dejectedly follow Sayori across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Sayori, full of energy, swings open the classroom door."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a 'new member--'"
    show sayori at lhide
    hide sayori
    "Eh? I glance around the room."
    show yuri 1a zorder 2 at t11
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Sayori always says nice things about you."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show monika 1a
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "What are you looking at?"
    n "If you want to say something, say it."
    mc "S-Sorry..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "Hmph."
    show natsuki zorder 2 at t32

    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    "She is also the one who made cupcakes, according to Sayori."

    show sayori 2q zorder 3 at f31
    s "You can just ignore her when she gets moody~"
    "Sayori says that quietly into my ear, then turns back toward the other girls."
    s 1x "Anyway! This is Natsuki, always full of energy."
    s "And this is Yuri, the smartest in the club!"
    $ y_name = 'Yuri'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "D-Don't say things like that..."
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Sayori and Natsuki."
    show yuri zorder 2 at t33
    mc "Ah... Well, it's nice to meet both of you."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "And it sounds like you already know Monika, is that right?"
    $ m_name = 'Monika'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "That's right."
    m "It's great to see you again, [player]."
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    mc "Y-You too, Monika."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Monika."
    s "I'll get the cupcakes~"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "Hey! I made them, I'll get them!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "Sorry, I got a little too excited~"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "Then, how about I make some tea as well?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "As Sayori mentioned, it's been widened so that there is one space next to Monika and one space next to Sayori."
    "Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet."
    "Still feeling awkward, I take a seat next to Sayori."
    "Natsuki proudly marches back to the table, tray in hand."
    show natsuki 2z zorder 2 at t32
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "Uwooooah!"
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show sayori zorder 3 at f31
    s 4r "So cuuuute~!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "I had no idea you were so good at baking, Natsuki!"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Monika. I follow."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "It's delicious!"
    "Sayori talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "Natsuki is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-Why are you thanking me? It's not like I...!"
    "{i}(Haven't I heard this somewhere before...?){/i}"
    show natsuki at s32
    n 5s "...Made them for you or anything."
    mc "Eh? I thought you technically did. Sayori said--"
    show natsuki zorder 2 at t32
    n 12c "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    mc "Alright, alright..."
    show natsuki zorder 1 at thide
    hide natsuki
    "I give up on Natsuki's weird logic and dismiss the conversation."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show yuri 1a zorder 2 at t21
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show monika 4a zorder 2 at t22
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show yuri at h21
    y 3n "Eh?! T-That's not..."
    "Insulted, Yuri looks away."
    y 4b "I meant that, you know..."
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    y 2u "I'm glad..."
    "Yuri faintly smiles to herself in relief."
    "Monika raises an eyebrow, then smiles at me."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "So, what made you consider the Literature Club?"
    mc "Um..."
    "I was afraid of this question."
    "Something tells me I shouldn't tell Monika that I was practically dragged here by Sayori."
    mc "Well, I haven't joined any clubs yet, and Sayori seemed really happy here, so..."
    m 1j "That's okay! Don't be embarrassed!"
    m 1b "We'll make sure you feel right at home, okay?"
    m "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    show monika 1a
    mc "Monika, I'm surprised."
    mc "How come you decided to start your own club?"
    mc "You could probably be a board member for any of the major clubs."
    mc "Weren't you a leader of the debate club last year?"
    m 5 "Ahaha, well, you know..."
    m "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    m 1b "And if it encourages others to get into literature, then I'm fulfilling that dream!"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "Monika really is a great leader!"
    show yuri 1 zorder 2 at t33
    "Yuri also nods in agreement."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "Then I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m 2k "I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "Yeah!"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "We'll do our best."
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "You know it!"
    "Everyone enthusiastically agrees."
    "Such different girls, all interested in the same goal..."
    "Monika must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't really know if I can keep up with their level of enthusiasm about literature..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c zorder 2 at t41
    "Natsuki's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1d zorder 3 at f33
    m "Really? I wouldn't have expected that, Yuri."
    m "For someone as gentle as you..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "I guess you could say that."
    y "But if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Ugh, I hate horror..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "Oh? Why's that?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "W-What?"
    n "What gives you that idea?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Fine, fine~"
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "Ehehe, your cupcakes, your poems..."
    s "Everything you do is just as cute as you are~"
    show sayori behind natsuki at t21
    "Sayori sidles up behind Natsuki and puts her hands on her shoulders."
    show natsuki at h42
    n 1v "{i}I'm not cute!!{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "Natsuki, you write your own poems?"
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"
    show yuri 2f zorder 2 at t31
    y "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s31
    y 3o "..."
    mc "I guess it's the same for Yuri..."
    show sayori 2g zorder 2 at t32
    s "Aww... I wanted to read everyone's poems..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "We all sit in silence for a moment."
    show monika 5a zorder 3 at f32
    m "Okay!"
    m "I have an idea, everyone~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "U-Um..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "..."
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "Yeaaah! Let's do it!"
    show monika zorder 3 at f43
    m 1a "Plus, now that we have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of the club."
    m "Isn't that right, [player]?"
    show monika zorder 2 at t43
    "Monika smiles warmly at me once again."
    mc "Hold on...there's still one problem."
    show monika zorder 3 at f43
    m 1d "Eh? What's that?"
    "Now that we're back to the original topic of me joining the club, I bluntly come forth with what's been on my mind the entire time."
    show monika zorder 2 at t43
    mc "I never said I would join this club!"
    mc "Sayori may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "I lose my train of thought."
    "All four girls stare back at me with dejected eyes."
    show monika at s43
    m 1p "B-But..."
    show yuri at s42
    y 2v "I'm sorry, I thought..."
    show natsuki at s44
    n 5s "Hmph."
    show sayori at s41
    s 1k "[player]..."
    mc "Y-You all..."
    "I...I'm defenseless against these girls."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "That is, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "One by one, the girls' eyes light up."
    show sayori at h41
    s 4r "Yesss! I'm so happyyy~"
    "Sayori wraps her arms around me, jumping up and down."
    mc "H-Hey--"
    show yuri zorder 3 at f42
    y 1m "You really did scare me for a moment..."
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "If you really just came for the cupcakes, I would be super pissed."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show monika zorder 2 at t43
    mc "Ah...thanks, I guess."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika zorder 1 at thide
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri and Natsuki clean up their food."
    show sayori 1a zorder 2 at t11
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I never walk home together anymore because she always stayed after school for clubs."
    mc "Sure, might as well."
    s 4q "Yaay~"

    scene bg residential_day
    with wipeleft_scene

    "With that, the two of us depart the clubroom and make our way home."
    "The whole way, my mind wanders back and forth between the four girls:"
    show sayori 1 zorder 2 at t41
    "Sayori,"
    show natsuki 4 zorder 2 at t42
    "Natsuki,"
    show yuri 1 zorder 2 at t43
    "Yuri,"
    show monika 1 zorder 2 at t44
    "and, of course, Monika."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "W-What..."
    s 1g "..."
    s "This..."
    s "What is this...?"
    s "Oh no..."
    s 1u "No..."
    s "This can't be it."
    s "This can't be all there is."
    s 4w "What is this?"
    s "What am I?"
    s "Make it stop!"
    s "PLEASE MAKE IT STOP!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return

