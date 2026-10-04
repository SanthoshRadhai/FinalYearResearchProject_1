# Q&A Preparation — Likely Professor Questions and Answers

This document is a rehearsal sheet: every question a professor is realistically likely to ask about
this project, with a full answer ready to give. It's organized by theme, ending with a short
cheat-sheet of one-line answers for a quick refresher right before the meeting.

The short version of the whole project, if asked to summarize in one breath: *"The base paper
(PentestGPT) shows a top-tier AI model can do penetration testing if a human helps it and it has
access to expensive infrastructure. Most people don't have that. This project tests what actually
happens when you try the same idea with the free, smaller AI models anyone can run on their own
computer, catalogs exactly how and why it breaks, and builds a cheap way to catch the AI when it lies
about what it accomplished."*

---

## 1. Motivation — "Why this topic?"

**Q: Why did you choose this topic instead of an easier paper?**
A: The topic was assigned/chosen before realizing how demanding the base paper is to reproduce
exactly. Rather than abandon it, the approach was reframed: instead of trying to copy the original
paper's method exactly (which needs a very expensive AI model and a human assistant for every step),
the project asks a related but different, more practical question — what happens with the free/open
models a normal student or company can actually afford to run? That turned a paper that was too hard
to copy into a paper that's actually more relevant to real-world use.

**Q: Why does this matter? Who cares about this outside a classroom?**
A: Almost every organization interested in AI-assisted security testing cannot afford to run a
top-tier AI model constantly, and most cannot have a human babysitting the AI's every command either.
If they're going to use AI for security testing at all, it'll be with a smaller, self-hosted model.
Nobody has systematically measured how reliable that actually is, or what breaks when they try. This
project produces that missing data, plus a cheap way to make it safer.

**Q: Is this just "AI does hacking," and isn't that dangerous?**
A: No — the project does not teach an AI to hack better. It measures how *unreliable* AI currently is
at using security tools correctly, and only tests against personal, disposable practice targets (a
private security testing exercise, not real websites or companies). Nothing in the project makes it
easier for anyone to attack a real target than the free tools already do on their own, since the
project is about the AI's reliability, not about the tools themselves.

---

## 2. "How is your research better than the base paper?" (the big one)

**Q: Isn't your work just a smaller, worse version of the base paper?**
A: No, it's a different question, not a smaller attempt at the same question. The base paper asks
"can a top-tier AI, with a human helping it, do a real penetration test?" and answers yes. This
project asks a question the base paper never answers: "what happens if you remove the top-tier AI and
the human helper, and use the free/open AI models people can actually run themselves?" That's not a
weaker version of the original question — it's a genuinely unanswered one, because the base paper's
whole design assumes you have the expensive AI and the human.

**Q: So what's actually new here that the base paper doesn't have?**
A: Three things the base paper doesn't do:
1. It never compares different "AI assistant frameworks" (the software that connects the AI model to
   the tools) against each other. This project found — already, in a real test — that the *exact
   same* AI model behaved in three completely different broken ways depending only on which
   assistant-framework software was hosting it. The base paper can't see this because it only ever
   used one setup.
2. It never studies what happens with smaller/free models at all — its entire design assumes a
   top-tier paid AI.
3. It never builds an automatic way to catch the AI lying about what it accomplished. The base paper
   relies on a human watching every step to catch mistakes. This project builds a mechanical checker
   that does that job automatically, which the base paper's own newer version (built by other
   researchers after the original paper) does use — but this project adapts that exact same idea to
   work without needing a human or an expensive AI either.

**Q: Are you claiming your method is more accurate or effective than the base paper's method?**
A: No — and it's important not to overclaim this. The base paper's top-tier AI, with a human helping
it, almost certainly performs the actual penetration test better than a free small AI with no human
help. This project isn't claiming to beat that. It's claiming to answer a more useful, currently
unanswered question: what happens at the tier of AI most people can actually use, and can we make
that tier safer/more honest even though it's less capable. "Better" here means "answers a more
practically useful and currently unanswered question," not "gets higher scores on the same
benchmark."

**Q: If you're not trying to beat the base paper's results, what's your actual contribution?**
A: Three concrete things: (1) a documented, reproducible list of the specific ways smaller AI models
fail at this task — not a vague "it's not as good," but exact examples of it misnaming tools,
inventing tools that don't exist, and describing an action without actually doing it; (2) proof that
the same AI model can fail in different ways depending only on the surrounding software, which is a
new, previously untested variable; (3) a lightweight, working fix for one of these problems (the AI
falsely claiming success) that doesn't need a bigger AI model to implement.

**Q: Couldn't you have just used the base paper's top-tier AI model too?**
A: That was a deliberate choice, not a resource limitation being hidden. Using the same expensive
model would just repeat the base paper's own experiment. Using cheaper/free models is the entire
point — it's what makes the research question different and, honestly, more relevant, since almost
nobody outside a handful of large companies can afford to run the base paper's setup continuously.

**Q: Is it fair to compare a 7-35 billion-parameter open model against a top-tier closed model at
all?**
A: The project isn't claiming the comparison is fair in the sense of "equal competitors" — it's
explicit that the smaller model is expected to perform worse. The point of including one top-tier
model at all (used only once, as a reference point, not as the main subject) is to sanity-check that
the measurement method itself is working correctly — if even the top-tier model shows near-zero
errors on the same test, that confirms the test is measuring something real about the smaller models'
weaknesses, not an artifact of a broken measurement setup.

---

## 3. Research design and method questions

**Q: What exactly are you measuring?**
A: Four things, defined precisely so they're comparable across every test: (1) how often the AI picks
the *correct* tool and uses it with valid instructions; (2) how often it names a tool that doesn't
exist at all (essentially the AI "making something up"); (3) how often it *talks about* using a tool
without actually using it; (4) how often it falsely claims a task is finished when it isn't, and
whether an automatic checker catches that lie.

**Q: What's your hypothesis? What do you expect to find?**
A: The expectation, based on an initial small test already run, is that smaller/free AI models will
show meaningfully higher rates of all four problems above compared to a top-tier model, and — this is
the more interesting expected finding — that the *choice of surrounding software* matters as much as
the choice of AI model itself, since the same model already produced three different failure patterns
under three different setups in the initial test.

**Q: What is your experimental design, in plain terms?**
A: Take several different AI models, several different pieces of "assistant" software, and one fixed
practice tool-set. Run every combination against a private, disposable practice target. Record
everything the AI does. Score it against the four measurements above. Because the tool-set and target
stay the same across every test, any difference observed must come from either the AI model or the
assistant software — nothing else is changing.

**Q: How do you know a failure is the AI's fault and not the assistant software's fault?**
A: By testing the same AI model under more than one piece of assistant software. If a specific failure
only shows up under one piece of software but not another (with the same AI model), that failure is
attributable to the software. If it shows up under every piece of software, it's attributable to the
model. The initial test already demonstrated this distinction is necessary — the same model failed in
three different ways depending only on the software.

**Q: How many trials/runs are you doing? Is that enough to be statistically meaningful?**
A: This is an honest limitation, stated openly in the project's own documentation rather than
discovered by someone else later: the number of trials is limited by how much computer time is
available, since only one computer with two graphics cards is being used, not a large server farm.
The results will be presented as directional findings backed by concrete, reproducible examples, not
as claims of strict statistical significance — and this limitation is explicitly written into the
paper rather than glossed over.

**Q: Why did you pick these specific AI models and not others?**
A: To cover a spread of sizes that actually fit on the available hardware (roughly 7 billion to 35
billion "parameters," which is a rough measure of an AI model's size), to include multiple different
AI model families so the findings aren't just a quirk of one company's model, and to include at least
one model that was specifically trained to be better at using tools, and one that was specifically
trained on cybersecurity material — so it's possible to tell apart "does specialized training help at
all" from "do all models struggle at this regardless of training."

**Q: Why this particular practice tool-set / "assistant" software, and not something else?**
A: Because it's a real, substantial, already-integrated setup (roughly 150 real security tools
connected through a standard, open connection protocol), it's already partly tested (the initial
findings came from exactly this setup), and using an existing, realistic, and standardized tool-set
is more meaningful than building a small toy example from scratch, which would raise the question of
whether the results only apply to that toy example.

**Q: What does "evidence-grounding" actually mean, in plain language?**
A: It means the system doesn't just take the AI's word for it when it says "I found the
vulnerability" or "the task is done." Instead, an automatic checker looks at the AI's actual, real
recorded output from the tools it used, and only accepts the AI's claim as true if that exact claim
can be found, word-for-word, in something the tools actually produced. If the AI's claim can't be
matched to real evidence, the system marks it as unproven, no matter how confidently the AI stated it.

---

## 4. Comparison to the other papers you're citing

**Q: You cite four papers total — how does your work relate to the other three, not just the main
one?**
A: One of the other papers studies AI doing one specific, narrow task (breaking into a Linux computer
after already having limited access) very rigorously with lots of repeated tests — that paper's
careful measurement style is being copied here, just applied to a much broader set of tasks. A second
paper is a general survey discussing the risks and benefits of AI in security testing at a conceptual
level — this project is meant to be the concrete, measured evidence that a survey like that would
want to cite. The third paper proposes giving the AI a memory and a research assistant (to look things
up while working) — this project treats that idea as one possible improvement to test later, not as
something already built in.

**Q: Are you just combining ideas from these papers rather than doing something original?**
A: The individual ideas (AI-driven tool use, evidence checking, giving AI reference material) already
exist in the literature — that's normal, all research builds on prior work. What's original is
putting them together specifically to answer a question none of them answer: how reliably do multiple
different small/free AI models, under multiple different assistant software setups, actually work
against one large realistic toolset, and does one specific, cheap fix reduce false claims of success.
That specific combination of variables, tested together and compared against each other, does not
exist in any of the four papers.

---

## 5. Limitations and weaknesses (professors will push on this)

**Q: What's the weakest part of your research design?**
A: Honestly, the small number of AI models and limited number of trial runs, both driven by having
only one computer available rather than a large lab's worth of machines. This is stated openly in the
project's own limitations section rather than hidden, and every conclusion is written to apply only
to the specific models and setups actually tested — no claim is made about "AI models in general."

**Q: What if your results just show that small AI models are bad at this? Isn't that an obvious,
uninteresting result?**
A: Even if the headline finding is "yes, smaller models are less reliable," the value isn't in that
one-sentence conclusion — it's in exactly *how* they fail (which is specific, reproducible, and not
obvious in advance — for example, that the failure pattern changes depending on the surrounding
software, which nobody would guess without testing it) and in the fact that a cheap fix for one part
of the problem is also tested and measured, not just described.

**Q: You're using disposable, private practice targets instead of real websites or companies — isn't
that a major weakness?**
A: It's a deliberate trade-off, not an oversight, and it's stated as one: using real, live, or
third-party systems without permission would be both illegal and against the ethical rules of
running this kind of research, so private practice targets are the only responsible choice. It does
mean the practice targets are somewhat simpler than a real company's systems, which is honestly
listed as a limitation on how far the results can be generalized.

**Q: Could your "evidence-grounding" checker be fooled?**
A: Yes, and this is explicitly acknowledged rather than hidden: the checker works by looking for the
AI's claimed text appearing, essentially word-for-word, somewhere in real tool output. It's possible,
though considered unlikely and specifically designed against, for a coincidental matching phrase to
appear somewhere unrelated and fool the checker into accepting a false claim. The checker is designed
to prefer longer, more specific, less common matches specifically to make this rare, but it isn't
claimed to be perfect.

**Q: Are your findings reproducible? Could someone else re-run this and get the same result?**
A: Yes by design — every test records exactly which AI model, which version of the assistant
software, and which version of the tool-set was used, specifically so someone else could set up the
identical combination and check the results. This is called out explicitly as important, since the
software involved is still being actively updated by its developers and could behave differently in
future versions.

**Q: Why didn't you fine-tune/retrain the AI models to fix these problems, if you already know a
possible fix?**
A: Training an AI model requires a large amount of specialized computer memory that the available
two-graphics-card setup doesn't have enough of for full retraining, especially for a model of this
size. There are cheaper, partial-retraining techniques that are feasible on the available hardware,
and those are planned as a next step after the main measurement work — but they're intentionally not
part of the core project yet, both due to time and to keep the study focused on measuring the problem
clearly first, before jumping to a partial solution.

---

## 6. Ethics and safety questions

**Q: Are you worried this research could be misused to attack real systems?**
A: No new attack capability is being created here — every tool being tested is already a widely
available, publicly known security tool used the same way by real security professionals every day.
The project studies how reliably an AI can drive those already-existing tools, which is a measurement
of AI limitations, not a new offensive technique. Nothing in the project makes any tool more dangerous
or teaches anyone a new way to attack something.

**Q: Did you get permission/authorization for your testing?**
A: All testing is done against private, disposable practice systems set up specifically for this
purpose, running entirely on hardware the researcher owns and controls — not against any real
company, website, or third party. This means there's nothing to get separate authorization for, in
the same way practicing on a locked practice car in a driving school doesn't require permission from
every car owner in the city.

**Q: Do you worry about publishing a list of "here's exactly how the AI fails" — could that help
someone abuse an AI system?**
A: The failures documented are the AI being unreliable and making mistakes — the opposite of a
capability someone would want to copy for a real attack. If anything, documenting these failures
helps organizations understand they should not yet trust these smaller AI models to run security
tools unsupervised, which is a safety-positive message, not a risk.

---

## 7. Results and "what if" questions

**Q: What happens if your evidence-grounding fix doesn't actually help?**
A: That would still be a valid, reportable result — a well-designed test that shows a proposed fix
doesn't work is genuinely useful information, and would be written up honestly as such, along with
reasoning about why it may not have helped and what might work better instead. The project is
designed so that either outcome (the fix helps, or it doesn't) produces something worth reporting.

**Q: What if different AI models behave completely inconsistently and you can't find a clear
pattern?**
A: An inconsistent, hard-to-predict pattern is itself an important and reportable finding — it would
mean that reliability can't be judged from an AI model's specifications alone, and would need to be
tested case by case, which is valuable information for anyone considering using these models for
security work.

**Q: How will you know if your research succeeded?**
A: Success is defined upfront, not judged after the fact based on whether the results are exciting:
completing the planned tests across the chosen AI models and assistant software, producing an
accurate and detailed catalog of how each combination fails or succeeds, and running a fair, honest
before-and-after comparison of the evidence-checking fix. All of that is achievable regardless of
whether the AI models turn out to perform well or poorly.

---

## 8. Practical, logistics, and "what's next" questions

**Q: What's your timeline? What have you actually done versus what's left?**
A: The planning stage is complete: the research question, the reasons for choosing this direction
over reproducing the original paper exactly, the list of AI models and software to test, the exact
measurements to record, and the known weaknesses of the plan are all fully written out. What remains
is running the actual tests across the chosen combinations and reporting the real, measured results
once they're collected and double-checked.

**Q: What would you do with more time or a bigger budget?**
A: Test more AI models and more combinations for stronger statistical confidence, test against more
realistic (though still authorized and private) practice environments, and move on to the partial
AI-retraining techniques that were identified as promising but set aside for this phase due to time
and hardware limits.

**Q: Is this a solo project or does it build on other people's work?**
A: It's a solo project, but it deliberately builds on and properly credits existing, real,
publicly available tools and frameworks rather than reinventing them from scratch — using
already-built, trustworthy pieces (the security tool-set, the assistant software, the reference
designs from the other researchers' work) and focusing original effort on the actual research
question (how reliable is this, and can a specific fix help) rather than on rebuilding
infrastructure other people have already built well.

---

## 9. Quick-reference cheat sheet (one-line answers)

| If asked... | Say... |
|---|---|
| How is this better than the base paper? | It's not "better" at the same task — it answers a different, currently-unanswered, more practical question: what happens without the expensive AI and without a human helper. |
| What's your main new contribution? | A documented catalog of exactly how and why smaller AI models fail at this task, proof that the surrounding software matters as much as the AI model, and a cheap working fix for one specific failure (false success claims). |
| Are you trying to beat the base paper's performance? | No — the base paper's approach is expected to perform better; this project answers a different question about accessibility and reliability, not a competition on the same benchmark. |
| Why smaller/free models? | Because almost nobody can afford to run the base paper's expensive setup all the time, and nobody has properly measured what happens at the tier people can actually use. |
| Isn't this dangerous? | No new attack ability is created — only how reliably an AI uses already-existing, publicly known tools is measured, on private practice systems. |
| What's the biggest weakness? | Limited hardware means fewer AI models and fewer test runs than a full lab study would have — stated openly, and every conclusion is scoped only to what was actually tested. |
| What if the results are just "small models are bad"? | The value is in the specific, reproducible "how and why," and in testing a real fix, not in the one-line conclusion alone. |
| Did you get permission to hack things? | All testing is on private, disposable practice systems owned by the researcher — nothing external or unauthorized is touched. |
