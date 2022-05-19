# ✒️ Sublime Outliner Notes to HTML
Create HTML pages from your indented / whitespace significant notes.

All from the comfort of Sublime Text!

## Publish HTML

![Screenshot](https://user-images.githubusercontent.com/24665/169255835-c632616a-b8e6-42df-91b3-0ac4e9100477.png)

## From your whitespace significant notes!

````
All you have to do...
    Is create an indented hierarchy.
    Of your notes.
    In a list.
    It will become a nice HTML file.
        With a hierarchy based on indent levels.
            Isn't this convenient?
            Whitespace significant outliner style notes.
            Similar to:
                Bike
                Dynalist
                Obsidian
                Workflowy
                Roam Research
                Notion
            In Sublime Text!
Great plugin for
    Note taking.
    Outlining.

🚧 Code blocks!

```javascript
document.addEventListener("click", ev => {
    alert("You selected the following element: " + ev.target)
})
```

✅ Common markdown / markup syntax.

# Header 1 line
## Header 2 line
* Emphasis line
** Bold line

💬 Comments.

// I will not be in the HTML file.

🏗️ Comments for structural metadata.

//title I will be added to <html> ▶️ <head> ▶️ <title>
````

## Installation

`Preferences` ➡️ `Browse Packages ...` ➡️ `cd User` ➡️ [Download and extract the latest.](https://github.com/gnat/sublime-outliner-html/archive/refs/heads/main.zip)

## How to use

1. Select text you want to convert.
2. `CTRL+SHIFT+P` ➡️ `Outline to HTML`
3. The resulting HTML will open in a new tab.

Manually invoke for development: `view.run_command('outline_to_html')`

Supported languages for [code blocks](https://prismjs.com/#supported-languages) powered by [Prism.js](https://prismjs.com).

## Roadmap

* Automatic table of contents.
* More metadata comments.

## Special Thanks

* Harrison of [Indent.txt](https://github.com/Harrison-M/indent.txt) for the inspiration for such a plugin.

## Suggested Sublime Color Schemes

* [Invader Zim](https://github.com/gnat/sublime-invader-zim) 🛸

## Other Cool Outliners / Bullet Point Note Software

* [Bike](https://www.hogbaysoftware.com/bike/)
* [Dynalist](https://dynalist.io/)
* [Obsidian Publish](https://obsidian.md/publish)
* [Workflowy](https://workflowy.com/)
* [Roam Research](https://roamresearch.com/)
* [Notion](https://www.notion.so/)
* [Standard Notes](https://standardnotes.com/)
* [Evernote](https://www.evernote.com/)
