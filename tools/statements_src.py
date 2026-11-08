#!/usr/bin/env python3
"""Writes content/map/statements.json from the compact list below.

Each statement is one thing one party said, placed in one of the five
questions of the problem situation map (what, who, where, why, how), under
a theme. Voices: A alumni (the survey), O organizers (Record #4, the C02
calendar), P the problem owner (Nov 6–7), S the steering committee (records
and parked notes), X other programs and research (the case library).

    python3 tools/statements_src.py && python3 tools/build.py
"""
import json, os

S = []
def add(q, theme, by, src, *texts):
    for t in texts:
        S.append({"q": q, "theme": theme, "by": by, "src": src, "text": t})

SURVEY = "Alumni survey, C01–C03, Sep–Oct 2026"
R4 = "Record #4, the organizers’ account, Oct 28"
R3 = "Record #3, team formation as a threshold"
CAL = "C02 calendar annotation"
PO6 = "Problem owner, Nov 6 records"
PO7 = "Problem owner, Nov 7 conversation"
SC = "Steering committee, Oct 28 and the region’s decision log"
LIB = "Case library, PR #5"

# ---------------- WHAT: what gets in the way, as people experience it ----------------
add("what", "lost between the parts", "A", SURVEY,
    "onboarding was tricky",
    "joining a project was not obvious",
    "jumping into projects felt overwhelming",
    "improve “what to expect”",
    "at times did not really understand what to do next",
    "needs more structure and a common goal",
    "more guidance on what to work on in a given week",
    "moderators should step in to get teams unstuck",
    "a clearer roadmap from individual work into team pods",
    "roles and expectations were unclear",
    "one person’s early setup didn’t fit the team that formed later",
    "course-correcting took a long time, even with Labs experts",
    "people constantly moving in and out of the project",
    "no way to get people to commit",
    "map out pathways so people can watch from the sidelines",
    "content from past Cycles should be in one central place",
    "links came from individual trainers, not one place; it felt ad hoc")
add("what", "too much to keep track of", "O", R4,
    "the biggest problem is cognitive load",
    "participants struggle to know what’s next and what’s expected right now",
    "important information didn’t flow through Slack",
    "it lived in Zoom meetings that weren’t very engaging",
    "the organization was siloed",
    "too little communication across teams",
    "too little time and too few resources",
    "organizer delays become participant emergencies")
add("what", "too much to keep track of", "O", CAL,
    "the “Communicating in Slack” session didn’t happen; too early in the cycle")
add("what", "the building falls to a few", "P", PO7,
    "on a team of five, the building often falls to one person",
    "the rest advise",
    "for three Cycles, advising and building counted the same",
    "asking for individual contributions cut across the team’s sense of itself",
    "it was felt as a cost to community and team-building",
    "being an owner means doing the work of ownership, and volunteers have limited hours")
add("what", "looking for the next step", "P", PO7,
    "people have come to expect each step to be handed to them",
    "people look to The Labs to say what to do next and what to learn",
    "people aren’t sure they’re allowed to go off and do it on their own",
    "the community is looking for the plan to be shared",
    "the big picture hasn’t been drawn out and written down yet",
    "people arrive expecting a finished product and find one still being built",
    "pods come in with their point of view and want to start building",
    "desk research and synthesis are taking a back seat to building",
    "interviews are slow to get started",
    "people have a lot competing for their attention at any one time")
add("what", "most programs lose most people when they end", "X", LIB,
    "about 16 in 100 Summer of Code students kept contributing",
    "57% had said they meant to continue",
    "of 73 hackathons’ projects, 3.6% were alive five months later",
    "stated intent to continue made no measurable difference",
    "AmeriCorps’ effects were half gone by year eight",
    "72% of Teach For America teachers were out of teaching by year five",
    "the Carpentries’ online course finished 5 to 10% of starters")
add("what", "a vote that produced only one pod", "P", PO7,
    "the voting math created only one pod",
    "at least one still-active participant was disappointed",
    "edge cases like this throw people for a loop")
add("what", "no life outside the Cycle", "P", PO7,
    "there is no non-Cycle experience at all",
    "a profile and an account mean nothing if you’re not in a Cycle",
    "leaving the Cycle means leaving The Labs",
    "“not ready” has nowhere to go")
add("what", "no life outside the Cycle", "O", R4,
    "everyone sees The Labs through the Cycle; there is no before or after")
add("what", "the pilot’s weekly room hasn’t been replaced", "P", PO7,
    "the pilot met four hours a week, in person, for twelve weeks",
    "that momentum let us fix things ad hoc without infrastructure",
    "the Cycle no longer has the in-person weekly check-in",
    "we haven’t been able to replicate it")

# ---------------- WHO ----------------
add("who", "twelve alumni who finished, and mostly stayed in touch", "A", SURVEY,
    "12 answered: 7 from C03, 3 from C02, 2 from C01",
    "11 of 12 joined a project team",
    "would recommend: median 8 of 10",
    "lasting relationships: 3–4 people for half of them",
    "7 of 11 still in touch with their team",
    "several in new jobs, contracts or job searches",
    "one is building a venture started in the Cycle")
add("who", "experienced adults, not paying, mostly not in a Cycle", "P", PO7,
    "working adults with lots of life experience",
    "mostly highly educated and professionally experienced",
    "high-agency adults who know how to solve their own problems",
    "they are not paying us; this is free",
    "most members, most of the time, are not in a Cycle")
add("who", "people who came once; not heard from yet", "P", PO7,
    "people who came once and moved on",
    "the person who got lost at the first door")
add("who", "people who came once; not heard from yet", "A", SURVEY,
    "respondents skew toward people who finished and joined teams")
add("who", "a few who build, more who advise", "P", PO7,
    "the people who build",
    "the people who advise",
    "people who pictured themselves in a pod that never formed")
add("who", "a handful of organizers, short on hands", "O", R4,
    "a handful of organizers, short on time and hands",
    "facilitators and moderators asked to step in")
add("who", "a new region, run by a committee and a few builders", "S", SC,
    "The Upskilling Labs of Greater Washington, new this Cycle",
    "a steering committee beginning the region’s self-organization",
    "builders who work in Claude Code in the browser",
    "pod maintainers who review every pull request")
add("who", "a new region, run by a committee and a few builders", "P", PO7,
    "the board, which reviews what the region changes",
    "partner organizations and sponsors interested in what gets built")
add("who", "employers, not asked yet", "P", PO7,
    "institutions and employers who need to pay attention",
    "they judge us against multi-million-dollar institutions")

# ---------------- WHERE: the stations and the channels ----------------
add("where", "the Cycle: twelve weeks and three dated gates", "O", R4,
    "the Cycle is the point of entry")
add("where", "the Cycle: twelve weeks and three dated gates", "P", PO6,
    "twelve weeks, an incubation sprint and a capstone",
    "the sense-making and direction-setting intensives")
add("where", "the Cycle: twelve weeks and three dated gates", "S", R3,
    "pod to team at Vote 2, Nov 14",
    "the team midpoint, Nov 26",
    "the showcase, Dec 8")
add("where", "sessions now come in kinds: trainings, workshops, meetups", "P", PO7,
    "monthly meetups",
    "workshops, virtual or in person",
    "we’ve called everything workshops; now trainings and workshops are different things",
    "a training teaches a tool; a workshop produces a work product",
    "“upskilling sessions” as the broader category")
add("where", "sessions now come in kinds: trainings, workshops, meetups", "S", SC,
    "trainings, workshops, open labs, meetups and happy hours; summits are national’s")
add("where", "five channels, and the information lived in Zoom", "P", PO7,
    "the web application",
    "Slack",
    "email",
    "LinkedIn, our only social account for now",
    "GitHub, where contributors open pull requests")
add("where", "five channels, and the information lived in Zoom", "O", R4,
    "Slack existed, but the information lived in Zoom")
add("where", "libraries: where it began, and every branch a door", "S", SC,
    "The Labs started in DC Public Library branches in 2025",
    "every public library branch in the region, on the Metro map",
    "an empty library is an invitation to host a workshop")
add("where", "libraries: where it began, and every branch a door", "P", PO7,
    "the pilot’s weekly four-hour room",
    "project nights in the Civic Tech DC style")
add("where", "before and after a Cycle: nothing yet", "P", PO6,
    "there is no pre-cycle experience",
    "there is no well-mapped post-cycle or between-cycle experience")
add("where", "before and after a Cycle: nothing yet", "P", PO7,
    "the route into a workplace and back")
add("where", "the region serves its own pages; national keeps the rest", "S", SC,
    "national’s pages redirect to theupskillinglabs.org",
    "the region serves its own home, cycle page, About and Get Involved",
    "the Ambassador program stays national")

# ---------------- WHY: causes and explanations ----------------
add("why", "the Cycle is designed to change as it goes", "O", R4,
    "the Cycle is meant to be adaptive; it changes as it goes",
    "most wayfinding complaints trace to organizers",
    "the Cycle is time-bound; when we take our time, participants lose the time")
add("why", "the Cycle practices skills; it doesn’t teach them", "P", PO7,
    "the Cycle is largely a self-help, autodidactic experience",
    "workshops and trainings are where we give skills, and they aren’t required",
    "the Cycle is the time to put skills into practice",
    "people say they don’t have the skills and can’t gain them here",
    "we serve people who are still learning to build; the Cycle needs people who can")
add("why", "it’s free, and nobody’s job is to guide you", "P", PO7,
    "we’re not doing coaching; they’re not paying us",
    "there is no one whose job it is to help them navigate",
    "we can’t promise to hold anyone’s hand",
    "we created a sandbox to enter, form teams and build community in")
add("why", "the big picture isn’t written down", "P", PO7,
    "how it all fits together isn’t written down anywhere",
    "nobody has had the job of drawing it out",
    "writing down someone else’s picture can feel like claiming authority",
    "documentation doesn’t count as a contribution")
add("why", "built only with volunteer hours", "P", PO7,
    "any intervention will be built with volunteer hours",
    "managing that work is a wayfinding problem of its own",
    "the Cycle needs a really clear vision behind it",
    "we depend on an amorphous volunteer community to build it",
    "expectations are anchored on experiences built by billion-dollar companies")
add("why", "losing the vote means losing your team", "P", PO7,
    "this is the first time working adults are asked to do real creative leadership",
    "ideas go into an arena and the ones with traction move forward",
    "people want one linear experience: one team, all the way through",
    "that creates a problematic dependency on that team",
    "team formation is tied at the hip to problem and project voting",
    "we want guaranteed results but don’t know what the teams will be")
add("why", "too few team meetings", "P", PO7,
    "we aren’t creating spaces often enough for the team to meet",
    "individuals don’t get to synthesize what everyone else is working on",
    "people don’t understand the thing they’re part of or how they fit",
    "it’s not one or the other; we need both the team and individual contribution")
add("why", "“pod” doesn’t say what it is", "P", PO7,
    "“pod” and “project” keep confusing people",
    "a pod should be seen as a much bigger community, a research group")
add("why", "people navigate by a few fixed landmarks", "X", LIB,
    "people navigate by a few fixed landmarks (Lynch)",
    "people keep going only while the scent stays warm (Pirolli & Card)",
    "working memory is small; the cost of “what’s next” is a packaging cost (Sweller)",
    "a map most people can’t read gets replaced by a line (Duolingo, Khan Academy)",
    "a visible head start speeds completion; an if-then plan roughly doubles follow-through")
add("why", "skill and belonging keep volunteers; choice alone doesn’t", "X", LIB,
    "competence and belonging predicted staying; choice alone did not (Deci & Ryan)",
    "“this matters to me” predicts persistence more than “this is fun”",
    "self-taught never means alone: about ten helpers per project (Tough)",
    "capacity for self-direction depends on the situation, not the person (Candy)",
    "you learn a community by doing small real work at its edge, witnessed (Lave & Wenger)",
    "groups that claim no structure run on hidden structure (Freeman)")
add("why", "effort drops in groups", "X", LIB,
    "effort drops as groups grow when contributions can’t be told apart (Ringelmann, Latané)",
    "effort holds up best when work is identifiable and the group matters (Karau & Williams)",
    "about 15 people wrote 80% of Apache",
    "preparation and skill mix predicted a project’s survival; intent did not",
    "heavy first-week activity raised the chance of stopping",
    "teams set their approach in the first meeting and overhaul it at the midpoint (Gersick)",
    "designers learn the problem by proposing solutions (Lawson, Cross)")
add("why", "too much rests on too few people", "X", LIB,
    "10 of 14 Code Club leaders ran their club alone",
    "a third of trained Carpentries instructors never taught",
    "60% of open-source maintainers have quit or considered it",
    "FIRST retired its six-week build window over mentor workload",
    "NaNoWriMo closed in 2025; its regions kept going on channels they owned",
    "Kubernetes pruned 146, then 600, then 300 inactive members")
add("why", "messages work only from a known person", "X", LIB,
    "summer-melt texts worked with a counselor behind them and vanished at state scale",
    "Wikipedia newcomers met by bots left; those invited to the Teahouse stayed",
    "a single-channel rule broke NaNoWriMo’s local layer",
    "Scouts’ counselors signed off requirements never completed")

# ---------------- HOW SOLVED: what each party proposes ----------------
add("how", "one source of truth, many channels", "O", R4,
    "an omnichannel notification strategy: Slack, email, text",
    "OLOS as the single source of truth",
    "“plumbing”: infrastructure that gets people to what they need fast")
add("how", "one source of truth, many channels", "P", PO6,
    "the OLOS app is the first head; other channels read from it",
    "turnkey, modular kits on OLOS, in a Cycle and out of one")
add("how", "one source of truth, many channels", "P", PO7,
    "expand beyond LinkedIn to other platforms")
add("how", "alumni asked for more structure and a common goal", "A", SURVEY,
    "more structure and a common goal",
    "weekly guidance on what to work on",
    "moderators who step in to get teams unstuck",
    "a roadmap into team pods, with roles and expectations",
    "guidance on tools and setup at the start of a project",
    "past Cycles’ materials in one central place",
    "pathways for different learning styles and availability")
add("how", "treat people as adults", "P", PO7,
    "treat you like a high-agency adult who solves their own problems",
    "say plainly: you don’t need us to tell you what to learn",
    "a small core offer: how to search, how to use AI tools to triage",
    "resources are activated and waiting; mobilized once you’ve exhausted your own",
    "ask: has the team discussed it? has the pod?",
    "say what we assume you already know going in",
    "people can step away from a Cycle, and that’s okay",
    "if you find you’re not ready, there are resources and a community")
add("how", "say it thirty times, the same way", "P", PO7,
    "create thirty touchpoints people are reasonably sure to come across",
    "assume they paid attention to five or seven",
    "those five to seven must say the same thing",
    "some of it can be subconscious, like the direction of airport tiles")
add("how", "form teams before the vote", "P", PO7,
    "a facilitated way for teams to form",
    "as a team, choose a research pod to belong to",
    "as a team, propose mini projects or select a frame",
    "create spaces for the team to meet and synthesize",
    "better terminology than pod and project")
add("how", "give people something to do between Cycles", "P", PO7,
    "mini-hackathon workshops: the tool and constraints predefined",
    "everyone has a seat and is onboarded to the stack fast",
    "everyone produces something by the end",
    "it all goes back into the commons, open source",
    "sponsored workshops that sample a partner’s tech stack",
    "prerequisite trainings, or certifying you know the tool",
    "project nights, like Civic Tech DC")
add("how", "give people something to do between Cycles", "P", PO6,
    "the Cycle should be built up to, not the front door",
    "member projects: ventures and civic projects The Labs partners with",
    "a mentor network: ask, triage, escalate, match",
    "a record of what each person has done and learned",
    "stepping back is honorable")
add("how", "the region’s first answers: three doors, a Metro map, a clock", "S", SC,
    "three doors: Learn, Build and Share",
    "every library on the Metro, with the nearest station and the walk",
    "a neighbor can offer to coordinate a workshop at their library",
    "contributors open pull requests; a maintainer reviews each",
    "one place to create an event and publish it everywhere (not built)")
add("how", "the region’s first answers: three doors, a Metro map, a clock", "S", "Parked notes, Oct 28",
    "a predictable Cycle clock, run nationally and facilitated locally",
    "trail ratings: signs at the junctions, relative to the mountain")
# HOW SOLVED, from the case library (PR #5): what each program did about the same gap.
# One statement per move, the program named first, the case file as the source.
def C(name): return f"Case library, PR #5: {name}"

add("how", "keep the door open after it ends", "X", C("Recurse Center"),
    "Recurse Center: alumni keep the chat, the calendar and the jobs board")
add("how", "keep the door open after it ends", "X", C("FIRST Robotics"),
    "FIRST: an off-season, April to December, for recruiting and training")
add("how", "keep the door open after it ends", "X", C("NaNoWriMo"),
    "NaNoWriMo’s regions kept going on channels they owned")

add("how", "show the whole route and where you are", "X", C("GOV.UK step by step"),
    "GOV.UK: every step on one page; the current and next step highlighted",
    "GOV.UK began with the journeys that had the most drop-off")
add("how", "show the whole route and where you are", "X", C("Hack for LA onboarding"),
    "Hack for LA: each listing says if the project can take volunteers now")
add("how", "show the whole route and where you are", "X", C("Contributor ladders"),
    "Kubernetes publishes what each rung takes, starting with one merged change")
add("how", "show the whole route and where you are", "X", C("Outreachy contribution period"),
    "Outreachy: one project list, shown to everyone the same day, one deadline")
add("how", "show the whole route and where you are", "X", C("Duolingo path redesign"),
    "Duolingo: one path, so nobody has to guess the right way through")

add("how", "a person at the first contact", "X", C("Wikipedia newcomers"),
    "Wikipedia’s Teahouse: people answer newcomers; those invited stayed longer")
add("how", "a person at the first contact", "X", C("Stack Overflow newcomers"),
    "Stack Overflow: a mentor read your draft question first; they scored 50% higher")
add("how", "a person at the first contact", "X", C("Extension and 4-H volunteers"),
    "Master Gardeners: a veteran per 2–4 trainees cut dropout from a quarter to 2%")
add("how", "a person at the first contact", "X", C("Open source newcomer barriers"),
    "open source: a starter task works when an experienced person is in the thread")
add("how", "a person at the first contact", "X", C("Summer melt"),
    "summer melt: ten texts, each with a counselor behind it, for $7 a student")
add("how", "a person at the first contact", "X", C("Extinction Rebellion"),
    "Extinction Rebellion added “integrator” roles to walk new members in")
add("how", "a person at the first contact", "X", C("P2PU learning circles"),
    "P2PU: co-facilitate your first circle with someone who has run one")

add("how", "make the first step small", "X", C("Outreachy contribution period"),
    "Outreachy: several small contributions before selection, not one big one")
add("how", "make the first step small", "X", C("Carpentries instructor pipeline"),
    "the Carpentries swapped one GitHub task for a menu of ways to get involved",
    "the Carpentries: setup steps before the workshop; a small fee cut no-shows")
add("how", "make the first step small", "X", C("Hack for LA onboarding"),
    "Brigades: a low-commitment first project, like a learning group",
    "Hack for LA: one central onboarding, then a community by discipline")
add("how", "make the first step small", "X", C("Mozilla Hive"),
    "Hive pop-ups had three depths: sample, try everything, or focus on one")
add("how", "make the first step small", "X", C("GetCalFresh"),
    "GetCalFresh: one question per page, ten minutes on a phone")

add("how", "a kit a stranger can run", "X", C("Code Club and CoderDojo"),
    "Code Club: step-by-step projects plus notes for the leader; leaders rated them first",
    "Code Club’s kit includes the person who runs it")
add("how", "a kit a stranger can run", "X", C("4-H lesson kits"),
    "4-H: “grab and go” lesson plans an untrained volunteer can deliver",
    "the Carpentries: two days became the unit; a week wore people out")
add("how", "a kit a stranger can run", "X", C("P2PU learning circles"),
    "P2PU: no subject expertise needed; a guide, a promo kit, recipe cards")
add("how", "a kit a stranger can run", "X", C("Indivisible"),
    "Indivisible: a 23-page guide on Google Docs seeded thousands of groups")
add("how", "a kit a stranger can run", "X", C("Extension and 4-H volunteers"),
    "Idaho 4-H: six-week project sessions for volunteers without a year to give")

add("how", "a clock everyone can see", "X", C("Google Summer of Code"),
    "Summer of Code: 4 weeks to propose, 3 to bond, 12 to code, a midterm check",
    "Summer of Code: two project sizes and a deadline you can stretch")
add("how", "a clock everyone can see", "X", C("FIRST Robotics"),
    "FIRST: a January kickoff and the same events for every team",
    "FIRST retired its fixed stop-build day over mentor burnout")
add("how", "a clock everyone can see", "X", C("NaNoWriMo"),
    "NaNoWriMo: one month, a kickoff, a weekly write-in and an end party")

add("how", "write the role down, and the way out", "X", C("NaNoWriMo"),
    "NaNoWriMo liaisons had a written list: forum, weekly write-in, two parties")
add("how", "write the role down, and the way out", "X", C("Extension and 4-H volunteers"),
    "Idaho 4-H: a “facilitation coach” role, with a signed description")
add("how", "write the role down, and the way out", "X", C("FIRST Robotics"),
    "FIRST: plan the handover before the lead mentor steps down",
    "FIRST team 1551: “back when eight students commit to a month of training”")
add("how", "write the role down, and the way out", "X", C("Contributor ladders"),
    "Kubernetes: a quiet year and you’re pruned, with a month to appeal")

add("how", "one source of truth, many channels", "X", C("NPR COPE"),
    "NPR: content stored once, unformatted; every outlet draws from it")
add("how", "one source of truth, many channels", "X", C("Channel overload"),
    "Python folded seven channels into one forum, with an email mode")
add("how", "one source of truth, many channels", "X", C("GetCalFresh"),
    "GetCalFresh: name the agency, text from one number, start one-way")

add("how", "hand it on instead of letting it end", "X", C("Hackathons and sprints"),
    "both corporate hackathon survivors were handed to other units",
    "hackathon projects lived on skill mix and preparation, not intent")
add("how", "hand it on instead of letting it end", "X", C("Hack for LA onboarding"),
    "Civic Tech DC: an incubator to turn a pitch into a plan with milestones")

add("how", "count the crossing, not the finish", "X", C("MOOC completion"),
    "MOOCs: four kinds of learner, not one completion rate")
add("how", "count the crossing, not the finish", "X", C("Pre-apprenticeship"),
    "most states track whether pre-apprentices enter, not only whether they finish")
add("how", "count the crossing, not the finish", "X", C("Hack for LA onboarding"),
    "Brigades: follow-up surveys of first-timers; task boards that list non-technical work")

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "map", "statements.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(S, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(S), "statements ->", out)
