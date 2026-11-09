# Case: Conversational "heads" on organisational systems, from GitHub's ChatOps to the NYC MyCity and Air Canada chatbots

**Kind:** failure (MyCity, Air Canada), set against an early success story (ChatOps)
**Bears on:** interfaces, facilitators, activation-mobilization
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
Three attempts to let people reach an organisation's systems or rules through a chat interface rather than its own screens: GitHub's Hubot, which ran infrastructure commands inside the team chat room (2013); New York City's MyCity business chatbot, a generative-AI layer over city business guidance (2023–2026); and Air Canada's website chatbot, whose wrong answer about a fare policy was ruled binding on the airline (2024). The 2024 Model Context Protocol (MCP) is noted as the current standard for wiring AI assistants to organisational data.

## 2. Where it came from
GitHub engineer Jesse Newland's 2013 conference talk and a 2016 GitHub-authored explainer; The Markup's investigations of MyCity (co-published with Documented and THE CITY) and StateScoop's 2026 report on its planned shutdown; the British Columbia Civil Resolution Tribunal decision 2024 BCCRT 149; TechCrunch and Wikipedia on MCP.

## 3. When
- ChatOps talk: 3 April 2013, MountainWest RubyConf ([RubyEvents](https://www.rubyevents.org/talks/chatops-at-github)); explainer 17 Oct 2016 ([Opensource.com](https://opensource.com/life/16/10/meet-hubot-devops-chat-bot)).
- MyCity: announced October 2023; investigated 29 March and 2 April 2024 ([The Markup, 29 Mar](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law); [The Markup, 2 Apr](https://themarkup.org/news/2024/04/02/malfunctioning-nyc-ai-chatbot-still-active-despite-widespread-evidence-its-encouraging-illegal-behavior)); shutdown planned January 2026 ([StateScoop](https://statescoop.com/mamdani-kill-nyc-ai-chatbot/)).
- Air Canada decision: 14 February 2024 ([CRT decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)).
- MCP: announced 25 Nov 2024 ([TechCrunch](https://techcrunch.com/2024/11/25/anthropic-proposes-a-way-to-connect-data-to-ai-chatbots/)).

## 4. What it says
**ChatOps at GitHub (chat as a shared control surface)**
- GitHub ran deploys, graph checks, pager handoffs and rollbacks through Hubot in its group chat; actions showed up in the room, so nobody had to announce work or ask "are you deploying?" ([RubyEvents](https://www.rubyevents.org/talks/chatops-at-github)).
- The speaker described the side effect as people learning by watching each other's commands; at the time 56% of GitHub staff worked outside the office ([RubyEvents](https://www.rubyevents.org/talks/chatops-at-github)).
- A 2016 GitHub explainer repeats visibility, shared context and learning-by-watching as the benefits and names no drawbacks ([Opensource.com](https://opensource.com/life/16/10/meet-hubot-devops-chat-bot)).

**NYC MyCity (an AI head over official guidance)**
- Built on Microsoft Azure AI and drawing on NYC Business web pages, the bot told reporters employers could take a cut of workers' tips, landlords need not accept housing vouchers, and businesses need not accept cash, all contrary to city law ([The Markup, 29 Mar 2024](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)).
- Answers were inconsistent: the same voucher question got "must accept" for one reporter and "need not" for ten other staff ([The Markup, 29 Mar 2024](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)).
- After publication the city relabelled it a beta, told users to verify answers and not treat them as legal advice, and kept it online; when asked, the bot said it could be used for professional business advice ([The Markup, 2 Apr 2024](https://themarkup.org/news/2024/04/02/malfunctioning-nyc-ai-chatbot-still-active-despite-widespread-evidence-its-encouraging-illegal-behavior)).
- In January 2026 the new mayor called it "functionally unusable" and said it would be taken down to save money; its foundations reportedly cost nearly $600,000 ([StateScoop](https://statescoop.com/mamdani-kill-nyc-ai-chatbot/)).

**Air Canada (who owns what the head says)**
- The airline's site chatbot said bereavement fares could be claimed within 90 days after travel; a linked policy page said the opposite. The airline argued the chatbot was a separate entity responsible for its own actions ([CRT decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)).
- The tribunal held the chatbot is part of the airline's website, found negligent misrepresentation, said a customer had no reason to trust one part of the site over another, and awarded $812.02 in total ([CRT decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)).

**MCP (wiring agents to organisational systems)**
- Anthropic released MCP as an open standard so AI assistants could connect to data in other systems without a custom integration per source; Block and Apollo were named early adopters; TechCrunch noted no benchmarks were offered ([TechCrunch](https://techcrunch.com/2024/11/25/anthropic-proposes-a-way-to-connect-data-to-ai-chatbots/)).
- OpenAI adopted it in March 2025; in December 2025 it was donated to a Linux Foundation fund; documented security problems include "tool poisoning" via hidden instructions in tool descriptions (April 2025) and a critical remote-code flaw in a widely used helper (CVE-2025-6514, July 2025) ([Wikipedia](https://en.wikipedia.org/wiki/Model_Context_Protocol)).

## Failure modes seen
- **Two heads, two answers:** Air Canada's chatbot and its own policy page disagreed, and the organisation was held to the chatbot ([CRT decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)).
- **Same question, different answer:** MyCity gave opposite answers to the same voucher question ([The Markup](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)).
- **Disclaimer as fix:** NYC responded with new warnings while leaving the bot live, and the bot contradicted the warning ([The Markup, 2 Apr](https://themarkup.org/news/2024/04/02/malfunctioning-nyc-ai-chatbot-still-active-despite-widespread-evidence-its-encouraging-illegal-behavior)).
- **Sunk pilot:** A "pilot" ran over two years before being cut as a budget saving ([StateScoop](https://statescoop.com/mamdani-kill-nyc-ai-chatbot/)).
- **Connector as attack surface:** Instructions hidden in tool descriptions can steer an agent without the user seeing them ([Wikipedia, MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- ChatOps worked because the actions happened *in front of* the team; MyCity answered *privately* to each user. Which Labs moments benefit from being seen by others (a pod forming, a project needing a maintainer), and which are private (deciding not to continue)?
- When an agent tells someone "your next step is X", whose statement is that in The Labs (the branch, the region, the commons, the volunteer who configured it)?
- MyCity's source pages existed and were mostly right; the head misread them. What is The Labs' single source that every head would be checked against, and does it exist yet?

## 6. Hearsay and limits
- ChatOps sources are GitHub's own staff speaking about GitHub; no independent evaluation found.
- MyCity testing was journalistic, not systematic; we do not know error rates across all questions.
- The Air Canada decision is a small-claims ruling in one province; its weight as precedent is limited.
- The Anthropic MCP announcement page could not be opened in this session (fetch blocked); MCP facts rely on TechCrunch and Wikipedia.
- **Rival explanation (MyCity):** The failure may reflect 2023-era model limits and thin retrieval over a few web pages, not chat as an interface; a better-grounded system might not have failed the same way.
- Could confirm: NYC Office of Technology and Innovation; GitHub engineering on whether ChatOps persisted and what it cost to maintain.

## Sources
- [ChatOps at GitHub](https://www.rubyevents.org/talks/chatops-at-github), Jesse Newland, MountainWest RubyConf, 3 Apr 2013 (auto-transcript on RubyEvents). Origin of the term in practice.
- [Meet Hubot: The DevOps chat bot](https://opensource.com/life/16/10/meet-hubot-devops-chat-bot), Brent Beer (GitHub), Opensource.com, 17 Oct 2016. Explainer.
- [NYC's AI Chatbot Tells Businesses to Break the Law](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law), Colin Lecher, The Markup, 29 Mar 2024. Investigation.
- [Malfunctioning NYC AI Chatbot Still Active](https://themarkup.org/news/2024/04/02/malfunctioning-nyc-ai-chatbot-still-active-despite-widespread-evidence-its-encouraging-illegal-behavior), The Markup, 2 Apr 2024. Follow-up.
- [Mamdani to kill NYC AI chatbot](https://statescoop.com/mamdani-kill-nyc-ai-chatbot/), StateScoop, 30 Jan 2026. Planned shutdown and cost.
- [2024 BCCRT 149 (Air Canada chatbot decision)](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), Civil Resolution Tribunal of British Columbia, 14 Feb 2024. Primary legal decision.
- [Anthropic proposes a way to connect data to AI chatbots](https://techcrunch.com/2024/11/25/anthropic-proposes-a-way-to-connect-data-to-ai-chatbots/), Kyle Wiggers, TechCrunch, 25 Nov 2024. MCP launch report with skepticism.
- [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol), Wikipedia, read 2026-11-05. Adoption, governance and security timeline (secondary).
