#!/usr/bin/env python3
"""The Plumber's Inbox: A 120-Word Cold Email — make.fun entry (program/v1).

Writes the entry text to /output/entry.txt.
"""
import os

ENTRY = """Subject: Your paperwork, finished before your first job

Morning — I know the pattern: 6 a.m. start, emergency call-out by nine, invoices still waiting when you get home at eight. I take that pile off your hands. For $95 a month, I chase unpaid invoices, match every receipt, and send you one tidy number each Friday: what came in, what went out, what's owed. Even the supplier receipts stuffed in the glovebox get matched. I flag late payers early. No software to learn, no hourly billing. If it helps, I'll do your last month free, so you can see the Friday number before you pay a penny. Reply "yes" and I'll send one page to sign.

— Sam, ClearBooks Bookkeeping"""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)

if __name__ == "__main__":
    main()
