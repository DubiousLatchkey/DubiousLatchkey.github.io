---
title: I'm Sorry I Doubted You PWA
date: 2026-07-03 11:42:00 -0700
categories: [Daily]
tags: [notes]
---

##  It wasn't the PWA

Ok, so I reworked my dialogue and story flow editor to be a native app using Tauri.  It was pretty easy since it still uses a "webapp" and all I had to change were the file interactions so they use the native file system file operations.  I thought this would solve the problem of my computer running out of memory and Windows Explorer crashing every few hours, but apparently it wasn't the issue.  I ran the new app and while it worked for its intended purpose, my Explorer still died.

Back to the drawing board on this issue, I suppose.  Basically, I've diagnosed that all of my RAM gets eaten up by what is only identified as "mapped file" in RamMap and not under any specific process.  This indicates it's some caching thing, but I think this is only a symptom since in theory these caches should be easily freed when other processes need memory.  My Windows Explorer keeps crashing, so they're not being released properly.

The other hint I have is that the number of processes goes crazy over time.  I'm talking like 500k processes.  Something is creating zombie processes and over time it kills Windows Explorer.  Other apps seem to continue to run fine, which is weird, although running something expensive would probably lead to a freeze.

Could it be a virus?  Codex running around my OS and forcing file caches?  A random driver?  I noticed git keeps running and indexing things, possibly  triggered by Codex.  I've tried all I know to diagnose where this stuff is coming, but still nothing.  For now, I'll just have to restart my computer every so often.  At least I know it wasn't something I made.

## Story Flow

Well, after having migrated the editor to Tauri, I've been making improvements there.  Unfortunately, this means it is no longer a PWA, and since I've already made some feature additions, it's not worth it to go back.  So far, the standalone app has had the same level of convenience as the PWA, so there's no real incentive to go back.  I liked how it was easy to build the PWA and just run it from the start menu, but it meant having to run a web server to serve it.  On the other hand, running the executable means I do have to navigate to the exe, but this is solvable with proper versioning and installation or even a shortcut.  The real inconvenience would then be having to install it each time, but then it gets on even footing with the PWA so there's not a significant difference.