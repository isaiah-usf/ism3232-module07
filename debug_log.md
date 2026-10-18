debug_log.md template
# debug_log.md
# Author: Isaiah Martin

## Bug 1
Error type: KeyError 'amount'
File + line: week8_buggy
What the error means: It means it tried to call to a term that isn't defined. I think it's because of the typo in amount up top.
What I told the duck: Basically the above? I need to check though because I'm not confident I have any idea what I'm talking about
What I tried: I added the missing letter
How I fixed it: Okay fixing the typo for 'amount' as amout up in the top of the file worked.

## Bug 2
Error type: TypeError '>' not supported between instances of 'int' and 'str'
File + line: File "/home/isaiah/ism3232/module05_functions/week8_buggy.py", line 16, in is_over_limit
What the error means: It means it is unable to compare two different types of terms, in this case an integer and a string. I need to figure out why.
How I fixed it: I noticed in line 16 amount wasn't in apostrophes so I figured that meant python probably interpreted it as literally the word amount rather than 'amount' which is a variable it can translate into a number to compare to 1500. I added the '' around it, it turned blue, it works now. Just kidding, it doesn't really work. I actually accidentally made them both into strings which caused the pytest to fail, so i removed the '' around both and NOW that works. Essentially one was right and one was wrong and I made them both wrong initially and tricked myself into thinking it was working. It did give me the correct output with them both broken, but the pytests were still failing but I think it's all good now.

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes / No
no, then yes. see above.

## AI Literacy Reflection
Did I use AI? -  No
If yes -- exact prompt I used: n/a
What AI explained: n/a
What I changed myself: everything
Can I explain every fixed line? Yeso

## What I learned
I learned that in the moment it's really easy to get confused by even very simple elements. It's kind of like checking an email for typos, it can be hard to spot them. I can definitely see how using AI could be helpful but to continue the metaphor, spellcheck is no substitute for being literate.