# Change Case — Workflow for Alfred

Changes the case of text selected, provided, or on the clipboard to UPPERCASE, lowercase, Title Case, CamelCase, kebab-case, or snake_case.

[Download the workflow](https://github.com/gillibrand/alfred-change-case/blob/master/Change%20Case.alfredworkflow).

![Screenshot](changecase.png)

## Usage

Change the case of text on the keyboard with the keyword `case`. All six styles are previewed as Alfred results. Select one to copy it to the clipboard and paste into in the current application.

Optionally, any text typed after `case` will be changed instead of the clipboard.

Manage the keybinding (set to `Cmd+Opt+Ctrl+Shift+t` by default) to transform the currently selected text.

## Version History

### 9/9/2018

- Updated icons and added additional cases to match original style 👍
- Added CamelCase, kebab-case, and snake_case to icons.acorn layered file

### 8/21/2018

- Added CamelCase, kebab-case, and snake_case options
- Updated/Removed Icons
- Added keybinding for text selection transformation
- Added additional keywords "tt" and "transform" to default workflow options

### 4/19/2013

- Always sorts the case styles in the same order now: lowercase, uppercase, then title case. (Removed the `uid` from results returned to Alfred as supported in Alfred 2.0.3.)

### 4/6/2013

- Title case will now leave common acronyms as uppercase (HTML, XML, etc.).

## Credits

- Workflow by Jay Gillibrand.
- `titlecase` module by [Stuart Colville](http://muffinresearch.co.uk).
- `CamelCase`, `kebab-case`, and `snake_case` additions added by [Ben Wagner](https://blizzrdof77.com)
