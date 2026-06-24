# TakeMeter- planning.md

---

## Community

**Chosen Community:** r/CharacterRant, a subreddit dedicated to in-depth discussion of fictional characters across anime, manga, comics, film, games, and TV

**Why this community?:** CharacterRant was chosen because its posting culture is unusually rich and self-aware. Unlike general media subreddits where posts trend toward reactions or news, CharacterRant explicitly encourages structured argument, which means posts tend to have identifiable rhetorical intent.

**Why is it a good fit for classification?:** The discourse is varied across multiple dimensions that map cleanly onto distinct label categories: posts range from carefully evidenced literary analysis to pure emotional reaction, from specific character arguments to meta-commentary about fandom culture itself. The community also has enough volume and consistent subject matter that examples across all labels can be collected without scraping wildly different contexts.

---

## Labels

`analysis`: A post that uses evidence, specific examples, or detailed reasoning to support a claim about a character, story, or piece of media — the core move is argument, not assertion.

**Example 1:** Powerscaling One Piece is a category error
One Piece is not a powerscaling manga. Oda has said in interviews that he deliberately avoids establishing consistent strength hierarchies because fights in One Piece are decided by story logic, not by who has higher numbers. Luffy beating Crocodile twice after losing once doesn't mean Luffy power-jumped — it means the plot needed him to win. Applying powerscaling frameworks from Dragon Ball or Naruto to One Piece produces contradictions because those frameworks assume a consistent internal logic that Oda explicitly rejects. The series rewards thematic reading, not stat comparison.

**Example 2:** Why Zuko's redemption arc works when others don't
Zuko's arc succeeds because his redemption is earned through repeated failure rather than a single turning point. Most redemption arcs give a character one dark moment, one realization scene, and then they're good. Zuko gets three seasons of backsliding. He chooses wrong in Ba Sing Se after seeming to come around. That choice has real consequences. By the time he actually joins the Gaang, the audience has watched him earn it incrementally. His final confrontation with Ozai isn't a dramatic heel turn — it's the endpoint of a long process the show made you watch in full.


`hot_take`: A post that leads with a strong, confident opinion, often unpopular or contrarian, supported by minimal formal reasoning, relying primarily on assertion and rhetorical force rather than evidence.

**Example 1:** Gojo Satoru is an overrated character being carried by his design
Gojo has a cool design and a fun personality and almost no character depth. His entire function in the story is to be the ceiling that everyone else measures against and then to be removed so threats feel real. His backstory chapters are the most interesting he gets, and even those are mostly about Geto. The fandom treats him as one of the best written characters in modern shonen because he's cool to look at and has good one-liners. That's not writing. That's aesthetic.

**Example 2:** Sasuke deserved a worse ending
Sasuke killed thousands of people and gets to wander the world as an independent redemption arc while Naruto is Hokage. The disparity is absurd. His crimes during the war arc alone should have resulted in imprisonment at minimum. The show treats his relationship with Naruto as sufficient justification for everything, which is emotionally resonant but narratively dishonest. The ending rewards him for being the protagonist's rival rather than holding him accountable by the same logic the show applies to everyone else.


`meta`: A post whose primary subject is the fandom, community, discourse, or audience itself rather than a specific work or character; it steps back from the object level to comment on how people engage with media.

**Example 1:** Why powerscaling communities are fundamentally misreading fiction
Powerscaling as a practice treats narrative fiction as if it were a physics simulation. It extracts feats from their narrative context, calculates implied magnitudes, and then uses those calculations to produce rankings that the authors never intended. This is a category error. Authors are not running simulations — they are producing emotional and thematic experiences. Powerscaling communities systematically extract the least interesting dimension of stories and argue about it indefinitely.

**Example 2:** The discourse around 'strong female characters' has gotten stupider over time
In 2012 the critique was that women in media needed more than love interest roles. Valid. In 2024 the discourse has degraded to: any female character who shows vulnerability is badly written, any female character who is competent at fighting is well written, and the two positions are treated as equivalent. Strength is not a personality. The discourse flattened a legitimate critique into a checklist and the checklist is producing worse arguments than the original critique.


`venting`: A post driven primarily by emotion — frustration, grief, affection, or exhaustion, where the goal is expression rather than persuasion, and the reasoning (if any) is secondary to the feeling.

**Example 1:** I watched the Promised Neverland season two in real time and I'm still not over it
Season one of The Promised Neverland is one of the best anime seasons I have ever watched. It is perfectly structured, it builds tension consistently, and the finale leaves you wanting more in exactly the right way. Season two exists. I watched it. I will not describe what happens except to say that if someone handed me a copy of it having never seen it before, I would not believe it was produced by the same people with any intention of honoring what season one built. The anger has faded into a kind of resigned sadness. What a waste.

**Example 2:** I actively resent how much I care about fictional characters
It's embarrassing. I know it's embarrassing. I'm a functional adult who has sat with actual feelings about the fate of characters who do not exist. After the Chimera Ant arc ended I needed a day. After a certain moment in Vinland Saga I needed two days. I have recommended shows to people and then had to stop because I started feeling protective about spoilers for events I already know. This is not a healthy relationship with fiction and I have no intention of developing a healthier one because the alternative is watching things with less engagement and that sounds worse.


---

## Hard Edge Cases
`hot_take` vs `analysis`

The most common hard case is a post that makes a confident, contrarian claim but supports it with some evidence or reasoning. The defining question is: is the evidence doing real argumentative work, or is it decoration for a conclusion the post already committed to?

An analysis post builds toward its conclusion, the evidence constrains what the conclusion can be. A hot_take post starts at its conclusion and selects examples that support it, dismissing counterevidence or not engaging with it at all. In practice: if removing the evidence would leave an undefended assertion, it's a hot_take. If removing the evidence would make the conclusion unsupportable, it's analysis.

**Handling edge cases during annotation**

When a post is genuinely ambiguous, the process is:
- Identify the primary move the post is making (arguing, asserting, feeling, reflecting on community).
- If still ambiguous, apply the "remove the evidence" test for hot_take vs analysis.
- If still ambiguous after both steps, label it with the best fit and add a note in the notes column flagging it as an edge case for later review.
- After 50+ examples are labeled, review all flagged edge cases together to check for consistent patterns and adjust label definitions if necessary.

---

## Data Collection Plan
**Primary source:** r/CharacterRant posts collected via PullPush API (api.pullpush.io), which archives Reddit content without requiring authentication

**Target:** 50 examples per label (200 total), with a 25-example buffer target (225 collected before filtering).

**If a label is underrepresented after 200 examples:**
- `analysis` underrepresented: Search specifically for posts with longer average length and flair tags like "Discussion" or "Essay."
- `hot_take` underrepresented: Search for posts with titles containing "unpopular opinion," "hot take," or "controversial."
- `meta` underrepresented: Search for posts explicitly about fandom discourse, powerscaling, or community behavior.
- `venting` underrepresented: Search for posts with first-person language and emotional register in the title ("I can't believe," "I'm tired of," "why does").


--- 

## Evaluation Metrics

**Macro F1 Score:** Macro F1 averages the F1 score across all four labels without weighting by class size, which means a poor-performing label on a small class is not hidden by good performance on large classes. This is appropriate because all four labels are equally important to the classifier's usefulness;  a tool that can't identify meta posts is not a useful tool even if it nails analysis.

**Accuracy is not enough:**  The dataset targets 50 examples per label, which produces a roughly balanced class distribution (25% each). In this setting, a classifier that predicts the majority class for everything would achieve ~25% accuracy — so accuracy is not misleading in the way it is for highly imbalanced datasets. However, accuracy still doesn't distinguish which labels the model is failing on. A model with 70% accuracy might be perfect on analysis and venting while being near-random on meta and hot_take. Per-class metrics surface this; accuracy does not.

---

## Definition of success
**Threshold for "genuinely useful":** Macro F1 ≥ 0.72, with no individual class F1 below 0.60.
- **Rationale:** A macro F1 of 0.72 means the classifier is performing substantially above chance across all four labels. A floor of 0.60 per class ensures no single label is effectively unusable. At this performance level, the classifier could plausibly be used to pre-sort a feed of CharacterRant posts for a researcher or community tool, with the expectation that a human reviews borderline cases.

**Threshold for "good enough for deployment":** Macro F1 ≥ 0.78, with no individual class F1 below 0.68.
- **Rationale for the gap:** The lower threshold (0.72) is "interesting and usable with oversight." The deployment threshold (0.78) reflects a tool a user could rely on without reviewing every prediction; error rates are low enough that occasional misclassification doesn't undermine the tool's value. These numbers are specific enough to determine objectively at evaluation time whether the threshold was hit.

**What would indicate failure?:** Macro F1 below 0.60, or any individual class F1 below 0.50 (near-random for a four-class problem). This would suggest the label definitions are too ambiguous, the training data is too small, or the feature representation is insufficient, all of which are diagnosable.

---

## AI Tool Plan

**Label stress-testing:** 
`hot_take` / `analysis` boundary
1. **Itachi is the most overrated character in Naruto and the retcon ruined the series**
The Itachi retcon is bad writing dressed up as a twist. Before the reveal, Itachi worked as a villain because his actions had weight — he destroyed his clan, he traumatized his brother, he did monstrous things. The retcon doesn't undo those actions, it just asks you to feel differently about them, which is emotional manipulation rather than storytelling. A well-written character shouldn't require retroactive reframing to be sympathetic. The reveal that he was secretly good all along cheapens every scene where his villainy mattered. It's the narrative equivalent of "it was all a dream." The fandom treats this as a genius twist. It's a cheat.

**Why it's hard:** Makes a structural argument with a specific mechanism ("emotional manipulation rather than storytelling"), but the conclusion is pre-committed and counterevidence isn't engaged. Does the one-sentence argument about what "well-written" means count as reasoning or assertion?

2. **Mob Psycho 100 earns its ending and here's exactly why**
The final arc of Mob Psycho works because it's not actually about Mob's power. It's about whether he can be a person without it. The Mogami arc established that Mob's biggest fear isn't losing — it's becoming someone who uses his power without caring about the cost. The final arc delivers on that fear directly: the 100% Awakening mode is Mob at his most powerful and his least himself. The resolution isn't him winning a fight. It's him choosing not to. Every prior arc was building the specific question this one answers. That's not a happy ending — it's a thematically complete one.

**Why it's hard:** Clear analytical structure with arc-to-arc evidence. But it's also defending a positive opinion with notable enthusiasm. The "here's exactly why" framing is hot_take energy even though the body is analysis.

3. **People who say Fullmetal Alchemist Brotherhood has a perfect ending are wrong**
Brotherhood's ending gives the characters everything back. Ed gets his alchemy back in the form of his father's portal. Al gets his body. Winry gets Ed. The Promised Day is won cleanly. This is the equivalent of a story about the cost of war ending with everyone coming home uninjured. The series spent sixty episodes telling you that equivalent exchange is real and painful, then spent its last two undoing every exchange that mattered. I understand why people find it satisfying. Satisfaction is not the same as earning it. The 2003 anime understood this. Brotherhood chose the comfortable version.

**Why it's hard:** Uses the 2003 comparison as evidence and makes a specific structural argument ("equivalent exchange is real and painful, then undoing every exchange"). But "satisfaction is not the same as earning it" is assertion. The post straddles the line throughout.

`venting` / `hot_take` boundary
4. **I'm so tired of people defending Boruto and I need to say this**
I have tried. I genuinely have. I watched the first fifty episodes looking for what people who like it are seeing. There are moments. The dynamic between Boruto and Kawaki has potential. But the show wastes so much time on filler-tier material, sidelines every character from the original series who made Naruto worth watching, and treats its title character's trauma as a personality substitute. I know people love it. I know it's not made for me specifically. I'm still allowed to be exhausted by the constant "it gets better" promise from a show that has had eight years to get better and hasn't. My patience is gone and I'm done pretending otherwise.

**Why it's hard:** Clearly emotional and exhaustion-driven. But also makes specific criticisms ("filler-tier material," "trauma as a personality substitute") that gesture toward argument. Is the frustration driving the post or is the post trying to persuade?

5. **Gege Akutami doesn't respect his own characters and I'm furious about it**
Nanami deserved better. Haibara deserved better. Gojo deserved better, and I say that as someone who thinks his return undercut his death. The post-Shibuya arc has been a machine for producing deaths that don't land because the series never gives you enough time with anyone before removing them. This is not bold storytelling. It's the illusion of stakes without doing the work that creates stakes. You can't make me feel something about a character you introduced three chapters ago. I'm angry at this in a way I'm not angry at most things I've watched, because the early material was so good and this is such a waste of it.

**Why it's hard:** The anger is genuine and primary (venting). But "illusion of stakes without doing the work that creates stakes" is a real craft argument. The post is emotionally driven but the criticism is structurally coherent.

6. **The Chimera Ant arc is peak fiction and I will die on this hill**
I have never felt more wrecked by a piece of media in my life. Meruem and Komugi. Gon's transformation. Killua carrying him home. The way the arc ends not with a victory but with everyone just going on with their lives, diminished. Fiction almost never does this — commits this fully to showing you that winning costs something real and irreversible. I've tried to explain to people why it matters and I can't. You either feel it or you don't. I feel it so strongly that I've recommended it to people specifically hoping they'll understand why I feel this way, and when they don't it's personally disappointing in a way I can't fully defend.

**Why it's hard:** "Fiction almost never does this" and the structural observation about how the arc ends are genuine analytical observations. But the post's goal is clearly to express feeling rather than persuade. The line "you either feel it or you don't" explicitly abandons persuasion.

`meta` / `analysis` boundary
7. **The reason everyone misreads Light Yagami the same way is a fandom structure problem**
Light Yagami gets read as a tragic hero by a significant portion of the fandom. This reading is wrong, but more interestingly, it's wrong in a predictable and structurally explicable way. Protagonist identification is a default cognitive move — we route for the POV character regardless of what the text tells us about them. Death Note exploits this by giving Light the POV while systematically indicting him through L, Ryuk, and the structure of his defeats. The fandom's misreading isn't careless — it's the expected output of engaging with a protagonist-centered narrative without meta-awareness of how POV shapes sympathy. The show anticipated this. A significant portion of its audience didn't.

**Why it's hard:** The subject is fandom behavior (meta) but the argument uses textual analysis to explain that behavior (analysis). Is this a post about how people engage with Death Note or a post about Death Note? It's genuinely both.

8. **We need to talk about why isekai protagonists keep being the same person**
The isekai protagonist formula — ordinary guy, hidden exceptional trait, rapid social and power accumulation, harem of admirers — isn't a coincidence or creative laziness. It's a response to market incentives. Light novel publishers know what sells and the audience has demonstrated that it wants this character. The formula is the product. This means criticizing any specific isekai protagonist for being a self-insert fantasy is misdirected — the character is doing exactly what the genre contract specifies. If you want to criticize isekai protagonists, you need to criticize the audience preference that created them. The character is downstream of the reader.

**Why it's hard:** Argues about why fandom/market produces a certain character type (meta), but builds the argument with structural analysis of genre economics (analysis). The conclusion is about reader behavior but the evidence is about narrative mechanics.

**Annotation assistance:** Claude was used to pre-label a batch of synthetic examples before human review. All 204 synthetic examples in the dataset were generated with labels assigned by the model. These labels were reviewed manually and each example was read and the label confirmed or corrected before inclusion in the training set. All synthetic examples have an empty url field, which distinguishes them from scraped posts. A separate notes column entry of synthetic was added during generation. Any example where the pre-assigned label was changed during review has been noted.

**Failure analysis:** Looking for:
- Whether `hot_take` → `analysis` errors cluster around posts with a specific structure (e.g., posts that cite one piece of evidence but don't engage with counterarguments).
- Whether `venting` posts about specific fandoms (Dragon Ball, Naruto) get misclassified as hot_take due to strong claim language.
- Whether `meta` posts that contain analysis of community behavior get pulled toward analysis.