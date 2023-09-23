---
title: Acapella
layout: post
---

Acapella was my team's project for SB Hacks 2023 where it won second place.  It is a Minecraft mod made in <a href="https://fabricmc.net/">Fabric</a> that add a command to beat the game autonomously.  It uses <a href="https://github.com/cabaletta/baritone">Baritone</a> to do pathfinding.  Check out the Devpost page <a href="https://devpost.com/software/acapella">here</a>!

Basically it uses a stack of tasks we made and pops those tasks off in order of dependency.  Each task may generate additional subtasks and the idea is that each task is easy enough to solve using Baritone and some manually coded behaviors.  It also automatically defends itself and maintains its hunger.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ku8DImxcO4c?si=_XwjdHc4u6ftj-v9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>