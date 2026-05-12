from bible_cli.types import RawNumber, SuperScriptNumber
from bible_cli.constants import (
    DIGITS,
    SUPERSCRIPT_DIGITS,
)

def get_superscript_number(raw_number: RawNumber) -> SuperScriptNumber | RawNumber:
    translation_map = str.maketrans(
        DIGITS,
        SUPERSCRIPT_DIGITS
    )
    super_script: SuperScriptNumber = str(raw_number).translate(
        translation_map
    )
    
    if not super_script:
        return raw_number

    return super_script

