# ✒️ Sublime Outliner Notes to HTML
Publish HTML pages using your regular tab indented notes.

Zero dependency publishing from the comfort of your code editor!

## Publish HTML

![Screenshot](https://user-images.githubusercontent.com/24665/169287961-c3ba086c-72d1-41df-a8b9-e37426957fba.png)


## Hierarchy aware notes!

````
All you have to do...
    Is create an indented hierarchy.
    Of your notes.
    In a list.
    It will become a nice HTML file.
        With a hierarchy based on indent levels.
            Isn't this convenient?
            Whitespace significant outliner style notes.
            Inspired by other cool outliners:
                Bike
                Dynalist
                Obsidian
                    Obsidian Publish
                Workflowy
                Roam Research
                Notion
                Standard Notes
                Evernote
            In Sublime Text (https://sublimetext.com)
Great plugin for
    Note taking.
    Outlining.
    Zero dependency publishing.

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

### Images with img

<img src="https://avatars.githubusercontent.com/u/24665" />

### Global and Local Links

http://github.com/gnat/sublime-outliner-html
(/local_links)

💬 Comments.

// I will not be in the HTML file.

🏗️ Comments to insert structural metadata.

//title I will be added to <html> ▶️ <head> ▶️ <title>
````

## Installation

`Preferences` ➡️ `Browse Packages ...` ➡️ [Download and extract the latest.](https://github.com/gnat/sublime-outliner-html/archive/refs/heads/main.zip)

## How to use

1. Select text you want to convert.
2. `CTRL+SHIFT+P` ➡️ `Outline to HTML`
3. The resulting HTML will open in a new tab.

Supported languages for [code blocks](https://prismjs.com/#supported-languages) powered by [Prism.js](https://prismjs.com).

## Roadmap

* Automatic table of contents.
* More metadata comments.

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

## Troubleshooting

* `View` ➡️ `Show Console`
* Manually invoke for development: `view.run_command('outline_to_html')`

## Special Thanks

* Harrison of [Indent.txt](https://github.com/Harrison-M/indent.txt) for the inspiration for such a plugin.
