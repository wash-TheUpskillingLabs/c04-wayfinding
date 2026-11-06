# Case: Khan Academy, retiring the Knowledge Map and then Missions in favour of linear Course Mastery

**Kind:** failure (a navigable catalog UI abandoned twice; the replacement is linear)
**Bears on:** pre-cycle, activation-mobilization, interfaces
**Product part:** kits | channels | post-between
**Logged:** 2026-11-06 (desk research, sources below)

## 1. What it is
Khan Academy's early math exercise catalog was shown as a zoomable "Knowledge Map" of prerequisite links; in 2014 it added adaptive "Missions" with a personal task queue, then removed the map, and later removed Missions in favour of a per-course linear "Course Mastery" with unit progress bars. The company says most students and teachers prefer linear progression.

## 2. Where it came from
Khan Academy, a US non-profit. Sources: an EdSurge report on the 2014 Missions launch, and three threads on Khan Academy's own support community, two of which carry staff replies.

## 3. When
Missions launched March 2014. The map's exact removal date is not established by the sources opened (community posts suggest the map was unmaintained by 2019 and "abandoned for 5 years" by the time of one comment; the brief's "2016" date is unverified). Missions were retired in 2020 per a staff reply's reference to that year's Course Mastery additions; the posts themselves carry no dates.

## 4. What it says

**Missions, 2014.** Common Core-aligned adaptive exercises from kindergarten to calculus, written with Smarter Balanced and 40 teachers; a pre-test placed each student, then a queue of exercises matched to level; progress required three to five correct in a row per skill; coaches could follow a dashboard; a separate Common Core map let teachers search by standard ([EdSurge, 25 March 2014](https://edsurge.com/n/2014-03-25-math-of-khan-sal-explains-academy-s-common-core-aligned-missions)). Khan framed it as meeting students where they are rather than where standards put them ([EdSurge](https://edsurge.com/n/2014-03-25-math-of-khan-sal-explains-academy-s-common-core-aligned-missions)).

**What the map was, from users.** A visual map of math concepts and their connections, linked to modules; users say it helped them choose their own topics, plan homeschool lessons and rekindled interest in math; one called it a standout feature ([Bring back the Knowledge Map, support community](https://support.khanacademy.org/hc/uz/community/posts/115007007148/comments/115003044068)). Commenters (not staff) say it depended on the Google Maps API and a skill-tree API that were discontinued, and that it crashed in several browsers ([Bring back the Knowledge Map](https://support.khanacademy.org/hc/uz/community/posts/115007007148/comments/115003044068)).

**Official reason for removing the map.** Staff: "This feature was removed after we introduced the updated Mission and then Course Mastery systems," and most students and teachers prefer linear course progression; there are no plans to bring it back; a surviving unlinked copy is unmaintained, slow, partly broken and can disrupt Mastery progress ([What happened to the knowledge map?, support community](https://support.khanacademy.org/hc/de/community/posts/360027982751/comments/360002975971)).

**Official reason for removing Missions.** Staff: the Missions code was old and caused errors, and while designing the new mastery system the team found gaps that made Missions hard to use in classrooms; in 2020 Mastery Challenges and elevated Course Challenges were added so learners could accelerate through familiar material ([Why did you remove Missions?, support community](https://support.khanacademy.org/hc/hu/community/posts/360070675772/comments/360011217992)).

**User response.** A "Bring back the Knowledge Map" thread reports no official response after more than three years; a later thread proposes a volunteer group to recreate the map ([Bring back the Knowledge Map](https://support.khanacademy.org/hc/uz/community/posts/115007007148/comments/115003044068); [Replacing or recreating the Knowledge Map](https://support.khanacademy.org/hc/tr/community/posts/4422868962701/comments/4428672777741)). Users also posted asking why Missions went and asking to keep them ([Why did you remove Missions?](https://support.khanacademy.org/hc/hu/community/posts/360070675772/comments/360011217992)).

Interpretation: two consecutive catalog interfaces that let the learner (or an algorithm) choose any next node were replaced by the one that follows a course's table of contents. The company gives three reasons across the threads: user preference for linearity, classroom fit, and code rot. Only the first is a design finding; the other two are maintenance.

## Failure modes seen
- **Map for the few, line for the many.** Staff cite majority preference for linear progression; the map's defenders are self-directed learners and home educators ([support community](https://support.khanacademy.org/hc/de/community/posts/360027982751/comments/360002975971)).
- **Catalog UI rots with its dependencies.** Commenters attribute the map's death to discontinued map and skill-tree APIs ([Bring back the Knowledge Map](https://support.khanacademy.org/hc/uz/community/posts/115007007148/comments/115003044068)).
- **Classroom fit beats self-direction.** Missions were dropped partly because they did not fit classrooms ([Why did you remove Missions?](https://support.khanacademy.org/hc/hu/community/posts/360070675772/comments/360011217992)).
- **Silence after removal.** A request thread went over three years without an official reply, then was closed ([Bring back the Knowledge Map](https://support.khanacademy.org/hc/uz/community/posts/115007007148/comments/115003044068)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- Khan Academy's self-directed minority lost its map because the classroom majority preferred a line. In The Labs, the autodidacts are also the minority. Who is the catalog view for?
- Two of three stated reasons were maintenance, not pedagogy. What does a map of OLOS kits cost to keep alive, and who pays when the volunteer who built it leaves?
- The map was a web artefact; the line survives in every channel. Which route representations survive SMS, email and an agent?

## 6. Hearsay and limits
The exact dates of both removals are not fixed by the sources opened; the support threads are undated in the fetched text. Reasons come from short staff replies on a support forum, not a published post-mortem; the API-dependency story is from users. Rival explanation: the map was not removed because people could not navigate it but because a 2014 strategic shift to Common Core classroom tooling made teacher-assigned, standards-ordered content the product, and the map simply had no owner afterward. Khan Academy's product team could confirm. Blocked: the English-locale support thread (permission not granted); the same thread was read via its German-locale URL.

## Sources
- ['Math of Khan': Sal Explains Academy's Common-Core Aligned 'Missions'](https://edsurge.com/n/2014-03-25-math-of-khan-sal-explains-academy-s-common-core-aligned-missions), EdSurge, 25 March 2014. Launch of Missions and the adaptive queue.
- [What happened to the knowledge map?](https://support.khanacademy.org/hc/de/community/posts/360027982751/comments/360002975971), Khan Academy support community, undated. Staff reply giving the removal reason.
- [Bring back the Knowledge Map](https://support.khanacademy.org/hc/uz/community/posts/115007007148/comments/115003044068), Khan Academy support community, undated (comments span several years to ~2019). User accounts of what the map was and why it mattered.
- [Why did you remove Missions?](https://support.khanacademy.org/hc/hu/community/posts/360070675772/comments/360011217992), Khan Academy support community, undated. Staff reply on retiring Missions.
- ["Knowledge Map" - "World of Math" Replacing or recreating it](https://support.khanacademy.org/hc/tr/community/posts/4422868962701/comments/4428672777741), Khan Academy support community, undated. Users proposing to rebuild the map.
