# File Preparation for SharePoint
## Project Summary
Migrate Job and Estimate files from sub office NTFS drives to consolidate into SharePoint using Python Scripts and SharePoint Migration Tool.
This was a real life work project!

## The Problem
- Corp office has a shared drive (the "P" drive, Windows Server 2012 physical server) that is running out of space. Most of the job and corp data is hosted here since this is the corp office.
 - SoCal office has a shared drive (the "Y" drive, Windows Server 2012 VM on Hyper-V) that is ok on space
 - Texas office has a shared drive (the "T" drive, Windows Server 2008 R2 physical server) that is ok on space, but the server hardware and software is outdated and ready to fail

These shares are accessible to the other offices via site-to-site VPN, but IT has to create these connections manually as needed. Permissions are nonexistent, and each drive is basically a free for all for any authenticated user. Each office saves data to their respective drive, but the offices commonly collaborate on projects (jobs) or legal cases, so the data is not readily accessible to the other offices. Duplicates were commonplace as files were typically shared over email then saved to the respective office drive. What a nightmare!
## The Solution
After looking around at file storage solutions, it was decided that the company would move all data to SharePoint. Since the company had already migrated email to Exchange Online and started rolling out Teams, it makes sense to keep everything in the same boat. 

SharePoint offers solutions for (I'm not endorsed by Microsoft):
- Unlimited Storage. SharePoint storage can be added at any time pay-as-you-go
- Central repository for files. Everyone works out of the same place!
- Anywhere access for internal employees. No need for VPN or access to other office drives
- Large file sharing. Individual files or whole folders can be shared internally/externally, and edit permission can be given if needed
- An opportunity for new permissions. Files can be structured into "Sites" and "Libraries" with independent permissions

It was easy to begin moving the Corp office files to SharePoint using the SharePoint Migration tool, but then what about the data from the other offices? I had to come up with a solution that would merge the data the best I could. Thankfully the SharePoint Migration tool (after some testing) could easily do this, but the folder names had to match to the point where I wanted them to be merged. See below for scripts used to prepare the data for migration.

## Remove Char.py
The estimate folders in the SoCal drive all started with "E" while the folders in the corp office just started with the estimate number. In order to begin merging the changes, at the very least the start of the folder name had to match.

## Rename.py
The first 6 characters in every job/estimate folder would be the job/estimate number which would match in every office. The description after the number may not match, so this program would look up the correct description from the corp office database (from names.csv, which is an export of the folder names) then rename the folder with the correct name. Now, the folder will merge properly in the SharePoint database.

## Move.py
Now the folder names match, but what about all the folders and data within that folder? How do we treat duplicate files? How do we determine which file is most up to date and has the correct data? No one has the time to go through all of them, so I wrote this to throw the files/folders into a folder within the job folder (if the path was "XXX Job Description/*", all of * would be moved to ""XXX Job Description/SoCal Y Drive/*). If something is missing in the future, users were instructed to go through that sub folder. This will prevent anything from being overwritten. This does create a massive amount of duplicates, but I don't want to overwrite a file revision we may need.
