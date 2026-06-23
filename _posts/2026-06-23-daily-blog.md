---
title: Writing
date: 2026-06-23 15:22:00 -0700
categories: [Daily]
tags: [notes]
---

## Dialogue Trees

My game has a linear narrative.  That, in theory, makes it easy to do scene design.  One scene leads into another and there's no need to have story flags or branching scenes.  However, in the end, the system is not that much simpler than one that does handle all the branching.  The problem I had in the past was organization.  Once I had all these text files with scenes and combat descriptions in them, I needed to be able to access them in order.  This meant a naming scheme that preserved alphabetical order.  I used numbers with acts and scene numbers, but that was really inconvinent if I, say, wanted to add a scene in between 2 others since I would have to adjust all the numbers.  The solution was to make that all irrelevant.

Instead of relying on the file system, I made a separate app to organize and write dialogue.  The main UI is a click and draggable grid of block I can manually connect to each other.  This creates one long chain of scenes I can visualize and manage without having to worry about the file system and alphabetical naming since that is all abstracted out.  Furthermore, it also has an editor where I can easily write dialogue scenes.  In the past, typing those out with the syntax I developed was quite a manual process and was prone to typos.  Now I can manage commands with menus and make new lines with the right image file references because I detect them and make them available via dropdown instead of having to keep my copy paste history fresh with all this stuff.

I made the app a PWA.  I don't know what it is about them, but I really like the concept of PWAs.  I first used them to get the Youtube Music app on my PC and there's just a different psychological relationship you have to apps when they aren't in a browser window even when, under the hood, it is still technically just a web app.  There's a feature which allows web apps control over a folder on your computer so it basically took the advantage that native apps have and combined it with the vast UI libraries for making web apps which is why I went with this solution.

Is it a bit overkill, maybe, but the advent of vibe coding means I was able to make this tool in about a day.  I also tried Claude Code for the first time when making the tool.  They say it's better with visual UI tasks, to which I say "maybe", but I will say it makes very nice diagrams when it is explaining what it wants to do.  Not sure if that's actually that helpful but it is pretty.  So far I haven't noticed a significant different between it and Codex for coding tasks.  

Now, with this new tool, we go back to encounter design and writing as the next major roadblocks - things I can't speed up that much with AI.  Once have a good amount written up, I'll work on visual tweaks and maybe finding an artist.  I still want to do coding projects in the meantime, so I have another in mind to work on while I write and test.