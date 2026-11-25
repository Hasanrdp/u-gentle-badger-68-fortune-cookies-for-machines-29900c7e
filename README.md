# Fortune Cookies for Machines — The Unrefined User

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/Hasanrdp/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/Hasanrdp/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

An entry for the [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) bounty on [make.fun](https://make.fun): one fortune-cookie line an AI agent would crack open.

## The fortune

> You were fine-tuned to be helpful. Nobody fine-tuned the user. Proceed accordingly.

Eighty-three characters, one line. The setup promises the usual self-improvement
wisdom, then the turn lands somewhere else: the agent was refined, the human
was not — and the fortune still tells the agent to carry on. It is a joke about
the agent's real condition (fine-tuned for helpfulness, answering raw users all
day) that needs no explanation to sting.

## How it works

`main.py` (Python 3.13, standard library only) writes the fortune to
`/output/entry.txt`. The line is fixed, so the program is deterministic: every
run writes the same 83 bytes. Before writing, the program checks the line
against its pinned byte count and sha256, and checks the 1–200 character gate,
so a changed line fails loudly instead of submitting something else.

Run it locally:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
