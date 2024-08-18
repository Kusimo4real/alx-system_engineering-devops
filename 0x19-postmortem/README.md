POSTMORTEM

Issue Summary(that is often what executives will read) must contain:
1. duration of the outage with start and end times(including timezone)
2. what was the impact(what service was down/slow? What were user experiencing? How many % of the users were affected?)
3. what was the root cause

Timelin(format bullet point, format: time-keep it short, 1 or 2 sentences) must contain:

1. when was the issue detected
2. how was the issue detected(monitoring alert, an engineer noticed something, a customer complained..)
3. actions take (what parts of the system were investigated, what were the assumption on the root cause of the issue)
4. misleading investigation/debugging paths that were taken
5. which team/individuals was the incident escalated to 
6. how the incident was resolved

Root cause and resolution must contain:
1. explain in detail what was causing the issue
2. explain in detail how the issue was fixed

Corrective and preventive measures must contain:
1. what are the things that can be improved.fixed (broadly/speaking)
2. a list of tasks to address the isue( be very specific, like a TODO, example: patch Nginx serverm add monitoring on server memory...)
3. Be brief and straight to the point, between 400 to 600 words


