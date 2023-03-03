#Enum Evolution

RULES
  - No changing the symbol/name  pairing 
  - No removing any pairs
  - Can add new symbol/name pairs


EXAMPLE RE RULE 1

Feb 19th:

Jessica
  11:12 AM

I just updated the telemetry names again (in gridworks-protocol and also scada). I didn't like the first names I picked for flow, so I did the thing we want to outlaw of replacing a name already in an enum (WATER_FLOW_GPM_TIMES100 is now gone, replaced by GPM_TIMES100 ... since for example the fluid sometimes has anti-freeze in it).  I also got rid of GALLONS_PER_MINUTE_TIMES10 which I don't think we will ever use since we have 100, and added GALLONS_TIMES100.  This means I will need to update the systems all at the same time or there will be breaking. I've looked at all the other symbols in that enum and am prepared to live with them .... so I guess I am ready to have this be the last time I take a symbol out of an enum.


Andrew
March 3

gwd events show on ubuntu machine and on my local machine show different units (Gx100 vs GPMx10) on the same snapshot enum uid, because the ubuntu machine has a newer version of gwproto in the gwd install.

The newer version of gwproto changed the text of the enum without changing its ID.

So this is an interesting phenomenon.
11:40
Our gwproto is now installed in something like 12 places. So we are already at the point that we have devices communicating with different versions, and probably too many to keep track of. Those 12 places are:
Andy’s Mac, 4 envs: gwproto-dev, scada-dev, gwd-pipx, gwd-dev
Jess’ Mac, 3envs:  : gwproto-dev, scada-dev, gwd-pipx
Ubuntu, 2 envs:  scada-dev, gwd-pipx
Pis, 3 envs: apple, orange, almond.

 This means I will need to update the systems all at the same time or there will be breaking
Nice!




12:32
We can add new symbol/name pairs but  we cannot  change that pairing and we cannot remove any pairs.
Nice!
12:33
Why didn’t you add a new one, just out of curiousity.


Jessica
  12:40 PM
Naive answer: I really didn’t like  . Gracious non-naive answer: I wanted to really experience why we want those rules. Ungracious answer: some perverse part of me likes to break things to point out we need more rules (like a schema registry that enforces the above rules)


Andrew Schweitzer
  12:42 PM
hahaha
12:44
I mean it cost you ~ $100
12:45
But it’s probably a useless and relatively harmless example specific to out case of what can go wrong, so that’s good to share.