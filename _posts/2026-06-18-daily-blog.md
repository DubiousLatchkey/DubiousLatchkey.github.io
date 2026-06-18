---
title: Fiddling with the pieces
date: 2026-06-18 01:14:00 -0700
categories: [Daily]
tags: [notes]
---

## Fiddling with the pieces

I'm going back to the fundementals of my match 3 game - the pieces itself.  I mentioned yesterday I didn't like the healing the multiplier pieces.  Healing pieces were my bane always because if they were powerful, they slowed gameplay to a halt and if they were weak they were pointless filler.  They also led to ludonarrative dissonance because my lore of magic doesn't really gel with something as handwavy as healing.  Anyway, I've ditched them.  The other problematic piece was the damage multiplier.  It was literally filler because I couldn't think of a 6th piece type so it always felt tacked on.

Instead, I've come up with three piece ideas which I implemented today which should be better for gameplay and storytelling.  First is the null piece.  It matches like all other pieces but gains no resources.  This combines with the second piece - the brick.  This one can't be moved and doesn't match at all.  Both of these pieces are basically hindrances and they help to tell the story.  Basically, the main plot of the story involves magic being lost from the world - as the story progresses, I can increase the spawn rates of the bricks and nulls to make things harder.  This should help challenge the player and make it so their more powerful spells don't trivialize things later in the game.  The last piece is to counteract all these negative pieces which I feel like can be annoying in excess without something to counterbalance them.  It's a wildcard which can match any color of mana which I can make plentiful earlygame but then rarer later.  I'll have to test to find the exact rates, but I like each of these pieces unlike what they replaced.

What's really cool is that this helps with my new design focus of "board matters".  Since moving things into patterns or positions is going to matter a lot in the new design of the game, these hindrance pieces can help make the gameplay more interesting as it will require more problem solving to manipulate the board rather than just "move this here to make a shape".

A problem I forsee is that these brick pieces, if a player has bad luck, can really start to gum up a board.  I need to make methods of destruction plentiful - perhaps the first spell the player gets is a cheap spell which destroys a single piece on the board.  I'm going to need to brainstorm a lot more forms of board manipulation to make sure we don't get into too many situations where the player has no resources and basically no moves - that's when gameplay is the least interesting.

Next, I want to add a wide variety of payoff and enabler spells.  Then, once I gauge the power level of each, I can turn their unlocking order into progression.  Then I'll base the rest of the game's design (encounter time / turns, enemy spells, ai, hp) around how good those board manipulation and payoffs are.