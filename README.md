fstring2fst
===

This is a tool to generate Formal State Transducers (FST) from python format strings.
The intended purpose is to create a language model for automatic speech recognition using rules instead of data.
The produced FST can be used as the grammar (G.fst) for the Kaldi toolkit to create a language model.


Another useful purpose for this tool is to generate random data, based on the desired rules, for an infinite or near infinite set of possibilities.
After including the rules for your grammar the script can produce any number of random samples from the defined language.

Example use case
---

Problem: We need to generate a random list of 7 digit phone number, the number can only start with 4, 5, 6, 7, 8 or 9.

Solution: 
We define the grammar like so:
```
VARIABLES = {
    "digit1": list(range(4,10)),
    "digit2": list(range(10)),
    "digit3": list(range(10)),
    "digit4": list(range(10)),
    "digit5": list(range(10)),
    "digit6": list(range(10)),
    "digit7": list(range(10)),
}
SENTENCES = {
    "phone_number": ["{digit1}{digit2}{digit3}-{digit4}{digit5}{digit6}{digit7}"],
}
OUTPUT = "phone_number"
```

Now we can create a FST and generate phone numbers by doing:
```
f, ist, ost = create_fst(VARIABLES, SENTENCES, OUTPUT)
generate(f)
```

results should be a list phone numbers respecting the grammar we provided.


Installation
---

Install using: 
```
    pip install .
```

For example usage look at `example.py`
