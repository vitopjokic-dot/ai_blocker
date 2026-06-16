import joblib
import numpy as np
from collections import Counter
model = joblib.load("ai_detector_model.pkl")
features = joblib.load("feature_fn.pkl")
ai1="""🧼✨ INTRODUCING: ULTRA-SHINE MAX CLEAN 3000™ ✨🧼
(Now with 97.8% more “sparkle optimization” technology)

Greetings valued consumer!

Are you experiencing suboptimal surface cleanliness in your residential or commercial environment? Do stubborn stains, dust particulates, and “unknown sticky substances” continue to negatively impact your spatial satisfaction metrics?

Fear not.

Ultra-Shine Max Clean 3000™ is here to revolutionize your cleaning paradigm.

Powered by next-generation nano-reactive citrus-ion molecules (derived from scientifically adjacent orange concepts), this advanced cleaning solution delivers:

⚡ Instant grime neutralization (results may vary based on belief strength)
🧽 Adaptive stain targeting algorithms
🌿 A vaguely botanical freshness profile optimized for emotional reassurance
✨ “Visually convincing cleanliness enhancement effects”

Simply apply Ultra-Shine Max Clean 3000™ to any surface, and observe as dirt is:

Analyzed
Emotionally discouraged
Removed with algorithmic precision

🧠 Independent internal simulations suggest a 99.999% perceived cleanliness improvement index, assuming adequate lighting and optimistic interpretation.

WARNING: Product may cause excessive admiration of countertops, spontaneous cleaning motivation, and mild confusion regarding whether surfaces were ever dirty in the first place.

Ultra-Shine Max Clean 3000™ — Because cleanliness is not just a state, it’s a computational experience."""
ai2mod="""✨ FreshEase Multi-Surface Cleaner ✨

Make everyday cleaning feel easier.

FreshEase Multi-Surface Cleaner is designed to help you tackle common messes around the home—kitchen counters, bathroom surfaces, and everyday spills—without needing multiple products.

With a light, clean scent and a fast-acting formula, it helps lift grease, dust, and grime so your surfaces look refreshed after each use. Just spray, wipe, and enjoy a cleaner space in seconds.

Why people like it:

Works on most hard surfaces
Helps remove everyday dirt and residue
Leaves a fresh, non-overpowering scent
Easy spray-and-wipe use

Whether you’re doing a quick tidy-up or a full clean, FreshEase fits easily into your routine.

Clean spaces don’t have to be complicated."""
ai3hide="""I’ve been using this all-purpose cleaner for a couple of weeks now, and it’s honestly made day-to-day cleaning a lot less annoying.

It handles most of the usual stuff—kitchen counters after cooking, bathroom sinks, even some sticky spots on the table—without needing to scrub forever. I like that it doesn’t leave a strong chemical smell behind, just a light fresh scent that fades pretty quickly.

Nothing fancy about it, which is kind of the point. Spray, wipe, done. It’s become one of those things I keep under the sink because I end up reaching for it more than I expect.

Not a miracle product, but it does exactly what I need it to do."""
aiidk="""On June 3, the European Commission published its legislative package on technological sovereignty, the urgency of which has escalated sharply after U.S. President Donald Trump's administration on Friday mandated that the company Anthropic cut off access to its most advanced artificial intelligence models for all foreign nationals. This decision by Washington highlights the European Union's structural vulnerability in the face of American tech companies, directly impacting the bloc's security. The European Commission's new initiative covers four key areas: the Chips Act 2.0, the Cloud and Artificial Intelligence Development Act (CADA), the EU Open Source Software Strategy, and the Strategic Plan for Digitalization and AI in Energy. The Commission's official statement notes that these legislative changes represent a fundamental shift in approach, with the primary goal of reducing dependence on external suppliers in technology policy. Analysts estimate that the presented documents lay the groundwork for isolating European digital infrastructure from global political volatility.

The CADA regulatory framework is based on a four-tier sovereignty classification that will apply on a mandatory basis to cloud and AI infrastructure. Under the new proposal, member states will be required to independently conduct sovereignty risk assessments for their providers and make procurement decisions solely based on the results of these studies. According to the rules, the most sensitive public sector systems must be hosted on servers under the control of EU entities. The strictest fourth tier provides for full EU ownership and control, personnel obtaining European security clearance, a total ban on transferring AI inference data outside the bloc, and independent audits validated by national authorities. The law also aims to triple the capacity of EU data centers over the next five to seven years. In parallel, the Chips Act 2.0 focuses on mobilizing €120 billion in investments by 2035 so that Europe can produce at least 20% of the world's advanced semiconductors by 2030. Both legislative proposals will be forwarded to the European Parliament and the Council for consideration, with the negotiation process expected to take 18 to 24 months.

Washington's forced restriction on Anthropic validates the fears of EU officials that underpin these new regulations. According to Reuters, Anthropic announced on Friday the shutdown of its leading models, Fable 5 and Mythos 5, after receiving an export control directive from the U.S. Department of Commerce prohibiting foreign access to these models. The tech giant explained that it was not provided with specific details regarding national security threats. Representatives from Amazon Web Services confirmed that Anthropic requested the revocation of access across all regions. This suspension clearly demonstrates the dependency risk that the European Commission is trying to eliminate, as European governments and businesses relying on American suppliers could find themselves without services overnight due to a White House decision. Anthropic's forced market exit, which occurred exactly ten days after the publication of the European Commission's proposals, strengthens the position of officials who demanded the introduction of mandatory sovereignty mechanisms instead of voluntary commitments.

To create a European alternative, the new package provides for the allocation of €2 billion over the next seven years for the open-source strategy, aiming to scale European products in cloud computing, artificial intelligence, and cybersecurity. The "free software first" principle will become mandatory in public procurement, with a target to reach 30 million active users in open-source tools by 2030. In a statement reported by Reuters, a Commission official indicated that these proposals aim to ensure Europe's ability to develop, deploy, and protect technologies for its own needs. The next step will be for member states to establish national monitoring groups to assess local industry readiness for transitioning to the new standards. The market reaction at this stage is cautious, though European tech associations welcome the increased funding, which will enable local developers to compete with American platforms"""
aigen100="""Our Mission
The high-signal hub for artificial intelligence — where serious discussion, quality content, and verified expertise drive the conversation. Open to everyone.

Rules
1. Be Civil
No personal attacks, harassment, slurs, or hate speech. Disagree with ideas, not people. Violations result in a permanent ban.

2. High-Signal Content Only
Every post should teach something, share something new, or spark substantive discussion. Removed: low-effort hot takes, vague posts with no context, AI conversation screenshots without analysis, and news reposts without new angles.

3. No Spam · Builders Welcome with Substance
No ads, marketing, or promotional content. Builder posts ("I built X") are welcome IF they include: - Explicit affiliation disclosure - 150+ word educational breakdown (technical approach, benchmarks, limitations, or lessons learned) - A repo, demo, or documentation link - No CTAs (waitlists, pricing, "subscribe")

Rate limit: 1 self-promotional post per author per 14 days. Open-source projects with a public repo get lighter review.

4. No Repetitive Doom or Hype
AI jobs/society/existential risk discussions are welcome — but only with new data, specific analysis, or first-person expertise. Generic takes, emotional venting, and rehashed topics get removed. This applies to both doom AND hype. Search before posting.

5. No Tool Requests
"What's the best AI for X?" posts are not allowed. Use: - AI Tools Directory — our curated list - r/AIToolBench — dedicated tool discussion

6. News Posts Need Context
Link posts require a submission statement (top-level comment within 30 min) summarizing the article and explaining why it matters. No statement = removal. Research paper links with clear abstracts are exempt.

7. Use Correct Flair
All posts must be flaired within 30 minutes. Available flairs: 📰 News · 🔬 Research · 🛠️ Project/Build · 📚 Tutorial/Guide · 🤖 New Model/Tool · 😂 Fun/Meme · 📊 Analysis/Opinion.

8. Title Standards
Titles must clearly describe the content. No ALL CAPS, no clickbait, no vague titles. Lead with the signal. Keep under 120 characters when possible.

Verification System
We verify professionals working in AI. Verified users receive a flair visible on all their posts and comments.

Tiers: - 🔬 Verified Engineer/Researcher — Full-time engineer or researcher at an AI company or lab - 🚀 Verified Founder — Founder of an AI company (funded $10M+ or demonstrable traction) - 🎓 Verified Academic — Professor, PhD researcher, or published academic in AI/ML - 🛠️ Verified AI Builder — Independent developer with public, demonstrable AI projects

How to apply: 1. Send a modmail with your role, and company/institution 2. We'll ask you to verify via ONE of: - Company email loop — we send a code, you reply from your company email - LinkedIn live tag — add a unique string to your LinkedIn bio, we verify, you remove it - GitHub live tag — add a unique string to your GitHub bio or a repo - HuggingFace live tag — add a unique string to your HuggingFace bio temporarily, we verify, you remove it 3. Verification is typically processed within 48 hours

Rules: - Full-time employees only (no contractors) - Must be currently active in the role - Screenshots are NOT accepted (too easy to fake) - Optional: add "@ Company" to your flair if you want

Platform Requirements
We check that your profile demonstrates real, established work — not just that you own an account.

GitHub
Account age: 6+ months
At least 3 public repos with original code (forks alone don't count)
At least 1 AI/ML related project
Recent activity (commits within last 6 months)
Meaningful contributions to established open-source AI projects (merged PRs) also count
HuggingFace
At least 3 published models or datasets
At least 1 with 100+ downloads
Work should be original or meaningfully adapted (not re-uploads of base models)
LinkedIn
Profile must match the claimed role and company/institution
We verify the tag is live on your profile — no screenshots accepted
Moderation Appeals
"""
def predict(text):
    f = np.array(features(text)).reshape(1, -1)
    return float(model.predict_proba(f)[0][1])
if __name__=="__main__":
    print(predict(ai1))
    print(predict(ai2mod))
    print(predict(ai3hide))
    print(predict(aiidk))
    print(predict(aigen100))
