---
title: Doom Via Spindas
layout: post
---

After watching <a href="https://www.youtube.com/watch?v=BuV_9XW8ymo&ab_channel=adef">this</a> video, I was inspired to actually make the game render on Spindas live. 

Some quick background info: Spinda is a pokemon which has a different spot pattern for each different personality value, of which there are about 4 billion.  This project takes the pixels rendered in the game DOOM, and translates that to a mosaic of Spinda patterns which looks like the game.  The previous method used a slow genetic algorithm, which I simplified and sped up by using a direct pixel corrleation between each of the 4 dots on Spinda and a pixel in the game.

You can try it out <a href="./spindafy/index.html">here</a>!