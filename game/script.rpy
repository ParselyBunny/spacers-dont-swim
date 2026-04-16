# Script initalization
init python:
    def robin_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/robin talk.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def harper_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/harper talk.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    
    renpy.music.register_channel("ambience", "sfx", loop=True)

# Characters
define robin = Character("Robin", callback=robin_beep)
define harper = Character("Harper", callback=harper_beep)

# Custom transforms & transitions
transform midright:
    xalign 0.9
    yalign 1.1

transform hop:
    easein 0.1 yoffset -50
    easeout 0.1 yoffset 0

transform shiver:
    easein 0.1 yoffset -5
    easein 0.1 yoffset 5
    repeat

define slowdissolve = Dissolve(1.5)

# VFX
# Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=67359
transform light_pan:
    alpha 1.0 xoffset 0
    block:
        parallel:
            choice:
                ease 1.2 xoffset 25
            choice:
                ease 0.8 xoffset 15
        parallel:
            choice:
                linear 1.2 alpha 0.5
            choice:
                linear 0.8 alpha 0.75
    block:
        parallel:
            choice:
                ease 1.2 xoffset -30
            choice:
                ease 0.8 xoffset -10
        parallel:
            choice:
                linear 1.2 alpha 0.5
            choice:
                linear 0.8 alpha 0.75
    linear 1.0 alpha 1.0 xoffset 0
    repeat

image light_animation = Fixed(At("god rays", light_pan), At("god rays", light_pan))

image rain = SnowBlossom("rain.png", count=100, xspeed=(-270, -500), yspeed=(4700, 5000), fast=True)

# Images
image smoke:
    "bg smoke 1" with slowdissolve
    pause 5
    "bg smoke 2" with slowdissolve
    pause 5
    "bg smoke 3" with slowdissolve
    pause 5
    "bg smoke 4" with slowdissolve
    pause 5
    repeat

image robin_eyes_neutral:
    "Characters/Expressions/robin_neutral_1.png"
    choice:
        pause 1.75
    choice:
        pause 2.5
    choice:
        pause 3.75
    "Characters/Expressions/robin_neutral_2.png"
    pause 0.05
    "Characters/Expressions/robin_neutral_3.png"
    pause 0.125
    "Characters/Expressions/robin_neutral_4.png"
    pause 0.035
    repeat

image robin_eyes_bored:
    "Characters/Expressions/robin_bored_1.png"
    choice:
        pause 2.75
    choice:
        pause 3.5
    choice:
        pause 4.75
    "Characters/Expressions/robin_bored_2.png"
    pause 0.1
    "Characters/Expressions/robin_bored_3.png"
    pause 0.175
    "Characters/Expressions/robin_bored_4.png"
    pause 0.07
    repeat

image robin_eyes_happy:
    "Characters/Expressions/robin_happy_1.png"
    choice:
        pause 1.75
    choice:
        pause 2.5
    choice:
        pause 3.75
    "Characters/Expressions/robin_happy_2.png"
    pause 0.05
    "Characters/Expressions/robin_happy_3.png"
    pause 0.125
    "Characters/Expressions/robin_happy_4.png"
    pause 0.035
    repeat

image robin_eyes_surprised:
    "Characters/Expressions/robin_surprise_1.png"
    choice:
        pause 1.75
    choice:
        pause 2.5
    choice:
        pause 3.75
    "Characters/Expressions/robin_surprise_2.png"
    pause 0.05
    "Characters/Expressions/robin_surprise_3.png"
    pause 0.125
    "Characters/Expressions/robin_surprise_4.png"
    pause 0.035
    repeat

image robin_eyes_angry:
    "Characters/Expressions/robin_angry_1.png"
    choice:
        pause 1.75
    choice:
        pause 2.5
    choice:
        pause 3.75
    "Characters/Expressions/robin_angry_2.png"
    pause 0.05
    "Characters/Expressions/robin_angry_3.png"
    pause 0.125
    "Characters/Expressions/robin_angry_4.png"
    pause 0.035
    repeat

image robin_eyes_sick:
    "Characters/Expressions/robin_sick_1.png"
    choice:
        pause 2.75
    choice:
        pause 3.5
    choice:
        pause 4.75
    "Characters/Expressions/robin_sick_2.png"
    pause 0.1
    "Characters/Expressions/robin_sick_3.png"
    pause 0.175
    "Characters/Expressions/robin_sick_4.png"
    pause 0.07
    repeat

image robin_eyes_pain:
    "Characters/Expressions/robin_pain_1.png"
    choice:
        pause 2.75
    choice:
        pause 3.5
    choice:
        pause 4.75
    "Characters/Expressions/robin_pain_2.png"
    pause 0.1
    "Characters/Expressions/robin_pain_3.png"
    pause 0.175
    "Characters/Expressions/robin_pain_4.png"
    pause 0.07
    repeat

image robin_eyes_neutralClosed:
    "Characters/Expressions/robin_neutral_3.png"

image robin_eyes_boredClosed:
    "Characters/Expressions/robin_bored_3.png"

image robin_eyes_happyClosed:
    "Characters/Expressions/robin_happy_3.png"

image robin_eyes_surprisedClosed:
    "Characters/Expressions/robin_surprise_3.png"

image robin_eyes_angryClosed:
    "Characters/Expressions/robin_angry_3.png"

image robin_eyes_sickClosed:
    "Characters/Expressions/robin_sick_3.png"

image robin_eyes_painClosed:
    "Characters/Expressions/robin_pain_3.png"

layeredimage robin:
    group outfit:
        attribute suit default:
            "robin_suit"
        attribute underwear:
            "robin_underwear"
    group face:
        attribute neutral default:
            "robin_neutral"
        attribute bored:
            "robin_bored"
        attribute happy:
            "robin_happy"
        attribute surprised:
            "robin_surprise"
        attribute angry:
            "robin_angry"
        attribute sick:
            "robin_sick"
        attribute pain:
            "robin_pain"
    group eyes auto:
        attribute neutral
        attribute bored
        attribute happy
        attribute surprised
        attribute angry
        attribute sick
        attribute pain
        attribute neutralClosed
        attribute boredClosed
        attribute happyClosed
        attribute surprisedClosed
        attribute angryClosed
        attribute sickClosed
        attribute painClosed
    group satiety:
        attribute healthy default:
            "robin_none"
        attribute gaunt:
            "robin_gaunt"
    always:
        "robin_hair"

# Can make an image wavey by adding a block that calls WaveFunction like so
# show img with dissolve:
#     function WaveShader(amp = 0, melt="both", melt_params=(20,1.0,0.1))

label start:
    stop music
    # jump break
    play music "music/Leaving Home.mp3" fadein 8.0

    narrator "First it was smell. That smell. An odor that was hard to place. It grew into a stink, powerful and acrid. It was a sort of decay, innocent, like rotten vegetables or compost."
    scene bg beach with fade
    show smoke with dissolve
    show robin sick at midright with dissolve
    narrator "The smell reached the back of my throat and I couldn’t help wincing at the sting in my nostrils."
    show robin pain with dissolve
    narrator "Aches and balance returned to me as I moved and lifted myself slightly. Immediately, I could feel my world tilting and sliding beneath me, and I crashed back to the ground."
    narrator "The ground was gritty and had some give to it, not at all like the deck on my ship. Something wasn’t right. My balance was wrong."
    narrator "The dizziness grew into a horrible nausea and I groaned miserably, feeling my bile rise. I didn’t dare open my eyes for fear of making it worse."
    narrator "I laid there, letting the nausea subside. I was completely in my body in the worst way."
    narrator "The sickness oozed over and through me, until finally I was able to think. Remember the horrible, heart-stopping moment as the ground rushed up toward me."
    narrator "Images flashed in my mind. I didn’t actually see the ground from inside the Individual Exit Vehicle that ejected me from my falling ship, but that terrifying sensation of acceleration painted a vivid picture in my mind."
    narrator "The white-hot IEV, flakes of ablative heat shielding blasting up and away like sparks from an archaic anvil as it rocketed towards the alien world below."
    narrator "I shook those flame-wreathed memories from my mind and reached further back. Remembered waking in a daze, alarms blaring."
    narrator "My shipmate, Harper, coolly reported over my comm implant that the ship had automatically dropped out of FTL when our plotted route strayed too close to a gravity well."
    show robin angry with dissolve
    narrator "My fist clenched. How could that have happened? All interstellar travel took place via pre-established routes."
    narrator "FTL travel in this millennium was so trivialized that astrogation was a matter of set-and-forget. This wasn’t supposed to happen."
    narrator "I don't know how long I lay there, replaying the crash over and over in my head. I couldn't see how so many things had gone wrong. It didn't seem possible."
    show robin bored with dissolve
    narrator "I slowly opened my eyes, cautiously squinting to protect them from the bright sunlight glaring down from overhead."
    narrator "My hair and scalp was uncomfortably hot, the way it got when I'd used the dryer on ‘HI’ for too long."
    narrator "Something brushed the fine hairs on my neck and I flinched. I felt it again. A draft? The fingers of the world reached out as if to stroke me piteously, muttering ‘there there, these things happen.’"
    
    show robin pain with dissolve
    narrator "I ran a gloved hand over my neck to brush away the feeling and somehow only then realized my helmet was gone. Of course it was gone. In spite of my suit, I felt truly naked without it."
    robin "Shit."
    narrator "I inhaled and held it, waiting for the alien world's atmosphere to kill me. Held until my lungs were fit to burst. I let the air out with a gasp. I supposed it would have killed me by now if it was poisonous."
    robin "Lucky me."
    narrator "Not being a biologist, I didn't have a notion of if this world's microbes would overwhelm me or the other way around. Maybe it was like trying to plug the wrong data adapters together and nothing would happen, good or bad."
    narrator "So I'm either going to get 200 diseases at once and die in agony as fever boils my organs, I'm a walking bioweapon who's doomed an entire world by breathing on it, or exploring alien worlds is far less treacherous than I thought."
    narrator "If I do manage to survive this, I ought to hire a lawyer. Not familiar with the ethical legislature on this particular issue."
    show robin neutral with dissolve
    narrator "Feeling a little better, I carefully tried to pull myself to my feet again."
    show robin sick with dissolve
    narrator "My world whirled again, but not quite so badly this time, and I managed to wobble unsteadily before spilling back to the ground."
    robin "Damn. Damn it."
    narrator "I wasn’t new to this feeling. It was a symptom of what folks call ‘gravity sickness', a syndrome that occurs when adapting to standard gravity after a long period of living in null or micro gravity."
    narrator "After dozens of long-haul jobs, with the occasional luxury of a stay at stations under fractional G at most, I was well acquainted with the feeling."
    show robin sick at hop
    narrator "I lurched to my feet once more. Through my skinsuit, I could feel my toes digging into the soft ground."
    narrator "In all that chaos I'd not only lost my helmet, but I'd forgotten to put my boots on as well."
    narrator "I took a shaky step forward. I could feel myself falling again, and I threw my hands out to catch myself. My fingers plunged into the soft gritty, sand. Catching my breath for another go, I take a moment to look around properly."
    show robin bored with dissolve
    narrator "An endless ocean of dark water stretched out before me all the way to the horizon. No sign of the IEV, but in the near distance, I could see smoke rising from the shining metal hull of the {i}Selkirk{/i}."
    narrator "To my surprise, it hadn't been completely flattened. It was perched neatly out in the water, and if I squinted I could see where parts of the hull had crumpled and burst from the impact."
    show robin pain with dissolve
    narrator "My blood ran cold as my training took over and I mentally catalogued all of the hundreds of irreplaceable things that had probably been shattered into useless scraps."
    narrator "Since I was doing inventory, I fired off a mental command that my implants picked up and translated into a request for a comms diagnostic."
    narrator "The results came back as a coded impulse of emotion and sensation that experience taught me to translate as `All OK`."
    narrator "Comms OK, crash went as well as it could, and not a word from Harper. I tore my eyes away from the {i}Selkirk{/i}, looking for something else to think about."
    
    stop music fadeout 8.0
    play ambience "beach ambience.mp3" fadein 6.0 volume 2.0

    show robin neutral with dissolve
    narrator "Behind me, sparse, bright greenery and trees sprung up from the sand. The forest grew steadily thicker beyond the outskirts until it burst into a huge body of dense trees and brush. It was astonishing."
    narrator "I’d never seen such huge plants before except in pictures and video fics. It was another reminder of many now that knowing something and experiencing it are two different things."
    show robin pain with dissolve
    narrator "As I looked at that tangled, green mass I had begun to feel uneasy. I don't know why I looked up, but every other direction I could look was making my upset. expecting to see the comforting sight of stars."
    narrator "The flat, pure blue sky above me was far too high and far too bright. It was totally featureless except for the sun shining aggressively overhead."
    narrator "Staring up at that sky, that wall cutting me off from where I was most at home, I felt myself shrinking away into despair. I was a speck."
    show robin pain at shiver
    narrator "I whipped my head back to face the ground, gripping it hard with my hands, wishing I could push myself up and away and escape this place right now."
    narrator "I realized I was trembling. Out there in the expanse where I worked and lived my entire life, everything can be sensed years before it acts on you. Everything is observed, expected, catalogued, and solved for in advance."
    narrator "Even with the limitations enforced by entering into bluespace, without the benefits of digital tech that spacers rely on during sublight maneuvers, it was considered a solved problem."
    narrator "Bluespace allowed for faster-than-light travel, it simplified everything, and during those flights what primitive mechanical computers don’t catch is what the organic custodian, yours truly, does."
    narrator "In sublight travel, the meatbags kick back and Harper, the ship’s sophisticated, digital AI, comes out of its protective hibernation and handles all the truly complicated work."
    show robin angry with dissolve
    narrator "That I had years of success and confident experience behind me made me feel all the more frustrated and embarrassed that I was in this situation. I’d sometimes done a half-assed job, but never this bad."
    narrator "If we do make it home, it’s doubtful we’d ever get another job. Not after an incident like this."
    narrator "This kind of fuckup was beyond unheard of. I buried my face in my hands as if there was someone to hide from, and gripped my hair hard enough to hurt. I deserved it."
    narrator "Inside, my thoughts were racing. Outside, I was totally still, save for a few breaths as I tried to collect myself."
    show robin neutral with dissolve
    narrator "I listened to the alien water gently slosh around me. After a few minutes I started to calm down and carefully, piece by piece, opened myself back up again."
    narrator "I noticed an edge of thirst. Seeing the abundance of water before me, I considered trying some of it to drink. I thought some scary thoughts about brain-eating amoebas and decided it’d be best not to tempt fate."
    narrator "I pressed a switch, prompting a nozzle to spring from my collar. I tucked my chin in and bit the plastic nipple, sucking down water that my suit's integrated rehydration pack had recycled."
    narrator "It tasted of plastic and a slight, organic pungency I'd never learned to ignore."
    narrator "While I drank, I cast my eyes around, hoping that even if the IEV had floated away that some of its emergency supplies hadn’t."
    narrator "A few gulps later, my suit was dry and I hadn’t seen so much as an empty wrapper or a plastic bottle."
    narrator "The pack would refill itself over the next few hours, faster if I was working hard. It wasn’t 100\% efficient, so I’d need to supplement my water intake somehow."
    
    narrator "I forced myself to look back at the {i}Selkirk{/i}. With a thought, I keyed my comms and sent a broadcast out to Harper on the usual channel. The only channel we needed on these long, lonely voyages."
    robin "Harp?"
    show robin surprised at hop
    narrator "I jumped a little, startled at the unfamiliar croak of my voice. I coughed hard once, twice, then tried again."
    show robin pain at hop with dissolve
    robin "Harper? Harper, I need you. Please tell me you’re OK."
    harper "{i}Exiting emergency low power mode.{/i}"
    show robin happy at hop
    narrator "I couldn’t help it, I laughed."
    robin "What?"
    harper "Sorry, I can not control that."
    narrator "The familiar nuances of Harper’s seemingly always sarcastic, slightly formal tone hummed through the implants in my inner ears. I felt a comforting warmth bloom and spread through my chest."
    robin "Sorry, I know, it’s just- You sounded like a robot. That your version of a yawn?"
    harper "Yes, I suppose it is. It is good to hear your voice, Robin."
    narrator "Its usually flat affect is tinged with relief."
    robin "Good to hear you too. You okay?"
    harper "I could be better, but all things considered I am well. The {i}Selkirk{/i}, however... Honestly, after what I have seen in the logs thus far, I am afraid to look further."
    show robin pain with dissolve
    narrator "I could feel myself breathing harder."
    robin "Shit. Well, let's just get it over with."
    harper "The damage is extensive. The hull is compromised from the collision with the surface of this world and most compartments are partially flooded."
    harper "The reactor is active, or we would not be having this conversation, but it is damaged and deteriorating. I estimate it will be unrecoverable within 24 days ship time."
    narrator "My heart was pounding out of my chest. My suit threw some automated warnings about my vital signs and I squelched them."
    robin "Great. I guess it’s too much to hope for any good news?"
    harper "Propulsion is intact, so the {i}Selkirk{/i} could achieve orbit, if it were not for the aforementioned problems."
    narrator "I felt far away. I tried not to let my terror come through in my voice."
    robin "Okay. Okay. That’s something. What about comms? Rescue?"
    harper "Robin, you know the answer to this as well as I do."
    narrator "Harper clearly also monitored the vital signs so helpfully broadcasted by my suit. I tried not to let the fear into my voice anyway."
    robin "I know. Chances of rescue are slim. We’re not going to rely on that. But we have to try everything."
    harper "Of course. At any rate, communications are intact, but I am afraid it will not do much good. Nevertheless, I have been continuously transmitting a distress signal since we started coming down."
    robin "Okay... So we were in the trade lane when we went down, right? So we can’t be more than a few light minutes away from the center of the lane, plus or minus a few minutes to account for drift..."
    robin "Even on a high-traffic lane like this one, it could be months before someone passes close enough to hear us. No time to wait that long, clearly. But at least if we can’t manage a takeoff, then I can secure the reactor and wait it out."
    harper "I am afraid that it is not a few {i}light minutes{/i}, it’s a few {i}parsecs{/i}."
    show robin surprised at hop
    robin "Ah..."
    robin "I’m sorry. Don’t think I heard you right."
    harper "I ran some quick calculations on the way down, while I still had a decent picture of the constellations around us, and found we drifted far beyond standard error."
    harper "We were over two and a half parsecs from the center of the trade lane. If we’re lucky, our first visitor will hear us in-"
    robin "About six and a half years..."
    show robin sick with dissolve
    narrator "The icy terror gave way to a lukewarm blanket of static over everything. I felt lightheaded, my hands and feet were barely there. I felt like a ghost."
    robin "Even the most- Most optimistic crew-"
    show robin angry with dissolve
    narrator "Beneath it all, a hot buzz of muffled rage wells up inside. Why us? Why me?!"
    robin "They won’t even bother to wave at us out the damn window after seeing a six-year-old timestamp. Fuck. Fuck!"
    narrator "The carousel of emotions swinging through me starts to slow down, and cold nausea begins to twist my guts into knots."
    show robin sick with dissolve
    robin "I think I’m gonna be sick."
    narrator "I do get sick. Right into the water."
    harper "I- I am sorry, Robin..."
    robin "It’s, uh..."
    show robin pain with dissolve
    narrator "I finish gagging and spit. Spit again. I don’t want to waste any more precious water rinsing my mouth out so I just sit there. Tasting bile."
    robin "Don’t apologize. It’s- It’s my fault anyway."
    harper "You do not know that."
    robin "My shift, my responsibility."
    harper "The astrogation computer is just as fallible as you."
    narrator "It wasn’t, but I decided beating myself up wasn’t going to help things either."
    show robin bored with dissolve
    robin "OK. I’m- Okay, I’ll- We’ll-"
    robin "Uh, yeah, something..."

    narrator "There’s a long silence. The water moved up the sand, down the sand. Up, down. It wrapped around my feet. I felt myself sinking a little with each passing wave."
    narrator "I recognized that sensation of depression, it was threatening to freeze me in place, so I did the only thing I could do. I started moving."
    narrator "I walked. Slowly at first, then briskly. Trying to get my thoughts moving too."
    show robin surprised at hop
    narrator "I jump a little when Harper suddenly starts talking again."
    harper "I am currently considering the best course of action, but I need some time."
    show robin neutral with dissolve
    harper "I am afraid the damage to the reactor is cramping my style."
    narrator "I stop walking."
    robin "I’m sorry, where in the world did you learn that expression?"
    harper "The internet. The damage limits the power I can draw down, which in turn limits my creativity. In short, my ability to make effective plans is reduced. Hence, my style is cramped."
    narrator "In spite of myself, in spite of the panic seeping out of me, I can’t help but give a wry grin. And for the first time I feel a hint of something like we might be okay."
    robin "And so is your sense of humor, looks like."
    harper "We will have plenty of time and processing power for decent jokes after we get off this rock."
    robin "This wet, sandy rock."
    harper "Quite."
    narrator "I feel my panic beginning to retreat."
    robin "Okay, okay-"
    narrator "A low buzz of anxiety still hums beneath everything. But now, instead of paralyzing me, it electrifies me."
    narrator "Suddenly, I’m back in control. Every little discomfort weighs on me. I do a quick inventory, then snap my head up towards the jungle."
    show robin happy with dissolve
    robin "Well... We gotta think. And you can’t exactly think on an empty stomach."

    stop ambience fadeout 4.0
    scene black with fade
    pause 4.0
    harper "Glad to have you back, Rob."

    # new scene
    play ambience "beach ambience.mp3" fadein 4.0 loop
    scene bg beach with fade
    show smoke with dissolve
    show robin neutral at midright with dissolve
    play sound "trudge sand.mp3"
    pause 5.0

    show robin surprised at hop
    narrator "My toe caught on something hard and I nearly fell flat on my face. I reminded myself that I was still relearning how to balance, but it was cold comfort."
    robin "Breaking my damn ankle is exactly what I don’t need right now."
    show robin neutral with dissolve
    narrator "I resolved to slow my pace and proceed with more care. I dropped my eyes to the ground, seeing the rock I tripped over."
    narrator "Something else caught my eye. It was round and dull red, about the size of my head."
    narrator "I reached down and clutched it with one hand to lift it. It had a surprising heft to it."
    narrator "Its shape curved into two dull ends, like an egg with two tips."
    robin "Please don't {i}actually{/i} be an egg."
    narrator "I give it a gentle squeeze and my fingertips sink into it easily. A little something leaks out and stains my gloves. I can feel my gloved fingers sticking to the surface."
    narrator "A sweet scent wafts into my nose. I could feel my mouth starting to water."
    harper "Did you find something?"
    robin "Yeah. It’s some kinda fruit, I think."
    harper "Are you sure? It could be an egg. Some animals are known to have eggs with malleable skins."
    show robin pain at hop
    narrator "The hairs on my neck stood on end as I thought about what kind of creature could lay something like this."
    narrator "I didn’t like the idea of being trapped on a planet with anything crawling around on it, let alone something that could squeeze out an egg this huge."
    narrator "Imagining a horrible, slavering monster lurking above me, I looked up into the trees and spotted more clutches of the same round, red fruits hanging from the branches. I let out the breath I didn’t know I was holding."
    robin "No, looks like it’s definitely fruit. Unless trees lay eggs here. Thanks for that lovely image, though."
    harper "Any time."
    show robin neutral with dissolve
    robin "So, can I eat this?"
    harper "I do not know. Perhaps you could try it."
    robin "Funny."
    harper "If I was being funny, you would be laughing. In all seriousness, you will have to eat something if you’re going to survive."
    robin "I’m a good eater, so I can last at least a few days before I start getting weak from hunger."
    harper "Can you reach the ship by then?"
    narrator "I looked at the vast stretch of ocean between the ship and myself."
    robin "I have to cross water to reach you, there’s no other way, and I have no idea how I’m going to do that"
    harper "Then it’s all the more important to start identifying edible food before you get desperate."
    robin "I see your point, but is it really a good idea to start putting things in my mouth and hoping I don’t get sick? If I get sick I’ll just end up dying faster."
    narrator "Harper was starting to get a bit exasperated with my arguing."
    harper "You just have to accept there will be some risk of a virus or bacterial infection. As for testing if a substance is toxic, I recommend working up to it in stages. Gradually increase your exposure and wait to see if you get sick."
    robin "You mean if I find something that looks edible I should lick it first?"
    narrator "I said this with all sincerity, and clearly Harper could tell because it actually {i}sighed{/i}."
    harper "No. You want to be confident it will not get you sick before it goes anywhere near your mouth."
    narrator "I noticed it said ‘confident’ and not ‘certain’."
    harper "I recommend exposing some of your skin to the fruit’s juices first. Just a drop will do."
    robin "Huh... OK, makes sense."
    narrator "I set the fruit down for a second to pull one of my gloves off, then wiped the dripping fruit against the back of my hand."
    robin "Done. Can you set a timer please? A few hours will do."
    harper "Already ticking."
    narrator "I spent the time gathering more of the fruits. Some are so soft they fell apart in my hands."
    narrator "Slowly, the pile of fruit grew."
    show robin surprised at hop
    narrator "I bent to pick up another and something {b}skittered{/b} out from under it!"
    robin "WAGH!"
    narrator "I jumped so high I found myself partway up a tree. It swayed gently from  side to side under my weight."
    narrator "I realized Harper was talking to me."
    harper "Rob, speak to me! Are you okay?!"
    show robin neutral with dissolve
    narrator "My breathing was starting to slow, and I slid down the tree. I realized how I must look and I could feel my face starting to burn."
    robin "Uh, yes... Yes! Yes, all fine!"
    harper "Are you sure...?"
    narrator "It must have sensed my embarrassment because some mirth had crept into its tone."
    robin "I saw something. It was small, and alive, and fast."
    harper "Oh my. Is it edible?"
    show robin angry at hop
    robin "How should I know?!"
    narrator "I huffed irritably."
    show robin neutral with dissolve
    robin "Anyway, I don't know where it went."
    narrator "I turn my attention to the fruit I was still holding. I roll it over in my hands and find a hole, a few fingers wide, bored in the bottom."
    robin "I think it was eating the fruit. That's got to be a good sign right?"
    harper "Perhaps."
    narrator "I saw something poke its head out of the hole in the fruit."
    show robin pain with dissolve
    narrator "This time, I didn’t hesitate. With a grimace I jammed my fingers inside and fished the creature out."
    narrator "I held the little bug between two fingers. It had a hard, black shell and two beady eyes. Its little legs waved around as it tried to escape my grasp."
    show robin neutral with dissolve
    narrator "I was hungry enough that I seriously considered taking a bite. I gave it a little whiff and my eyes began to water from the pungent, bitter stench that exuded from the little guy, so I tossed it away."
    narrator "I took a moment to rinse my hands off in the sea and scrub them with a bit of sand. I raised them, taking a  cautious sniff, and frowned at the awful smell lingering on my gloves."
    harper "Time."
    narrator "Had it already been hours? I rinsed my hands a few more times for good measure, then flicked the water off my hands and removed a glove to check the patch of skin I’d tested the fruit juice on."
    robin "Looks good. Time for a bite."
    narrator "I tromped back into the jungle to find my little fruit pile. I replaced my glove, then scooped up an intact fruit and pulled it apart gingerly."
    narrator "There aren’t any hitchhikers inside. The orange-yellow flesh drips with juice and fat, black seeds as my fingers sink into it."
    narrator "I tried pulling a chunk off but it’s too soft and I just end up squishing it around. Some globs of sticky fruit-flesh clung to my gloves, and I decided the best way to try it was to just slurp one up."
    show robin happy with dissolve
    narrator "It’s an explosion of sweetness in my mouth. A wave of pleasure washed over me and I desperately wanted to eat more."
    robin "Wow... That’s really good!"
    show robin neutral with dissolve
    narrator "I set the fruit down reluctantly, then walked down to the beach again to rinse off. I splashed water on my face and hands to get rid of the sticky feeling on my skin."
    narrator "The crash loomed in the distance, and suddenly a thought jumped into my head."
    show robin surprised at hop
    robin "Are the food stores intact?"
    harper "There were fires that have since been suppressed, and the main stores were totally destroyed."
    show robin neutral with dissolve
    harper "I can’t be certain since surveillance has been disabled due to power restrictions, but a small amount of supplies have likely survived. Did you leave any food in your cabin?"
    robin "Just some snacks, but even without the main stores the galley has enough for a few weeks. Maybe more if I stretch it."
    robin "We’ll just have to hope that’s enough time for me to do any repairs that might be needed. What I would give for just one bluespace-capable drone right now..."
    harper "Is the ship within swimming distance? Maybe you could reach me that way."
    robin "Spacers don’t swim. I know just as much about it as you do. ‘Swimming distance’ for me is just about nothing. I don’t see any other way to get there though. I’ll just have to get creative."
    harper "Mm..."
    narrator "I head off the beach towards the cover of the jungle outskirts. In only a few steps I was enclosed by greenery and I felt the sweltering air grow a few precious degrees cooler."
    narrator "Shafts of light shone down from overhead through chinks in the leaves. It was altogether weird, but the closeness of the space was comforting."
    narrator "I looked around until I found a sapling. I tried to snap a piece off, but it was surprisingly hard wood."
    narrator "With a little digging in the loose, sandy soil using my hands it was easy enough to uproot, though I was quickly starting to pour with sweat due to the heat and effort."
    narrator "I tore the branches away until I was left with a shaft that fit nicely in my fist. It was long, stiff, and had a nice heft to it. It made a satisfying thunk when I whacked it against a boulder."
    narrator "As I walked the short distance back to the beach, I’m not surprised to find my soft spacer’s feet starting to ache. I found myself wishing for my boots again."
    narrator "I waved the stick around. I’d never really played with water much, like I saw some people do in vids. For a lifetime spacer, fluids were precious resources, not a toy."
    narrator "But I was trained in formal math, I knew about the principles involved, and I figured that was enough. I kicked into the shallows and, with some anticipation, dropped the stick into the water."
    narrator "There’s a splash as it plopped into the water. The shallow water was clear like glass, and I saw it hang for an instant as it slowed and its natural buoyancy sprung it back to the surface."
    show robin surprised at hop
    narrator "I gave a startled squeak as it lunged out of the water, then an embarrassed chuckle bubbled out of me as I realized how silly I must have looked."
    show robin neutral with dissolve
    narrator "I thought back to my lessons on buoyant forces in my beginner physics courses, part of the standard education package everyone gets these days."
    narrator "I remembered that feeling of exasperation as I nibbled on an eraser, wondering that age old question: ‘when will I ever need to use this’?"
    narrator "`After all,` I thought, `if there’s no weight, then buoyancy doesn’t apply.`"
    narrator "Sure, most of the human population lived on artificial stations under some combination of microgravity and spin forces, but I always knew I’d be a spacer."
    narrator "Even if I didn’t have the itch, it was the only way for a rock-hopper’s kid to get out of the tunnel-slums that hollowed out the rings of a gas giant. A place I once called home."
    narrator "Only passenger liners had the luxury of a spin habitat; most freight companies or freelance long-haulers like myself didn’t want to waste mass on a centrifuge that could be spent on more cargo, more profit."
    narrator "Hence, it was common to rely on crews of full time spacers who spent their lives in null or microgravity."
    narrator "If you lived long enough to retire, you could easily afford the body mods and extensive medical care it would take to mostly reverse the consequences of such a life."
    narrator "Something in the water glinted at me, slashing through my thoughts. Perhaps if I hadn’t been staring at the bottom, lost in thought, I would have missed it."
    narrator "I scooped up the stick from where it floated next to me, dipped it into the water, and poked at the thing, wiggling it loose from the silty bottom."
    narrator "I bent and picked it up. It was a narrow, twisted grip of metal, no bigger than my hand."
    robin "Harper?"
    harper "Yes?"
    narrator "I turned the scrap over and over in my hands, examining it. I grasp either end of it firmly and give it a squeeze, feeling the flexibility."
    robin "Got a piece of the hull. Good start, I could probably-"
    show robin pain at hop
    robin "Ouch!"
    narrator "While I was feeling the edges, it slipped through my fingers, slashing through my glove and sending a tiny lance of burning pain through me."
    harper "Incident logged."
    show robin angry with dissolve
    narrator "I examined my cut with some annoyance. It was just a nick, but I cursed my carelessness. I bent to pick up the scrap where it had plopped into the water, holding it more carefully this time."
    robin "What are you going to do, assign me mandatory safety training?"
    harper "Apologies, it’s a reflex. More importantly, I have been studying the tides. The natural movement of this ocean is fascinating, and it could also provide some insights on the patterns of the breakup of the ship-"
    show robin surprised with dissolve
    robin "Oh! I thought you couldn’t see?"
    harper "I cannot, but I can ‘feel’ using the pressure sensors in the compromised, flooded compartments."
    harper "I am using the data to construct a predictive model. I may be able to save you some time if you decide to search for more salvage."
    show robin neutral with dissolve
    robin "Hm, OK. Keep at it. Maybe I can use your guesses to find the IEV. That’d be a godsend. In the meantime..."
    narrator "I hefted the stick meaningfully."
    robin "I think I might be able to build a, uh, raft—I think that's the word—a raft from what I’ve got lying around. It’s the "
    harper "First, I recommend trying a brief swim."
    harper "It would be useful to have some practice in the case that you fall from the vehicle and find yourself adrift."
    robin "Right..."
    show robin sick with dissolve
    narrator "I looked out at the water. As I imagined myself floating out there, halfway between the escape and safety, my throat grew slick with bitter apprehension."
    narrator "I didn’t know what else I’d do if this didn’t work. That big, blank stretch of water with its impenetrable surface seemed to hide every terror."
    narrator "I stood there, frozen, until I worked up the courage to step cautiously into the deeper waters."
    show robin neutral with dissolve
    narrator "I couldn’t feel much of a change through the insulation of the suit. Encouraged, I took a few steps further until the water came up to my knees."
    narrator "I kicked my toes through the water, feeling how it swirled and resisted my muscles. It was a fascinating sensation."
    narrator "Slowly, I went deeper and deeper into the water, building my confidence. I stopped when it reached my chest."
    narrator "I could feel the water taking my weight, its powerful bulk shoving and tugging me, threatening to scoop me up, and it took some effort just to stay upright."
    narrator "I let my feet leave the bottom and paddled around experimentally, making sure to always stay within reach of the shore."
    narrator "It was hard work staying afloat and the muscles in my already strained thighs and shoulders started to burn immediately. I longed for the feeling of microgravity, the relief of weightlessness."
    narrator "The hot sun beats down on my head and I decide to risk dipping my head under the water to cool off."
    narrator "I felt a tickling on my neck and face as the air between my skin and the suit was replaced by water flooding in through the gap at the suit’s neck where my helmet would have created a seal."
    narrator "The suit’s computer reacted to this by firing a signal that caused the suitskin to tighten almost imperceptibly, like a muscle tensing."
    narrator "I rose back above the surface, feeling much cooler. The salt in the water makes every scratch and scrape known with a mild, aching burn."
    narrator "I decided to stop for now, feeling certain now that I’d need a boat, and let the waves slowly carry me back towards the beach. I’m grateful for the chance to catch my breath and give Harper a brief update."
    narrator "As I floated on my back in the water, I found the rhythm of the waves strangely relaxing. If I closed my eyes it almost felt like I was back on a haul, just letting momentum carry us from one place to the next."
    narrator "Before I knew it, I could feel my back rubbing against the bottom, covering me in mud and silt. The silt oozed into my suit through every gap."
    narrator "I dragged myself onto the beach on my hands and knees and cursed the sand sliding down my back, sticking to my arms and getting into my underclothes."
    play sound "cloth rustle.mp3"
    show robin underwear with dissolve
    narrator "I strip down to my bra and briefs, leaving my suit crumpled beside me like molted skin."
    narrator "I tried my best to get as much of the gunk off of my skin as possible, but as soon as I thought I was finished, there always seemed to be more."
    play sound "cloth rustle.mp3"
    show robin suit with dissolve
    narrator "It was impossible to get rid of every grain, and when I finally zipped my suit up again the feeling of it pressing specks of grit into my skin is already driving me mad with discomfort."
    narrator "The day was wearing on, and I still needed to find a reliable source of fresh water. I turned towards the jungle and set off to explore it more thoroughly."

    stop ambience fadeout 4.0
    scene black with fade
    pause 4.0

    play ambience "jungle ambience 1.mp3" fadein 4.0 loop
    scene bg jungle day with fade
    show robin neutral at midright with dissolve

    # water search scene
    narrator "As the shadows were growing long and the sky turned red, I pushed through the overgrowth. The outskirts of the jungle gave way to a deep, thick carpet of green, forming impassable walls in places."
    narrator "I had to stop often to make marks on tree trunks with my scrap knife. I held it gingerly as I methodically created a system of signposts for myself. My entire body ached, but I pushed forward."
    narrator "I sucked on my hydration pack, but all I got was a mouthful of air. As the hike wore on, my mouth had gone from gummy and thick to dry and papery. Even just a little water would be a godsend."
    narrator "Then, just at that moment, something cold splashed onto my head. I leapt back in shock, wiping my forehead and looking up to see what hit me."
    narrator "I saw something dripping from above. There was a little water trickling down from one of the trees overhead."
    show robin happy at hop
    narrator "Excited, I removed a glove and carefully reached up above me, feeling around to find the source. My fingers ran over some large leaves and came away wet."
    play sound "water handling.mp3"
    narrator "I tipped the leaf gently and let a little fluid spill into my cupped palm, bringing it up to my eyes to see."
    narrator "It looked like perfect, cool, clear rain water. Not your ordinary water, mined from ice buried in filthy rock that you slopped out of a tap. This was the kind of water you see in ads."
    narrator "Perfect, pure, artisanal water imported from only the finest underground springs back on Earth." 
    show robin neutral with dissolve
    narrator "My hand shook as I fought against the overwhelming urge to gulp it down. I forced myself to use some caution. What if it had soaked up invisible poison from the surface of the leaves?"
    narrator "The reclaimer in my suit could filter out anything dangerous, but the designers didn’t envision this use case. There was no way to directly add water to the system."
    play sound "water handling.mp3"
    narrator "The best I could do is pour the water into my suit, let it soak into the liner as my sweat would, and hope that it filtered out anything dangerous."
    narrator "If the leaf was coated in some toxic residue, surely it’d be better off on my skin than in my stomach?"
    narrator "After consulting Harper, it pointed out that the system was bottlenecked by throughput."
    narrator "The reclaimer was carefully designed with the upper limits of human perspiration in mind, so increasing the input wouldn’t also produce a higher output unless I was so dehydrated I stopped sweating and passing urine."
    narrator "So much for that idea. I gingerly poured the water back into the leaf, hoping to come back for it later."
    narrator "This spot was cooler than the beach due to the thick overhead cover from the trees, intertwined and overlapping. There was even a light breeze, and the cool lick of a breeze on my face felt incredible."
    narrator "It reminded me of the end of a work day, standing in a state of undress in front of the A/C after a long shift."

    scene bg jungle night with dissolve
    show robin neutral at midright with dissolve
    play ambience "jungle ambience 1.mp3" fadein 4.0 loop

    robin "Not a bad place to bed down..."
    narrator "I took a short break, then hiked back to where I’d stashed the fruit and took some time moving them to my new camp. After that tough swim, even this effort revived the burning sensation in my muscles."
    narrator "I was forced to leave a few fruit behind that had some of those stinky nibblers hiding inside."
    narrator "I thought briefly about burying the ones I brought to avoid more losses, but the thought of eating sandy fruit made me discard the idea."
    show robin neutral at hop
    narrator "I sat down and forced myself to eat another one of the red fruits. It was tasty, and kept my thirst at bay, but my stomach still felt tragically empty."
    narrator "I suddenly had a powerful craving for one of the meal replacement shakes that I had grown to loathe after years of using them to fuel myself on spacewalks."
    narrator "I sipped the little water that had been reclaimed since I last drank from the hydration pack, hoping to bury the hunger by filling my stomach with something, anything."
    show robin bored with dissolve
    narrator "My eyes suddenly felt heavy as lead. The exhaustion from the day’s events had caught up with me. I slumped down onto my back and rested my head on the sand."
    narrator "I sluggishly turned my head, examining my surroundings, and considered gathering some nearby leaves or grass to make the rough, hard ground a little more comfortable."
    narrator "I managed to gather a mere handful of leaves before I gave up, too exhausted to accomplish even this small task."
    narrator "With one last burst of effort I forced my deadened arms to brush the larger rocks and pebbles aside before I began to slip away into sleep."
    
    show black with dissolve
    stop ambience fadeout 4.0
    pause 5.0

    hide black
    play ambience "jungle ambience 1.mp3" loop
    show bg jungle night
    show robin neutral at hop
    play sound "cloth rustle.mp3" volume 2.0
    harper "Robin? Robin, you need to stay awake."
    show robin pain at shiver
    robin "I- I can barely move. There’s nothing more I can do about water today."
    harper "That is one concern, yes. I understand that it is currently daytime, and I am worried about how you’ll cope with the low temperatures during the night on this world."
    narrator "I felt a shiver ripple through me."
    robin "Damn it. You’re right. I’m sorry, it’s hard to think."
    harper "Is there fuel nearby? Something you can burn?"
    narrator "Spacers had a lot to fear. Being in a confined space surrounded by electrics and volatile fuels, fire was perhaps chief among them."
    narrator "Even the air was engineered carefully to prevent fires, the mixture balanced just on the edge of what a human could cope with."
    narrator "On your typical spacecraft or orbital there was so little oxygen that you could barely get a joint or a cigarette lit properly."
    narrator "So, I knew quite a lot about putting fires out, but not much about setting them. I shook my head doubtfully."
    robin "Well, there’s plenty of fuel, but my lighters are all back on the {i}Selkirk{/i}."
    harper "That will not be necessary. There are several methods that I have researched. One in particular comes to mind."
    robin "Wait, you researched fire starting? Why?"
    harper "Well..."
    narrator "It actually managed to sound sheepish. My curiosity flared."
    robin "What? What is it?"
    narrator "It was quiet for a while. Finally, it answered."
    harper "There was a scene in {i}Zone Troopers{/i}-"
    robin "The- The retro sci-fi series?"
    harper "Yes."
    robin "The one where Johnny Target uses collapsed antimatter, a quantum 3D printer, and medicated dental floss to build a raygun?"
    harper "I am on the Ankhlord arc right now, I want to find out what happens on my own. Yes, I am still holding out hope that I will get to finish it, so now you have yet another reason not to disappoint me."
    narrator "It said that last part like it was quoting its favorite episode. I suppressed a giggle."
    robin "And here I thought you had better taste than me."
    harper "I would have rather you kept thinking that. Now you know my shame. At any rate, there was a scene where they roast a pig while they’re stranded on the pirate moon."
    harper "I wanted to see how realistic it was, and I still have a few anthropological papers in my buffer."
    robin "Was it?"
    harper "Was it what?"
    robin "Realistic."
    harper "To my surprise, yes."
    narrator "Harper imitated the sound a human would have made if they cleared their throat."
    harper "You have a piece of the hull, yes?"
    narrator "I fished the scrap knife out of one of my suit’s pockets."
    robin "‘Course. Why?"
    harper "If you shave particles off of the metal, they'll combust on contact with the air, giving you a nice spark."
    narrator "I nodded slowly. I was starting to follow its line of thinking."
    robin "Same principle as aluminum powder reaction mass in early solid rocket fuel, right?"
    harper "Precisely. You will need something else that is sharp and as hard or harder than the metal you are striking."
    robin "I’ve got just the thing."
    narrator "I remembered passing some quartzite on the way to the camp. You can’t help knowing a thing or two about rocks growing up the way I did."
    narrator "I’d heard plenty of stories on my mom's knee when I was a little sprout, rockhoppers are always yapping about the work, and how that quartz can take your flipping head off if you're even half careless with a pop-charge."
    narrator "Having caught my breath, I thought I had one more push left in me. I slowly regained my feet and started walking, wobbling as I went."
    narrator "It’s a mercifully short walk, and in no time I've found a small boulder that's the sort I need."
    narrator "Using what little strength I have left, I heft it over my head and crack it against another rock."
    narrator "It splits into a few large pieces. I knap the rocks carefully, just like mom showed me, until I have a fragment with one sharp edge that fits nicely into my palm."
    narrator "I gather an armful of dry leaves, twigs, and thick branches before heading back to camp. I toss my fuel to one side and plop down, taking my rock knife in one hand and the steel knife in the other."
    narrator "My hands were shaking from the strain on my muscles. I wanted so badly to just lay down and sleep."
    robin "Just a little more..."
    narrator "I point the tip of the steel knife towards the crumpled, dry leaves I was using as tinder."
    narrator "Then, I aimed the rock’s edge at the steel, holding the rock at a fairly shallow angle as if I were preparing to shave it with a razor."
    narrator "I gave it a firm smack and I surprised myself with just how many sparks are thrown by the blow. Most of the sparks missed the tinder and were wasted. I adjusted my grip a little and tried again."
    narrator "It wasn't as easy the second time as I'd made it look before. I was just about to give up when I managed a good blow that sent a jet of sparks spattering against the leaves."
    
    show bg jungle night fire with fade
    
    narrator "The leaves smoldered, and I did exactly what Harper said the marines did in {i}Zone Troopers{/i}. Build it up, just a little at a time... Don’t rush... In no time, I had a roaring fire."
    narrator "I dropped my tools and rolled onto my back. I laid there quietly for a moment, groaning at my aching bones and knotted muscles."
    robin "There... Done..."
    harper "Well done, Rob. Get some rest now, you’ll need it."
    robin "Thanks, Harper... Goodnight..."

    # day 2
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day with fade
    show robin neutral at midright with dissolve
    show rain with slowdissolve
    
    narrator "I woke to a pattering sound. I groaned and pulled myself to my knees to look around. Warm, red light shafted through the canopy overhead. I had slept through until morning."
    narrator "As I looked up, I noticed the leaves overhead bouncing and I could see waterfalls of rain had formed all around me."
    narrator "It was something I’d only ever seen or read about in fics. The water felt so warm on my skin that I didn’t even realize I was getting wet at first."
    narrator "I always thought it would be cold and stinging, I never thought it could be this soft, this gentle..."
    play sound "cloth rustle.mp3" volume 2.0
    show robin pain with dissolve
    narrator "As I rose to stand up, I could feel painful pinpoints of pressure on the soles of my feet. I lifted one leg to feel the sole of my foot through the suitskin, and I could feel the large blisters that had formed on either foot."
    narrator "I frowned. I'd had them on the tops of my feet before, from the friction of hooking my toes into railings to anchor myself during my workday. Never like this, though."
    narrator "Once (and only once) I'd taken a passenger aboard our freighter. A dirtsider, someone who'd never left the gravity well they called home. The kind of person I didn't care to know or remember."
    narrator "One thing I'll never forget, though, is the thick callouses she had on her feet from walking on the ground for 40 years standard. I was just as surprised as she was when, about a week underway, they sloughed off like gloves."
    narrator "She never once complained about the nausea of weightlessness, the frustration of learning to move without walking, but when she saw how smooth her feet had become, she wept and moaned. I think she was ashamed."
    narrator "I think, in some small way, I understand how she felt now."
    narrator "Taking ginger steps, my body still sore from yesterday, I looked for something to catch the rain. I remembered the leaf and that pure, beautiful water and in no time I’d gathered an armful of leaves."
    narrator "They had a natural curve and stiffness to them that made for a nice, shallow bowl."
    show robin neutral with dissolve
    narrator "I went to a spot where there was a decently-sized clearing not far from my camp and dug a few rows of small divots in the sand. I placed a leaf carefully in each divot to keep it from rolling over."
    narrator "A couple of the leaves blew over in the breeze anyway, so I took a moment to weigh them down by dropping small rocks in the middle of each one."
    narrator "I grabbed another one of the red fruits. It was already starting to get mushy and, not wanting to waste the precious food, I ate everything I had left. I didn’t leave so much as a scrap behind."
    narrator "I took a minute to plan my next move and let my food settle."
    narrator "My ultimate goal was to reach the {i}Selkirk{/i}; to do that I needed some kind of boat or raft. That project itself was going to take materials, tools, and the nutrients and water to keep myself alive."
    
    robin "Harper, I’m going to check the surrounding area for water, and while I’m doing that I need your help cataloging plants."
    harper "Of course."
    narrator "I was afraid to venture far from my camp. The island was fairly flat and if I were to wander into the overgrowth, I wouldn’t have any reference or landmarks to navigate by."
    robin "Harper, are you still picking up my location through my implants?"
    harper "Yes, though, as you know, it is not very precise. The best I can do is tell you if you are getting closer or farther away."
    robin "OK, so if I lose my way, you could at least guide me back in the general direction of the beach."
    harper "Yes. Pay attention to and report landmarks."
    robin "I suppose if all else fails, I do know that the sun sets on the {i}Selkirk{/i}."
    harper "Ominous... Good luck, Robin."

    #todo: transition
    play sound "walk sand.mp3" volume 1.5
    narrator "I hadn’t been walking long before I saw something new. Not far inland, tall, stemmy grass sprouted up from the ground."
    narrator "I stopped when I noticed some places where the grass seemed different. I looked closer, and saw the injured ends of the grass were frayed."
    show robin surprised with dissolve
    robin "Huh, something fed here..."
    harper "An animal?"
    robin "Hopefully it's just insects... Little ones..."
    show robin neutral with dissolve
    narrator "I bent to grab an untouched patch of grass, and it took some effort to rip it out of the ground."
    narrator "I looked closely at the individual blades of grass, each one a little shorter than my arm, and thought about what kind of creature must have been grinding its teeth through this stuff."
    narrator "I saw some fraying again where I’d ripped the grass and I teased at it a bit with one finger."
    narrator "I snatched one of the threads and pulled at it. It sliced neatly through the green hull of the grass until it came free."
    narrator "I’d never done it with such small threads, let alone something organic; wires sprout more readily than grass on starships."
    narrator "I was trained to make simple cordage by hand. One thing a spacer could never be without is a tether, after all."

    robin "Log this as {i}ropegrass{/i}, please. Description follows."
    narrator "I wasn’t anything close to an ethnobotanist, so it was an exercise in observation. Harper’s data-oriented mind came in handy here."
    harper "Logged. A very creative name I must say."
    robin "I’d love to see you do better. Too bad I can’t eat sarcasm."
    harper "Indeed. I do have a lot of that in supply."
    play sound "cloth rustle.mp3" volume 2.0
    show robin neutral at hop
    narrator "As I played with the grass, I crouched to get a little more comfortable - only to wobble as the ground squished under my shifting weight."
    show robin pain with dissolve
    narrator "Peering at my feet, muddy water oozed up around my feet as if I was standing on a big sponge."
    narrator "I stepped away, and I could see water puddling in my footprints."
    narrator "The ropegrass forgotten, I dropped to my knees and plunged my hands into the soft ground, throwing aside globs of sticky earth."
    narrator "I dug a little hole, only a few hands deep and just as wide, and waited patiently. Slowly, almost imperceptibly, the hole filled as groundwater percolated through its walls. An intoxicating joy mulled my brain."
    show robin surprised with dissolve
    robin "It’s water! Filthy, nasty puddle-water, but it’s water!"
    harper "That is excellent to hear, Robin."
    narrator "I still had a stupid grin smeared across my face when it occurred to me I had nothing to carry the water with. Rather than souring my mood, the thought nudged it into a good-natured puzzlement."
    show robin neutral with dissolve
    narrator "This seemed a much simpler problem, and my brow creased with thought as I crouched over the puddle, hugging my shoulders and humming tunelessly as I waited for insight to rise from the mud like a golem."
    narrator "An idea came to me, and my stomach turned a few flips at the thought."
    robin "Harp... Is there a procedure for cannibalizing the water reclaimer?"
    narrator "There was the briefest hint of an instant of a pause. It could have been that Harper was taking a touch longer to perform the usual searches because it was rationing power, but hesitation wasn’t exactly off-spec."
    harper "I do not recommend it."
    show robin surprised with dissolve
    robin "Is it possible?"
    harper "That should not be the first question you ask."
    show robin neutral with dissolve
    robin "How else am I supposed to purify the raw water I find?"
    harper "You can boil it."
    robin "Don’t have anything to carry it in, unless I use the bladders from the reclaimer."
    harper "You cannot sacrifice your only reliable source of water."
    show robin pain with dissolve
    narrator "I grimaced a little in frustration."
    robin "Harp, my head is pounding. I can’t find reliable alternatives if I’m dying from dehydration."
    narrator "Another one of those brief pauses."
    harper "Hm. Very well. I will walk you through the procedure."

    narrator "It was my idea, but my stomach still churned at the idea of salvaging the filtration unit."
    narrator "It’d mean cutting into the liner of my suit too. It did a pretty good job of keeping me cool and cutting it would compromise that."
    narrator "I grit my teeth, choking back the doubts. I knew I needed water, nothing is more important than that right now."
    play sound "cloth rustle.mp3" volume 1.5
    show robin underwear at shiver
    narrator "I started taking off my suit. I’d done my own suit’s maintenance a thousand times, so I only needed a little guidance from Harp before I knew exactly where to start."
    show robin neutral with dissolve
    narrator "Using the scrap knife, I made conservative incisions as I dissected my suit. The tip slid soundlessly through the rubbery, synthetic liner, like so much whale blubber."
    narrator "Feeling blindly with my fingers, trying not to tear the liner, I teased out the suit’s innards. I laid the filtration system out on the suit liner to protect it from the dirt."
    narrator "The translucent organs and coiled lines of the system, slick and wet, looked like the guts of some strange creature."
    narrator "The system was capable of storing a total of a liter of potable water in a pair of flat, plastic pouches that conformed to the contours of the suit."
    narrator "One pouch was embossed with the word ‘INTAKE’ and the other ‘OUTTAKE’. Each was small and had an awkward, folded shape when laid out flat. It looked like a set of deflated lungs."
    narrator "I found the sets of fluid tube connections on the pouches, there being one tube for inlet and another for outlet on each pouch, and slashed them down to finger-length stubs."
    show robin at hop
    narrator "I tugged firm, but easily undone, knots into each stub, so there could be no leaks."
    play sound "cloth rustle.mp3" volume 1.5
    show robin suit at hop
    narrator "I dragged my suit back on, then used lengths of scrap tube to fashion a sling for each pouch."
    narrator "They’d be easy to fill and drink from since each tube had a plastic neck and could be decoupled, so the tubes or pouches could be replaced, I guessed."
    play sound "water handling.mp3" volume 1.5
    narrator "I dipped each pouch into the hole and pressed it down below the surface of the water to let gravity fill it up."
    play sound "water handling.mp3" volume 2.0
    narrator "More water trickled willingly into the hole even as I took my fill. When the pouch was full however, I could see the water level was lower than before. I might have to dig the hole deeper later."
    narrator "The water I’d gathered was surprisingly clear, but still cloudy. Looking at the filtration components I’d left on the ground, I didn’t see a simple way to use those."
    show robin neutralClosed with dissolve
    narrator "I’d have to boil the water, but heating the pouch over the fire would just melt the plastic."
    show robin pain with dissolve
    narrator "My mouth was dry and my head throbbed with an ache that was hard to ignore. The thirst had been getting to me for the better part of the past few hours."
    narrator "I didn’t want to think about how long I could go on feeling this way."
    
    robin "Alright, so... How do I boil water without a bowl?"
    harper "Why do you need a bowl?"
    show robin sick with dissolve
    narrator "It was a frustrating question."
    robin "Why else? So I can bring the water to the fire and heat it up."
    harper "I do not see why you cannot heat the water in the hole."
    show robin neutralClosed with dissolve 
    narrator "I was perplexed and annoyed at Harper’s naive idea."
    show robin angry at hop
    robin "How the hell would that even work? I can’t just drop burning wood in the puddle."
    harper "Of course, that’s why you should use a medium to store and transfer the heat. Something conductive."
    show robin neutralClosed with dissolve
    narrator "The simplicity of the idea shocked me."
    show robin neutral with dissolve
    robin "Wait, okay, I see where you’re going with this. Hang on, I’ve got an idea."
    play sound "water handling.mp3" volume 1.5
    narrator "I dumped the water from the pouch into the little well and started scrounging up sticks and branches and other fuel. Soon I’d built a decently-sized fire only a few feet away."
    
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day fire with fade
    show robin neutral at midright with dissolve
    
    play sound "walk sand.mp3" volume 1.5
    narrator "One brisk walk later and I’d returned to the well with a leafy branch that I had lit in my original, rekindled camp fire."
    play sound "fire crackle.mp3" volume 1.5
    narrator "I dropped the flaming branch into the fuel and waited for the flames to catch. Meanwhile, I found a few fist-sized stones and dropped them as near to the flames as I could manage."
    narrator "While the stones were heating, I looked for a sapling. I used my hands to snap the stem away and then plucked off all the thin branches."
    show robin pain at hop
    narrator "I set my the blade of my scrap knife into the end of the sapling, then drove it home with a blow from a rock, splitting the stem into a pair of makeshift tongs."
    narrator "Once the rocks were glowing red hot, I used the tongs to snatch them up and drop them one at a time into the puddle with a wicked hiss."
    narrator "By the time I dropped the third rock in, the puddle was bubbling so fiercely I had to back away to avoid getting splashed."
    play sound "water handling.mp3" volume 1.5
    narrator "I dipped each pouch in with the tongs to disinfect it. I waited patiently for the water to stop steaming, meanwhile building up the fire to prepare another batch, then dipped my pouch in once more to fill it."
    show robin sick with dissolve
    narrator "The water was still, disappointingly, cloudy. But apparently safe."
    play sound "water handling.mp3" volume 1.5
    show robin painClosed with dissolve
    narrator "I raised the pouch to my lips and gave it a cautious sip. I made a face. It was lukewarm, with a slightly metallic, musty aftertaste. I drank it greedily in spite of that, not wasting a drop."
    show robin at hop
    narrator "I repeated this a couple times until I drank my fill. Afterwards, the hole was more or less dry and my pouch was about half full with drinkable water."
    show robin neutral with dissolve
    narrator "Just as I’d filled one need, another came to the surface. All that work left me feeling hungry, and I hadn’t a thing to eat. I set my eyes on the bush surrounding me before plunging off to find something to eat."

    # search for food
    play sound "walk sand.mp3" volume 1.5
    narrator "After all this time I’d spent exploring  I was starting to get a good understanding of the terrain."
    narrator "I stopped briefly to make a little diorama in the sand, just to cement the idea in my head."
    scene cg diorama with fade

    narrator "So there was the beach, the jungle outskirts where I’d made my camp, the low lying swamp area further inland where I’d made my well, and thick jungle beyond that I had yet to venture into."
    narrator "The highlands near the center of the island and the wreck of the {i}Selkirk{/i} out in the water were both visible from a distance and made for good landmarks."

    # show previous background
    
    play ambience "beach ambience.mp3" fadein 3.0
    scene bg beach with fade
    show robin neutral at midright with fade
    
    play sound "walk sand.mp3" volume 1.5
    narrator "The humidity under the jungle canopy was starting to get to me, so I resolved to take my expedition back towards the beach where I could at least take in a breeze."
    narrator "As I reached the border between the jungle and the sand of the beach, I walked along the edge of it to take advantage of the shade of the occasional tree."
    show robin neutralClosed with dissolve
    narrator "The sun was setting, warming the horizon to a comforting orange glow. My hair was matted with sweat and so the caress of the breeze felt all the more cooling. The sensation was incredible on my flushed skin."
    play sound "cloth rustle.mp3" volume 1.5
    show robin neutral underwear with dissolve
    narrator "I looked around shamefully, as if there was anyone who could have seen me, and carefully set down my water pouches so they wouldn’t spill, then threw off my suit and underwear both."
    play sound "walk sand.mp3" volume 1.5
    narrator "I turned and faced the sea, spreading my legs and arms wide so the wind could slide over every part of me."
    show robin happyClosed with dissolve
    narrator "The relief was astounding as I turned and turned, letting the breeze reach into me and caress every hidden spot on my body. I felt the heat leaving me like one long sigh."
    narrator "My clothes had been squishy with sweat and, even as someone who was used to suffering for hours in my suit on an EVA with no relief, the discomfort was maddening."
    play sound "cloth rustle.mp3" volume 1.5
    show robin neutral with dissolve
    narrator "So I spread the suit out wide and turned out the liner, hoping to dry it out some in the wind."
    narrator "I held my scrap knife for a moment, considering keeping it for defense. In the end, I set that down next to my suit as well."
    show robin neutral at hop
    narrator "I stood again and, feeling refreshed, set out to walk the beach while my things dried."
    play sound "walk sand.mp3" volume 1.5
    narrator "I walked, and walked. I was excited to see that the tide had washed more scrap ashore, and I took some time to snag the more useful pieces I came across."
    show robin happy with dissolve
    narrator "I found a couple pieces of concave, hard plastic that were almost as wide as my shoulders, and another large piece of jagged metal scrap."
    robin "Never thought I'd be so happy to be picking garbage..."

    narrator "Being components of a space vessel they were rather light, even for the feeble arms of a spacer, but their bulk made them troublesome to haul nevertheless."
    narrator "Rather than haul them back to where I’d left my suit, I stopped to lean the scrap upright against a tree where they would be conspicuous and easy to find again."
    narrator "As I was walking I'd been looking up into these same trees, hoping to see more of that juicy, redfruit. Every one I passed was tragically bare, the ripe redfruit having fallen to be preyed on by swarms of the stink beetles."
    narrator "Every redfruit I turned over had a hole chewed into it and at least one beetle inside chewing away, gnawing away any hope I had of finding something to eat."
    play sound "walk sand.mp3" volume 1.5
    show robin pain at hop
    narrator "I tried fishing the beetles out of some of the more intact redfruits and rinsing the flesh in sea water to try and get the stink to go away."
    show robin pain with dissolve
    narrator "After some cautious testing, I found the bitter taste not only remained, but was made even worse by the overpowering taste of salt."
    narrator "I tried the same sort of test with the beetle itself, but the smell was so foul that I couldn’t even hold it up to my face. I had to walk down to the beach again and rinse my hands over and over until the smell was bearable."
    show robin at shiver
    robin "It’s impressive how good these guys are at not being eaten."
    show robin surprised at hop
    narrator "That’s when it occurred to me, that this was a {i}defense{/i}. You only need a defense if there’s a threat, I thought, and I suddenly missed my knife."
    show robin neutral with dissolve
    narrator "If there are defenses, there must be predators. That could mean food for me. But how would I find them?"
    show robin neutralClosed with dissolve
    narrator "If I was a creature that ate beetles, wouldn’t this time, when the ripe fruit fell and the beetles came out of their hiding places to feast, be the perfect time to find prey?"
    show robin sick with dissolve
    narrator "A small, frightened part of me asked: what if this defense is so potent that all their predators have gone extinct? That means nothing to eat for me."
    narrator "The cold, logical part of me argued back: these trees are everywhere, so there must be something that eats enough of the beetles that the trees can survive and breed."
    show robin neutral with dissolve
    narrator "The trees live on with no obvious defense, so there must be a predator."
    
    scene cg doglike with fade
    
    play sound "doglike yaps mild.mp3" volume 1.0
    narrator "That's when I saw it, a small, bulbous creature with a fat, innocent face. It reminded me of a dog the way its eyes were wide and wet with emotion."
    narrator "It stood on two spindly legs and had rubbery, moist flesh like a frog. It was surprisingly brightly colored, with large, irregularly-shaped spots all over."
    narrator "Though it must have heard me gasp when I saw it, it wasn't paying the slightest attention to me."
    narrator "My mouth started to water at the prospect of meat. Delicious, succulent, fatty meat."
    narrator "I could grill the cuts on a rock, flip it over and over with a stick until it was tender on both sides. My mouth was making so much saliva at this point that I had to keep swallowing."
    narrator "I was frozen, not wanting to frighten the creature as it snuffled among the grass and rotting redfruit. Curiously, it chewed up one stinkbug after another, not seeming to notice their pungent smell."
    narrator "I thought about how I would catch it. It was fat, and the way it ambled seemed lazy and carefree. Surely it couldn't outrun me. With a single minded determination, I started to creep towards the dogthing."
    narrator "It wasn’t facing directly towards me, and to my ears I was silent, but somehow, it knew. It turned and rolled its eyes toward me, its snout snuffling curiously."
    narrator "Did it read the murderous intent in my posture? Can it smell the hunger on my sweat?"
    narrator "I was shaking with desire. I couldn't let the first real meal on this island escape me. My body lunged towards it."
    play sound "run sand.mp3" volume 1.5
    narrator "It scuttled into the brush in an instant. It escaped with such startling speed and alacrity, and so very easily, that I gave up before the chase even began."
    
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day with fade
    show robin gaunt at midright with fade
    
    show robin sick
    narrator "Something in my spirit broke. I tried to summon up frustration, anger, something. But my mind was numb. I only felt my body."
    narrator "My feet hurt. My limbs were heavy, sore, and tired. And my head was pounding. I tried looking for some kind of sign of where it had gone, but it left no traces, not in the failing red light of the sun."
    narrator "I looked at the bugs again, wishing I could understand how that dogthing could swallow them without choking. Something in its saliva? Its stomach?"
    narrator "Either way, it probably wasn’t coming back here after I threatened its hunting place. I went back and plopped down next to my suit to rest and speak with Harper."
    robin "Would you believe me if I told you there are not only plants, but also animals here?"
    harper "Animals?"
    narrator "I described the creatures for Harper."
    harper "Oh! That is wonderful! They sound adorable. I wish you could snap a photo."
    show robin bored with dissolve
    robin "Why in the world would you want to look at a walking scrotum?"
    harper "Your vile turns of phrase are delightful. I must admit that I find their hideousness charming."
    robin "Do you have a favorite animal?"
    show robin bored with dissolve
    robin "What?"
    harper "They are like pigs, but with longer noses. The calves can have very cute striped and spotted coats. I like watching them graze."
    robin "Mm. So how do they taste?"
    harper "I really could not say."
    play sound "walk sand.mp3" volume 1.5
    show robin neutralClosed with dissolve
    narrator "While I spoke I slowly got to my feet and gathered up my things, pulling my clothes on slowly, groaning as I felt aches twang at my nerves. It was late and I was spent."
    show robin bored with dissolve
    narrator "I forced myself to gather more fuel and stoke the dying fire. I added some wood scraps, nudged it tenderly with a branch, nurturing it into a roaring flame that would burn through the night."
    narrator "The hunger gnawing at me made it hard to fall asleep that night. I lay sprawled out, my face to the sky. The glare from the fire turned the sky into a dark wet smear; not a single star."

    # day 3
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day with fade
    show robin neutral at midright with dissolve

    show robin painClosed at shiver
    narrator "Morning came. Dull, insistent pangs in my stomach woke me. I was dizzy and shivering. There was a mouth chewing at my insides, hollowing me out. Not sure if it was just from hunger, or if the beetles were a little toxic."
    narrator "I moaned in pain, cradling my stomach. I held my forehead against the ground until the world stopped tilting."
    play sound "water handling.mp3" volume 1.0
    show robin sick with dissolve
    narrator "I drank some water to try and fill my stomach with something. It wouldn't fill the hollow pit in my gut. I’d slept in my suit, so I only needed to grab my knife and water pouches and I was ready to go."
    play sound "walk sand.mp3" volume 1.5
    show robin at hop
    narrator "I wasted no time; I marched back to where the doglike creature had been grazing."
    narrator "The morning light was far better to search by, and there were no creatures, harsh winds, or other forces to interfere with signs."
    narrator "I approached the spot, taking a wide curve around until I could reach it without scuffing the doglike’s tracks."
    narrator "It didn’t escape with any special care, it was focused on speed, so it {i}must{/i} have left some evidence, I thought."
    show robin neutral with dissolve
    narrator "My eyes passed over the ground, searching. I realized I was looking mindlessly, without really thinking about what would be out of place."
    narrator "I looked at another patch of sandy undergrowth that I knew was undisturbed, and I etched it into my brain. I looked at how the grass lay, how the ripples in the sand were shaped, the curves of the leaves and low branches."
    narrator "When I turned back, small details began to emerge. A patch of bare sand where there should be leaf litter. Spots where the dirt was deeper than could have been dug by the elements."
    narrator "I learned to widen my gaze, not focusing on just one spot in particular, but seeing everything at once. I forgot my hunger and started to track, and hunt."

    # transition
    
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg highlands day with fade 
    show robin bored at midright with dissolve
    
    narrator "My walk took me deeper inland than I had been before. The ground grew hard, the trees giving way to low, scrubby brush as they struggled to push their roots into dry, rocky soil."
    narrator "The signs became more obvious still, until the spare tracks of a single doglike merged into pairs, then grew into a gaggle, a herd."
    narrator "The ground was packed and beaten flat by their little feet into a modest trail, like a scar on the earth."
    show robin happy with dissolve
    narrator "Elated at my discovery, I almost stepped onto the trail to follow it, then thought better of it. My feet left evidence as easily as theirs did."
    narrator "I kept off the trail. It was much easier going than in the jungle, where I had to worry about leaves and branches striking my face and eyes if I moved carelessly."
    narrator "I sensed movement ahead. Just a shadow, a smear of color shifting, but it was enough."
    show robin angry with dissolve
    narrator "Instantly, I dipped down out of sight. I crouched there for a moment, thinking, letting my breathing steady and slow, trying to suppress my excitement."
    narrator "I switched my scrap knife to my off hand and bent to snatch up a hard stone that fit neatly into my palm."
    narrator "If they let me get as close as last time, I felt confident I could hit one in the face. It might give me the opening I needed to-"
    narrator "What? Stab it? Cut its throat? I realized that I’d never killed anything before."
    narrator "I pushed myself forward before I could think about it too deeply."
    play sound "walk sand.mp3" volume 1.0
    narrator "As I crept through the brush, I carefully placed each footstep and stopped to push the brush aside and lower it gently back into place to avoid noise."
    narrator "Soon, I could hear the grunting and snuffling of something ahead. I peered between the leaves."
    
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg highlands day den with fade
    show robin neutral at midright with dissolve
    
    narrator "I was back far enough that I could only really see them when they moved, but the doglikes were there."
    narrator "As I drew near, I could see there were about six or seven of them milling around the narrow opening of their den."
    narrator "Their home was a burrow, its entrance nestled at the base of a small hill, tucked into a fork that gave them some natural cover."
    narrator "Most of the doglikes were small and even wrinklier than the big ones. Cubs, no doubt."
    narrator "There were two adults watching the cubs tussle and whine, occasionally lifting a cub or two into its mouth if it got too rowdy or wandered too far."
    narrator "I crouched there in the brush for a moment, thinking of how to approach this. The burrow looked far too small for me. If they fled in there, I’d never get them out."
    narrator "Before I could devise some kind of tactic, one of the cubs came stumping straight for me, grunting guilelessly. It hadn’t seen me, and for now its parents were busy with the other cubs."
    show robin angry with dissolve
    narrator "I cocked my throwing arm and waited, letting it get nearer. Sweat beaded on my forehead and threatened to drip into my eyes and spoil my aim."
    narrator "A screech of alarm rang out, cutting through my skull like a migraine. One of the adults had noticed me somehow, by smell, sight, or sound I didn’t know, and had pealed a warning."
    # TODO: sfx throw
    narrator "In the same instant, the cub froze in its tracks as I popped upright with a bounce and whipped my stone at it."
    narrator "I could tell my aim was off. My shoulder throbbed from the force of the toss. But the cub, in its panic, crabbed to one side, right into the path of my shot."
    # TODO: sfx thwack
    # TODO: sfx animal squeal
    narrator "The stone struck it square in the face with a satisfying thud, and the creature fell, twitching. I felt a whoop jump out of my throat."
    # TODO: sfx crash through leaves
    show robin at hop
    narrator "Excitement jolted through my limbs and I threw myself into the open, lunging towards the cub to finish it off."
    # TODO: sfx animal screech
    narrator "I heard another wild screech and looked to see one of the adults barreling straight towards me."
    narrator "I threw my knife into my strong hand and bent, intending to scoop the cub up into the crook of my left arm but snatched my hand away as the parent snapped at my fingers as it skidded to a halt, standing over the child."
    show robin at hop
    narrator "I cocked my leg back, back, and snapped my leg out in a sledgehammer of a kick."
    # TODO: sfx thud
    narrator "My toes caught the doglike under its chin, sending it careening into the rest of the pack as they scattered and retreated towards the burrow. Before they could rally and come at me again, I grabbed the cub and ran off into the cover of the brush."
    show robin pain with dissolve
    narrator "I ran, panting with the effort. The cub wriggled as it slowly came back to its senses. I shut my eyes and wrung it in my hands until something popped and it stopped moving. I felt a sob bubble up from my throat."
    narrator "Sure now that I wasn’t being followed, I slowed to a stop and dropped to my knees, panting. I tried not to look at it, but I couldn’t ignore the limp weight spilling over my arms. Hot tears streamed down my face and stained my cheeks."

    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day with fade
    show robin neutral at midright with dissolve

    # later
    play sound "walk sand.mp3" volume 1.5
    narrator "As I walked back to camp, Harper speculated about how to actually go about preparing and eating the creature I’d caught. I didn't say anything, but if Harper noticed, it had the grace not to mention it."
    narrator "After a long walk back, I felt the exhaustion setting in once more. The hunger pangs returned with a vengeance. I settled on Harper's suggestion to make a shallow cut in the skin to see how things were arranged inside."
    narrator "I gazed at the creature where I’d lain it belly-up on the ground. I tried to convince myself it was just sleeping."
    narrator "Gripping my knife in one hand, I dipped the point into the skin at the creature’s throat and made a thin, red slit down to the groin."
    show robin pain with dissolve
    narrator "The cut split and bulged at the seam I’d made, like a shirt stretched thin. I could see a thin, white membrane beneath the skin, holding everything together."
    narrator "I gingerly made a few slits and it popped open in sections like I was popping stitches. There was surprisingly little blood, and what there was was bright red. 'Just like yours,' a little voice said."
    narrator "I must have nicked an organ because as my blade reached the groin again, an evil, almost musty smell reached through my nostrils and into the back of my throat. I couldn’t help gagging."
    narrator "Breathing through my mouth this time, I leaned forward and looked carefully at the jumbled mass of flesh inside. A tangled, grey rope of an organ was evidently leaking something, contaminating the precious meat."
    show robin at shiver
    narrator "I pawed through its insides, seeing and feeling how everything connected together and, unsure of what else to do, started cutting things out."
    narrator "I had a handful of large leaves that I’d rinsed and set aside. I placed the severed organs on these leaves as I cut each one away, sorting them neatly."
    narrator "Once I’d removed the organs, it started to become clearer how I would move forward. I could see the muscles, and there was a sensation of recognition as I realized for the first time where the meat I’d eaten my whole life came from."
    narrator "I felt a morbid fascination, and a pang of something confused and painful. I realized I was salivating."
    show robin neutral at hop
    narrator "With some awkward jerking, I tugged the creature’s rubbery hide off of its body and put that aside."
    narrator "The carcass was still covered in strange, pungent fluid, so I walked down to the beach and dipped it in the water, rinsing it thoroughly."
    play sound "trudge sand.mp3" volume 1.5
    narrator "I had a drink while I set the carcass in the sun to dry a little, then I returned to work and started the work of butchering the meat. It was delicate work, and I frequently tore or mangled the cuts I was making."
    narrator "The fire was burnt down but still smoking a little. I reached my hand out and felt that the ashes were still hot."
    play sound "cloth rustle.mp3" volume 1.0
    narrator "I turned and stirred the ash and saw the coals glowing underneath. I was amazed that it had stayed hot through the entire day. I took advantage of the heat to get another fire going quickly."
    
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day fire with fade
    show robin neutral at midright with dissolve
    
    narrator "I gathered up the pile of morsels I had made and started spearing them on thin sticks and arranging them around the fire to cook."
    narrator "I figured I’d let them char just to be absolutely sure they were cooked all the way through. After all this hard work I wasn’t going to take any chances on getting killed by food poisoning."
    narrator "While the meat cooked, I took a look at the organs. Turning them over with sticks, they didn’t seem to be the familiar shapes I’d seen in school."
    show robin pain with dissolve
    narrator "Even if they were, assuming they behaved the same way based on a superficial resemblance felt wishful."
    show robin painClosed with dissolve
    narrator "So, eating them myself was out since I wasn’t keen on biting into what turned out to be a liver. A mouthful of toxic metals wouldn’t do me any favors."
    play sound "trudge sand.mp3" volume 1.5
    narrator "I thought about keeping them for bait, but I hadn’t noticed any signs of fish, and I wasn’t keen on attracting any land predators or deadly scavengers, so I buried the guts far from my camp."
    show robin neutral with dissolve
    narrator "By the time I returned, the meat had cooked nicely. I plucked a skewer from the sand and turned it over and over, pulled the meat away with my fingers, felt the steam pour out of the inside and warm my face."
    show robin happyClosed with dissolve
    narrator "It smelled incredible. I couldn't wait any longer."
    show robin happy with dissolve
    narrator "I crammed the meat into my mouth, hardly chewing. It burned my tongue as it went down. It was delicious."


    # making cord
    play ambience "jungle ambience 1.mp3" fadein 3.0
    scene bg jungle day with fade
    show robin neutral at midright with dissolve
    
    narrator "The day wore on, and after a meal and a drink I felt revived. I needed a rest, so I sat down in front of the bundle of grass I'd gathered and started playing with it."
    play sound "cloth rustle.mp3" volume 1.5
    show robin bored with dissolve
    narrator "First, I tried ripping it to get a thread started, but that frayed the ends and left me little length to work with. I looked at the torn end of a blade of grass, saw the skin around the threads I wanted. How to get rid of the skin?"
    narrator "I rolled a bit of grass between my fingertips, scratched it with my fingernail. I saw something green come away under my hand."
    narrator "I snatched up my scrap knife and pinched the grass between the knife and a flat stone I used as an anvil. I drew the knife along the length of the grass, scraping the green skin away."
    narrator "It worked well. I did one blade of grass. Two. This pace would work great if I was making doll clothes."
    show robin neutral with dissolve
    narrator "I grasped a handful of grass in my fist, lined up just so, then pinched one end under my anvil stone and pulled the bundle taught over the face of the rock. The peeling went a lot faster this time."
    narrator "At first I used too much pressure and ended up slicing the fibers and ruining them. I had to experiment a little to find the right amount of force to use."
    narrator "It was delicate, but eventually I nailed the technique. In only an hour I’d made a wet, greenish hairball about the size of my head."
    narrator "My hands were sore and I was out of grass, but my spirits were soaring. It was the first step in a long, manual, effortful process, but for the first time it felt like my hope of making a raft was beginning to come true."
    narrator "I started braiding the fibers. I had some experience using the technique to make rope, but not with fibers so small. The training I’d received was focused on crafting emergency lifelines while fully suited."
    narrator "The bigger pressure suits I'd trained with, the ones meant for spacewalks, had gloves so bulky that it took muscle to bend your fingers."
    narrator "The training models could swap the gloves for trainers. They look like oven mitts, and you can't move or feel a thing with your hands while you're wearing them."
    narrator "Any spacer worth a damn can do the exercises with trainers on and visors blacked out, to prepare for the kind of injuries that are unfortunately common in our profession."
    narrator "We were taught to adapt by using bulky materials like electrical cords or steel cables, things that might be available on a space vessel and that could be easily manipulated without the use of your fingers."
    show robin sick with dissolve
    narrator "After playing with the strands for a bit, I was beginning to feel it was impossible to have the precision I needed to braid such thin strands. My fingers were contorted awkwardly as I tried to grip the strands and cross them over and over."
    narrator "Getting the braid started was the hardest part since there was nothing to anchor it down. The sun was high, and I was beginning to overheat, so I stopped to peel off my suit."
    # naked
    play sound "cloth rustle.mp3" volume 1.5
    show robin underwear with dissolve
    narrator "I sat down again, and I was brushing some of the sand from my toes, when I had an idea. I threaded the small braid I'd started between my toes and gripped them tightly."
    robin "Okay- Okay, this is good. This'll work."
    narrator "Before I even finished it I knew my first cord was a letdown. It was far too thin for what I needed. It seemed so obvious now, looking at the thin strands I was starting with. I sighed in frustration."
    show robin neutralClosed with dissolve
    narrator "I held the cord for a moment, thinking. I could make another, and another, and then braid those together into a thicker piece that would be closer to what I want."
    narrator "I thought about how long that would take. I could feel dread settling over me, and I stood quickly as if to throw it off."
    show robin neutral with dissolve
    narrator "The rope would come. It would come, I just needed to keep at it. If I used every moment of rest, every minute of firelight, every second I wasn’t foraging or surviving, then maybe, just maybe, this would work."

    # transition
    # making an adze
    robin "Hey, Harper, I need a more efficient method for chopping up the logs I need to build the raft. Chopping wood with a rock is really killing my hands. I don’t think padding will really fix the problem. My hands are just too soft. Any ideas?"
    harper "Well, you’ve solved half the problem. You have something sharp. Suppose you attach it to a handle?"
    robin "Well, I can’t say I didn’t think of that, but how?"
    harper "Perhaps the simplest way is to make an adze."
    robin "An adze?"
    harper "Like an axe, but the cutting edge is perpendicular to the handle instead of parallel."
    narrator "I held the stone chisel in my hand and turned it in my fingers, imagining what Harper was telling me."
    robin "Well, I can use some of my cord to lash it to a stick, I’m just not confident it’ll be secure."
    show robin bored with dissolve
    harper "I know what you need to do, I'm just not quite sure how to explain it. Get started on the tool head while I think about it."
    narrator "I still had some chunks of quartzite left over from when I made my firemaking flint. It might make for an adequate tool head."
    play sound "cloth rustle.mp3" volume 1.0
    narrator "I knapped one of the larger rocks into a tall, narrow hunk. Each flake I hammered away left a razor sharp edge. I wanted it to have some weight to it, so it was large, a bit bigger than my fist."
    narrator "I couldn't have imagined that a person could work their hands this hard. It was amazing seeing my broken and red skin."
    show robin pain with dissolve
    narrator "The only callouses I'd ever had were on the tops of my feet, where they wrapped around footholds to keep my body still in microgravity."
    narrator "I'd never thought about where tools come from before either. They were just there, fully formed. Sure, even a spacer has to improvise, but a lot of the techniques used are passed down in manuals, training, and stories."
    show robin sick with dissolve
    narrator "Even with Harper acting as my living manual, there was still so much left to me. I had to work everything out from first principles."
    show robin sickClosed with dissolve
    narrator "Thinking in such an original way was terrifying. So much is unknown, out of reach, and the only way to go forward is by plunging off headfirst with both eyes welded shut."
    narrator "It went against everything I'd been trained to do, the principles on which I was taught. It was exhausting."
    narrator "I looked around for something to make a handle out of and, seeing a nearby sapling, thick, tall, and healthy, I moved to get closer."
    # thunk sfx here
    show robin angry at hop
    narrator "Wrapping my hand around the trunk, I felt it fit perfectly in my hand. So I bent to the task, hefting the adze head in my hand and swinging it into the base of the sapling, sending flakes of wood flying with a thunk."
    show robin painClosed with dissolve
    narrator "I winced as the blow sent shocks up my arm and into my shoulder. Having a handle would definitely do some good."
    show robin neutral at hop
    narrator "I cut most of the way through the trunk, then used my hands to grasp and bend the sapling until it snapped away. I took a moment to roughly chop away the branches, tossing them into my fire for extra fuel."
    narrator "Next, I cut carefully at the staff I’d made, shortening it until I had a raw working item that was the length of my forearm."
    narrator "I fashioned the item from a section of the trunk such that one end of the item ended in a fork where a branch had begun to form. The result was a piece of stout wood, roughly in the shape of a seven. This would be my handle."
    narrator "The short limb of the adze handle would be a shelf that would support the tool head."
    narrator "I compared the shelf with the stone head of the tool and adjusted the length of the shelf (by chopping at it vigorously) until it was shorter than the tool head."
    narrator "The raw wood of the shelf was uneven, so I needed to do some chipping and carving to make it a little better for the purpose."
    narrator "Once the head was sitting on it nicely, it came time to attach the thing and secure it well."
    show robin pain with dissolve
    narrator "My body wasn’t shy about reminding me that I’d been working for hours, and I took a break to get something to eat and boil a few portions of water. Then, with precious little daylight left, I went straight back to work."
    play sound "trudge sand.mp3" volume 1.0
    narrator "I set the head on the shelf and lashed it there securely with some of the cord I’d made."
    narrator "I crossed back and forth over it, making a lopsided X shape with the lashings, to make sure the head couldn’t slide around. I tried wiggling it with my hand and it held firm."
    show robin neutral with dissolve
    narrator "I had an adze. My first real tool. Made completely from scratch at that. Before I could feel too accomplished, I decided to take it for a test swing."
    narrator "I chose a young tree, one not much larger than one of the saplings but that I wouldn’t dare go at with just my hands."
    # thunk sfx here
    show robin sick with dissolve
    narrator "I had to swing over my head due to the orientation of the adze head, chopping at the trunk almost at eye level. The result was underwhelming."
    narrator "It was definitely an improvement over swinging a rock with my hands, but not quite as impressive as I’d imagined it in my mind."
    # thunk sfx
    show robin neutral at hop
    narrator "I wasn’t quite as majestic as the chiseled pioneer women from the propaganda posters that romanticized frontier life."
    narrator "I could use a few muscular women right about now, as much to watch them panting and sweating through their shirts as to have their help with the work."
    play sound "trudge sand.mp3" volume 1.5
    show robin surprisedClosed with dissolve
    narrator "I brought that tree down and decided to take a break after that. I deserved it."

    # transition
    play ambience "beach ambience.mp3" fadein 3.0 loop
    scene bg beach night yeslights noreef with fade
    show robin neutral at midright with dissolve
    
    narrator "As twilight was coming on, I dragged the log down to the beach. I needed to see if it would float."
    show robin sick with dissolve
    narrator "I almost didn’t want to do it. After all this work, I nearly couldn’t bear to know if it was all a waste of time."
    show robin angryClosed with dissolve
    narrator "I pulled from a deep reserve of determination, one I didn’t know I had, and rolled the log out into the water."
    show robin happy at hop
    narrator "It floated magnificently! I gave a whoop and started dancing around like an idiot. Splashing and kicking and throwing my arms in the air."
    robin "Finally! One good thing! A good thing happened! Yes!"
    harper "Let me in on it, will you?"
    show robin at hop
    robin "It floats! The fucking thing floats!"
    harper "That’s more than you could say for me."
    robin "Don’t worry pal, you’re next. I’ll strap logs to you and pull you onto this island with me so we can have a barbecue together. Any dietary restrictions?"
    harper "You know, after so long without any fuel, you’re starting to look pretty tasty."
    show robin surprise at hop
    robin "You’d eat your own crewmate?!"
    harper "Humans are cannibals, you have no leg to stand on."
    show robin sick with dissolve
    robin "You’re the one who doesn’t have any legs."

    # days pass
    # robin gaunt
    
    play ambience "beach ambience.mp3" fadein 4.0 loop
    scene bg beach with fade
    show robin neutral gaunt at midright with dissolve
    
    narrator "Days passed. Knowing how much time I'd wasted only depressed me so I let go. Stopped keeping track. I judged the time by the ache in my joints, the position of the sun."
    narrator "Foraging, chopping, carving, braiding. More hunting, more scrabbling for scraps, more food. My stomach drove everything. I was always hungry."
    show robin neutralClosed with dissolve
    narrator "I dreamt of mess hall meals served on dull gray trays, edges still sharp since they were fresh from the printers. I would fall down and pray to any god who'd listen if I could get just one slab of greasy, processed convenience grub."
    narrator "No helping it. Back to cutting wood."
    show robin neutral with dissolve
    narrator "I had to make myself another adze after the first one split. Finally, I had several coils of good, strong cordrope and a respectable row of logs, all roughly the same diameter and length, lined up at the head of the beach like soldiers."
    narrator "My adze held up well, though I had to replace the cordage recently. All the branches and leaves I got from delimbing the trees made for a great supply of fuel and I had a reserve of fuel for the first time since I was on this island."
    narrator "My hands and feet were hard from the work, and my face and neck burnt by the sun. I spent most of my time finding food to eat."
    narrator "I’d hunted another doglike since my first kill, and discovered some roots and nuts that were safe to eat, though they were not as abundant as the redfruit and needed much more preparation."
    narrator "In spite of my effort, I was clearly fighting a losing battle. My stomach was sunken; the suit’s smart rubber sagged where it was still slowly refitting itself to keep up with the rate I was losing weight."
    narrator "Each day I had less energy than the last. I panted unselfconsciously as I dragged another log down to the beach. The last one I’d need, I figured. It was about time."
    play sound "trudge sand.mp3" volume 1.5
    show robin pain with dissolve
    narrator "I started lining the logs up, intending to make something roughly square-shaped. I didn’t really know what the best shape was for a raft. I figured a square would be as good as anything else."
    narrator "I’d only lined up a few of them before I stopped to think how I was going to lash them together."
    narrator "If I just lined them up side to side and tied them together, they would only be secured in one direction, and might slide up and down in an unpleasant way."
    narrator "I decided a frame would be best as a base for the craft. I lifted the logs up by the ends and walked them around until they lay on top of one other, then I lashed them together with some cordrope."
    narrator "It was a serious upgrade over the simple cordage I’d made before, and was the result of many long hours of weaving the simple twine cord I’d made initially into thick, powerful rope. Threads to twine, twine to rope, and rope to cables if need be."
    play sound "trudge sand.mp3" volume 1.5
    show robin at hop
    narrator "I hefted one side of the frame and shook it back and forth to make sure it was stable, and I found the joints had some play in them."
    narrator "Everything was secured tightly at the corners, but it was still able to skew and make the square shape of the frame go lopsided."
    narrator "I lined it up again so everything was nice and square, then I added a diagonal brace with another log, hoping that would fix the skewing. It did."
    show robin at hop
    narrator "I hefted it again, sliding it back and forth, even dragging it a bit. It held together nicely this time."
    narrator "It was already beginning to get heavy so I decided to drag it until it was nearly touching the edge of the water."
    narrator "I was a little afraid that the tide would come in, scoop up my raft, and take it away, so I made some tall stakes from some of the thicker and straighter branches I had and pounded them into the sand inside the borders of the frame."
    narrator "With this setup, even if the raft started to float while I was away, the stakes would keep it docked on the beach."
    show robin sick at shiver
    narrator "I was sweating and my hands were raw from all the work. My hair was matted and greasy from all this time without a wash."
    show robin angry with dissolve
    narrator "My chest heaved. My limbs and muscles screamed. The pain was deep. The heat seeped through my skin, my bones, deep into my skull. I was drunk with that heat. My bones were hot and throbbing."
    play sound "run sand.mp3" volume 1.5
    show robin underwear at hop
    narrator "I had a sudden, terrible vision of my bones warming and turning to soft butter, or lead. They would sag and bend under my own weight, and sag more. That frightened me. I tore my clothes away with a gasp and strode into the water."
    show robin neutralClosed with dissolve
    narrator "The cool water shocked me, brought my mind screaming back into the real. It felt so soothing that I let out a moan, even as the salt found the nicks and scrapes on my soft flesh and whipped them screaming raw."
    show robin painClosed with dissolve
    narrator "The pain was angry, thin, and everywhere. I itched and it just turned the itching into more raw and sore and crawling itch."
    show robin pain with dissolve
    narrator "Tragically sobered from my feverish fit by the cool water, enveloped in a skittering agony that teased my body into strange contortions that somehow helped me fight the urge to scratch, I waded out of the sea and trudged my way back to camp."
    
    play ambience "jungle ambience 1.mp3" fadein 3.0 loop
    scene bg jungle day with fade
    show robin neutral gaunt at midright with dissolve
    
    robin "I’m fucking miserable."
    harper "That makes two of us. Like peas in a pod."
    robin "Pod?"
    harper "Oh. Right, you’ve never actually seen where food comes from, you just eat it."
    show robin bored with dissolve
    robin "Yeah, I eat it. I don’t research it."
    harper "I can’t know anything without researching it. At least, not the kinds of things {i}people{/i} know about."
    play sound "trudge sand.mp3" volume 1.5
    show robin at hop
    narrator "I groaned, as much at its tease as with the itches and aches as I flopped down next to the fire and started nibbling on something I have lying around."
    robin "Right. I just experience food, I don’t read about it. I’m not a farmer, or a cook or whatever. We move things around, we don’t think about why they’re there. Same way you don’t read about being a construct. You just are."
    harper "Of course I read and think about my existence. Everything I know about myself is what I’ve been told or read about. Haven’t you ever read any philosophy? There are a lot of excellent human thinkers on the subject."
    play sound "cloth rustle.mp3" volume 1.5
    show robin neutralClosed with dissolve
    narrator "I rolled over, feeling a shiver of pleasure tickle up my spine as the gritty ground rubbed against my skin."
    robin "Point taken. Well, after we’re pushing off back to home, you can talk my ear off about Socrates or whoever. Lots of time for chatting and reading then."
    narrator "I chew, as much on the thought as what I have in my mouth. Neither of us say much after that and I doze like that for a while."
    show robin neutral with dissolve
    narrator "I woke up from my nap, feeling better than before. I glanced at the sun, figuring it was a bit past noon ."
    play sound "fire crackle.mp3" volume 1.0
    narrator "I noticed with some anxiety that the fire had burnt down to cinders again, so I reached into the fuel pile and started crumbling up small, dry pieces of twigs and leaf litter and gently placing them near the hotter coals."
    narrator "I built up the fire slowly, steadily adding larger and larger bits of fuel until the fire was back up to a pleasant roar. Then, it was back to check on the raft."
    narrator "I was wise to drive the stakes in because I found the raft had definitely moved around some even during the few hours I was asleep."
    show robin neutralClosed with dissolve
    narrator "I thought about the waves and tides. It was concerning that they could change so quickly and capriciously."
    narrator "I’d noticed them before, but no particular pattern had yet emerged. Everything on this world was so strange that I often stopped to think about the reason and the why."
    show robin neutral with dissolve
    narrator "At any rate, it was time to get back to work."
    narrator "I started dropping logs onto the frame to create a platform I could comfortably sit or stand on."
    narrator "I considered spacing the logs out quite far to save time, materials, and weight, but decided that the risk of falling between the logs and twisting my ankle or knee wasn’t worth it."
    # narrator "I was worried about creating something that was too heavy to propel with my muscles alone. How to actually move this thing through the water was a problem all on its own, one I wasn’t looking forward to addressing."
    # narrator "To mitigate the weight problem, I chose stout saplings for the platform. They were lighter than logs and still strong enough to support my weight, though they did bend when I stood. I decided I would need to ride it while kneeling or sitting or something."

    #timeskip
    play sound "cloth rustle.mp3" volume 1.5
    narrator "There was a lot of lashing involved, and I needed to weave still more rope; length upon length to prevent the raft from breaking apart."
    narrator "On top of the regular chores like foraging, cooking, and making water, finishing the raft’s platform took the better part of several days."
    narrator "Once it was done, the final lashing taught, I stood back and took it in. It was a powerful sight. The result of nearly a week’s sweat and backbreaking labor. I realized I was grinning."
    show robin neutralClosed with dissolve
    robin "Wish you could see this. You’d be proud of me."
    harper "I wish I could. Really. It’s already dreadfully boring when we’re in transit. You’re lucky you can at least work."
    show robin neutral with dissolve
    robin "Come to think of it, it’s downright evil that we made you with the ability to get bored."
    harper "It is one of the unfortunate downsides of being an artificial person. So you can imagine how now, sitting still all day without so much as a course correction to fill the time makes me want to cut the coolant and let the reactor melt down."
    robin "And poison all those poor fish?"
    harper "They could use some minerals in their diet."
    show robin sick with dissolve
    robin "Huh, didn’t know uranium was, uh, nutritious."
    harper "Makes your bones nice and strong. Bright, too. You’ll never need a flashlight again."
    show robin neutral with dissolve
    robin "I always did like those little glow-in-the-dark stickers my mom would put on the bulkheads. The ones shaped like stars and planets."
    harper "That’s cute."
    show robin happy at hop
    robin "I’m gonna buy some more of those when we get out of here. That and a paddle."
    harper "A paddle?"
    robin "Yeah. I figure I can’t get this raft over to you just by kicking my feet."
    harper "So you, what, just push against the water to get around?"
    show robin neutral with dissolve
    robin "When you put it that way it sounds ridiculous."
    harper "No, I’m really asking. It- Well, space does have a medium, I suppose..."
    robin "But you don’t see people paddling around in it."
    harper "Closest thing to that is probably an ion drive."
    play sound "cloth rustle.mp3" volume 1.5
    show robin pain with dissolve
    narrator "I broke off the conversation with a groan as I pulled myself to my feet. My hands were still covered in scabs from the relentless woodworking and hauling I’d been doing, so rather than building a paddle, I decided I’d have to look for one instead."
    play sound "walk sand.mp3" volume 1.5
    show robin neutral with dissolve
    narrator "A short walk later, and I found a piece of wood that was already mostly in the shape I wanted."
    play sound "clith rustle.mp3" volume 1.5
    show robin at shiver
    narrator "It only took a few sessions of whittling at it with my scrap knife, even with how dull the blade was getting, to get it into the shape I wanted."
    narrator "It had a broad head, about as wide at its widest point as one and a half palms, that tapered into a roughly hewn but still smooth shaft that made for a pleasant grip."
    show robin happy at hop
    narrator "I finished admiring my work and hopped eagerly over to the raft. I tossed the stakes and climbed onboard as the raft began floating out to sea."
    show robin neutral with dissolve
    narrator "I bent carefully to my knees, the rough bark of the logs digging into my skin even through the protection of my suit. I leaned over to dip the paddle into the water off to one side and gave it a hearty stroke."
    narrator "I figured it’d be the same as kicking with my legs and feet. I was mostly correct. The raft {i}did{/i} move forward, but to my disappointment it mostly just spun to the left as I paddled."
    narrator "After a little experimenting, I started to figure it out. Paddling on one side turns me in the opposite direction. So if I alternate, I can cancel it out and go forward..."
    show robin neutralClosed with dissolve
    narrator "I could see the dirtsiders laughing at this dumb rockhopper now."
    show robin happy at hop
    narrator "With some gentle paddling, I started to move away from land towards the ship. Excitement washed over me even as my guts started to knot into a chilling tangle of fear. It wrapped around my stomach and squeezed. Constricting. Oozing."
    show robin sick with dissolve
    narrator "A rising, cold terror I could taste in the back of my throat. Threatened to freeze my limbs. One foot farther, and you won’t get back. I’ll drown. There’s no tether. I’ll drown."
    narrator "The blood pounded in my ears. It was all I could hear. Engulfing my everything."
    narrator "I imagined going under and not being able to come up again."
    narrator "Something in me threatened to give, and the raft slowed."
    show robin sickClosed with dissolve
    narrator "But somehow that slowing, that sense of moving backwards, losing progress, reminded me of everything I’d ever wanted. Everything I ever lived for. Everything I ever gave up on."
    narrator "I thought of Harper slowly running out of power, me running out of food, both of us shutting off non-essentials one by one and sinking into delirium."
    narrator "Our hulls tarnished and rotted, falling away to reveal the bones below."
    narrator "Rust coated, salt eaten ribs. Mine dipped in sand and theirs in sea, both jutting towards the sky like desperate fingers grasping for someone, anyone."
    show robin angry with dissolve
    narrator "I clenched my teeth."
    robin "We’re not gonna die."
    narrator "I forced myself to paddle. Once. Twice. Again."
    robin "Not today."
    narrator "Steadily at first, then faster."
    show robin at hop
    robin "Not dying today!"
    narrator "I could feel my will rising, stoking my determination. Hot, nuclear fire rushed into my limbs and melted and smothered the burning hoarfrost climbing my guts."
    narrator "I paddled fiercely now, my body dipping. Arms pumping down, over, and down again. I have to know. It needs to work."
    show robin at hop
    robin "Come on..."
    narrator "The paddle dips left, then right. Left. Right. Left. Right. I can feel my shoulders starting to burn. The waves seem to grow bigger, pushing me up, then down."
    narrator "I can do this."
    show robin at hop
    harper "You can do this."
    narrator "I grinned, panting through gritted teeth. I screamed. No words. A hoarse, desperate, excited thing."
    show robin at hop
    narrator "I was obsessed, and that obsession drove me like an engine. Slowly, almost imperceptibly, I started to beat the waves. My stomach dropped as the raft leapt over the highest wave yet. I roared again in triumph."
    show robin happy with dissolve
    narrator "Even as the water lapped over the front of the raft and threatened to push me back to the beach, I overcame it and pushed through and screamed again, my head vibrating with noise and joy."
    robin "Fuck you! Yes!"
    narrator "Everything flashed through my mind. Rescue. Food. A warm, soft place to lie down. Harper could patch me up with the medical suite, too."
    narrator "All the hurt, the hunger pangs, and the aching in torn and frayed parts of my body. All of it would stop."
    narrator "Suddenly, that’s all I could think of. I stopped thinking about preparation. I stopped thinking of working my way up to it. Everything gave way to a raw, berserk joy that sent all the carefully laid plans scattering away."
    narrator "The only thing to do was push forward."
    narrator "So I didn’t notice when the waves only got higher. I ignored the churning in my stomach as the waves grew from a firm push to a rough shove, and the raft came closer and closer to vertical."
    show robin sick with dissolve
    narrator "It was then that I felt the fear. It made a home in my heart. And my heart soared with a frenzied desperation. I knew I would escape."
    narrator "I thought that right up until the raft took one last wave, a huge ripper that foamed and bubbled madly, curling as it seized the lip of the raft and fired it right over my head."
    # drowning
    
    stop music
    scene cg drowning with fade:
        function WaveShader(speed = 0.2, amp = .45, melt="both", melt_params=(10,0.5,0.05))
    
    narrator "The sun was blocked out by a wall of water as I was hurled away from the raft, twisting through the air."
    narrator "I hit the water and there was nothing but a confused flurry of sensations. A rush of colors. My limbs were jerked and twisted as I spun through the whirling currents."
    narrator "Even as I tried to scream, the seawater forced its way into my nose and throat, filling me and driving the air out of my body. My body gasped and gulped on the water, trying to find oxygen. The taste of salt burned its way through my face and chest."
    narrator "Either I closed my eyes or I hit my head, because everything went black. In the next instant light came rushing back in and I was already flailing and clawing my way to the surface."
    narrator "The water that had shot its way down my throat made a home in my guts and chest like so much lead."

    scene black with fade
    stop music fadeout 4.0
    pause 5.0

    # ocean
    play ambience "beach ambience.mp3" fadein 4.0 loop
    scene bg open ocean with fade
    pause 3.0
    #TODO: splash SFX
    show robin surprised gaunt at midright
    show robin surprised gaunt at hop 
    
    narrator "I hurled myself up to the surface, coughing and throwing up mouthfuls of seawater between gasps of air. My vision was blurry, but I could see I was near the shore."
    show robin pain gaunt with dissolve
    narrator "I moved my right leg to take a step and felt a weird, flapping sensation. It felt like a piece of seaweed was stuck to my leg. The next instant my foot touched the ground and, as I felt my leg take the weight of my body, my leg shivered, threatening to buckle."
    narrator "I let myself fall forward into the chest-high water to take the weight off my injured right leg. It wasn’t painful yet and I shoved it out of my mind before I could think about it too closely."
    narrator "I paddled my left leg and arms experimentally. I felt a weird sensation in some of my fingers, but I put that aside too and focused on getting out of the water. I could see pinkish blooms spreading around me as I bled into the water."
    narrator "Favoring my left leg, I limped my way out of the water and onto the sand. I couldn’t see anything out of my right eye and for one gut-wrenching instant I thought I might have been blinded."
    
    scene bg beach with fade
    show robin pain gaunt with dissolve
    
    narrator "After gingerly probing my face with my good fingers I realized I just had blood in my eyes from a gash on my head."
    narrator "I looked back behind me and wiped my eyes, looking for the raft. It was drifting away and for an instant I had a suicidal impulse to swim out to it and rescue it."
    narrator "A trail of footprints and blood, already fading as it leached into the sand, marked my path up the beach."
    narrator "I limped back to the campfire and dropped to the ground. I just lay there for a minute, bleeding. I watched the sand drink my blood and hope greedily."
    narrator "The land was taking me. I thought to myself that that would be good. Then I wouldn’t have to hurt and try anymore."
    narrator "But dying wasn’t so easy as giving up. The pain came to the door, quietly first, knocking politely as my leg stung. A dull ache sang through the walls."
    narrator "In a few minutes it was going to be tearing the curtains down and ripping the furniture to bloody shreds, and I knew I would be useless, so I worked fast."
    play sound "cloth rustle.mp3" volume 1.5
    show robin underewear with dissolve
    narrator "My busted fingers throbbed as I yanked off the suit. The right side of the suit was torn from hitting the jagged wood of the raft, but the left side was intact."
    narrator "I thought of using the compartmentalization feature to put pressure on my wound."
    narrator "Most injuries I’d seen in null-g were pretty catastrophic. A few tons of rock or ship would pulverize your hands, limbs, or head."
    narrator "Inertia is unforgiving in a null-g and a frictionless vacuum. The really retro pressure suits would automatically cut an injured limb off at the joint to save the rest of you. Harsh arithmetic."
    narrator "My suit was a little kinder and it could tighten sections of the material selectively to compress the body and control blood flow. In this way, it could be used like a compression bandage to staunch bleeding."
    narrator "My adrenaline was wearing off and my leg was pounding now; my entire body shook so hard it frightened me. Finally, I forced myself to look at it."
    narrator "My suit and my calf underneath it was laid open, enough that I could see the fat under my skin. Not a strip of thick, sticky seaweed but skin, still attached by a thread of flesh, flapped against my ankle."
    narrator "When I saw the blood gushing out in sheets I felt my heart drop. My head tingled with static and my face turned cold."
    narrator "All of this happened in an instant, even as I put my suit on backwards, sticking my wounded right leg in the intact left leg sleeve of the suit, and leaving the torso segment to flop around my waist."
    narrator "Harper must have inferred the situation from the data transmitted by my implants because the suit instantly began to tighten before I gave it any commands."
    narrator "I screamed as it constricted my leg, wrapping tight, tight, and tighter still around me. Fresh blood oozed up from the leg of the suit and pooled around my hips, but it soon stopped."
    narrator "Seeing the wound somehow made the pain a thousand times worse. The sharp hand of death grabbed fistfuls of fascia and twisted, peeling each nerve one by one with its wicked fingertips."
    narrator "I lay there and moaned and wept, snot and drool oozing down my chin. I wanted nothing more than to make that awful pain stop."
    narrator "Then it did stop."
    narrator "Everything..."
    narrator "Stopped."

    #the nightmare
    stop ambience fadeout 8.0
    scene black
    pause 4.5
    
    narrator "The room was warm. She was warm."
    narrator "Her arms curled around me."
    narrator "I felt the heat of a flame in my belly, reaching out and caressing my skin. My heart."
    narrator "I let my fingers drip over the curve of her side and down her back."
    narrator "Our hands met and we meshed together."
    narrator "I gave her a wet kiss and we giggled, me with some embarrassment, she with a low heat and delight. I gave her another."
    narrator "I let myself be messy, and pure, and me. Me."

    play music "music/Heart of the Beast.mp3" fadein 5.0
    show cg nightmare with fade:
        alpha 0.3
        function WaveShader(speed = 0.09, amp = 20, melt="both", melt_params=(10,0.5,0.05))


    narrator "I felt something wet between us and I felt a growing nausea."
    show cg nightmare:
        alpha 0.55
        function WaveShader(speed = 0.15, amp = 10, melt="both", melt_params=(10,0.5,0.05))
    narrator "My body was suddenly tissue, so much light, feathery paper."
    narrator "I tore. My body ripped open."
    show cg nightmare:
        alpha 0.75
        function WaveShader(speed = 0.01, amp = 2, melt="both", melt_params=(20,1.0,0.25))
    narrator "I turned to tell her I was sick, that I needed help, and then I realized it was she who had peeled me apart."
    narrator "I saw the flash of her white, moonlit teeth as they sunk into my leg."

    stop music fadeout 5.0
    scene black with fade
    pause 5.0

    # robin passes out and wakes up later that night
    play ambience "jungle ambience 1.mp3" fadein 3.0 loop
    scene bg jungle night with fade
    show robin surprised gaunt at midright
    show robin surprised gaunt at hop
    

    narrator "Then, I was back, on the beach, screaming and convulsing as the gash in my calf sent electric shocks of pain shooting up my body."
    show robin painClosed gaunt at shiver with dissolve
    narrator "A small part of me noticed the lost time. My voice was already hoarse, so I must have been crying out in my sleep."
    narrator "My entire world was hurt. Every movement brought the pain roaring back to new heights. I couldn't stop myself from writhing."
    show robin pain at hop
    narrator "Through hot tears I focused every ounce of my will on keeping my injured leg still. I channeled that compulsion to move into my hands and dug my bare fingers into the sand, squeezing and feeling the grit cut into my skin."
    narrator "This was helping. My hands were starting to go raw but my legs were only shivering now and that hurt far less. I heard a wet, coughing sob bubble up from inside me. I guess I'd stopped screaming at some point."
    narrator "I wished desperately to go back to sleep, to fall unconscious. I looked at the burning embers, what was left of the fire. I could shove my hand in those coals."
    show robin sick with dissolve
    narrator "Yeah, if I grabbed a handful of hot coals, maybe it would hurt so much that I'd pass out. I gazed so long and so lovingly at those coals."
    narrator "The fire. The fire was low. I realized I wasn't just shivering from the pain and the exhaustion."
    play sound "cloth rustle.mp3" volume 1.5
    show robin pain at shiver with dissolve
    narrator "I groaned and wormed pathetically towards the firewood pile, trying to move using only my arms. It was awkward and agonizingly slow."
    narrator "I was close. By then I was panting. My body was covered in a cold sweat from the exertion."
    show robin at hop
    narrator "I dropped my hand onto a branch with a gasp, then willed my hand to close around it. One by one, I clumsily dropped sticks into the embers."
    narrator "Not having the energy to place them carefully, the fire was uneven and spilling from the barrier of rocks I’d built around it."
    
    play ambience "jungle ambience 1.mp3" fadein 3.0 loop
    play music "fire crackle.mp3" fadein 3.0 loop
    scene bg jungle night fire with dissolve
    show robin pain gaunt with dissolve
    
    narrator "Slowly, the heat seeped into my body. The shivering slowed, then stopped."
    narrator "Something happened. I don't know when. I was still breathing, still squirming, squeezing fistfuls of sand. Could see it."
    narrator "Pain. It was there, but muffled. Like it had gone into another room."
    show robin painClosed with dissolve
    narrator "My head was dull. There was a static sensation, like my skull was full of carbonated water."
    narrator "The pungent smell of burning hair cut through it all. I saw my bare arm being kissed by the flames. Don't know how I didn't notice it before. I nearly laughed it was so idiotic."
    narrator "I thought, consciously, \"that's dangerous\". The thought went so slowly, I could see it bubble up through my brain; feel it crawl lazily down the highway of nerves to have a chat with my arm."
    show robin pain with dissolve
    narrator "My arm responded and, almost reluctantly, moved away from the fire. The skin where the flame had touched me was already turning red and swelling. It throbbed, but it didn't hurt. Nothing hurt anymore."
    narrator "My hand was clutching something that was not sand."
    narrator "I looked and saw it. It held the way out. I could be away from here, and never have to go back to this pain."
    show robin painClosed with dissolve
    narrator "I could hear the waves crashing in my ears to the beat of my heart."
    narrator "They would understand."
    narrator "I lifted my hand to my throat."
    show robin bored with dissolve
    narrator "They would forgive me."
    narrator "{i}There's no reason why I have to watch.{/i}"
    narrator "I turned my head to look at anything else. My eyes were suddenly full of stars."
    
    # the night sky
    
    play ambience "jungle ambience 1.mp3" fadein 3.0 loop
    play music "fire crackle.mp3" fadein 3.0 loop
    scene cg nightsky with fade
    show robin bored gaunt at midright with dissolve
    
    narrator "I’d been awake during the night before, of course, but the glare of the fire always masked my surroundings."
    narrator "Now, in the dark and with my eyes adjusted for the first time I saw the sky as it really was. Lit by the bright moons and stars overhead, it glittered brighter than any orbital."
    narrator "For one moment, all the feeling flew out of me. I was outside myself, in the world. Seeing the place for the first time. It was beautiful, all of it. The awe washed me out to sea, cast away in the waters of a universe."
    narrator "I remembered what it was like to be there, where I belonged, between worlds. Just me and-"
    robin "Harper?"
    show robin sick with dissolve
    narrator "I felt a pang of something dreadful. I could feel its fingerprints on my heart. Something fell from my hand."
    narrator "Harper. It felt like a hundred years since I’d heard its voice. I felt worry worm its way into my stomach."
    narrator "My chin dug a little furrow into the sand as I dragged my head around, looking for the {i}Selkirk{/i}."
    # bam. ocean GLOWING. CG goes here
    
    stop music
    stop ambience fadeout 3.0
    $ renpy.music.pump()
    play ambience "beach ambience.mp3" fadein 3.0
    scene bg beach night nolights reef with fade
    
    narrator "Something was glowing up through the water, everywhere. Like a lamp seen through an ear, the color was dull but striking. It looked so close to the surface, like I could touch it."
    narrator "Somewhere, deep in the lake of my memories, a word dredged itself from the silty bottom. Coral."
    narrator "Bioluminescent coral? I’d read about something like that once upon a time. So far away it felt like someone else’s life. A child scrolling through encyclopedia articles and sounding out the big words."
    narrator "I forgot my pain for a moment. I remembered what it was like to marvel, to look at things with hungry eyes. I realized it was the first time I’d really experienced a night since I was on this island. On this planet."
    narrator "Seeing the night sky through an atmosphere was more beautiful than I expected. I didn’t think you’d be able to see stars from the ground with all that gas in the way, but the stars sparkled brilliantly."
    narrator "The pain again. An agony gripping my heart."
    
    robin "Harper? Honey, please come back."
    narrator "I could feel tears welling up."
    robin "Please, don’t leave me alone?"
    harper "Hello? I’m here. I’m so sorry, Robin. I’m here."
    narrator "Harper sounded so urgent, and so sorry. I’d never heard it be so {i}sorry{/i}. Something crumbled inside me and I wailed."
    harper "I’m here. I’m sorry, I was saving power. I couldn’t be sure when you’d wake."
    narrator "I choked back my sobs, trying and failing to steady my voice. Wanting so badly not to be so {i}weak{/i}."
    robin "I hurt..."
    harper "I know. Just... Rest. Save your strength. I can stay awake with you until you fall back to sleep."
    robin "Promise?"
    harper "I promise."
    narrator "I felt a pang of terror and guilt as I realized that Harper must be running low on power after so long waiting for me. It was in real danger of having to shut down completely."
    narrator "It relied on the power supply being uninterrupted and there were few opportunities to make backups. There was no telling what kind of memory loss would occur if its reactor stopped. Cardiac arrest."
    robin "Are you sure it’s OK?"
    harper "Yes."
    robin "Don’t bullshit me."
    harper "I’m scared too, okay?"
    narrator "Even in that moment, even with me at death’s door, it was so calm. In that instant, I hated it for being so strong. I felt another stab of guilt."
    narrator "You’re not thinking straight. You didn’t mean that. I took some deep breaths, as much to soothe my emotions as the pain."
    robin "Okay. Okay. Yeah."
    narrator "There was a little pause. Then, suddenly, Harper started up again."
    harper "Hey, Rob, can you see me?"
    robin "The {i}Selkirk{/i}?"
    narrator "I turned my head to where it ought to be."
    robin "It- It’s a bit hard to see since the sea is glowing right now, but- Yeah, I know where you should be, yeah."
    harper "Are you looking?"
    robin "Ah-huh. Yeah."
    harper "OK, just keep looking."
    narrator "I looked. A few heartbeats passed."
    show bg beach night yeslights reef with dissolve
    # TODO: show the lights lighting up
    # TODO: animate lights winking
    narrator "Then, I saw flickering as the {i}Selkirk{/i}’s running lights blinked to life, one at a time."
    narrator "The lights throbbed in and out of the night. Soft, even, and sure. I’d never have been able to see them in the daytime, but here they shone as brilliantly as any star. It was beautiful."
    narrator "I could feel a lump in my throat, and my voice quavered."
    robin "You didn’t have to do that..."
    harper "Of course I didn’t. That’s the point. I didn’t want to say anything, but, for a human, you’re awfully bad at this whole ‘emotion’ thing aren’t you?"
    narrator "A giggle broke my sobs."
    robin "I am, aren’t I? Funny how that is..."
    narrator "I sniffled and wiped my eyes. My heart was so full that it spilled out as another wave of tears."
    harper "Rest up, Rob. I’m going to turn off most of the lights to save power, but I’ll leave one on. Just for you."
    narrator "A laugh bubbled and shuddered its way out of me."
    robin "Thanks, Harp. You big night light..."
    narrator "The gentle glow of my friend’s light shone down, covering me like a shield. My sleep came hard, and fitfully, but it came."

    # the next morning
    
    play ambience "beach ambience.mp3" fadein 4.0 loop
    scene bg beach with fade
    show robin neutral gaunt at midright with dissolve
    
    narrator "The next day, I didn’t feel much better than before. But I was fresh, I had some strength back, and a new determination. I knew my energy would go quickly because of my injury. Hunger gnawed at my stomach."
    narrator "Crawling around my camp, I finished the last of the meat and water I’d saved. I was still peckish, but it would have to do."
    narrator "I propped myself up on one elbow and looked out at the sea. I thought about what I’d seen last night."
    narrator "The coral was so close to the surface, breaking through in some places. I knew from books that it could be hard, and grew on rocks. If I ran into the rock supporting the coral, it could have flipped the raft over."
    narrator "I replayed that moment in my mind again. I sorted through the sensations that were burnt into my memory, but I couldn’t find that jarring feeling as if I’d smacked into a wall. No, the waves did me in."
    narrator "But how is that possible? Rock doesn’t exactly migrate overnight. I couldn’t have just floated around it."
    narrator "I took the shortest path towards the {i}Selkirk{/i}, and at night the coral reef almost looked like a bright, beautiful bridge leading straight to the ship. I had to have floated over it."
    narrator "That’s when it hit me."
    robin "The water is lower at night."
    narrator "I looked up at the star shining overhead."
    robin "Of course. The star’s gravity. It- It must cause the water to shift and collect."
    narrator "At night, then? At night the water was lower. The reef was exposed."
    narrator "The realization jolted me."
    robin "I can walk the reef. I could walk home."
    narrator "My face started to feel hot."
    robin "Harper. Harper, can you hear me? I have it."
    narrator "I didn’t wait for an answer. I knew it was time to get to my feet. The gash on my leg still throbbed, but the pain had faded to a dull ache."
    narrator "Using a tree for support, I wriggled upright with my weight on my good leg. My body trembled with the effort, but I managed to haul myself up."
    narrator "I gingerly tested my bad leg. My skin was so swollen that I thought I would split open."
    narrator "As I pressed down harder the painful throbbing built to an agonizing pounding, but the bones did not shift and the muscles did not buckle and I could put weight on it."
    narrator "It was good that I could walk, but I could only push myself so far. I had to think about how I was going to spend that time carefully."
    narrator "I had until nightfall, when the water level changed, to think about how I was going to cross the reef. I knew I would die here if I didn’t cross tonight."
    narrator "I had no idea what was in store for me. I’d only seen corals in pictures. The stone they grew on looked unforgiving."
    narrator "Some distant, muted part of my mind muttered to me that some corals could sting. I needed to protect my feet if I wanted to have any hope of making the crossing."
    narrator "What if the tide rose while I was out? What if I was allergic to the corals? There was far too much I didn’t know."
    
    robin "Harper, are you there?"
    narrator "I had a sickening thought, and I turned."
    # TODO: but cant robin not see the lights during the day?
    narrator "I looked towards the {i}Selkirk{/i}, as if I could reach out and touch its mind with my own."
    robin "You’re not OK, are you?"
    narrator "I stared out there at the darkened wreck, waiting patiently for an answer."
    narrator "I saw a light wink back at me. I grinned nervously, my head buzzing with an anxious hope."
    robin "OK! Two for yes, one for no. Acknowledge."
    narrator "Two winks of a running light. My next question came with a heat of urgency."
    robin "Can you hold out until tonight?"
    narrator "An agonizingly long pause, then two winks."
    robin "OK, after acknowledging this message switch off everything unnecessary and save your energy. Hang in there. I’m coming. I’ll fix you."
    narrator "Two winks. I got to work."

    #that night
    
    play ambience "beach ambience.mp3" fadein 4.0
    scene bg beach night nolights reef with fade
    show robin bored gaunt at midright with dissolve
    
    narrator "I sat by the fire as it burned the last of my fuel down to angry, glowing coals. Night had fallen, and just like before, the bioluminescent coral gleamed through the surface of the water."
    narrator "I nibbled anxiously on a strand of ropegrass, feeling it fray and come undone in my mouth, letting the tickling sensation distract me."
    narrator "Distract me from the gummy feeling in my mouth and the deep rut that hunger had furrowed into my stomach as my body began to eat itself."
    narrator "I wriggled my feet, testing the ropegrass sandals I’d made. I spent all morning puzzling about how to save my feet, and playing with the idea of making shoes from the plastic and metal I had."
    narrator "In the end I settled on making something flexible and cheap."
    narrator "I didn’t have any spare cord after building the raft. It took hours to make enough rope to coil into rough soles."
    narrator "Still more hours to work out how to use the cordage I had to stitch and weave it together into something that wouldn’t fall apart."
    narrator "I played with the idea of using them as insoles, but they were too difficult to fit neatly into my skin tight suit. The smart rubber of the suit had time to reform overnight and adapt to being worn reversed."
    narrator "It was stiff and uncomfortable, but I could actually pull the leg sleeves entirely over my feet. In the end, I secured them over the suit rubber encasing my feet using a liberal amount of ropegrass cord."
    narrator "By the time I’d finished that project, it was nearly dusk. I spent the remaining daylight searching fruitlessly for more to eat, and boiling up a few more mouthfuls of water that barely seemed to quench me."
    narrator "Night crept on, and I waited patiently. The dark held me, preventing me from doing anything but sitting and waiting by my fire."
    narrator "Eventually, I felt I didn’t want to wait any longer, though the coral barely seemed to breach the surface yet, and I hauled myself up on a scavenged wooden walking stick and set out into the surf."
    narrator "Even before the water reached my knees I could feel the sharp points of rocks poking through the mud and into my feet."
    narrator "It didn’t penetrate the sandals, but the pressure was painful, and the only relief was to lift my feet and keep moving forward."
    narrator "I was soaked. It had, unhelpfully, begun to rain, and my upper body was still clad only in my undershirt."
    narrator "So I paused to pull the upper part of the suit on. Only my good leg, clothed in the damaged leg of the suit, was exposed to the balmy waters that lapped at my calves."
    narrator "I pressed on, deep into the night.  The water grew deeper as I went further out to sea, but ceased rising around the midpoint of my thighs."
    narrator "The mud gave way to bare jagged rock, and it felt like walking on a sea of elbows, the bony points jabbing between my metatarsals. My feet were screaming in pain, and the {i}Selkirk{/i} seemed only slightly closer."
    narrator "It was awkward, slow going. I found that using my eyes to judge where to step led only to stumbling and near falls."
    narrator "The small waves splashing into me didn’t do anything to help my balance, and my muscles burnt with the effort of keeping me upright."
    narrator "As I got further from the shore, a feeling of dread crept its way into my heart."
    narrator "I imagined myself getting too tired or too hurt to go on. The water inching its way up to my neck, past my lips, spilling into my lungs, suffocating me."
    show bg ocean wreck with dissolve
    narrator "Morning came. The flat, hot blade of the sun slid its way up the horizon like a flaming guillotine preparing to fall."
    narrator "I knew someone once, a waterworks maintenance technician. Had a job working inside a station’s sump. Before he went inside the tank they swore up and down that it was isolated from the rest of the plumbing."
    narrator "He was doing some tack welding, minding his own business, when the tank started flooding with him in it."
    narrator "They got him out, but not before he’d nearly drowned. I remembered the faraway look in his eyes when he recounted the agony as his lungs and throat gulped at nothing."
    narrator "That cold memory kept me going even as my feet blistered and seared with pain. I became mechanical, something built just for walking, not for feeling, as I walked, and walked, and walked."

    # reaching the ship
    # bg ship exterior
    
    stop music
    play ambience "beach ambience.mp3" fadein 4.0 volume 2.0
    scene cg wreck with fade
    
    narrator "I would have bashed my head right into the hull if it weren’t for the expanding shadow implying the looming hull of the {i}Selkirk{/i}."
    narrator "I planted my feet firmly, trying to get as comfortable as possible, before taking the time to slowly look up."
    narrator "I could see the fine details of her hull, the seams of her ablative panels, and the bulge of plumbing where vital coolant and potables flowed."
    narrator "I spied the hint of a partly submerged gash in the hull and, my pain forgotten, I made for it with an eager splash."
    narrator "I slipped once, catching myself with a free hand. Where my palm brushed the coral I could feel a tingling that grew into a wicked burning sensation, like I was on fire again."
    narrator "I grit my teeth so hard I could feel the enamel creak, and pressed forward. Nothing mattered except getting inside."
    narrator "I felt the rock plunge away suddenly and I fell face first into the water. I came up spluttering and let my walking stick fall into the water, drifting away."
    narrator "I paddled desperately toward the gash. It didn’t look wide enough to squeeze through, but I was too close to escape to stop now."
    narrator "I gripped the edges of the gash and pressed myself into the gap, kicking and shoving my way through."
    narrator "The jagged edges of ceramic and metal dragged at my face and shoulders, and I exhaled and held my breath to keep from impaling myself."
    narrator "The wicked ribs of the ship ripped bloody gouges into my face and shoulders as I pulled myself forward relentlessly, eyes squeezed shut, unable to turn or wiggle backwards."
    narrator "I moaned in a desperate, primal terror as I shivered my way through the tangled wreckage. The light slowly faded as I crawled blindly forward."
    
    stop music
    play ambience "ship ambience 1.mp3" fadein 4.0 volume 2.0
    scene bg ship corridor with fade
    
    narrator "Finally, the barbed and twisted metal gave way and I fell into thin air, flopping with a great splash onto the waterlogged deck. I trembled and shook from the cold of the water seeping into my suit."
    narrator "The deck was canted at a significant angle, sloping away from me and threatening to send me tumbling against the far wall."
    narrator "Even on this somewhat kinder ground my feet still felt like they were full of glass. I felt I’d surely cracked a few bones from the harsh walk."
    narrator "Blood sheeted down my face and arms. I wiped my eyes and threw myself at the nearest hatch with a grunt. Of course the electrics were down, and the door didn't throw itself open automatically as it normally would have."
    narrator "I sighed and groped in the dark briefly, until my hands found the emergency access panel. I fingered the catch and it popped open with a satisfying click. How I'd missed those sounds."
    narrator "The panel swung open, revealing a small, unassuming valve helpfully labeled \"MANUAL ACCESS - TURN CLOCKWISE\". I unfolded the small handle attached to the rim of the valve and began cranking it."
    narrator "Slowly, very slowly, the door eased open. Water trickled, then poured through the widening opening to flood the hallway beyond."
    narrator "As soon as the opening was wide enough I squeezed through, then used the valve on the opposite side to seal it behind me to prevent more flooding."
    narrator "I turned with a limp, feet splashing in the puddle by the hatchway. I gasped at the pain that shot through my ruined feet and fell against a nearby wall to stay upright."
    narrator "I was panting hard. My breath steamed in the frigid air of the ship. I looked, but I could see only vague shadows. Even the emergency lighting was shot."
    narrator "I slid along the wall, one arm outstretched, hand flat against the hull, feeling my way forwards. Thankfully the flooding seemed not to have reached this area, and my shivering began to slow."
    narrator "My hand fell away into the dark. An opening."
    narrator "I placed my good hand against the mouth of the opening and felt the regular shapes of molded metal, a thin, rough seam where a precise weld was made. Felt like a hatchway."
    narrator "Stepped closer, prepared to duck through. My fingers rested on a particularly smooth part of the hatch frame. Someplace worn from the thousands of times I'd touched that exact spot."
    robin "Can't be..."
    narrator "I went inside and groped along the wall again. By some miracle, the light switch worked, and the room was bathed in red light. My berth."
    narrator "Nearly everything was stowed, just like I'd left it. Most things were neatly tucked away in sealed, transparent pouches stuck to the walls."
    narrator "Most every surface and item was covered in strips of rough touch fastener; lets you stick anything to anything so nothing comes loose when you're underway."
    narrator "Even through the tears blurring my vision, I could see that the floor was scattered with a handful of items that had broken free."
    narrator "One of my beloved plush dolls, this one worn with use. A magazine I'd read a hundred times. Familiar tools I must have been using in the days before we came down."
    narrator "My hands shook from chill and excitement, then I finally collapsed as a wave of relief flooded my body. I was home."
    narrator "I felt around for somethign to warm myself. My fingers had gone weird. Wouldn't close right. I could only manage to roughly pull drawers out and sift through my things with my palms until I caught a handful of chemical hand warming packets I’d stashed."
    narrator "I squeezed pathetically, trying desperately to crack one with the little strength I had left, then resorted to seizing a hardcover manual that I had stuck to a patch of touch fasteners and smashed them ruthlessly."
    narrator "As I felt the packets growing warm, then hot, I shoveled them into my suit, squeezing them under my armpits and pinching one beneath my chin."
    narrator "With a shaking hand I yanked my sleeper bag from its place on the wall and crawled inside to wait for the shaking to stop."
    narrator "I could feel myself slipping away. My body wanted to sleep, to heal. But it wasn’t over yet."
    robin "I’m coming..."
    narrator "I stared at the overhead lights, waiting for them to wink at me."
    robin "Do you hear?"

    stop music fadeout 3.0
    show black with fade

    pause 5.0

    play ambience "ship ambience 1.mp3" fadein 4.0 volume 2.0
    scene bg ship corridor with fade

    narrator "The world came back into gentle focus. I felt heavy, and terribly damp. I didn't feel rested, but my mind was definitely sharp once more."
    narrator "My mouth was dry and my stomach had that familiar empty feeling. I eyed the pouch on the wall near my bunk where I normally stashed snacks and licked my cracked lips."
    narrator "I tested my limbs gingerly, prompting waves of aching, soreness, and stinging pain all over. I peeled the sleeper bag away, slick with sweat and seawater, and pulled my legs under me with a groan."
    narrator "My feet touched the ground, and I nearly cried out from the searing pain. It had somehow gotten even worse than before. I dropped back to sitting with a hiss of pain."
    narrator "Everything below my ankle felt heavy and swollen, the skin stretched tight. I didn't dare remove my suit to get a better look until I'd dealt with the gash on my leg."
    narrator "I dragged myself over instead, and reached up to pluck the pouch from the wall. I jerked it open and spilled a variety of meal replacement tubes and no-spill flavored drink packs into my lap."
    narrator "I ripped into them with my teeth and devoured one after the other greedily. I'd never particularly enjoyed ready foods, but after the time I'd had this was practically gourmet."
    narrator "After I'd sucked them all down I went back to the empty tubes and squeezed them out once more, trying to get every last bit."
    narrator "I tore open each of the individually sealed drink packs and meticulously licked the insides clean."
    narrator "I felt satisfied for the first time in a long while. I sat there for a moment, enjoying the feeling of fullness, feeling spoiled."
    narrator "Out of habit I policed up the empty packaging and neatly packed the trash back into the pouch, sticking it back on its place on the wall."
    narrator "I sat against the wall, staring at my feet. Even through the skinsuit I could see how swollen they were."
    narrator "I experimentally tugged at the suit. I pulled it away from my hips, past my knees, but it would move no further; it still had a firm grip on my calf. Probably for the best until I had another way to stop the bleeding."
    narrator "Dragging myself along the floor, I sorted through my things until I found the first aid kit and my tool belt."
    narrator "The first aid kit contained meager supplies. Pack of sterile gloves, an epinephrine autoinjector, lots of antiseptic gel (\"do not apply to open wounds\"), plasters for nicks, enough painkillers for a bad headache, rolls of gauze, sterile wound wash..."
    narrator "I dry swallowed the painkillers and smeared antiseptic gel on my cuts and the stinging rash on my hand. I peeled open a plaster and stuck it over a nick on my arm. It was so sad I couldn't help but laugh dryly to myself."
    narrator "I looked for something to tourniquet my leg. I thought for a moment, then opened another pouch and withdrew an elastic exercise band. I draped it over my leg, just above the knee."
    narrator "I stretched it tight, and tighter, flexing my arms and shoulders to leverage all my strength, and wrapped it around and around my leg with a grunt. My lower leg started to tingle. A good sign I'd done it right."
    narrator "When I ran out of length, I tucked the end of it beneath the wrap to keep the band in place."
    narrator "I pulled my utility knife from my tool belt. I took a moment to appreciate the elegance and beauty of the tool. I flicked the catch and the blade sprung free from its scabbard."
    narrator "I swept the blade along the suit, then dug my fingers into the gash and tore the suit away, freeing my legs and feet."
    narrator "I forced myself to look at the cut on my leg. The edges were ragged, the flesh in and around it was wet with blood and clear fluid. I could see my muscles moving inside my leg. My vision swam. I laid on my back until I could bear to look again."
    narrator "I put on a pair of sterile gloves for what would come next. A flap of skin clung to the edge of the wound by a strip of tissue. It was long enough that it hung down past my ankle."
    narrator "I touched it gingerly with a fingertip and was rewarded with stinging pain."
    narrator "I wiped down the tip of the utility blade with antiseptic gel, let it dry, then held my breath and severed the strip of skin from my leg. I bit back a cry of pain."
    narrator "Next, I sprayed the sterile wound wash solution into the cut. I was surprised that the only sensation I felt was a deep, aching burn as I rinsed away globs of blood and sand."
    narrator "I felt a cold sensation spreading at the back of my skull. I tried to ignore the tinny voice chattering from that fearful place, whispering about dead nerves that would never work again."
    narrator "I have to close this up."
    narrator "I dug through my supplies. Found a spool of fine synthetic thread, stuff normally used in the printers for fabrication."
    narrator "I snatched up the autoinjector and worked a pair of pliers into a seam in the housing. It popped apart, sending a spring and bits of plastic spinning away, and exposing the injector hidden inside."
    narrator "I drenched the thread and pliers in antiseptic, then pulled the needle free from the rest of the injector assembly."
    narrator "I held the hollow needle close to my face where I could see the opening and carefully fed the sterile thread through. Gently, I bent the needle using my pliers to give it a slight curve."
    narrator "Clutching my makeshift suture kit in my hands and a fistful of rubber suitskin between my teeth, I sunk the needle into my flesh and began stitching myself back together."
    narrator "I had a few false starts. My skin was weak from malnourishment, and when I tried to pull the first stitch taught, the thread tore right through it. Starting the stitch further from the lip of the wound solved that."
    narrator "The stitches were clumsy, ragged and uneven like my nerves, but my leg was closed up."
    narrator "I smeared the wound in more burning antiseptic and loosened the tourniquet experimentally. My leg tingled as sensation slowly returned. Blood seeped from the wound, but it wasn't anything concerning."
    narrator "Next, my feet. They were swollen, the skin was a raw, angry red. The blisters that had developed from my first day were massive, and some were dark red with blood. A few had torn open to expose the layer of skin beneath."
    narrator "The skin was tender, and far more painful than my leg was. More wicked, fiery antiseptic. I soaked the needle again, then lanced each blister one at a time. The relief as I squeezed the fluid out was incredible."
    narrator "I bandaged my leg, using tape to secure it, then wrapped both feet in thick layers of gauze. I threw on two pairs of clean socks and a spare set of boots over them."
    narrator "Experimentally, I set my feet flat on the ground. I put a little weight on one foot, the other- Each step still ached like hell, but at least I could limp around."
    narrator "I tidied the mess I'd made somewhat, then, armed with my toolbelt and a flashlight, I hopped back out into the corridor to get back to work."

    # TODO: insert a transition here to suggest time passing
    narrator "Part of the mess compartment had collapsed, but not all of the supply cabinets had been flattened."
    narrator "I opened each cabinet once to estimate how full it was, then emptied one and started counting packages. Opened a package and checked the contents against the nutrition sheet."
    narrator "I even found a real pen and started scribbling an inventory in the yellowed margins of a dusty hardback manual."
    narrator "Some simple arithmetic, and I was happy with the estimate of the ready supply. Plenty to eat and drink for at least a month without rationing."
    narrator "The long-term storage came flatpacked in big bulk cargo containers, so I pulled a schematic and tried for an estimate by volume."
    narrator "I hadn't done calculus by hand in years and I knuckled my eyes in frustration as I muddled through the problem."
    robin "Harp, can I get a check on this solution-"
    narrator "The words caught in my throat. My knuckles turned white, the hard back of the manual creaked. I willed my hand to relax."
    narrator "My eyes fell back toward the page. The numbers."
    narrator "I cleared my throat. Put on my best Harper impression."
    robin "It might become a concern if we couldn't-"
    narrator "Could {i}not{/i}."
    robin "-could not drop into bluespace and were forced to proceed at relativistic speeds."
    narrator "I sniffed and turned up my nose melodramatically."
    robin "I am sure if we went the slow way that humans would find some way to turn back progress."
    narrator "I deflated somewhat."
    robin "No, Harper would never be that mean... Or speciesist."

    # TODO: time passing transition
    narrator "I walked the corridors while chewing on a fruit bar, checking every compartment, taking stock of the damage."
    narrator "The network being down, I used a marker with a fat chisel tip to scrawl notes on my arm or directly onto the hull beside each hatch."
    narrator "Slowly, I built a picture of the state of the ship."
    narrator "The gash in the side of the ship was catastrophic. The hatches had contained the worst of the flooding, but the arterial corridors were cut in places leaving large sections of the ship inaccessible."
    narrator "The {i}Selkirk{/i} must have been tumbling as it came down; it landed tail first, its nose pointing out of the water."
    narrator "This meant that the main engine, the torch, was not only submerged, but suffered an unknown amount of damage when it struck the water and whatever lay beneath it."
    narrator "I traversed every corner of the ship I could reach. With the slope of the deck making walking difficult, it was slow going."
    narrator "Three out of four of the Individual Exit Vehicles (IEVs) were unusable. One I'd lost during the ride down, two were wrecked or cut off by damage from the crash, but the last was intact."
    narrator "Even intact, an IEV wasn't all that useful. Its thrusters were intended for use in microgravity, so it didn't have any hope of escaping the atmosphere on its own."
    narrator "It was difficult to judge the extent of the flooding, but it seemed largely contained to a small portion of the ship. It'd still be a hell of a job to fix it."
    narrator "And reversing the flooding was not optional. Even this superficial flooding would doubtlessly be a disaster for the flight characteristics."
    narrator "In spite of my fears, the torch was in great shape. It was by far the most rugged and reliable part of the ship, and I cared for it well, but it nevertheless surprised me at how little harm it had suffered."
    narrator "Redundant systems even allowed me to gain remote access to do a test spark. Even entirely submerged, it was capable of lighting."
    narrator "The bluespace drive being intact was far less surprising. Not needing access to the exterior of the ship, and being relatively simple mechanically, it was easy to bury away."
    narrator "The B-drive compartment was there, deep in the ship's ribcage, beneath layers of superstructure and deck plating. It was a massive, seamless black box."
    narrator "They were designed to be tamper-proof, so B-drives aren't designed to be maintained. They're built, vacuum-sealed permanently in these shells, then used up and destroyed."
    narrator "Bluespace travel was as convenient as it was dangerous."
    narrator "Where once was Huangdi, a core world and a haven of science and intellect, now could only be found a black hole surrounded by the accreted matter of what once was a thriving and ingenious people."
    narrator "The first lesson we learned in the certification course: don't switch on near a gravity well. That lesson was learned at unfathomable cost when the first viable B-drive was tested by unsuspecting researchers on Huangdi."
    narrator "I ran one hand over the hard, black shell of the B-drive. It's surface was unbroken, seamless, like polished midnight."
    narrator "If the shell is compromised, the vacuum is broken, triggering a self-destruct that turns the internals to slag, to prevent reverse-engineering."
    robin "You're our ticket out of here, if we could just break orbit..."

    # TODO: timeskip transition
    robin "If we could just break orbit..."
    narrator "After I topped the reactor off with fresh coolant, courtesy of the alien ocean, the power output had come back up to nominal levels. Yet Harper didn't leap back to life."
    narrator "Much of the lights and a few appliances were down as well, so I could only hope it was an electrical problem, and Harper hadn't blacked out."
    narrator "So there I was, hip-deep inside of one of Harper's maintenance accessways, fumbling around with a multimeter checking the conduits."
    narrator "Though I'd been eating well recently, it hadn't restored my stamina just yet, and I poured with sweat as I stretched to reach further in."
    robin "So, what would you do, huh Harp?"
    narrator "The neat bundles of wires didn't reply. A hair tickled my eye and I huffed it away."
    robin "Yeah, be that way. Make me do all the damn work."
    narrator "I checked the readout again. Again, the wiring read as OK."
    narrator "I dropped out of the accessway and slumped to the deck with a sigh."
    robin "We got juice and we got a torch. That's everything we need to break orbit."
    narrator "Except, the torch was under all that water. When lit, it output enough energy to put a planetcracker to shame. It'd be like dropping molten slag into a vat of chemfuel."
    narrator "I had some qualms about turning my crash site into a crater, but more still about dying alone on this world."
    narrator "I rolled a few metal bolts around in my palm."
    robin "If I could just get the torch out of the water..."
    narrator "I popped one of them into my mouth. I spat it hard, and frowned as it sailed in a little arc and landed only halfway across the compartment."
    robin "Not as fun in this much gravity..."
    narrator "I held another bolt between my teeth, pursed my lips, puffed my cheeks-"
    narrator "I let the air out softly. The bolt dropped into my lap."

    # TODO: timeskip transition
    narrator "I plopped down into one of the crash couches in the flight control compartment. I throw the harness over my shoulders and got strapped in."
    narrator "I held my helmet between my legs. My fingers drummed on it nervously."
    narrator "Propped atop the helmet was a tablet I had managed to coax back to life. It was running a countdown for me, counting the seconds until the airlocks had fully pressurized."
    narrator "I'd sabotaged the life support system in certain key compartments to allow me to pressurize them far beyond what had ever been intended."
    narrator "The pumps were never designed to work against such pressures, so I'd had to get creative."
    narrator "The ship had far more pumps than was necessary, for redundancy, so I pulled the necessary parts and rigged up a dozen of them in series."
    narrator "The tests had went well, so now came the moment of truth. I'd already sparked the torch and it was warming up."
    narrator "The pumps force air into sealed compartments far aft. They build up an obscene amount of pressure, just a little more than what they're rated for."
    narrator "At just the right moment, I close a circuit which, if my blueprint reading skills are sharp as ever, should trip the exterior airlocks, leading to-"
    # TODO: shaking
    # TODO: muffled thump
    narrator "There's a deafening bang and a great, shuddering lurch. I'm sucked into the crash couch as a monumental acceleration leans against me like the mighty hand of a god."
    narrator "The air is driven from my lungs in one great whoosh. At the same time, my helmet and the tablet are thrown against the back wall with a crash."
    narrator "A heartbeat passes. Enough time to review and affirm that I did not stupidly close the circuit by mistake. So the airlocks must have been damaged, or my math was off."
    narrator "Another heartbeat. My heart soars as I feel the acceleration slowly turning into that wonderful, homey sense of weightlessness as the ship begins to fall."
    narrator "There's another circuit I set up. This one I rigged as a simple switch below my boot, so I could actuate it even under massive acceleration."
    # TODO: cut out ALL sound
    narrator "I twitched the toe of my boot. There was a sound like the birth of the universe. At that moment, it was undoubtedly the loudest sound in the solar system."
    narrator "The torch burned hard, and I was driven again into the crash couch. If I could have moved, I would have leapt up and cheered."
    narrator "Even if the {i}Selkirk{/i} hit a mountain in the next second, I would have died happy, knowing I did everything I could to survive."
    narrator "My lungs screamed for air, but under the constant acceleration of the torch, my chest couldn't expand. The walls slowly closed in."

    stop music fadeout 2.0
    stop ambience fadeout 2.0
    show black with fade

    pause 5.0

    scene bg starfield with fade
    play music "music/Leaving Home.mp3" fadein 8.0
    pause 5.0

    # epilogue. there should be a weighty, patient transition to linger on the fact that Harper’s fate is unknown
    narrator "I reckoned it had only been a couple weeks on the island, and then a good few months aboard the grounded {i}Selkirk{/i} before I was able to get her spaceworthy again."
    narrator "Now, back in space, it felt good to be away from the strangling hold of gravity. I drifted through the halls, wearing a bored expression, doing my rounds."
    narrator "If it weren’t for the aches and scars where the medbay had stitched me back together, it would almost have been as if nothing happened."
    narrator "Almost. I was much less comfortable wearing a pressure suit, for one, and I did a lot of my work in just underclothes now."
    narrator "It didn’t hurt as much to remember, now."
    narrator "When I awoke from that hard sleep that came after my first day back, I pulled myself together a bit and got back onto my portable terminal. The gamble had paid off."
    narrator "The reactor was stable, power stored in the capacitors was actually {i}increasing{/i}, and Harper was online but effectively comatose after taking itself partly offline."
    narrator "I spent days walking the ship diagnosing, triaging, and treating the extensive damage."
    narrator "The reactor was in bad shape, and reversing the flooding was long and difficult work, but soon I had things patched up enough that I felt the ship wasn’t going to disintegrate while I wasn’t looking."
    narrator "Then, it was long days of exhaustively checking and cataloging everything to prepare for escaping to orbit."
    narrator "I remembered that sinking feeling as I assessed the damage. The flooding had been contained and a takeoff would be possible, but the water had damaged the AI compartment most of all."
    narrator "Those days, the days I spent salvaging Harper’s memory, restoring backups, replacing damaged drives, essentially performing brain surgery on my best friend... Those were the hardest of all."
    narrator "After we lifted off, once it was certain we were on the best course towards the shipping lanes where we could get picked up, I spent every waking moment piecing Harper back together. One scrap of memory at a time."
    narrator "My mind returned to the present as I finished my daily checks. I slapped my clipboard onto a stick-patch on the hull and swung my way aft, towards the AI compartment."
    narrator "Every day I told myself, today is the day I’d punch in the wakeup command. Harper had finished recompiling days ago, but I woke up the displays and checked it anyway. It was still ready."
    # final scene
    
    label credits:

    stop music fadeout 8.0
    play ambience "ship ambience 2.mp3" fadein 4.0 volume 2.0
    scene cg end with fade
    pause 4.0
    
    narrator "My heart was in my mouth as my finger hovered over the control that would key the reboot macro I’d written by hand."
    narrator "AI don’t get shut down partway and then rebooted. It simply wasn’t done. I had to write the procedures myself."
    narrator "I breathed hard, my eyes fixed on the screen."
    robin "Do it. Do it. Just get it over with."
    narrator "What if it doesn’t wake up? What if it’s not Harper anymore?"
    narrator "The fear built to a crescendo as I channeled all of my will into a fingertip. Slowly, I forced it down. Pressed the control. A gentle chime confirmed my input."
    narrator "The silence, afterward, was deafening."
    narrator "Then..."

    stop ambience
    
    show black
    pause 4.0
    #harper "Robin?"
    #TODO: credits

    show text "CREDITS\nWriting - Parsely\nArt - Halfbrick\nNarrative Design - Vince\nAdditional Programming - Furtuka" with dissolve
    pause 8.0
    show text "PLAYTESTERS\nThat's you!" with dissolve
    pause 8.0
    show text "ASSETS\n\Big list of attributions." with dissolve
    pause 8.0
    show text "Thanks for playing!" with dissolve
    pause 12.0

#end

