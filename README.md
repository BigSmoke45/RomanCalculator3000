# RomanCalculator3000

A console calculator for working with Roman numerals in the range I–MMM (1–3000), written in Python as an Object-Oriented Programming course project.

Supports bidirectional conversion between Roman and Arabic numeral systems, arithmetic operations, and comparisons — all implemented via operator overloading.

---

## Features

- Roman → Arabic conversion (`romanToInt`)
- Arabic → Roman conversion (`intToRoman`)
- Arithmetic: addition (`+`), subtraction (`−`)
- Comparisons: `>`, `>=`, `<`, `<=`, `==`, `!=`
- All operations are performed via Python **operator overloading** (`__add__`, `__sub__`, `__gt__`, etc.)
- Custom exception hierarchy for invalid input and out-of-range values
- Reference table of Roman numerals saved and loaded from `nums.json`
- Continuous input loop with graceful exit via the word `СТОП`

---

## Project structure

```
├── main.py           # Entry point, input loop, operation dispatch
├── RomanSystem.py    # RomanSystem class: conversion + all operator overloads
├── ArabSystem.py     # ArabSystem class: Arabic → Roman conversion
└── Exception.py      # Custom exceptions: MyError, Over3000, ZeroOrLess, ErrorNumber
```

---

## Custom exceptions

| Class | Triggered when |
|-------|----------------|
| `Over3000` | Either operand exceeds 3000 |
| `ZeroOrLess` | Subtraction result ≤ 0 |
| `ErrorNumber` | Invalid Roman numeral entered |
| `MyError` | Base class; also handles graceful exit |

---

## Example session

```
Введіть перше число у римській системі (від 1 до 3000): X
Введіть друге число у римській системі (від 1 до 3000): IV
1: >   2: >=   3: <   4: <=   5: ==   6: !=   7: +   8: -
Введіть номер операції: 7

Результат у римській системі:  X + IV = XIV
Результат в арабській системі: 10 + 4 = 14
```

---

## Tech Stack

`Python 3` · OOP · operator overloading · custom exceptions · JSON

---

## Run

```bash
python main.py
```

---

## Notes

University coursework project (OOP course). The focus was on class design, operator overloading mechanics, and building a proper exception hierarchy — not on UI or performance.
