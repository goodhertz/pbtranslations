All files in `translatable` are translatable.

The value `1` is a special value that means the English string should be displayed even when the interface is translated into another language; i.e. `.ja(0)` means the Japanese version of the interface will display whatever the English text is.

The value `0` is a special value that means the string has not been translated. When you run the check code below, all `0`s will be flagged as untranslated. This means, in a code editor, if you open up this entire repository and run a search over it, if you search for the string `.ja(0)`, that will quickly show you all the strings that need to be translated into Japanese.

To run auto-checking:

```
python3.8 -m venv venv --prompt=pbt
source venv/bin/activate
pip install -e .
./check.py
```