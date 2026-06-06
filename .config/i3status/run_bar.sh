#!/bin/sh
# Feed i3status JSON into the weather wrapper for i3bar.
i3status | python3 "${HOME}/.config/i3status/wrapper.py"
