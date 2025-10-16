# Setup Guide: Prerequisites Installation

Quick installation guide for all required tools. Follow in order.

---

## 1. Python 3.10+

**macOS:**

```bash
# Download and run the installer
# Visit: https://www.python.org/downloads/
```

**Windows:**

```bash
# Download and run the installer
# Visit: https://www.python.org/downloads/
```

**Linux:**

```bash
# Usually pre-installed. Check version first:
python3 --version
```

**Verify installation:**

```bash
python3 --version  # Should show 3.10 or higher
```

📚 [Official Python Downloads](https://www.python.org/downloads/)

---

## 2. UV (Python Package Manager)

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (Homebrew):**

```bash
brew install uv
```

**Verify installation:**

```bash
uv --version
```

📚 [Official UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)

---

## 3. Node.js & npm

**Recommended: Official Installer**

- Download from: https://nodejs.org/
- Choose the LTS (Long Term Support) version
- npm is included automatically

**Alternative (macOS - Homebrew):**

```bash
brew install node
```

**Alternative (Windows - Chocolatey):**

```bash
choco install nodejs
```

**Verify installation:**

```bash
node --version
npm --version
```

📚 [Official Node.js Downloads](https://nodejs.org/en/download/)

---

## 4. Claude Code

**NPM Install (Recommended if you have Node.js 18+):**

```bash
npm install -g @anthropic-ai/claude-code
```

**Native Install - macOS/Linux (Homebrew):**

```bash
brew install --cask claude-code
```

**Native Install - macOS/Linux/WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Native Install - Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Verify installation:**

```bash
claude --version
```

📚 [Official Claude Code Quickstart](https://docs.claude.com/en/docs/claude-code/quickstart)

---

## 5. VS Code (Recommended)

**All Platforms:**

- Download installer for your OS: https://code.visualstudio.com/download
- Run the installer
- Follow the installation wizard

**Verify installation:**

```bash
code --version
```

📚 [Official VS Code Downloads](https://code.visualstudio.com/download)

---

## 6. Git

**macOS:**

```bash
# Trigger automatic installation
git --version

# Or via Homebrew
brew install git
```

**Windows:**

- Download from: https://git-scm.com/download/win
- Run the installer

**Linux (Ubuntu/Debian):**

```bash
sudo apt install git-all
```

**Linux (Fedora/RHEL):**

```bash
sudo dnf install git-all
```

**Verify installation:**

```bash
git --version
```

📚 [Official Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## Final Verification

Run all commands to verify everything is installed:

```bash
python3 --version    # Should show 3.10+
uv --version         # Should show version number
node --version       # Should show version number
npm --version        # Should show version number
claude --version     # Should show version number
code --version       # Should show version number
git --version        # Should show version number
```

✅ **All commands show version numbers? You're ready to start!**

❌ **Getting "command not found"?** Restart your terminal and try again. If the issue persists, revisit the installation steps for that specific tool.

---

## Alternative AI Coding Assistants

This course teaches frameworks that work with **any** AI coding assistant:

- **Cursor**: https://cursor.sh/
- **GitHub Copilot**: https://github.com/features/copilot
- **Aider**: https://aider.chat/

Use what you're comfortable with.

---

## Need Help?

- Check the official documentation linked above
- Join the community # channel
- Post your error message with the tool name

**Installation Time:** 20-30 minutes from scratch is normal.

---

_Last updated: October 2025_
