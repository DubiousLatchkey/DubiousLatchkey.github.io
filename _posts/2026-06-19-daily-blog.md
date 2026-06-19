---
title: Arbitrary Decisions
date: 2026-06-19 09:46:00 -0700
categories: [Daily]
tags: [notes]
---

## Design Space 

I've reached a point in two places of design where I have effectively infinite options but I need to narrow things down to a testable number.

### The Board

After testing the changes to the board with the null and brick pieces, I realized that in order to do the cool story thing where they become more commonplace over time, they need to start off not spawning much.  However, if I tweak the probabilities too much against them, the other 4 main pieces just start endlessly cascading.  To prevent this, I need another piece type that doesn't match with the others.  The question is, what kind.

I brainstormed about a bajillion different designs that I thought were ok, but I think to really key into the "magic is draining from the world" motif, I need something that represents abundance.  Then, we can reduce that piece's spawn rate over time and have the nulls and bricks take its place.  Eventually, I implemented rainbow mana, where matching it gives one of each color per piece.  It's stronger but less common than other mana pieces and doesn't match with the individual colors.  Might have to remove wildcard pieces to prevent confusion, but that can wait for later.  This has a cool side effect where once their spawn rate is too low, rainbow pieces start gumming up the board because they don't have enough partners to match with.  I might have to make some spells that can mitigate this - i.e turns mana into rainbows or something.

I had ideas of pieces that could manipulate the board itself - like pieces that could fill nulls or break bricks or something or even change the probability of piece spawns, but I decided to go with this route because its simpler.  I'll leave the board manipulation to the spells and have the board not able to affect itself outside of matching 3.

The other main batch of ideas were those which took more of a Puzzle Quest route with outside the battle effects - that game had gold and experience.  I decided early in this game's development I wanted to keep the out of game economy / progression limited because my narrative is pretty linear, so those were written off.

### Spells

The other design where I feel I need to boil things down to essentials is spell design.  I have my main 3 "schools" of spells so to speak of destruction, board manipulation, and payoffs for patterns, but just in my one day of experimentation, I realize the design space here is huge.  There are just a lot of levers to pull.  Let's take a spell that destroys some pieces for example.  I know I want the purpose of this spell to clear some pieces, but the question becomes - how?  Should the spell end the caster's turn?  Should it be a cross shape, a square shape, or a single target?  Should it score the piece of just destroy it?  I know I can't have a spell for each of these varieties - that's just choice overload for a player, so I need to start thinking of some consistent design pattern so a player can "grok" how things work and not be blindsided by spells that don't follow these rules.

First arbitrary design principle I'm thinking of is that a spell should always cost a turn.  I had designs in the past for engines which would require casting many spells in a turn or more utility based spells which would not cost a turn, but maybe to keep the mental load down, I can just have everything at least cost a turn.  This also means I can't have spells with small effects since they would not be worth the opprotunity cost of making a move on the board.  Overall, it's probably a good thing the player feels each spell is significant, so I'm ok with that.

Another potential one I'm still thinking about is that spells that "destroy" pieces should always score them as well.  In my testing of all these new destruction type spells is that their outcomes are random and often barely give any advantage at all.  They can be useful for clearing bricks and the like, but not much else.  There are niche situations where you can engineer a set of pieces to fall perfectly to get a lot of resources / do a lot of damage, but those are few and far between.  To make the destroy spells useful, they should score everything they destroy.  The only problem with this is that it might make looping too easy - i.e you get enough mana to cast the spell again by casting one of these spells that scores a large number of pieces.  I think a solution might be to keep targeted small destructions scoring, but make the larger disruptive ones as destroy only.  I tried some spells which destroy 32 or 16 pieces randomly, and by leaving them as destroy only, I can make them cheaper and let player have fun blowing up large swathes of stuff.

One concept I learned about for design here is limiting things by their purpose and not having 2 spells that do the same thing.  I feel like a good course of action is to divide the game into early, mid, and lategame and then have one of each function for each stage in the game.  So, a function might be to clear out bricks, and we have 3 progressively bigger / more efficient versions.  Then I can test these all individually with other spells of their "tier". I do want to throw in some cool or fancy spells in their just for fun, but this might be a good course of action design-wise to limit the amount of variation that is possible in my spell system to make the design language more grokkable.  