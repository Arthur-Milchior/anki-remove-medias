from .addToBrowser import addToBrowser
from .config import getUserOption
from re import sub, IGNORECASE

def remove_media(browser):
    for nid in browser.selected_notes():
        note = browser.mw.col.get_note(nid)
        change = False
        for idx, field in enumerate(note.fields):
            original_field = field
            print(f"{original_field=}")
            if getUserOption("Remove images", True):
                field = sub("<\s*img[^>]+>", "", field, flags=IGNORECASE)
                print(f"{field=}")
            if getUserOption("Remove sounds and videos", True):
                field = sub("\[sound:[^]]+\]", "", field, flags=IGNORECASE)
                print(f"{field=}")
            if original_field != field:
                change = True
                note.fields[idx] = field
        if change:
            print("flush")
            note.flush()

addToBrowser(remove_media, "Remove medias")