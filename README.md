# SmartRun

> **A lightweight Windows command launcher and automation tool.**

SmartRun is a lightweight command launcher designed to make everyday tasks faster through a simple keyboard-driven interface.

Press **`Ctrl + Space`**, type what you want to do, select a suggestion, and press **Enter** to execute it.

---

## Early Access

> **SmartRun is currently in Early Access.**

This project is **actively under development** and should be considered experimental.

Expect:

* Frequent updates
* Major UI changes
* New features and commands
* Changes to the underlying architecture
* Bug fixes and behavior changes
* Features being added, redesigned, or removed
* Potential breaking changes

Development will happen on a regular basis as SmartRun evolves.

**The current version is not considered a final or stable release.**

---

## Features

### Command Launcher

Launch commands quickly using the global:

```text
Ctrl + Space
```

Example:

```text
open youtube
open gmail
open chatgpt
open telegram
open moodle
```

### Command Suggestions

SmartRun provides suggestions while typing.

For example:

```text
open
```

can display:

```text
Open YouTube
Open YouTube Incognito
Open Gmail
Open Telegram
Open Moodle
Open ChatGPT
```

Suggestions can be navigated using the keyboard.

### Calculator

SmartRun can also evaluate basic mathematical expressions directly from the launcher.

Examples:

```text
4/5
```

```text
1+2
```

```text
3*4
```

```text
9-4
```

The result appears directly in the suggestion area.

Example:

```text
4/5 = 0.8
```

### Keyboard Driven

The interface is designed around quick keyboard interaction.

```text
Ctrl + Space
      ↓
 Type command
      ↓
 Select suggestion
      ↓
 Enter
      ↓
 Execute
```

The launcher disappears immediately when the command is submitted.

---

## Current Commands

Some currently supported commands include:

| Command           | Action                              |
| ----------------- | ----------------------------------- |
| `open youtube`    | Open YouTube                        |
| `open -p youtube` | Open YouTube in an incognito window |
| `open gmail`      | Open Gmail                          |
| `open telegram`   | Open Telegram                       |
| `open moodle`     | Open NCI Moodle                     |
| `open books`      | Open the configured books website   |
| `open -p books`   | Open books in an incognito window   |
| `open claude`     | Open Claude                         |
| `open chatgpt`    | Open ChatGPT                        |
| `open -p chatgpt` | Open ChatGPT in an incognito window |
| `open anime`      | Open the configured anime website   |
| `open -p anime`   | Open anime in an incognito window   |

More commands will be added as development continues.

---

## How It Works

The project currently separates the launcher interface from the automation logic.

```text
                 SmartRun
                    │
                    ↓
              Ctrl + Space
                    │
                    ↓
             Search / Command
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
     Suggestions          Calculator
          │
          ↓
       Enter
          │
          ↓
    Command Executor
          │
          ↓
   Windows Automation
```

The launcher UI is built with **PyQt6**, while automation is currently handled through Python automation libraries.

---

## Tech Stack

* **Python**
* **PyQt6**
* **PyAutoGUI / automation tooling**
* **pywinauto**
* **Keyboard**
* **Windows**

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SmartRun.git
```

Enter the project directory:

```bash
cd SmartRun
```

Install the required Python packages:

```bash
pip install PyQt6 keyboard pywinauto
```

Then run:

```bash
python UIpyautotask.py
```

> The exact dependencies and project structure may change during Early Access.

---

## Usage

After starting SmartRun:

### 1. Open the launcher

Press:

```text
Ctrl + Space
```

### 2. Type a command

For example:

```text
open youtube
```

### 3. Choose a suggestion

Use:

```text
↑
↓
```

or your mouse.

### 4. Execute

Press:

```text
Enter
```

The launcher closes immediately and the selected command is executed.

---

## Roadmap

SmartRun is still in its early development stage. Planned areas include:

* [ ] More application launching
* [ ] More Windows system commands
* [ ] Better command suggestions
* [ ] Fuzzy command matching
* [ ] Command aliases
* [ ] Custom user commands
* [ ] Multi-step automation
* [ ] Workflow creation
* [ ] Better error handling
* [ ] Improved UI/UX
* [ ] Configurable shortcuts
* [ ] Plugin/extension system
* [ ] Natural-language commands
* [ ] AI-assisted task automation

The roadmap is expected to change as development progresses.

---

## Development Status

**Status: Early Access**

SmartRun is being actively developed.

The project is currently focused on experimenting with the launcher experience, command execution, automation architecture, and future workflow capabilities.

Expect significant changes between versions.

If you are checking out the project during this stage, the code and interface may change substantially without maintaining backwards compatibility.

---

## Contributing

Contributions, ideas, bug reports, and suggestions are welcome.

Because SmartRun is currently in Early Access, the project structure and APIs may change frequently.

Before making major changes, please consider opening an issue to discuss the proposed change.

---

## Disclaimer

SmartRun is an experimental personal automation project.

Some commands may interact with applications or websites installed/configured on the user's system. Commands should be reviewed before execution, particularly when adding automation that interacts with external applications.

---

## License

**All Rights Reserved**

Copyright © 2026 Shahazaad Ahmed.

SmartRun is publicly available for viewing and evaluation purposes.
No permission is granted to copy, modify, distribute, redistribute,
sublicense, or commercially use this software without explicit
permission from the author.

The project is currently in Early Access and is actively under development.

---

**SmartRun — Early Access**

*Fast commands. Less clicking. More automation.*
