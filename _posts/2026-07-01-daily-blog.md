---
title: Has the PWA Betrayed Me?
date: 2026-07-01 00:55:00 -0700
categories: [Daily]
tags: [notes]
---

## Windows Explorer issues

I've been noticing a suspicious pattern of behavior as I continue to write my game.  It seems like after my computer is on a while, my windows explorer dies and takes a long time to come back.  It's quite annoying not having a taskbar.  This didn't happen until I resumed my game dev, so it has to be something related to it.  At first, I assumed it was the fault of Unity.  As a game engine, it does take a lot of memory, but after I began closing it after use, the problems persisted.

My current theory is that it has to do with the Progressive Web App I made to edit the dialogue of my game.  Since it works in the Unity project folder, it has a lot of permissions and does make a lot of read, write, and search operations in it.  I wouldn't have thought this was the case, but it only seems to happen when I have the app running.  The crash and subsequent computer slowdown seems to be associated with all of my RAM being used up.  When I did a more detailed look into the memory use breakdown, RamMap revealed everything was taken up by caches of the file system for quick file usage.  This points to something that's trying to cache a bunch of files - possibly the PWA.

That's a shame since I love the concept of PWAs, but I may now have to find a way to run this app as native app instead.  AI should be pretty good at this kind of conversion, but I feel like the UI would not survive such a library / language transition.  Only one way to find out.  Luckily, even remaking it from scratch should not take very long.

## Improvements

I did make a few improvements to the PWA which I do hope transition over easily to a native app.  Most were quality of life related that let me make the dialogues and combat nodes faster.  I added things like click and drag transitions between nodes, a few dialogue system syntax improvements, and reorganized some ui elements for readability, but the coolest thing I made was a scene preview.  I could have made like a whole simulation of what the scene looked like, but I actually didn't need that.  The important point was to be able to see at a glance where the characters were currently in the scene at a given point in the dialogue so I didn't have to remember it all since it's all defined by commands in my dialogue file syntax.  

I've made a lot of progress on finishing the first act of the game's writing and encounter design - just got to keep soldiering on.