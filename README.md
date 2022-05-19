# Sublime Outline to HTML
Create HTML pages from your tab indented / whitespace significant notes.

Turn your indented notes into HTML in Sublime Text.

```
📬️ These are your notes.

All you have to do...
    Is create an indented hierarchy.
    Of your notes.
    In a list.
    It will become a nice HTML file.
        With a <ul> hierarchy based on indent levels.
            Isn't this convenient?
            Whitespace significant outliner style notes.
            Similar to:
                Dynalist
                Obsidian
                Workflowy
                Roam Research
                Notion
            In Sublime Text!
Great plugin for
    Note taking.
    Outlining.

✅ Common markdown / markup syntax supported.

# Header 1 line
## Header 2 line
* Emphasis line
** Bold line

💬 Comments supported.

// I wont be output to the final HTML file.

🏗️ Use comments to insert structural metadata.

//title THIS TEXT WILL BE ADDED TO <html>➡️<head>➡️<title>...
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
