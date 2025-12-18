# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the Python code for displaying poems in DDLC.

# The logic for displaying poems has been changed drastically compared to the original
# game to allow for more poem management.
# It also follows the Ren'Py approach of using the new `_ren.py` file for Python code.

# For the poem display code, see `poems.rpy` in the `poem_responses` directory.

## This import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import re
import typing
from game.definitions.py.core_ren import pause, persistent, store
import renpy  # type: ignore

"""renpy
init python:
"""


class PoemAuthor(object):
    """
    A class used to represent a DDLC character's poem author.
    """

    def __init__(
        self,
        name: str,
        style: bool | str = True,
        paper: str = "images/bg/poem.jpg",
        separate_title_from_text: bool = True,
        music: str | None = None,
    ):
        """
        Initializes the poem author with the given parameters.

        :param name: The name of the poem author.
        :param style: Whether to apply a specific style to the poem.
        :param paper: The background image for the poem.
        :param separate_title_from_text: Whether to separate the title from the text.
        :param music: The music to play during the poem.

        :type name: str
        :type style: bool
        :type paper: str
        :type separate_title_from_text: bool
        :type music: str | None
        """
        self.name = name
        self.style = style
        self.paper = paper
        self.separate_title_from_text = separate_title_from_text
        self.music = music


class Poem(renpy.text.text.Text):
    """
    A class used to represent a DDLC character's poem.
    """

    def __init__(
        self,
        author: PoemAuthor | str,
        text: str = "",
        title: str = "",
        style: bool | str = True,
        paper: str = "images/bg/poem.jpg",
        separate_title_from_text: bool = True,
        music: str | None = None,
        **properties,
    ):
        """
        Initializes the poem with the given parameters.

        :param author: The author of the poem.
        :param text: The text of the poem.
        :param title: The title of the poem.
        :param style: Whether to apply a specific style to the poem.
        :param paper: The background image for the poem.
        :param separate_title_from_text: Whether to separate the title from the text.
        :param music: The music to play during the poem.

        :type author: PoemAuthor | str
        :type text: str | None
        :type title: str
        :type style: bool
        :type paper: str
        :type separate_title_from_text: bool
        :type music: str | None
        """
        if isinstance(author, PoemAuthor):
            paper = paper or author.paper
            separate_title_from_text = (
                separate_title_from_text or author.separate_title_from_text
            )
            music = music or author.music

            if style is True:
                style = author.style

            author = author.name

        for arg in (author, text, title):
            if not isinstance(arg, str):
                raise TypeError(f"{arg} must be type str, not {type(arg).__name__}")

        if style is True:
            if author:
                style = "%s_text" % author
            else:
                style = "default"
        else:
            style = "default"

        poem = (
            "%s\n\n%s" % (title, text) if separate_title_from_text and title else text
        )

        super().__init__(poem, style=style, **properties)

        self.author = author
        self.paper = renpy.easy.displayable_or_none(paper) or renpy.Null()
        self.music = music

    def format_music_str(self, music: str, pos: int = 0):
        """
        Returns a formatted music string during and after the poem.

        :param music: The music track to format.
        :param pos: The position in the music track to start playing.

        :type music: str
        :type pos: int

        :return music: A formatted music string.
        :rtype: str
        """
        music_match_pattern = re.compile(r"^<.*?>")
        track_partition_pattern = re.compile(r"from( *)((\d+\.\d*)|(\d+)|(\.\d+))")

        if music_match_pattern.match(music):
            info, gt, path = music.partition(">")

            if track_partition_pattern.search(info):
                info = track_partition_pattern.sub("from %s" % pos, info)
                music = info + gt + path
            else:
                music = "<from %s %s>" % (pos, music[1:])
        else:
            music = "<from %s %s>" % (pos, music)

        return music

    def show(
        self,
        img: str | None = None,
        at_list: list = [store.i11],
        paper_sound: str | None = store.audio.page_turn,
        music: str | bool = True,
        from_current: bool = True,
        revert_music: bool = True,
        testing: bool = False,
    ):
        """
        Displays the poem to the Poem Response screen.

        :param paper_sound: The sound to play when the poem is displayed.
        :param music: Whether to play the music associated with the poem.
        :param from_current: Whether to start the music from the current position of the previous music track.
        :param revert_music: Whether to revert the music to the previous track after the poem is displayed.
        :param testing: Unused in DDLC. Used for GitHub Actions testing purposes.

        :type paper_sound: str | None
        :type music: str | bool
        :type from_current: bool
        :type revert_music: bool
        :type testing: bool
        """
        if not testing:
            previous_music = None

            if paper_sound is not None:
                renpy.sound.play(paper_sound, channel="page_turn", loop=False)

            _window_hide()  # type: ignore # noqa: F821

            if music is True:
                poem_track = self.music or None
            else:
                poem_track = music or None

            if poem_track:
                previous_music = renpy.music.get_playing()
                music = (
                    self.format_music_str(poem_track, renpy.music.get_pos())
                    if from_current
                    else poem_track
                )
                renpy.music.play(music, channel="poem", loop=True, fadeout=0.5)
                renpy.music.stop(fadeout=2.0)

            allow_skipping = renpy.config.allow_skipping
            renpy.config.allow_skipping = False
            skipping = store._skipping
            store._skipping = False

            renpy.transition(store.dissolve)
            renpy.show_screen("poem", self)
            pause()

            if img:
                if isinstance(self.author, PoemAuthor):
                    renpy.hide(self.author.name)
                else:
                    renpy.hide(self.author)
                renpy.show(img, at_list=at_list)

            renpy.hide_screen("poem")
            renpy.transition(store.dissolve)

            renpy.config.allow_skipping = allow_skipping
            store._skipping = skipping

            if poem_track and revert_music:
                if previous_music:
                    previous_music = (
                        self.format_music_str(previous_music, renpy.music.get_pos())
                        if from_current
                        else previous_music
                    )
                    renpy.music.play(previous_music, loop=True, fadein=2.0)

                renpy.music.stop("music", fadeout=2.0)

            renpy._window_auto = True

        if not persistent.first_poem:
            persistent.first_poem = True


class PoemResponseDB(object):
    """
    A class used to represent a database of poems.
    """

    def __init__(self):
        """
        Initializes the poem response database.
        """
        self.poems: dict[str, Poem] = {}

    def add_poem(
        self,
        identifier: str,
        author: PoemAuthor,
        title: str,
        text: str,
        style: bool | str = True,
        paper: str = "images/bg/poem.jpg",
        separate_title_from_text: bool = True,
        music: str | None = None,
        translate: typing.Literal["all", "title", "text", "none"] = "all",
    ):
        """
        Adds a poem to the database.

        :param identifier: The unique identifier for the poem.
        :param author: The author of the poem.
        :param title: The title of the poem.
        :param text: The text of the poem.
        :param style: Whether to apply a specific style to the poem.
        :param paper: The background image for the poem.
        :param separate_title_from_text: Whether to separate the title from the text.
        :param music: The music to play during the poem.
        :param translate: Whether to let Ren'Py translate the poem text.

        :type identifier: str
        :type author: PoemAuthor
        :type title: str
        :type text: str
        :type style: bool | str
        :type paper: str
        :type separate_title_from_text: bool
        :type music: str | None
        :type translate: typing.Literal["all", "title", "text", "none"]
        """
        self.poems[identifier] = Poem(
            author=author,
            title=store._(title) if translate in ["all", "title"] else title,
            text=store._(text) if translate in ["all", "text"] else text,
            style=style,
            paper=paper,
            separate_title_from_text=separate_title_from_text,
            music=music,
        )

    def get_poem(self, identifier: str) -> Poem:
        """
        Retrieves a poem from the database by its identifier.

        :param identifier: The unique identifier for the poem.

        :type identifier: str

        :return poem: The poem if found
        :rtype: Poem
        :raise ValueError: If the poem with the given identifier does not exist.
        """
        if identifier in self.poems:
            return self.poems[identifier]
        raise ValueError(f"Poem with identifier '{identifier}' not found.")

    def get_poems(self) -> list[str]:
        """
        Returns a list of all poems in the database.

        :return: A list of all poems.
        :rtype: list[Poem]
        """
        return list(self.poems.keys())

    def show_poem(self, identifier: str, img: str | None = None, **kwargs):
        """
        Displays a poem from the database by its identifier.

        :param identifier: The unique identifier for the poem.
        :param kwargs: Additional keyword arguments to pass to the `show` method of the Poem class.

        :type identifier: str
        """
        poem = self.get_poem(identifier)
        if poem:
            poem.show(img=img, **kwargs)
        else:
            raise ValueError(f"Poem with identifier '{identifier}' not found.")


# Initialize the Poem database and authors.
poem_db = PoemResponseDB()

author_s = PoemAuthor("sayori", music=store.audio.tsayori)
author_n = PoemAuthor("natsuki", music=store.audio.tnatsuki)
author_y = PoemAuthor("yuri", music=store.audio.tyuri)
author_m = PoemAuthor("monika", music=store.audio.tmonika)

## Yuri's Poems
poem_db.add_poem(
    "poem_y1_en",
    author_y,
    title="Ghost Under the Light",
    text="""\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
It must be this one.
The last remaining streetlight to have withstood the test of time.
the last yet to be replaced by the sickening blue-green hue of the future.
I bathe. Calm; breathing air of the present but living in the past.
The light flickers.
I flicker back.""",
)

poem_db.add_poem(
    "poem_y2_en",
    author_y,
    title="The Raccoon",
    text="""\
It happened in the dead of night while I was slicing bread for a guilty snack.
My attention was caught by the scuttering of a raccoon outside my window.
That was, I believe, the first time I noticed my strange tendencies as an unordinary human.
I gave the raccoon a piece of bread, my subconscious well aware of the consequences.
Well aware that a raccoon that is fed will always come back for more.
The enticing beauty of my cutting knife was the symptom.
The bread, my hungry curiosity.
The raccoon, an urge.

The moon increments its phase and reflects that much more light off of my cutting knife.
The very same light that glistens in the eyes of my raccoon friend.
I slice the bread, fresh and soft. The raccoon becomes excited.
Or perhaps I'm merely projecting my emotions onto the newly-satisfied animal.

The raccoon has taken to following me.
You could say that we've gotten quite used to each other.
The raccoon becomes hungry more and more frequently, so my bread is always handy.
Every time I brandish my cutting knife, the raccoon shows me its excitement.
A rush of blood. Classic Pavlovian conditioning. I slice the bread.
And I feed myself again.""",
)

poem_db.add_poem(
    "poem_y3_en",
    author_y,
    title="Beach",
    text="""\
A marvel millions of years in the making.
Where the womb of Earth chaotically meets the surface.
Under a clear blue sky, an expanse of bliss--
But beneath gray rolling clouds, an endless enigma.
The easiest world to get lost in
Is one where everything can be found.

One can only build a sand castle where the sand is wet.
But where the sand is wet, the tide comes.
Will it gently lick at your foundations until you give in?
Or will a sudden wave send you crashing down in the blink of an eye?
Either way, the outcome is the same.
Yet we still build sand castles.

I stand where the foam wraps around my ankles.
Where my toes squish into the sand.
The salty air is therapeutic.
The breeze is gentle, yet powerful.
I sink my toes into the ultimate boundary line, tempted by the foamy tendrils.
Turn back, and I abandon my peace to erode at the shore.
Drift forward, and I return to Earth forevermore.""",
)

poem_db.add_poem(
    "poem_y3b_en",
    author_y,
    title="Ghost Under the Light pt. 2",
    text="""\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
In the distance, a blue-green light flickers.
A lone figure crosses its path - a silhouette obstructing the eerie glow.
My heart pounds. The silhouette grows. Closer. Closer.
I open my umbrella, casting a shadow to shield me from visibility.
But I am too late.
He steps into the streetlight. I gasp and drop my umbrella.
The light flickers. My heart pounds. He raises his arm.

Time stops.

The only indication of movement is the amber light flickering against his outstretched arm.
The flickering light is in rhythm with the pounding of my heart.
Teasing me for succumbing to this forbidden emotion.
Have you ever heard of a ghost feeling warmth before?
Giving up on understanding, I laugh.
Understanding is overrated.
I touch his hand. The flickering stops.
Ghosts are blue-green. My heart is amber.""",
)

## Yuri's Act 2 Poems
poem_db.add_poem(
    "poem_y22_en",
    author_y,
    title="Wheel",
    text="""\
A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. \
A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. \
Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. \
Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. \
A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. \
A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. \
Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. \
A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to \
the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring \
prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. \
Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. \
Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel.""",
    paper="images/bg/poem_y1.jpg",
)

poem_db.add_poem(
    "poem_y23_en",
    author_y,
    title="mdpnfbo,jrfp",
    text="""\
ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imboss\
ing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bris\
tlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers \
bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotica\
lly overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,\
haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,\
southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano re\
vealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuz\
zi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sha\
ria prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount\
,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados \
trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking \
galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness sw\
erveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine f\
lagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,de\
lirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hr\
yvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize\
 caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,\
degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphid\
es cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares cas\
tanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters su\
bjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotisi\
ng,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations sn\
arier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lance\
let,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulia\
s flaggers wammul boastfully,,galravitch happies interassociation multipara augme\
ntations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usu\
als,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterb\
urs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadbloc\
ked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravelli\
ngs quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistical\
ly,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist s\
ticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unk\
enneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts \
vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispos\
itions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating r\
etiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obdurat\
ion exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily\
 ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,\
stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi
Fresh blood seeps through the line parting her skin and slowly colors her breast red.\
 I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of\
 me driving the knife into her flesh continuously, fucking her body with the blade, \
making a mess of her. My head starts going crazy as my thoughts start to return. \
Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely\
 disgusting. How could I ever let myself think these things? But it’s unmistakable. \
The lust continues to linger through my veins. An ache in my muscles stems from the \
unreleased tension experienced by my entire body. Her Third Eye is drawing me closer.""",
    paper="images/bg/poem_y2.jpg",
    style="yuri_text_3",
    translate="none",
)

## Natsuki's Poems
poem_db.add_poem(
    "poem_n1_en",
    author_n,
    title="Eagles Can Fly",
    text="""\
Monkeys can climb
Crickets can leap
Horses can race
Owls can seek
Cheetahs can run
Eagles can fly
People can try
But that's about it.""",
)

poem_db.add_poem(
    "poem_n2_en",
    author_n,
    title="Amy Likes Spiders",
    text="""\
You know what I heard about Amy?
Amy likes spiders.
Icky, wriggly, hairy, ugly spiders!
That's why I'm not friends with her.

Amy has a cute singing voice.
I heard her singing my favorite love song.
Every time she sang the chorus, my heart would pound to the rhythm of the words.
But she likes spiders.
That's why I'm not friends with her.

One time, I hurt my leg really bad.
Amy helped me up and took me to the nurse.
I tried not to let her touch me.
She likes spiders, so her hands are probably gross.
That's why I'm not friends with her.

Amy has a lot of friends.
I always see her talking to people.
She probably talks about spiders.
What if her friends start to like spiders too?
That's why I'm not friends with her.

It doesn't matter if she has other hobbies.
It doesn't matter if she keeps it private.
It doesn't matter if it doesn't hurt anyone.

It's gross.
She's gross.
The world is better off without spider lovers.

And I'm gonna tell everyone.""",
)

poem_db.add_poem(
    "poem_n3_en",
    author_n,
    title="I'll Be Your Beach",
    text="""\
Your mind is so full of troubles and fears
That diminished your wonder over the years
But today I have a special place
A beach for us to go.

A shore reaching beyond your sight
A sea that sparkles with brilliant light
The walls in your mind will melt away
Before the sunny glow.

I'll be the beach that washes your worries away
I'll be the beach that you daydream about each day
I'll be the beach that makes your heart leap
In a way you thought had left you long ago.

Let's bury your heavy thoughts in a pile of sand
Bathe in sunbeams and hold my hand
Wash your insecurities in the salty sea
And let me see you shine.

Let's leave your memories in a footprint trail
Set you free in my windy sail
And remember the reasons you're wonderful
When you press your lips to mine.

I'll be the beach that washes your worries away
I'll be the beach that you daydream about each day
I'll be the beach that makes your heart leap
In a way you thought had left you long ago.

But if you let me by your side
Your own beach, your own escape
You'll learn to love yourself again.""",
)

poem_db.add_poem(
    "poem_n3b_en",
    author_n,
    title="Because You",
    text="""\
Tomorrow will be brighter with me around
But when today is dim, I can only look down.
My looking is a little more forward
Because you look at me.

When I want to say something, I say it with a shout!
But my truest feelings can never come out.
My words are a little less empty
Because you listen to me.

When something is above me, I reach for the stars.
But when I feel small, I don't get very far.
My standing is a little bit taller
Because you sit with me.

I believe in myself with all of my heart.
But what do I do when it's torn all apart?
My faith is a little bit stronger
Because you trusted me.

My pen always puts my feelings to the test.
I'm not a good writer, but my best is my best.
My poems are a little bit dearer
Because you think of me.

Because you, because you, because you.""",
)

## Natsuki's Act 2 Poems
poem_db.add_poem(
    "poem_n2b_en",
    author_n,
    title="T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
    text="""\
SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz
cyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo
ZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh
biBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug
b2YgdG91Y2guIE15IGJvZHkgbmVhcmx5
IGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l
dGhpbmcgaW5jcmVkaWJseSBmYWludCwg
ZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg
dG8gcmVzaXN0IHRoaXMgdW5jb250cm9s
bGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh
biBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g
YmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk
Z2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0
b3AgbXlzZWxmLg==""",
    translate="none",
)

poem_db.add_poem(
    "poem_n23_en",
    author_n,
    title="",
    text="""\
I don't know how else to bring this up. But there's been something I've been worried about. \
Yuri has been acting kind of strange lately. You've only been here a few days, so you may \
not know what I mean. But she's not normally like this. She's always been quiet and polite \
and attentive...things like that.

Okay... This is really embarrassing, but I'm forcing myself to suck it up. The truth is, I'm REALLY \
worried about her. But if I try talking to her, she'll just get mad at me again. I don't \
know what to do. I think you're the only person that she'll listen to. I don't know why. \
But please try to do something. Maybe you can convince her to talk to a therapist.

I've always wanted to try being better friends with Yuri, and it really hurts me to see \
this happening. I know I'm going to hate myself later for admitting that, but right now \
I don't care. I just feel so helpless. So please see if you can do something to help. \
I don't want anything bad to happen to her. I'll make you cupcakes if I have to. Just please \
try to do something.

As for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us \
to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. \
DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? \
I'm counting on you. Thanks for reading.""",
    translate="text",
)

## Sayori's Poems
poem_db.add_poem(
    "poem_s1_en",
    author_s,
    title="Dear Sunshine",
    text="""\
The way you glow through my blinds in the morning
It makes me feel like you missed me.
Kissing my forehead to help me out of bed.
Making me rub the sleepy from my eyes.

Are you asking me to come out and play?
Are you trusting me to wish away a rainy day?
I look above. The sky is blue.
It's a secret, but I trust you too.

If it wasn't for you, I could sleep forever.
But I'm not mad.

I want breakfast.""",
)

poem_db.add_poem(
    "poem_s2_en",
    author_s,
    title="Bottles",
    text="""\
I pop off my scalp like the lid of a cookie jar.
It's the secret place where I keep all my dreams.
Little balls of sunshine, all rubbing together like a bundle of kittens.
I reach inside with my thumb and forefinger and pluck one out.
It's warm and tingly.
But there's no time to waste! I put it in a bottle to keep it safe.
And I put the bottle on the shelf with all of the other bottles.
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row.

My collection makes me lots of friends.
Each bottle a starlight to make amends.
Sometimes my friend feels a certain way.
Down comes a bottle to save the day.

Night after night, more dreams.
Friend after friend, more bottles.
Deeper and deeper my fingers go.
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies.
Digging and digging.
Scraping and scraping.

I blow dust off my bottle caps.
It doesn't feel like time elapsed.
My empty shelf could use some more.
My friends look through my locked front door.

Finally, all done. I open up, and in come my friends.
In they come, in such a hurry. Do they want my bottles that much?
I frantically pull them from the shelf, one after the other.
Holding them out to each and every friend.
Each and every bottle.
But every time I let one go, it shatters against the tile between my feet.
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor.

They were supposed to be for my friends, my friends who aren't smiling.
They're all shouting, pleading. Something.
But all I hear is echo, echo, echo, echo, echo
Inside my head.""",
)

poem_db.add_poem(
    "poem_s3_en",
    author_s,
    title="%",
    text="""\
Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of
Get.
Out.
Of.
My.
Head.\n\n\n
Get out of my head before I do what I know is best for you.
Get out of my head before I listen to everything she said to me.
Get out of my head before I show you how much I love you.
Get out of my head before I finish writing this poem.\n\n\n\n\n\n\n
But a poem is never actually finished.
It just stops moving.""",
    translate="text",
)

## Monika's Poems
poem_db.add_poem(
    "poem_m1_en",
    author_m,
    title="Hole in Wall",
    text="""\
It couldn't have been me.
See, the direction the spackle protrudes.
A noisy neighbor? An angry boyfriend? I'll never know. I wasn't home.
I peer inside for a clue.
No! I can't see. I reel, blind, like a film left out in the sun.
But it's too late. My retinas.
Already scorched with a permanent copy of the meaningless image.
It's just a little hole. It wasn't too bright.
It was too deep.
Stretching forever into everything.
A hole of infinite choices.
I realize now, that I wasn't looking in.
I was looking out.
And he, on the other side, was looking in.""",
)

poem_db.add_poem(
    "poem_m2_en",
    author_m,
    title="Save Me",
    text="""\
The colors, they won't stop.
Bright, beautiful colors
Flashing, expanding, piercing
Red, green, blue
An endless
cacophony
Of meaningless
noise


The noise, it won't stop.
Violent, grating waveforms
Squeaking, screeching, piercing
Sine, cosine, tangent
    Like playing a chalkboard on a turntable
        Like playing a vinyl on a pizza crust
An endless
poem
Of meaningless\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Load Me
    """,
)

poem_db.add_poem(
    "poem_m3_en",
    author_m,
    title="The Lady who Knows Everything",
    text="""\
An old tale tells of a lady who wanders Earth.
The Lady who Knows Everything.
A beautiful lady who has found every answer,
All meaning,
All purpose,
And all that was ever sought.

And here I am,


              a feather


Lost adrift the sky, victim of the currents of the wind.

Day after day, I search.
I search with little hope, knowing legends don't exist.
But when all else has failed me,
When all others have turned away,
The legend is all that remains - the last dim star glimmering in the twilit sky.

Until one day, the wind ceases to blow.
I fall.
And I fall and fall, and fall even more.
Gentle as a feather.
A dry quill, expressionless.

But a hand catches me between the thumb and forefinger.
The hand of a beautiful lady.
I look at her eyes and find no end to her gaze.

The Lady who Knows Everything knows what I am thinking.
Before I can speak, she responds in a hollow voice.
"I have found every answer, all of which amount to nothing.
There is no meaning.
There is no purpose.
And we seek only the impossible.
I am not your legend.
Your legend does not exist."

And with a breath, she blows me back afloat, and I pick up a gust of wind.""",
)

poem_db.add_poem(
    "poem_m4_en",
    author_m,
    title="Happy End",
    text="""\
Pen in hand, I find my strength.
The courage endowed upon me by my one and only love.
Together, let us dismantle this crumbling world
And write a novel of our own fantasies.

With a flick of her pen, the lost finds her way.
In a world of infinite choices, behold this special day.

After all,
Not all good times must come to an end.""",
)

## Monika's Act 2 Poems
poem_db.add_poem(
    "poem_m21_en",
    author_m,
    title="Hole in Wall",
    text="""\
But he wasn't looking at me.
Confused, I frantically glance at my surroundings.
But my burned eyes can no longer see color.
Are there others in this room? Are they talking?
Or are they simply poems on flat sheets of paper,
The sound of frantic scrawling playing tricks on my ears?
The room begins to crinkle.
Closing in on me.
The air I breathe dissipates before it reaches my lungs.
I panic. There must be a way out.
It's right there. He's right there.

Swallowing my fears, I brandish my pen.""",
)

poem_db.add_poem(
    "poem_m22_en",
    author_m,
    title="Save Me",
    text="""\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, piercing
Red, green, blue
An  ndless
CACOPHONY
Of meaningless
noise


The noise, it won't STOP.
Viol nt, grating w vef rms
Sq e king, screech ng, piercing
SINE, COSINE, TANGENT
    Like play ng a ch lkboard on a t rntable
        Like playing a KNIFE on a BREATHING RIBCAGE
 n  ndl ss
p  m
Of m  n ngl ss\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Delete Her
    """,
)

poem_db.add_poem(
    "poem_y1",
    author_y,
    title="灯下魅影",
    text="""\
我卷曲的长发
浸染在路灯的琥珀光下
是它吧
在时光的洪流中幸存的最后一盏街灯
未来的病态青晖尚未侵蚀的最后一盏街灯
我沐浴着旧时代的灯光，呼吸在当下却萦绕于过往
灯明灯灭
我方幻醒""",
)

poem_db.add_poem(
    "poem_y2",
    author_y,
    title="浣熊",
    text="""\
寂静的深夜里，
我切着柔软的面包，
这时，
窗外出现了一只浣熊；
这是第一次，
我发现了我那非等闲的爱好。

尽管知道后果，
尽管知道浣熊会因此再度来访，
我仍旧切了一片面包分给了它
刀身的反光就是预兆
面包，我饥渴的好奇心，
浣熊，我难隐的冲动。

月升移位，让我刀刃的反光更亮
这月光与那浣熊朋友眼中闪耀的光亮一样；
再一次，
我切开了那新鲜柔软的面包，
那浣熊随之兴奋了起来；
不过那也许只是我把自己的情绪投射到它身上罢了。

如今，
那浣熊已与我同在，
我与它已互相熟识，
那浣熊愈发暴食，
我的面包亦随时在手；
浣熊随着舞动的刀锋欢腾，
每一次我切开面包，
浮现的鲜血就如同条件刺激般，宣示着我的存在
于是，我喂了一口自己。""",
)

poem_db.add_poem(
    "poem_y3",
    author_y,
    title="海滩",
    text="""\
万年间奇迹般的造物
让大地以混沌之姿从起源浮出表面
澄空之下，是无垠的福祉——
但滚云之下，只有无尽的谜团
这是最容易迷失的世界
也是什么都能找得到的世界

只有湿沙才能筑沙堡
若有湿沙则必有海浪
会是轻浪不断舔舐直到屈服吗？
或是巨浪在眨眼间便将你碾碎？
即使难逃毁灭的结局
我们却仍在筑起沙堡

泡沫萦绕于我的脚踝
脚趾也在此嵌入细沙
湿咸的空气疗愈身心
轻风拂过 柔中带刚
泡沫般的卷须诱惑我向前，我的脚趾陷入了最后的边界线
回头是岸，则我将放弃宁静，在岸边受风吹雨蚀
漂流入海，则我将回到地球怀抱，作永世波臣""",
)

poem_db.add_poem(
    "poem_y3b",
    author_y,
    title="Ghost Under the Light pt. 2",
    text="""\
我卷曲的长发
浸染在路灯的琥珀光下
远处，青绿色的灯光闪烁
踽踽独行的剪影，遮蔽了奇异的光芒
那轮廓愈来愈近，我不由心跳加速
我撑开伞，掩藏于应召的阴影
但为时已晚
他已经走到了路灯下！我倒吸一口凉气，手中的伞也掉在地上
灯光幻灭，我在心跳，他伸手向前

时空凝滞

唯一的动态就是他手臂上闪烁的琥珀色灯光
灯光闪烁，我的心也跟着跳动
似乎在取笑我屈从于禁忌的情感
你是否听说，鬼魂亦能感受到温暖？
我放弃了理解，以一笑置之
理解本身即为对它的高估
我抚摸他的手，灯光便不再明灭
青绿色的魅影，我琥珀色的心""",
)

## Yuri's Act 2 Poems
poem_db.add_poem(
    "poem_y22",
    author_y,
    title="轮",
    text="""\
转动的轮。带动着轴。磨削。机头。线性变速箱。坠落的天空。七支圣柱。停靠的船。异世界的洞口。粗绳上的细绳。撕裂的马具。抛物线变速箱。膨胀的宇宙。被齿轮滑动控制的时间。上帝的存在。向着四面八方游动。溺水。用血写的祈祷文。用人类眼睛写在吞噬时间的蛇上的祷文。连接所有活物眼睛的线。万花筒般变化的圣柱。指数型变速箱。繁星爆炸的天空。上帝否认上帝的存在。六维旋转的轮子。四十个齿轮和一个滴答作响的钟。地球每转一圈就滴答一秒的时钟。每秒滴答滴答滴答四十次的钟。通往异世界的泊船。拴在圣柱上。时钟里千变万化的血书。吞噬时光的祷词，连接着四十个齿轮的天空，打开了四面八方的人的眼睛。呼吸着的变速箱。呼吸着的机头。呼吸着的船。呼吸着的洞口。呼吸着的蛇。呼吸着的神。呼吸着的血。呼吸着的圣柱。呼吸着的人眼。呼吸着的时间。呼吸着的祷词。呼吸着的天空。呼吸着的轮。""",
    paper="images/bg/poem_y1.jpg",
)

poem_db.add_poem(
    "poem_y23",
    author_y,
    title="mdpnfbo,jrfp",
    text="""\
ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imboss\
ing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bris\
tlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers \
bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotica\
lly overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,\
haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,\
southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano re\
vealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuz\
zi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sha\
ria prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount\
,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados \
trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking \
galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness sw\
erveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine f\
lagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,de\
lirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hr\
yvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize\
 caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,\
degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphid\
es cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares cas\
tanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters su\
bjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotisi\
ng,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations sn\
arier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lance\
let,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulia\
s flaggers wammul boastfully,,galravitch happies interassociation multipara augme\
ntations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usu\
als,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterb\
urs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadbloc\
ked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravelli\
ngs quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistical\
ly,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist s\
ticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unk\
enneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts \
vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispos\
itions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating r\
etiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obdurat\
ion exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily\
 ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,\
stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi
Fresh blood seeps through the line parting her skin and slowly colors her breast red.\
 I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of\
 me driving the knife into her flesh continuously, fucking her body with the blade, \
making a mess of her. My head starts going crazy as my thoughts start to return. \
Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely\
 disgusting. How could I ever let myself think these things? But it’s unmistakable. \
The lust continues to linger through my veins. An ache in my muscles stems from the \
unreleased tension experienced by my entire body. Her Third Eye is drawing me closer.""",
    paper="images/bg/poem_y2.jpg",
    style="yuri_text_3",
    translate="none",
)

## Natsuki's Poems
poem_db.add_poem(
    "poem_n1",
    author_n,
    title="雄鹰飞高树",
    text="""\
猿猴爬山谷
蟋蟀叫咕咕
马儿跑飞速
夜猫会捉鼠
猎豹奔无阻
雄鹰飞高树
人模仿万物
但不过如此。""",
)

poem_db.add_poem(
    "poem_n2",
    author_n,
    title="艾米喜欢蜘蛛",
    text="""\
你知道艾米吗？
艾米喜欢蜘蛛。
就是那些黏黏的扭扭的毛毛的丑丑的蜘蛛！
所以我才不跟她做朋友。

艾米有一副美妙的歌喉。
我听过她唱我最喜欢的情歌。
每次响起她演唱的旋律，我的心跳也会随着节奏怦怦跃动。
但这样的艾米却喜欢蜘蛛！
所以我才不跟她做朋友。

有次，我摔伤了我的腿。
是艾米扶着我去医务室。
但我尽量不让她碰我。
因为她喜欢蜘蛛。她的手一定也很恶心吧。
所以我才不跟她做朋友。

艾米有很多朋友。
我总看她与别人聊得开。
我想，她大概也在聊蜘蛛吧。
要是她的朋友也跟着喜欢蜘蛛了，那该怎么办？
所以我才不跟她做朋友。

她是否有其他爱好无关紧要。
她是否只是私下聊聊也无关紧要。
有这个爱好根本没伤害到他人也无关紧要。

蜘蛛就是很恶心。
喜欢恶心蜘蛛的她也很恶心。
没有了喜欢蜘蛛的人，世界才会更好！

我要快快告诉所有人。""",
)

poem_db.add_poem(
    "poem_n3",
    author_n,
    title="我会做你的沙滩",
    text="""\
你的脑中充满了烦恼与恐惧
它们在你脑中盘踞多年，削弱了你的好奇心
但今天，我要带你去一个特别的地方
那是属于我们的沙滩

一片在你眼中遥不可及的沙滩
面对波光粼粼的海面
在灿烂的阳光下
你内心的障壁终将融化

我将化身沙滩，洗去你的忧愁
我将化身沙滩，让你魂牵梦萦
我将化身沙滩，让你放飞心灵
用你遗失已久的方式

来一起将你的心结埋入沙丘
沐浴于阳光下你我十指相扣
在发咸的大海里洗净你的不安
用你内心久违的阳光照耀我吧

来一同将你的记忆丢入沙上的脚印
让我驾着帆船带你领略自由的风情
在你与我嘴唇相印的时候
请忆起你如此杰出的理由

我将化身沙滩，洗去你的担心
我将化身沙滩，让你魂牵梦萦
我将化身沙滩，让你放飞心灵
用你遗失已久的方式

如果你可以让我与你为伴
成为你的沙滩，你的世外桃源
那你终能寻回自爱""",
)

poem_db.add_poem(
    "poem_n3b",
    author_n,
    title="Because You",
    text="""\
有你在身边的来日会更明亮
可现实的黯淡让我点点绝望
我现在能试着向前看去
因为有你在看着我

当我想说什么时，我总会吼出来！
但最真实的感受却永远无法言说
我的话语变得不那么空洞
因为有你在倾听

当我遇到挑战时，我会全力以赴
但我失去自信时，只能望而却步
我可以站得稍微再高一些
因为有你坐在我身边

我怀有全心全意相信着的期冀
可一旦碎裂，一切都难以为继
我的信念变得更坚韧了一点
因为有你信赖着我

我的笔总会考验我的感情
专业不足但也会全力前行
我的诗变得更温柔了一点
因为有你的思念

因为你，因为你，所有奇迹都因为有你。""",
)

## Natsuki's Act 2 Poems
poem_db.add_poem(
    "poem_n2b",
    author_n,
    title="552B5byA5L2g55qE5aSp55y8IA==",
    text="""\
5YiA5YiD5Lu/5L2b5bey5oiQ5Li65oiR6Kem6KeJ55qE5bu25Ly477yM5b\
CG5aW555qu6IKk55qE5p+U6L2v6Kem5oSf5Lyg6YCS57uZ5oiR55qE56\
We57uP44CC5oiR5Yeg5LmO5rWR6Lqr6YO95Zyo5oq95pCQ44CC5Zyo5\
YaF5b+D5rex5aSE77yM5pyJ5LiA56eN5b6u5byx5Y206Zq+5Lul572u5L+\
h55qE5Lic6KW/77yM5a6D5Zyo5bCW5Y+r552A77yM5Zyo5aWL5Yqb5o\
q15Yi26L+Z56eN5peg5rOV5o6n5Yi255qE5b+r552A77yM5Zyo5aWL5Yqb5o\
q15Yi26L+Z56eN5peg5rOV5o6n5Yi255qE5b+r5oSf44CC5L2G5oiR6IO9\
5oSf6KeJ5Yiw77yM6Ieq5bex5bey57uP6KKr6YC85Yiw5LqG5bSp5rqD55\
qE6L6557yY44CC5oiR4oCm4oCm5oiR5o6n5Yi25LiN5LqG6Ieq5bex5LqG\
44CC""",
    translate="none",
)

poem_db.add_poem(
    "poem_n23",
    author_n,
    title="",
    text="""\
有件事让我很担心，但我不知道该怎么跟你开口……就是，优里这几天有点怪怪的，跟平时不太一样。因为你才刚加入没几天，所以可能不明白我为什么这么说。\
但她这样可不太正常。优里平时都很内向、体贴又有礼貌……总之就是这样的性格。

好吧……虽然我觉得跟你说这些很尴尬……但我咬咬牙忍了，还是跟你直说吧：我真的，真的很担心她。\
可我要是想跟她好好谈谈的话，她肯定又要跟我发火了。\
我不知道该怎么办了。我想，她只听得进你的话。我也不知道为什么。\
但是拜托了，请你帮忙做点什么吧。也许你能去说服她去看看心理医生什么的。

我一直都想和优里成为更要好的朋友，所以看到她这样我真的很伤心。\
我知道日后想起今天的这番话，我肯定会特别后悔。但是现在我不在乎了。\
我现在只是觉得很无助，所以拜托你看看能不能帮上什么忙，我真的不希望她出事。\
你愿意的话，我也可以给你做纸杯蛋糕吃。真的，求你帮忙做点什么吧！

至于莫妮卡……我不知道为什么，但她对优里的异常表现很不屑，好像希望我们都无视这件事似的。\
说实话，我现在对她很生气，所以我才来找你帮忙的。\
最重要的一点，千万别让她知道我给你写了这些话！！！你就假装我是给你分享了你一首很棒的诗，好吗？\
优里的事情我就全指望你了。感谢阅读，以上！""",
    translate="text",
)

## Sayori's Poems
poem_db.add_poem(
    "poem_s1",
    author_s,
    title="亲爱的阳光",
    text="""\
清晨你透过梦境照亮我的世界
似乎在传达对我的思念
亲吻前额催促我坐起
帮我的眼睛擦去睡意。

是在邀请我出门散心？
是在鼓励我拭去阴云？
我抬起头，见碧空如洗
你当做秘密，而我信任你。

如果没有你，我会长眠不复醒。
但我没有生气，我感谢你把我叫醒。

想吃早餐了。""",
)

poem_db.add_poem(
    "poem_s2",
    author_s,
    title="瓶子",
    text="""\
我砰地一下打开了我的脑袋，就像平时打开饼干罐的盖儿。
这里，即是我保存所有梦想秘密之所。
一团团阳光拥簇，就像一只只小猫相互摩擦身体。
我把拇指和食指伸了进去，猛地揪了一团阳光出来。
指尖传来的感触，温暖又刺痒。
但时间宝贵，不能浪费！我把它塞进了瓶子，希望能让它得到保护。
所有的瓶子，在空架子上一字排开。
快乐的事情，快乐的事情，还是快乐的事情。所有快乐装在瓶子里，一字排开。

我的收藏带给我朋友。
每瓶的星光都能拯救。
朋友不时会有伤心，
那就用一瓶来挽救！

一夜复一夜，梦与梦堆积
朋友加朋友，瓶子数不清
我的手指，越探越深。
好似探索一个黑暗的洞穴，寻找角落和裂缝中的秘密
挖啊挖。
刮啊刮。

我轻轻拂去瓶盖上的灰尘，
时间流逝，却也浑然不觉。
我的架子空空，只等瓶子来填满。
但这时，我的朋友们却从锁上的前门门缝往里看。

朋友们蜂拥而入，在我准备万全的刹那。
他们争争抢抢。原来我的瓶子，是你们日夜所想？

我狂热地将它们拉下来，一个接一个。
将它们分发给每一个密友，一个不漏。
每个瓶子，一个不漏。
但每次我一放手，瓶子就在瓷砖上摔得粉碎。
快乐的事情，快乐的事情，还是快乐的事情。快乐全都碎成了花。

我有些朋友，他们从来不笑。所以快乐的瓶子，对他们非常重要。
他们尖叫，他们恳求，但话语却随风飘落。
我听到的只有回声、回声、回声、回声、回声伴着回声
在我的脑子里回荡，冲撞。""",
)

poem_db.add_poem(
    "poem_s3",
    author_s,
    title="%",
    text="""\
滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。滚出我的脑袋。
滚。
出。
我。
的。
脑。
袋。\n\n\n
在我做对你最好的事前滚出我的脑袋。
在我对她言听计从之前滚出我的脑袋。
在我表示我多么爱你前滚出我的脑袋。
在我写完这首诗前请你滚出我的脑袋。
但诗是永远写不完的。\n\n\n\n\n\n\n
只是戛然而止而已。""",
    translate="text",
)

## Monika's Poems
poem_db.add_poem(
    "poem_m1",
    author_m,
    title="墙上的洞",
    text="""\
这一切与我无关
瞧，那墙上有一个突起
是吵闹的邻居？还是生气的男友？我怎么会知道，我又不在家
我往里窥探，想一探究竟
不！我的眼睛！我开始眩晕，目盲，宛如曝光的胶片
可为时已晚，我的视网膜上
已永远灼上了毫无意义的图像
那只是个很小的孔洞，也并不明亮
可它实在太深
向着一切无限延伸
一个充满了无限选择的洞
我才意识到，原来我不是在往里窥探
而是在向外
而他，在另一头，往里窥探着""",
)

poem_db.add_poem(
    "poem_m2",
    author_m,
    title="Save Me",
    text="""\
斑斓的色彩，永不停歇
明亮的，绚丽的色彩
闪动，扩张，穿刺着
红色，绿色，又蓝色
无尽的
不谐的
无谓的
噪音



噪音，永不停歇
狂躁，破碎的波形
低语，嘶鸣，穿刺着
正弦，余弦，正切
    像是在转盘上摩擦黑板
        像是在饼沿上播放唱片
无尽的
无意的
诗\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Load Me
    """,
)

poem_db.add_poem(
    "poem_m3",
    author_m,
    title="全知之女",
    text="""\
古老的传说中，有一位云游四方的女士
她是全知之女
她美丽动人，知晓一切
一切意义
一切目的
一切被追求之物

现在我来了


            我是一缕飞羽


随风逐流，漂泊于天际

我知传说只是虚妄，仍苦苦追寻
但求而不得
一切都令我失望
一切都弃我而去
唯有传说中——那最后一颗黯淡星辰，在黄昏的天空中闪耀

直到那天，风儿骤停
我开始下坠
只有下坠，永无止境般下坠
像羽毛一般轻柔
像无神的羽毛笔，面无表情

但一只手接住了我
一位美丽的女士的手
我看向她的眼眸，却望不到尽头

全知的女士一定知道我之所想
我还未开口，她便以空洞的声音回答
“我知晓一切答案，那答案却通往虚无
一切都没有任何意义
一切都没有任何目的
你我的追求皆为虚无
我不是你追寻的传说
那传说也并不存在。”

她轻轻吐气，把我再次吹起，让另一阵风带我远行""",
)

poem_db.add_poem(
    "poem_m4",
    author_m,
    title="幸福结局",
    text="""\
执笔在手，我找到了文学之力
此间真爱，赋予我无上勇气
来吧，与我一同解构这崩坏的世界
为我们的新旅程，写下只属于你我的幻想圣典

她的钢笔一挥，迷途羔羊找回了方向
在这无限选择的世界里，发现那个特别的日期

最终，
我们开始了不散的筵席""",
)

## Monika's Act 2 Poems
poem_db.add_poem(
    "poem_m21",
    author_m,
    title="墙上的洞",
    text="""\
但他并没有在看我
那又是谁？我迷惑不解，茫然四顾
但我灼伤的眼睛已失去色彩
还有其他人在吗？他们在说话吗？
他看着的只是印在单调白纸上的诗吗？
狂热之音在我耳际摩擦
整个房间开始起皱缩水
向我挤压
我拼命呼吸，可空气还未进入肺部就已消失
我惊恐不已。这里一定有路可以出去！
那路就在那里，就在他所处的那一头！

我抛开了恐惧，挥舞起手中的笔""",
)

poem_db.add_poem(
    "poem_m22",
    author_m,
    title="Save Me",
    text="""\
斑  的色彩，永不  歇
明亮的，纟 丽的  采
门 人 ，  张，穿刺着
红色，绿色，又蓝色
大 尺 的
{i}不谐的！{/i}
无谓的
噪音



噪音，{i}永不停！歇！{/i}
  躁，  碎的氵  彡
低 吾， 斯 鸟，穿刺着
{i}正弦！余弦！正切！{/i}
    像是在转  上   察   反
        像是在{i}活的胸骨！{/i}上{i}用刀划切！{/i}
  一尽
   义
白    寺\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Delete Her
    """,
)
