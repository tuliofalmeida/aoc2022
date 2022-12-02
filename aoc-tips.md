EXTRACTED FROM: [link](https://gist.githubusercontent.com/mcpower/87427528b9ba5cac6f0c679370789661/raw/b4b1e1ec83bac2c8c3e0effbb345f6d7ae0ecbba/aoc-tips.md)

Hi, I'm mcpower. I've done Advent of Code seriously for two years now in Python, placing 9th in 2018 and 12th in 2017. This year, I'm taking a break from aiming for the leaderboard - while it's fun and all, it is a bit stressful at times (the good kind of stress, though!). As such, I'd like to share a few tips for anyone wanting to aim for the leaderboard.

This is everything that worked for me. Your mileage may vary, though - don't take this as gospel, see what works for you.



# Go fast

Go fast.



# Code

## Language

Which language you use matters *a lot*.

- Use a language which you're familiar and comfortable with. You don't want to go looking up "how to convert string to integer" in the middle of a problem. In my opinion, this is the most important part about selecting a language - even if the code takes a long time to type, you're comfortable with the language and don't have to stop your train of thought when coding.
- Preferably, use a concise language. The less code you have to write for a problem, the faster it is.
  - Most of these are scripting languages (Python, Perl, Ruby, etc.). While scripting languages are definitely slower than their compiled counterparts, almost all AoC problems don't require the speed of a compiled language.
  - If you're using Python, the [PyPy](https://pypy.org/) interpreter significantly speeds up most AoC problems without changing a single line of code.


## Libraries

Get to know your language's libraries, especially the standard library. You often don't need to write common code such as sorting or implementing a priority queue. I didn't use any third party libraries, but some things like Python's [`sortedcontainers`](http://www.grantjenks.com/docs/sortedcontainers/) would've come in handy if I knew about it back then!

You should have your own utility library - see the "Tooling" section for more details.


## Regexes

Learn the basics of regexes (especially capturing groups and non-capturing groups). They're very useful for parsing weird and long inputs, like [2018 day 24](https://adventofcode.com/2018/day/24). You don't need to write a very strict regex for things you can do with code - for example, in the aforementioned problem, I parsed everything inside parentheses with `\([^)]*\)` and did the splitting with code.

In most cases, you can get away with really "loose" regexes. One regex I used a lot was finding all `-?\d+` in my `ints` function, which finds all integers in a given string - thanks mserrano!


## Debugging

Using a full-blown debugger may be worth it, but for most cases print debugging does the job (and is fast enough). A well-placed breakpoint should be faster than many print statements, but requires the additional overhead of setting up a debugger. What you use is personal preference, although I'd recommend looking into a debugger (even though I didn't use one 😛)


## General coding tips

- You often get some guarantees with the input, like "these numbers can't be negative". Use this to your advantage and **don't validate the input** - assume they fit the format given.
- Anything goes when you're coding for speed. Know of a horrible hack which could help you save a bit of time in a problem? *Use it.* Most of the horrible hacks I know about come from my experience with code golfing - I'd definitely recommend code golfing as a way of getting to know a language better!
- For part 2 of a given problem, you should work in the same file you used for part 1 - don't bother starting from scratch. If you want to save a copy of your part 1 code, make a copy of your code before working on part 2.



# Problem solving

## Competitive programming

I come from a competitive programming background - I started doing a tiny bit of competitive programming in 2014, ramping up a fair bit in 2016 where I got into my university's ACM ICPC club, and kinda fell off in 2018.

My competitive programming experience definitely helped *a lot* with the tougher problems in AoC. In my opinion, most problems in 2017 could be classified as "just do it" problems - problems which are straightforward to understand and requires you to just... do it. However, in 2018, there were more problems which were non-trivial. Doing harder competitive programming problems gets you in the mindset of how to think about these problems, and helps you more easily identify what data structures and algorithms you need for a problem. For example, [2018 day 25](https://adventofcode.com/2018/day/25) was a perfect use of union-find, and the top two people ([one](https://www.reddit.com/r/adventofcode/comments/a9c61w/2018_day_25_solutions/eci5kaf/), [two](https://www.reddit.com/r/adventofcode/comments/a9c61w/2018_day_25_solutions/eci7dju/)) used union-find in their solutions - most other people used a DFS/BFS to count components. Algorithms and data structures appear relatively often in AoC, especially graphs, so be sure to know some basic graph algorithms (BFS, DFS, Dijkstra)!

To be completely honest, I'm unaware of any good resources for people starting competitive programming - heck, doing AoC is probably a great introduction. My advice would be to do some "Div. 3" contests on [Codeforces](https://codeforces.com/), or do some past Qualification Round problems from [Google Code Jam](https://codingcompetitions.withgoogle.com/codejam/archive).

## Past problems

AoC has been around for... 4 years now. Doing past problems is definitely useful for familiarisation of the problems you'll see, especially the assembly questions. To be honest, I didn't do many past problems when I started in 2017 - probably four problems in total. As a result, I did pretty badly on the first assembly question in 2017 (day 18). Definitely try out an assembly problem if you haven't done them before!



# Tooling

## AoC website

I don't use any special userscripts or anything for the AoC website, but I do use [custom CSS](https://gist.github.com/mcpower/e224e66699a3bfe774e9eee2fe43bb8a) based on [@chordbug](https://twitter.com/chordbug)'s CSS to make the website significantly more readable.

If I were to compete this year, I would probably write a userscript to assist with copying `<code>` blocks for copying sample inputs. If someone writes such a script, do share it with the community!

**UPDATE**: I wrote a simple script to do this! Add this as a userscript, and click on code blocks to copy them:

```js
// ==UserScript==
// @name         AoC copy code blocks
// @author       mcpower
// @match        https://adventofcode.com/*
// ==/UserScript==
let style = document.createElement("style");
style.innerHTML = "code.copied:before{background: #30304f;}";
document.head.appendChild(style);
Array.from(document.getElementsByTagName("code")).forEach(el => {
    el.addEventListener("click", async event => {
        if (window.getSelection().type === "Range") {
            return;
        }
        await navigator.clipboard.writeText(el.textContent);
        el.classList.add("copied");
        await new Promise(resolve => setTimeout(resolve, 500));
        el.classList.remove("copied");
    });
});
```

## Templates

You should create a template for your solutions. My template comprised two files - [`a.py`](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/a.py), my main file, and [`utils.py`](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/utils.py), my utility library. The majority of the code went into the utility library, and my main file contained a skeleton of a solution to be filled in.

I recommend copying *both* the main file and the utility library for every new problem. You'll probably be updating the utility library as you do more problems, so having each problem have its own copy of the utility library will prevent any library changes from breaking past problems. This does mess up some IDE features like autosuggestion, unfortunately.


### Utility code / libraries

**Write your own utility library**. You could use someone else's, but if you write it yourself you know *exactly* how things work, and exactly when things can go wrong. This should include very common things like "getting all integers from a line of input", "distance between two points", etc. You should definitely use other people's code as inspiration, but I personally recommend writing it yourself for the aforementioned reasons. For example, [here is my utility library](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/utils.py).

Most of my utility library comes from things that I believe would be useful, or have often appeared in previous problems. The things that I believe would be useful... often aren't... but there's some which have definitely come in handy. See "My Code" below.


## Running code on inputs

My preferred way of taking in input is taking it in as a string argument to a function. You can then run your code on the samples and the actual input with one run of your program. This depends on how you get your inputs - see the below section. This also allows the function to differentiate between sample inputs and the actual input, which comes in handy for problems where the sample behaviour differs from the expected behaviour such as [2018 day 7 part 2](https://adventofcode.com/2018/day/7#part2) - and for debug printing only in sample inputs.

Alternatively, you could take in input from standard input and create a secondary script to run all inputs in the folder on your program. This is more useful in contests where you need to submit *a program* instead of submitting an answer like AoC. I personally don't recommend this method for AoC.

My preferred way of outputting the answer is using a print statement. It's simple, it works from anywhere, and it allows you to do print debugging if needed. The only time when this is not ideal is when you want to diff an answer to an expected answer. I didn't do this as it's easy enough to eyeball, sometimes it's worth it to do manual adjustment of the answer, and copying the expected answer takes a bit of time. However... in retrospect, this probably isn't the best idea, and diffing the answer would be easy enough - especially as AoC answers are often not that long and on one line. Perhaps returning the answer instead of printing it out would be better?


## Getting inputs

To get the input for each problem, I used to open up the input in my browser, then save it to the appropriate folder. This worked, but was a bit tedious and wasted a bit of time.

There's a few scripts out there to automatically fetch your inputs - for example, [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data). You should definitely use these scripts or something similar - they make your life much easier and they're pretty set-and-forget. I didn't really trust any of them for some weird reason, so I wrote [my own input downloader](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/utils.py#L480) as part of my template - it automatically downloads and caches the input for a given problem whenever I run my template for the first time.

For sample inputs, I personally copy and paste them into [a list of strings](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/2018/25/a.py#L54) in my main file. It keeps the sample input close to the code in case I need to refer to it (for parsing purposes), and I don't have to bother creating a file for each sample input.


## Submitting your answer

I don't trust any tool to submit my answer for me, so I manually submit my answers through a browser. It's probably faster to submit through a tool, but I personally wouldn't risk submitting something I didn't intend and having to wait a minute to submit my next answer.


## Editor

It doesn't really matter what editor you use, but being able to run your code easily - preferably in the background with a keybinding - is a must have. I personally used VS Code with the [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) extension to run it in the built-in terminal.


## Version control

If you want to commit your code to a version control system like Git, here's what I recommend:

- **NEVER PUSH YOUR CHANGES PUBLICALLY UNTIL THE LEADERBOARD IS FULL**. That is, never push your changes to a publically accessible repository until 100 or more people have solved part 2 of the problem.
- Don't bother committing your part 1 code right after you solve it - make a copy of your part 1 code, work on part 2, then commit everything once you're done with part 2.



# General advice

- Have fun! Going for the leaderboard is stressful but very fun. If you feel like you're not enjoying the experience, perhaps take it a bit slower - maybe even use AoC to learn a new programming language!
- Take a look at other people's code, posted on the subreddit after the leaderboard is full.
- Get involved with the community! There's an IRC channel on Freenode, ##adventofcode, and the subreddit is pretty active, /r/adventofcode.



# My code

All my Advent of Code code can be found in my [`adventofcode` GitHub repo](https://github.com/mcpower/adventofcode). Some comments:

- I barely had a template until 2017 day 5, which got refined and refined throughout the 2017 and 2018 events through to the version you see today.
- The `ints` (gets all integers from a string) function was used *a lot* - thanks again, mserrano! `fst` and `snd` (gets first and second items of input) were used surprisingly often.
- I have this huge comment on the top of my template. I barely used anything in it - the "to do" became second nature, the list of utility functions were pointless as I memorised them anyway. The notes about deque and dict methods did come in handy, though.
- In my `run_samples_and_actual` function, I have two separate lists for part 1 and part 2. However, most questions didn't give additional cases for part 2, so that was rarely used.
- My code is half-typed, half-untyped, mainly for autocomplete purposes. Using mypy during coding resulted in too many errors and was pretty distracting - making my programs type-check wasn't worth the hassle.
- Whenever I felt that some concept appeared more than once, I wrote a class / function for it and rewrote my previous solutions using that concept with the class / function. For example, [2018 day 12](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/2018/12/a-improved.py) and [2018 day 18](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/2018/18/a-improved.py)'s [repeating sequence](https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/utils.py#L54). I don't think I ever used that repeating sequence class after that, unfortunately.