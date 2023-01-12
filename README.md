# ✒️ Sublime Outline Notes Publisher
Publish HTML pages using tab indented notes or markdown (md)! It's Obsidian in Sublime Text. 🔥

Zero dependency publishing from the comfort of your code editor.

Perfect for:

* Note takers who love using tab indentation / whitespace for organization.
* Static site generator for personal sites, blogs, micro wiki.
* Zettelkasten
* Replacing your outliner with Sublime Text.
  * What is an [Outliner](https://en.wikipedia.org/wiki/Outliner)?

<a href="https://github.com/gnat/sublime-outline-notes-publisher/tags">
    <img src="https://img.shields.io/github/v/tag/gnat/sublime-outline-notes-publisher?label=release&style=for-the-badge&color=%230288D1" /></a>
<a href="https://packagecontrol.io/packages/Outline%20Notes%20Publisher">
    <img src="https://img.shields.io/packagecontrol/dt/Outline%20Notes%20Publisher?style=for-the-badge&color=%2315b713" /></a>
<a href="https://www.sublimetext.com/">
    <img src="https://img.shields.io/badge/Only%20For-Sublime-ff9800?logo=sublime%20text&style=for-the-badge" /></a>

## Publish HTML Pages ...

![Screenshot](https://user-images.githubusercontent.com/24665/169327275-2b53060d-22ce-40b5-90d1-10c5399d81c2.png)

## Using your hierarchy aware notes!

````
All you have to do...
    Is create an indented hierarchy.
    Of your notes.
    In a list.
    It will create a nice HTML file...
        With a hierarchy based on indent levels.
            Isn't this convenient?
            Whitespace significant outliner style notes!
            Other cool outliners:
                [Bike](https://news.ycombinator.com/item?id=31409077)
                Dynalist
                [Obsidian](https://obsidian.md)
                    [Obsidian Publish](https://obsidian.md/publish)
                Workflowy
                Roam Research
                Notion
                Standard Notes
                Evernote
                    Ever-who? 🐘
            Only for:
                Sublime Text (https://sublimetext.com)
                Super Nintendo
🔥 Great plugin for
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

<img src="https://avatars.githubusercontent.com/u/24665" style="max-width: 200px" />

### Global and Local Links. Plain, named and pure HTML links.

http://github.com/gnat/sublime-outliner-html
🔗 [Local named link!](/local_link) 🌐 [Global named Link!](http://google.com) https://google.com <a href="https://google.com">Pure HTML link!</a>

💬 Comments.

// I will not be in the HTML file.

🏗️ Comments to insert structural metadata.

//title I will be added to <html> ▶️ <head> ▶️ <title>
````

## Installation

Option A: `Preferences` ➡️ `Package Control` ➡️ `Install Package` ➡️ `Outline to HTML` ➡️ ENTER

Option B (Direct): `Preferences` ➡️ `Browse Packages ...` ➡️ [Download and extract the latest.](https://github.com/gnat/sublime-outline-notes-publisher/archive/refs/heads/main.zip)


## How to use

1. Select text you want to convert.
2. `CTRL+SHIFT+P` ➡️ `Outline to HTML`
3. The resulting HTML will open in a new tab.

Supported languages for [code blocks](https://prismjs.com/#supported-languages) powered by [Prism.js](https://prismjs.com).

## Global Configuration (Optional)

Configure using Preferences ➡ Settings

```js
{
    // ...
    "outline_to_html": {
        // "css": "", // Override CSS.
        // "title": "", // Override Title (or use meta comment //title ...)
        // "header": "", // Add to <head>
        // "body": "", // Add to <body>
        // "footer": "", // Add before </body>
    }
}
```

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
