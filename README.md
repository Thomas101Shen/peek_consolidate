# Peek Consolidate

This is a Python utility designed to inspect, merge, and align multi-timeframe financial datasets — such as minute-level intraday breakouts with daily ATR values — into a clean master research file.

---

## Features

- Preview CSVs before merging (see structure, head, tail)
- Merge similar-format CSVs into one master file
- Join interday and intraday datasets on `Time`
- Includes example data to test functionality
- CLI-style menu for ease of use

---

## Directory Layout

```
├── example_prices/        # Intraday data samples
├── example_atr/           # Daily ATR samples
├── master_merge/          # Folder created during merge steps
├── main.py                # Program entry point
```

---

## Sample Usage

1. Run the program:
```bash
python main.py
```

2. Choose:
- `A`: Preview contents of a folder
- `B`: Merge CSVs with similar structure → `master_merge/*_master.csv`, drops rows with duplicate `Time` (refer to Warnings & Considerations)
- `C`: Merge by "Time" column into `master.csv`
- `D`: Exit

3. Example walkthrough:
```bash
> A
Enter directory: example_prices

> A
Enter directory: example_atr

> B
Enter directory: example_prices
> B
Enter directory: example_atr

> C
Enter directory: master_merge
```

4. You will now see a merged `master.csv` in your current working directory.

---

## Warnings & Considerations

- Option C **preserves NaN values** to avoid implicit bias. Use `dropna()` as needed.
- Merge direction (left vs right) defaults based on row count — may introduce inconsistencies in edge cases.
- Primary key is `Time` and is assumed to be in standard datetime format.
- When merging "different" together, the program will prefix the filename to whatever column it is adding. If there is an `_` in the filename, it will prefix the characters preceding the first `_`
- Feedback on merging logic (e.g., timestamp tolerance) is welcome.

---

## Dependencies

- `pandas`
- Python 3.6+

Install as needed:
```bash
pip install pandas
```

---

## Feedback

If you work with multi-timeframe datasets or have opinions on safe joins for intraday/interday structures, your input would be appreciated.

Pull requests, suggestions, or performance optimizations welcome.
