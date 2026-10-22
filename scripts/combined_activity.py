"""Render one contribution heatmap that sums several GitHub accounts.

Usage: GITHUB_TOKEN=... python scripts/combined_activity.py Dzzuy Dzuy123 > assets/activity.svg
"""
import datetime as dt
import json
import os
import sys
import urllib.request

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

# Tokyo Night palette, matching the other cards on the profile
BG, TEXT, MUTED = "#1a1b27", "#c0caf5", "#787c99"
LEVELS = ["#24283b", "#1e4d6b", "#2a6f97", "#38bdf8", "#7dd3fc"]

CELL, GAP = 11, 3
LEFT, TOP = 34, 58


def fetch_days(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise SystemExit(f"{login}: {body['errors']}")
    weeks = body["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return {d["date"]: d["contributionCount"] for w in weeks for d in w["contributionDays"]}


def level(count, peak):
    if count == 0:
        return 0
    return min(4, 1 + int(3 * count / max(peak, 1)))


def longest_streak(dates, totals):
    best = cur = 0
    for d in dates:
        cur = cur + 1 if totals[d] else 0
        best = max(best, cur)
    return best


def render(logins, totals):
    dates = sorted(totals)
    first = dt.date.fromisoformat(dates[0])
    start = first - dt.timedelta(days=(first.weekday() + 1) % 7)  # back up to Sunday
    peak = sorted(totals.values())[int(len(totals) * 0.95)] or 1

    cells, months, last_month, last_label_col = [], [], None, -9
    for d in dates:
        day = dt.date.fromisoformat(d)
        col, row = (day - start).days // 7, (day.weekday() + 1) % 7
        x, y = LEFT + col * (CELL + GAP), TOP + row * (CELL + GAP)
        cells.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{LEVELS[level(totals[d], peak)]}"><title>{d}: {totals[d]}</title></rect>'
        )
        if row == 0 and day.month != last_month:
            # skip a label that would collide with the previous one
            if col - last_label_col >= 3:
                months.append(f'<text x="{x}" y="{TOP - 8}" class="m">{day.strftime("%b")}</text>')
                last_label_col = col
            last_month = day.month

    ncols = (dt.date.fromisoformat(dates[-1]) - start).days // 7 + 1
    width = LEFT + ncols * (CELL + GAP) + 20
    height = TOP + 7 * (CELL + GAP) + 36
    total = sum(totals.values())
    active = sum(1 for v in totals.values() if v)
    legend_x = width - 20 - 5 * (CELL + GAP) - 70
    legend = "".join(
        f'<rect x="{legend_x + 34 + i * (CELL + GAP)}" y="{height - 26}" width="{CELL}" '
        f'height="{CELL}" rx="2" fill="{c}"/>'
        for i, c in enumerate(LEVELS)
    )
    days = "".join(
        f'<text x="6" y="{TOP + r * (CELL + GAP) + 9}" class="m">{n}</text>'
        for r, n in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
    )
    accounts = " + ".join(f"@{l}" for l in logins)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
  text {{ font-family: 'Segoe UI', Ubuntu, sans-serif; fill: {TEXT}; }}
  .t {{ font-size: 15px; font-weight: 600; fill: #38bdf8; }}
  .s {{ font-size: 12px; fill: {MUTED}; }}
  .m {{ font-size: 10px; fill: {MUTED}; }}
</style>
<rect width="100%" height="100%" rx="8" fill="{BG}"/>
<text x="20" y="26" class="t">{total:,} contributions in the last year</text>
<text x="{width - 20}" y="26" class="s" text-anchor="end">{accounts} · {active} active days · longest streak {longest_streak(dates, totals)} days</text>
{''.join(months)}{days}{''.join(cells)}
<text x="{legend_x}" y="{height - 16}" class="m">Less</text>{legend}
<text x="{legend_x + 34 + 5 * (CELL + GAP) + 4}" y="{height - 16}" class="m">More</text>
</svg>
"""


def main():
    logins = sys.argv[1:]
    token = os.environ["GITHUB_TOKEN"]
    totals = {}
    for login in logins:
        for date, count in fetch_days(login, token).items():
            totals[date] = totals.get(date, 0) + count
    sys.stdout.write(render(logins, totals))


if __name__ == "__main__":
    main()
