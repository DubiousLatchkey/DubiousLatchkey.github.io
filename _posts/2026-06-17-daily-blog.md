---
title: Back in the groove
date: 2026-06-16 12:00:00 -0700
categories: [Daily]
tags: [notes]
---

## Reviving Match-3-Adventure

So, today I decided to revive my old match 3 adventure game that I never finished.  Looking at my old code from 2019 was really something.  Some parts were pretty smart like my interface system for weapons and status effects, but some parts were really dumb like how I had the enemy and player controller scripts basically duplicate everything like health and mana between them.  

With the new power of AI, I had Codex do the arduous work of refactoring the whole thing to update to the new version of Unity and fix my poorly thought out design decisions.  That honestly felt very good and was probably the reason why I didn't get back to this project sooner.  

I also was able to patch the things I didn't understand how to build back in 2019.  The first big one was data storage.  I was storing data for spells and enemies in a file that ran every time the game ran.  There was a serializer that then took my hardcoded data objects and saved them.  Of course this means the first time the game ran there would be no data to fetch from and it wouldn't work, but I didn't know how to solve this back in 2019.  Now, I replaced all that by defining my game data in json files that get parsed normally.  Honestly don't know what I was thinking back then.

The second big thing was testing - I had some default data that would allow me to test the combat system, but the only way to customize it was actually hardcoding the defaults in the scripts.  Moved that out to a proper debug asset and made a custom runner to load it in.  My goal here was to get everything into a workable state so I can rapidly iterate game mechanics to get something fun before building the rest of the game around it.  That was the big issue from before - I had built things in a vertical slice, but since the core gameplay wasn't there yet things kept changing and I kind of added things haphazardly before knowing if they were even good or going to be in the final design.  

## Gameplay tweaks

Another thing I did was to really give a good think as to what I wanted to accomplish with the game.  My original vision was quite similar to Puzzle Quest with using the board to acquire resources and then using equipment and spells to build engines you can defeat enemies with.  So, for example, I was thinking weapons would be enablers for archetypes that would then be executed via spells.  There was a design I had for a poison mage build which would have a weapon deal extra poison damage and then just try to get resources to spam a poison spell.  A similar design went for a storm mage which would have a cheap spell to do 0 damage but a weapon that would increase damage by one for all spells.  

These designs were fine, but they feel a bit linear to me now - basically just my RPG and Magic: the Gathering experience just in match-3 form.  I looked at some of my old notes for the "chaos mage" build that went around destroying pieces on the board and I realized I actually want to build something that cares more about the board itself.  Actual Puzzle Quest gameplay boils down to pattern recognition - look for 4 in a row matches, look for the colors you want, etc - and you look for those patterns the whole game.  I think we can switch up the core pattern recognition and make the spells care more about the patterns you see.  I tested out a couple of spells that make you look for patterns - the four corners of the board, L-shapes, and I found that that was actually pretty interesting and different.

I'm going to design the new gameplay around that - enablers for board manipulation (e.g. swap 2 pieces anywhere on the board) and payoffs (e.g damage that scales on how many pieces of the same type are touching).  I'm also going to put some more flashy stuff that kind of just blows stuff up and hopes for the best.  These 3 kinds of spells nicely into my 3 colors of mana which is nice.

Another thing I was always dissatisfied with was the pieces themselves.  You need like 6 unique pieces for a match 3 game to work, but I was always torn on the last 2.  I have 3 colors of mana, direct damage, and then the ones I was never certain about: healing and damage multipliers.  I was never sure how to design around those last 2 and they just felt out of place with the engine system from before.  Definitely going to revisit these later and see if we can't get some ludonarrative harmony going on.