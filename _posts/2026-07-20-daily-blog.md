---
title: I'll just train my own model
date: 2026-07-20 23:06:00 -0700
categories: [Daily]
tags: [notes]
---

## Back to my Karaoke Maker

I went back to my karaoke maker project and I reworked things.  I never liked how there was a delay in the gui so I could never tell for fine changes if the sound was in the right place and the word level timings that it made were always off.  The first was easy to fix - I was going to remove PyQt anyway since it was GPL licensed and replaced it with Tauri so I could be more permissive.  With AI, the ui changeover was flawless.  The other problem was bigger and more fundemental.

When I first made the project, it was a stitching together of existing vocal isolation models, ASR, and forced alignment.  I didn't train anything myself.  Unfortunately, that leaves me at the mercy of the limitations of those models.  ASR inaccuracy isn't a huge problem since I'm using a many-to-many matching scheme to connect them to the ground truth lyrics.  I actually improved my implementation of that a lot while I was reworking things by using Needleman-Wunsch instead of Viterbi.  No, the real problem was in the alignment.  The quality was always mediocre since it was trained on speaking and singing is different in that we connect words together and hold sounds longer.  So I had a thought after going to the AGI summit and hearing all the people there speak about AI powered research - why not just train my own model?

The way wav2vec (the existing alignment method) works is with a CTC based model that produces letters from audio in a time series.  It then uses a projection algorithm to force the word we have in ASR onto the letters and uses the boundaries as the timings.  That's 2 avenues for improvement.  I found an existing dataset with word level timings and trained a LORA on the existing wav2vec model on it.  Initially, it was only better on finding starting times of words, but the ending time error was higher than before.  That's when I reworked the projection algorithm to cater to how singing works - the biggest difference being that sounds held out for longer get attached to the previous word rather than dropped.  After sticking them in my gui to see which was better on new data, I was tickled pink to see my new method did indeed mean I had to edit less manually.

I have to credit Codex for being able to implement all this in a day.  Learning how to implement and train a CTC model would have taken days or weeks, and then getting the data and cleaning it just as much time.  My implementation would probably be worse than what OpenAI could give me too.  Even analyzing the results was only possible with AI as it saw the better starting times and worse ending times.  This is really a case where AI in enabling me to do things that I just couldn't do before.  Anything in our current understanding of programming is basically there for the taking to use however and you don't need to know much about how.