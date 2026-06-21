---
title: Being Self-Taught
date: 2026-06-21 09:53:00 -0700
categories: [Daily]
tags: [notes]
---

## What You Miss from Being Self-Taught

Refreshing the dialogue system brought something into perspective for me.  This happened when I was doing my refactor from before, but seeing it a second time made me realize things.  When I first went around building this in 2019, I thought only unity scripts that were attached to gameobjects got compiled, so I stuffed all my logic into monolith script files.  It worked, but there was always something itching in my about the script length bloat.  Returning to the project now, I learned that actually everything gets compiled and I just don't need the Unity Monobehavior class.  With this I was able to debloat everything including my dialogue controller which split off parser logic and command logic.

It's one of those weird quirks that happens when you don't learn something formally - in this case Unity for me.  If your focus is on getting the thing in front of you to work, you learn how to get that thing to work - and that's it.  You'd think that would eventually lead to problems and you have to fix them eventually, which I would say is mostly true, but not always.  I probably would have needed to return to the seralization problem I had before which was straight up not a functional design for a release product but things like script bloat just aren't a visible enough concern to ever warrant coming back to.  It just just slowly makes things slower and more inefficient to work with without ever being a "need to fix" issue.  It all stemmed from one minor system design misunderstanding that a one-off line in a class somewhere could have prevented.  

Well, I'm more experienced a software engineer now, so I knew to go back and to fix these things - I'm relatively confident these principles will get me through the rest of this projects at least.  With the dialogue system working better now, I do need tooling to write and edit dialogues more easily.  I tried using a unity editor panel, but its pretty ugly and I'm not sure if I can get fancy with the UI to make it an actually smooth experience.  I might vibe code a python or web based one later.  

Additionally, I've always been dissatisfied with the way scenes flow into each other.  Right now, all dialogue and combat transitions are determined like a linked list, each text asset references the next.  It has always felt fragile and naming was always a puzzler.  A master scene list never felt right either.  This one needs more brainstorming.  The key is I need it to be flexible so I can insert or remove scenes with minimal editing in case I change the story's structure.  It would be cool to have a structure open for modding too.