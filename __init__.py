import sublime, sublime_plugin
import re

HTML_TITLE = "Hello World" # Replace using //title New Title
HTML_STYLES = """
body { font-size: 1em; font-family: "sans"; background: #222; color: #aaa; padding: 2rem 2.4rem; }
ul { list-style-type: circle; }
a { color: white; }
"""

INDENT_TABS = '\t'     # One tab is typical.
INDENT_SPACES = '    ' # If you use something other than 4 spaces.
WS = INDENT_TABS       # Whitespace.
HTML_WS = f"\n{WS*2}"

class OutlineToHtml(sublime_plugin.TextCommand):
	def run(self, edit):
		parser = OutlineToHtmlCreator()

		# Get current selection
		sels = self.view.sel()
		sels_parsed = 0
		if(len(sels) > 0):
			for sel in sels:
				# Make sure selection isn't just a cursor
				if(abs(sel.b - sel.a) > 0):
					self.fromRegion(parser, sel, edit)
					sels_parsed += 1

		# All selections just cursor marks?
		if(sels_parsed == 0):
			region = sublime.Region(0, self.view.size() - 1)
			self.fromRegion(parser, region, edit)

	def fromRegion(self, parser, region, edit):
		lines = self.view.line(region)
		text = self.view.substr(lines)
		indented = parser.fromSelection(text)
		newview = self.view.window().new_file()
		newview.insert(edit, 0, indented)

class OutlineToHtmlCreator:
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

	def create(self, text_iterable):
		indent_level_previous = 0
		inside_code_block = False
		output = ""

		global HTML_TITLE, HTML_STYLES, HTML_WS, INDENT_TABS, INDENT_SPACES, WS

		# Compile whitespace regex for reuse.
		regex_indent = re.compile(f"^({INDENT_TABS}|{INDENT_SPACES})")

		# Parse text
		for line in text_iterable:

			# ```lang Code block.
			if(inside_code_block or line.find("```") == 0):
				if not inside_code_block and line.find("```") == 0:
					if line == "```\n":
						language = 'html'
					else:
						line = line.replace("```", "")
						language = line.split("\n")[0]
					output += f"<pre><code class='language-{language}'>"
					inside_code_block = True
					continue
				# End of code block.
				elif inside_code_block and line.find("```") == 0:
					line = line.replace("```", "")
					output += f"{line}</code></pre>"
					inside_code_block = False
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
			indent_level = 0

			while(regex_indent.match(line)):
				line = regex_indent.sub("", line)
				indent_level += 1

			indentDiff = indent_level - indent_level_previous

			# Does a new level of indentation need to be created?
			if(indentDiff >= 1):
				output += f"{HTML_WS}{WS*(indent_level-1)}<ul>"
				'''
				# W3C compliant, but UGLY. Leave for now.
				if indent_level > 1:
					output += f"{HTML_WS}{WS*(indent_level-1)}<li><ul>"
				else:
					output += f"{HTML_WS}{WS*(indent_level-1)}<ul>"
				'''
			# Outdent
			elif(indentDiff <= -1):
				outdent_level = abs(indentDiff)
				for i in range(outdent_level):
					output += f"{HTML_WS}{WS*(indent_level+outdent_level-i-1)}</ul>"
					'''
					# W3C compliant, but UGLY. Leave for now.
					if indent_level+outdent_level-i > 1:
						output += f"{HTML_WS}{WS*(indent_level+outdent_level-i-1)}</ul></li>"
					else:
						output += f"{HTML_WS}{WS*(indent_level+outdent_level-i-1)}</ul>"
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


			if indent_level > 0:
				output += f"{HTML_WS}{WS*(indent_level)}" + "<li>" + prefix + line + suffix + "</li>"
			elif prefix in ['<strong>', '<em>']:
				output += f"{HTML_WS}{WS*(indent_level)}" + prefix + line + suffix + "<br />"
			elif prefix:
				output += f"{HTML_WS}{WS*(indent_level)}" + prefix + line + suffix
			else:
				output += f"{HTML_WS}{WS*(indent_level)}" + prefix + line + suffix + "<br />" # Plain text.

			indent_level_previous = indent_level

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

	"""
	# TODO: Unused currently. For generating from full directories.
	def fromFile(self, filename):
		input = open(filename, "rU")
		output = self.create(input)
		input.close()
		return output
	"""
