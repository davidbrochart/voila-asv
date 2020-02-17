# voila-asv
[asv](https://asv.readthedocs.io)-powered performance regression for [Voila](https://voila.readthedocs.io).

In order to benchmark all commits since e.g. the first release:
```
asv run 0.0.1..master --quick --show-stderr
```
