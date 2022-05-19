import sublime, sublime_plugin
import re

INDENT_TABS = '\t'     # One tab is typical.
INDENT_SPACES = '    ' # If you use something other than 4 spaces.
WS = INDENT_TABS       # Whitespace.

class OutlineToHtml(sublime_plugin.TextCommand):
	def run(self, edit):
		parser = OutlineToHtmlCreator()

		# Get current selection
		sels = self.view.sel()
		selsParsed = 0
		if(len(sels) > 0):
			for sel in sels:
				# Make sure selection isn't just a cursor
				if(abs(sel.b - sel.a) > 0):
					self.fromRegion(parser, sel, edit)
					selsParsed += 1

		# All selections just cursor marks?
		if(selsParsed == 0):
			region = sublime.Region(0, self.view.size() - 1)
			self.fromRegion(parser, region, edit)

	def fromRegion(self, parser, region, edit):
		lines = self.view.line(region)
		text = self.view.substr(lines)
		indented = parser.fromSelection(text)
		newview = self.view.window().new_file()
		newview.insert(edit, 0, indented)

class OutlineToHtmlCreator:
	"""
	def fromFile(self, filename):
		# TODO: Unused currently.
		inputFile = open(filename, "rU")
		output = self.create(inputFile)
		inputFile.close()
		return output
	"""

	def fromSelection(self, text):
		return self.create(text.split("\n"))

	def tagify(self, text, token, token_end, formatter, remove_token=False):
		pos = 0
		found = True
		while found:
			found = False
			''' Attempt to convert tokens into tags. '''
			if (pos := text.find(token, pos)) >= 0:
				found = True
				url = ''
				url_name = ''
				url_end = 0
				token_remove = len(token)
				# Bail if this token is inside a quote (ex: HTML tag attribute)
				if text[pos-1] == '"' or text[pos-1] == "'":
					pos = pos+1
					continue
				# Bail if this ")[" token does not have supporting "[" or ")"
				if token == "](":
					if text.find('[', 0, pos) == -1 or text.find(')', pos) == -1:
						return text
				# Extract name.
				if token == "](":
					url_name = text[text.find('[', 0, pos)+1:pos]
				# Extract URL
				partial = text[pos:]
				for i,c in enumerate(partial):
					if c.isspace() or c == token_end: # Will end at whitespace or token_end
						url_end = pos+i
						break
				if not url_end: # We reached EOL
					url_end = len(text)
				url = text[pos+token_remove:url_end]
				if token == "](": # Special case.
					text = text[:text.find('[', 0, pos)] + formatter.format(url, url_name) + text[url_end+len(token_end):]
				else:
					text = text[:pos] + formatter.format(url, url_name) + text[url_end:]
		return text

	def create(self, textIterable):
		indentLevelPrevious = 0
		insideCodeBlock = False
		output = ""

		HTML_TITLE = "Hello World"
		HTML_STYLES = """
		body { font-size: 1em; font-family: "sans"; background: #222; color: #aaa; padding: 2rem 2.4rem; }
		ul { list-style-type: circle; }
		a { color: white; }
		"""
		HTML_WS = f"\n{WS*2}"

		# Compile whitespace regex for reuse.
		regexIndent = re.compile(f"^({INDENT_TABS}|{INDENT_SPACES})")

		# Parse text
		for line in textIterable:

			# ```lang Code block.
			if(insideCodeBlock or line.find("```") == 0):
				if not insideCodeBlock and line.find("```") == 0:
					if line == "```\n":
						language = 'html'
					else:
						line = line.replace("```", "")
						language = line.split("\n")[0]
					output += f"<pre><code class='language-{language}'>"
					insideCodeBlock = True
					continue
				# End of code block.
				elif insideCodeBlock and line.find("```") == 0:
					line = line.replace("```", "")
					output += f"{line}</code></pre>"
					insideCodeBlock = False
					continue
				else:
					# Inside code block.
					output += f"{line}\n"
					continue

			# // Metadata comments.
			if(line.find("//title ") == 0):
				line = line.replace("//title ", "")
				HTML_TITLE = line
				continue

			# // Comments.
			if(line.find("//") == 0):
				continue # Skip line.

			# Levels of indentation
			indentLevel = 0

			while(regexIndent.match(line)):
				line = regexIndent.sub("", line)
				indentLevel += 1

			indentDiff = indentLevel - indentLevelPrevious

			# Does a new level of indentation need to be created?
			if(indentDiff >= 1):
				output += f"{HTML_WS}{WS*(indentLevel-1)}<ul>"
				'''
				if indentLevel > 1:
					output += f"{HTML_WS}{WS*(indentLevel-1)}<li><ul>"
				else:
					output += f"{HTML_WS}{WS*(indentLevel-1)}<ul>"
				'''
			# Outdent
			elif(indentDiff <= -1):
				outdentLevel = abs(indentDiff)
				for i in range(outdentLevel):
					output += f"{HTML_WS}{WS*(indentLevel+outdentLevel-i-1)}</ul>"
					'''
					if indentLevel+outdentLevel-i > 1:
						output += f"{HTML_WS}{WS*(indentLevel+outdentLevel-i-1)}</ul></li>"
					else:
						output += f"{HTML_WS}{WS*(indentLevel+outdentLevel-i-1)}</ul>"
					'''

			# Special format line.
			prefix = ""
			suffix = ""
			line = line.strip()

			special = {
				"# ": "h1",
				"## ": "h2",
				"### ": "h3",
				"#### ": "h4",
				"##### ": "h5",
				"###### ": "h6",
				"** ": "strong",
				"* ": "em",
			}

			for key,value in special.items():
				if line.startswith(key):
					line = line.replace(key, "")
					prefix = f"<{value}>"
					suffix = f"</{value}>"

			line = self.tagify(line, "](", ')', '<a href="{0}">{1}</a>', remove_token=True) # Named link.
			line = self.tagify(line, "https://", ')', '<a href="https://{0}">{0}</a>')
			line = self.tagify(line, "http://", ')', '<a href="http://{0}">{0}</a>')


			if indentLevel > 0:
				output += f"{HTML_WS}{WS*(indentLevel)}" + "<li>" + prefix + line + suffix + "</li>"
			elif prefix in ['<strong>', '<em>']:
				output += f"{HTML_WS}{WS*(indentLevel)}" + prefix + line + suffix + "<br />"
			elif prefix:
				output += f"{HTML_WS}{WS*(indentLevel)}" + prefix + line + suffix
			else:
				output += f"{HTML_WS}{WS*(indentLevel)}" + prefix + line + suffix + "<br />" # Plain text.

			indentLevelPrevious = indentLevel

		HTML_HEADER = f"""<!doctype html>
<html lang='en'>
	<head>
		<title>{HTML_TITLE}</title>
		<style>{HTML_STYLES}</style>
		<link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.28.0/themes/prism-twilight.min.css" rel="stylesheet" />
	</head>
	<body>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.28.0/components/prism-core.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.28.0/plugins/autoloader/prism-autoloader.min.js"></script>
"""

		HTML_FOOTER = f"""
	</body>
</html>
"""
		return f"{HTML_HEADER}{output}{HTML_FOOTER}"
