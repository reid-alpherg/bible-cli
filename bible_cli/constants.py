import re
from bible_cli.database import Translation

SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"

DIGITS = "0123456789"

QUERY_PATTERN = re.compile(
    r"^(?P<book>.+?)\s+(?P<chapter>\d+):(?P<verse>\d+)(?:-(?P<end_verse>\d+))?$",
    re.IGNORECASE,
)

DEFAULT_TRANSLATION = Translation.ACF