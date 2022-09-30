from datetime import datetime, date

import pytz
from tzlocal import get_localzone_name


def ensure_localisation(dt, timezone=get_localzone_name()):
    """Insures localisation with provided timezone on "datetime" object.

    Does nothing to object of type "date"."""

    if isinstance(dt, datetime):
        tz = pytz.timezone(timezone)
        if dt.tzinfo is None:
            dt = tz.localize(dt)
        return dt
    elif isinstance(dt, date):
        return dt
    else:
        raise TypeError('"date" or "datetime" object expected, not {!r}.'.format(dt.__class__.__name__))
