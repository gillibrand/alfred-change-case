# Change Case — Workflow for Alfred

Changes the case of text selected, provided, or on the clipboard to UPPERCASE, lowercase, Title Case, CamelCase, kebab-case, or snake_case. Now works with diacritics.

[Download the workflow](https://github.com/bpetrynski/alfred-change-case/releases/).

Python 3 is required, [install it before use](https://installpython3.com/mac/).

![Screenshot](changecase.png)

## Usage

Change the case of text on the keyboard with the keyword `case`. All six styles are previewed as Alfred results. Select one to copy it to the clipboard and paste into in the current application.

Optionally, any text typed after `case` will be changed instead of the clipboard.

## Version History

### 4/8/2021
- Support for diacritics by changing interpreter from Python 2 to Python 3.

### 9/9/2018

- Added CamelCase, kebab-case, and snake_case options
- Added additional keywords "tt" and "transform"

### 4/19/2013

- Always sorts the case styles in the same order now: lowercase, uppercase, then title case. (Removed the `uid` from results returned to Alfred as supported in Alfred 2.0.3.)

### 4/6/2013

- Title case will now leave common acronyms as uppercase (HTML, XML, etc.).

## Credits

- Workflow by Jay Gillibrand.
- `titlecase` module by [Stuart Colville](http://muffinresearch.co.uk).
- `CamelCase`, `kebab-case`, and `snake_case` additions added by [Ben Wagner](https://blizzrdof77.com)
