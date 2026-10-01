# Pattern Log

Before starting a problem, read the Trigger column. If the problem is asking
one of these questions, you already know the tool.

---

## Arrays & Hashing

### 217 — Contains Duplicate
**Asks:** does any number appear twice?
**Tool:** set
**How:** walk the list. If the number is already in the set, return True.
Otherwise add it and keep going.
**Why a set:** you only need yes/no, not counts. Checking `in` on a set is
instant; on a list it's slow.
**O(n)**

---

### 242 — Valid Anagram
**Asks:** same letters, same counts?
**Tool:** two dicts
**How:** count every character of each string into its own dict, then compare
the dicts with `==`.
**Key line:** `count[c] = count.get(c, 0) + 1`
`.get(c, 0)` returns 0 when the letter hasn't been seen yet, so the `+ 1` has
something to add to. Without it, reading a missing key crashes.
**Why dicts compare cleanly:** dict `==` ignores insertion order, so you don't
need to sort anything.
**O(n)**

---

### 1 — Two Sum
**Asks:** which two numbers add up to the target?
**Tool:** dict storing value → index
**How:** one pass. At each number, work out `diff = target - n`. If `diff` is
already in the dict, you've found the pair. If not, store this number and move on.
**Key line:** `prevmap[n] = i`
The number is the key because you search *for a number*. Only keys get instant
lookup.
**Order matters:** check first, store second. Store first and `[3,3]` matches
itself and returns `[0,0]`.
**O(n)**

---

### 49 — Group Anagrams
**Asks:** which words belong together?
**Tool:** dict where each value is a list
**How:** for each word, build a fingerprint with `"".join(sorted(word))`.
Anagrams produce the same fingerprint, so they land in the same bucket.
Return `list(res.values())` to drop the fingerprints.
**Key lines:**
```python
if key not in res: res[key] = []
res[key].append(word)
```
The `if` creates the empty list; `append` adds to it. Writing `key = []`
instead of `res[key] = []` is the bug to watch for.
**Why join:** `sorted()` returns a list, and lists can't be dict keys.
**O(n·m log m)** — m is word length
**If asked to do better:** use a 26-slot letter count as the key instead of
sorting → O(n·m)

---

### 347 — Top K Frequent
**Asks:** which k numbers appear most often?
**Tool:** count dict, then sort by count
**How:** count into a dict, sort the pairs by count descending, take the first k,
pull the numbers out.
**Key line:** `sorted(rev.items(), key=lambda x: x[1], reverse=True)[:k]`
- `.items()` gives `(number, count)` pairs
- `key=lambda x: x[1]` sorts by the count instead of the number
- `reverse=True` puts the biggest first
- `[:k]` takes the first k
**O(n log n)** — the sort is the slow part
**Better, not written yet:** bucket sort. Make a list where index = count, put
each number at its count's index, walk backwards until you have k. O(n).

---

## Syntax I keep getting wrong

| Wrong | Right | Why |
|---|---|---|
| `count = count.get(c,0)+1` | `count[c] = count.get(c,0)+1` | brackets on the left = store in the dict |
| `key = []` | `res[key] = []` | same thing — plain `=` just renames a variable |
| `nums[n]` inside `enumerate` | `n` | enumerate already gave you the value |
| `return list[i, j]` | `return [i, j]` | `()` calls, `[]` indexes |
| `sorted(x: key=...)` | `sorted(x, key=...)` | arguments take commas |
| `len(set(nums)) == len(nums)` | `< len(nums)` | `==` means NO duplicates |

---

## Rules of thumb

- **Set** when you only need *did I see it*
- **Dict** when you need *how many* or *where*
- Whatever you search for goes in the **key** slot — only keys are fast
- O(n²) usually means there's a dict solution hiding
- `enumerate` when you need both index and value; plain `for x in list` otherwise

---

## Re-solve

- [ ] Oct 4 — 217, 242, 1, 49, 347
- [ ] Oct 15 — same
