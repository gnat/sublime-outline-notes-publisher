# Sublime Outline to HTML
Create HTML pages from your tab indented / whitespace significant notes.

Turn your indented notes into HTML in Sublime Text.

```
All you have to do...
    Is create an indented hierarchy.
    Of your notes.
    In a list.
    It will become a nice HTML file.
        With a ul hierarchy based on indent levels.
        * And simple.
        ** formatting.
        //This line will be left out of the HTML file.
        //title Hello World
        Special comments will be inserted as page metadata.
Great plugin for:
    Note taking.
    Outlining.
```

## Installation

`Preferences` ➡️ `Browse Packages ...` ➡️ `cd User` ➡️ [Download and extract the latest.](https://github.com/gnat/sublime-outliner-html/archive/refs/heads/main.zip)

## How to use

1. Select text you want to convert.
2. `CTRL+SHIFT+P` ➡️ `Outline to HTML`
3. The resulting HTML will open in a new tab.

Manually invoke for development: `view.run_command('outline_to_html')`

## Formatting

We borrow just a few very common non-whitespace things from Markdown.

* `*` will wrap the item in an `<em>` tag.
* `**` will wrap the item in a `<strong>` tag.
* `//` indicates a comment, excluding the line from the results.
* `//title Sample Title` to add a page title.

## Roadmap

* Automatic table of contents.
* More metadata comments.

## Special Thanks

* Harrison of [Indent.txt](https://github.com/Harrison-M/indent.txt) for the inspiration for such a plugin which I hope to improve upon and make available to people who want to edit and publish their notes in Sublime Text.

### Suggested Sublime Color Schemes

* [Invader Zim](https://github.com/gnat/sublime-invader-zim) 🛸
