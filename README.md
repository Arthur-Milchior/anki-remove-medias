# Remove all medias from selected notes
## Rationale
Someone wanted to remove media from notes. Since it takes not even half an hour
to do it, I thought I'll help them.

## Configuration
You can decide to delete only images, only sound and videos, or both. 

## Technical
It's simple regexps searching for `<img` and `[sound:`. If someone tries to have
fun creating falty card which are not valid html, unexpected result may occur.

## TODO
### Sounds or videos
Separate option for sound and video (but it's hard to determine whether
something is a sound or video, so I won't do it unless there is a real need)

### Be efficient
Right now, it's a simple brute force. I could theoretically use regexp in sqlite
directly. I don't believe the time lost here is worth my time optimizing and
testing this add-on.

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU GPL, version 3 or later; http://www.gnu.org/licenses/gpl.html
Source in   | https://github.com/Arthur-Milchior/anki-
Addon number| [575171746](https://ankiweb.net/shared/info/575171746)
