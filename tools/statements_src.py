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
    """q may name two questions, "what+who": the statements answer both, so the theme
    sits in the overlap of the two circles, an interchange station on both lines."""
    q, _, q2 = q.partition("+")
    for t in texts:
        d = {"q": q, "theme": theme, "by": by, "src": src, "text": t}
        if q2: d["q2"] = q2
        S.append(d)

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
add("what+who", "the building falls to a few", "P", PO7,
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
add("what+why", "losing the vote means losing your team", "P", PO7,
    "the voting math created only one pod",
    "at least one still-active participant was disappointed",
    "edge cases like this throw people for a loop")
add("what+where", "nothing before or after a Cycle", "P", PO7,
    "there is no non-Cycle experience at all",
    "a profile and an account mean nothing if you’re not in a Cycle",
    "leaving the Cycle means leaving The Labs",
    "“not ready” has nowhere to go")
add("what+where", "nothing before or after a Cycle", "O", R4,
    "everyone sees The Labs through the Cycle; there is no before or after")
add("what+where", "the pilot’s weekly room hasn’t been replaced", "P", PO7,
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
add("who+what", "people who came once; not heard from yet", "P", PO7,
    "people who came once and moved on",
    "the person who got lost at the first door")
add("who+what", "people who came once; not heard from yet", "A", SURVEY,
    "respondents skew toward people who finished and joined teams")
add("who+what", "the building falls to a few", "P", PO7,
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
add("where+how", "a clock everyone can see", "O", R4,
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
add("where+what", "five channels, and the information lived in Zoom", "P", PO7,
    "the web application",
    "Slack",
    "email",
    "LinkedIn, our only social account for now",
    "GitHub, where contributors open pull requests")
add("where+what", "five channels, and the information lived in Zoom", "O", R4,
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
add("where+what", "nothing before or after a Cycle", "P", PO7,
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
add("why+who", "it’s free, and nobody’s job is to guide you", "P", PO7,
    "we’re not doing coaching; they’re not paying us",
    "there is no one whose job it is to help them navigate",
    "we can’t promise to hold anyone’s hand",
    "we created a sandbox to enter, form teams and build community in")
add("why+what", "the big picture isn’t written down", "P", PO7,
    "how it all fits together isn’t written down anywhere",
    "nobody has had the job of drawing it out",
    "writing down someone else’s picture can feel like claiming authority",
    "documentation doesn’t count as a contribution")
add("why+who", "built only with volunteer hours", "P", PO7,
    "any intervention will be built with volunteer hours",
    "managing that work is a wayfinding problem of its own",
    "the Cycle needs a really clear vision behind it",
    "we depend on an amorphous volunteer community to build it",
    "expectations are anchored on experiences built by billion-dollar companies")
add("why+what", "losing the vote means losing your team", "P", PO7,
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
add("why+what", "“pod” doesn’t say what it is", "P", PO7,
    "“pod” and “project” keep confusing people",
    "a pod should be seen as a much bigger community, a research group")
add("why+how", "people navigate by a few fixed landmarks", "X", LIB,
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
add("why+what", "effort drops in groups", "X", LIB,
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
add("why+how", "a person at the first contact", "X", LIB,
    "summer-melt texts worked with a counselor behind them and vanished at state scale",
    "Wikipedia newcomers met by bots left; those invited to the Teahouse stayed",
    "a single-channel rule broke NaNoWriMo’s local layer",
    "Scouts’ counselors signed off requirements never completed")

# HOW SOLVED is evidence only: what one of the 51 cases in the library (PR #5) did about
# the same gap, kept only where the case reports that it worked. Proposals, wishes and
# the region's own first answers live in the records, not here.
def C(name): return f"Case library, PR #5: {name}"

add("how+why", "a person at the first contact", "X", C("Wikipedia newcomers"),
    "Wikipedia’s Teahouse: newcomers invited to a room where people answer stayed longer, in a controlled trial",
    "Teahouse answers with fewer rule links and more words kept more newcomers")
add("how+why", "a person at the first contact", "X", C("Stack Overflow newcomers"),
    "Stack Overflow: a mentor read your draft question first; those questions scored 50% higher")
add("how+why", "a person at the first contact", "X", C("Extension and 4-H volunteers"),
    "Master Gardeners: a veteran per 2–4 trainees cut first-year dropout from a quarter to 2%")
add("how+why", "a person at the first contact", "X", C("Open source newcomer barriers"),
    "open source: a starter task is 71% likelier to be finished when an experienced person is in the thread")
add("how+why", "a person at the first contact", "X", C("P2PU learning circles"),
    "P2PU: new facilitators who co-ran their first circle with a colleague did best, by P2PU’s account")

add("how", "a reminder at the moment it matters", "X", C("Summer melt"),
    "summer melt: ten texts with a counselor behind them raised college enrollment 4–7 points where there was no other help")
add("how", "a reminder at the moment it matters", "X", C("GetCalFresh"),
    "GetCalFresh: a text before the interview made people 55% likelier to complete it",
    "GetCalFresh: letting applicants pick their own interview moment raised approvals 6 points",
    "Louisiana: people who opted into reminders kept appointments at 52% against 29%")
add("how", "a reminder at the moment it matters", "X", C("Microcredentials and employers"),
    "a nudge to post a certificate you already held raised employment 6%, and 12% for the least employable")

add("how+where", "a kit a stranger can run", "X", C("Code Club and CoderDojo"),
    "Code Club: step-by-step projects plus notes for the leader; a trial found gains in coding skill and confidence")
add("how+where", "a kit a stranger can run", "X", C("4-H lesson kits"),
    "the Carpentries: two days became the unit; 91 workshops reached 4,300 people in a year after week-long courses failed")
add("how+where", "a kit a stranger can run", "X", C("P2PU learning circles"),
    "P2PU: a guide, a promo kit and recipe cards; about half finished, against 5–10% taking the course alone")
add("how+where", "a kit a stranger can run", "X", C("Indivisible"),
    "Indivisible: a 23-page guide on Google Docs seeded 3,800 groups in seven weeks; most still met in 2019")
add("how+where", "a kit a stranger can run", "X", C("Extension and 4-H volunteers"),
    "Idaho 4-H: six-week sessions and a “facilitation coach” role let one or two volunteers serve 10–15 youth")

add("how+where", "a clock everyone can see", "X", C("Google Summer of Code"),
    "Summer of Code: 4 weeks to propose, 3 to bond, 12 to code; 1,000+ finished projects a year",
    "Summer of Code: two project sizes and a stretchable deadline brought in people with jobs")
add("how+where", "a clock everyone can see", "X", C("FIRST Robotics"),
    "FIRST: a January kickoff and the same events for every team; 3,000+ teams a year, 91% return")
add("how+where", "a clock everyone can see", "X", C("NaNoWriMo"),
    "NaNoWriMo: one month, a kickoff, a weekly write-in and an end party, for 400,000 people a year",
    "NaNoWriMo: 900 liaisons with a written duty list ran 633 regions")

add("how+what", "show the whole route and where you are", "X", C("GOV.UK step by step"),
    "GOV.UK: every step on one page, the current and next highlighted; task completion and confidence rose",
    "GOV.UK began with the journeys that had the most drop-off; one was used 1.2 million times in six months")
add("how+what", "show the whole route and where you are", "X", C("GetCalFresh"),
    "GetCalFresh: one question per page, ten minutes on a phone; 7 million people used it")

add("how", "a small stake up front", "X", C("4-H lesson kits"),
    "the Carpentries: a $20–40 fee cut no-shows from a third to 5%")
add("how", "a small stake up front", "X", C("MOOC completion"),
    "MOOCs: learners who paid for a certificate finished at 44–56%, against 3–6% overall")

add("how+what", "keep the door open after it ends", "X", C("Recurse Center"),
    "Recurse Center: alumni keep the chat, the calendar and the jobs board; they stayed involved for years")
add("how+what", "keep the door open after it ends", "X", C("NaNoWriMo"),
    "NaNoWriMo’s regions kept going on channels they owned; one night, 148 people wrote 404,500 words")
add("how+what", "keep the door open after it ends", "X", C("Extension and 4-H volunteers"),
    "Master Gardeners stayed for the local association, five of eight coordinators said")

add("how+what", "hand it on instead of letting it end", "X", C("Hackathons and sprints"),
    "the hackathon projects that lived were handed to other units, not kept by their teams",
    "hackathon projects with a skill mix and preparation were half as likely to stop; intent didn’t matter")
add("how+what", "hand it on instead of letting it end", "X", C("Indivisible"),
    "Indivisible groups that lasted met monthly, split work into subcommittees and replaced leaders as they left")

add("how", "a network that vouches beats a certificate", "X", C("Opportunity@Work"),
    "Opportunity@Work: non-degree workers moved up at 59% inside employer networks, 40% in the open market")
add("how", "a network that vouches beats a certificate", "X", C("GitHub activity traces"),
    "GitHub: employers read contributions to other people’s projects as an endorsement")
add("how", "a network that vouches beats a certificate", "X", C("Skills-based hiring"),
    "employers that really dropped degree screens kept non-degree hires 10 points longer")

add("how+what", "one source, bundled messages", "X", C("NPR COPE"),
    "NPR: content stored once and drawn by every outlet; requests went from 3.5 to 53 million"),
add("how+what", "one source, bundled messages", "X", C("Channel overload"),
    "notifications bundled three times a day made people calmer and more attentive; hourly and none did not")

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "map", "statements.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(S, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(S), "statements ->", out)
