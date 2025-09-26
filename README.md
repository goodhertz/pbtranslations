All files in `translatable` are translatable.

The value `1` is a special value that means the English string should be displayed even when the interface is translated into another language; i.e. `.ja(1)` means the Japanese version of the interface will display whatever the English text is.

The value `0` is a special value that means the string has not been translated. This means, in a code editor, if you open up this entire repository and run a find-all, if you search for the string `.ja(0)`, that will quickly show you all the strings that need to be translated into Japanese.

### Previewing translations in the interface

![](viewer-screenshot.png)

`pbtranslations` includes a Python program that can display a text-only, interactive version of the plugin interfaces that pulls translations directly from the code (so if you launch the viewer and then save a change in a translation file, that change will automatically appear in the viewer).

To run the viewer, you'll need `uv`.

```bash
git clone https://github.com/goodhertz/pbtranslations.git
cd pbtranslations
uv run noto.py # to download fonts (only needs to be done once)
uv run ct view.py 1
```

After a moment, a window should appear showing the English version of CanOpener (aka catalog #1). To cycle through available languages, use the left or right arrow key. To cycle through plugins, hit `Shift+v`.

The command also accepts optional arguments for specifying catalog and language, in that order:

```
uv run ct view.py 2 ja
```

This will open Vulf Compressor in Japanese. The arrow keys will work as they do in the no-argument mode.

The catalogs are listed with their corresponding plugin names and translation file paths in the LOOKUP.md file in this repo, and the language abbreviations are listed here (and will appear in the top-bar of the viewer when a given language is selected).

```
en English
es Spanish
pt Portuguese
fr French
it Italian
ja Japanese
ko Korean
zh-Hans Chinese (Simplified)
zh-Hant Chinese (Traditional)
ar Arabic
```

#### Colors

- __Green__ == a clump label
- __Blue__ == a parameter label
- __Purple__ == a control value
- __Pink__ == a string that cannot/should not be translated (untranslatable)
- __Orange__ == a multi-value control (see below)

#### Multi-value controls

Because some translatable strings are not shown in the interfaces in their default state, if you click on a string in an orange box in the viewer, that will cycle through the available values for that multi-value control. (If there is no orange box, all the translatable strings are visible in the viewer.)

#### Note on aesthetics

If you think to yourself when you open the viewer `dang this is ugly`, don't fret! That's intentional — the viewer is meant to display translated strings in their correct location in the interface, not to closely mimic how the eventual plugin will actually look in terms of typography, i.e. font choice. (We can't distribute the actual fonts we use in the plugins, so the Noto open-source family is the next best thing.)