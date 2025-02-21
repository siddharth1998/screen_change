# Screen Share Application

A Python program for monitoring even the smallest screen changes, ideal for systems requiring precise change detection. Sends notifications via Slack and includes audio alerts for Darwin-based systems

## Prerequisites

- Python 3.8 or higher
- Poetry (Python package manager)
- macOS (for screen sharing capabilities)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/siddharth1998/screen_change.git
cd screen_change
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# For macOS/Linux:
source .venv/bin/activate

# For Windows:
.\.venv\Scripts\activate
```

4. Install dependencies using Poetry:
```bash
poetry install
```

## macOS Screen Recording Permissions

Before running the application, you need to grant screen recording permissions:

1. Go to System Preferences > Security & Privacy > Privacy
2. Scroll down to Screen Recording
3. Click the lock icon to make changes (you'll need to enter your password)
4. Find and check your terminal application (e.g., Terminal.app or VS Code)
5. Restart your terminal or IDE after granting permissions

If you're using VS Code:
- You'll need to grant screen recording permission to VS Code specifically
- If running through the integrated terminal, make sure VS Code is added to the Screen Recording permissions

## Running the Application

1. Ensure your virtual environment is activated
2. Run the main script:
```bash
python main.py
```

## Troubleshooting

### Screen Recording Permission Issues

If you encounter permission errors:

1. Verify permissions are granted in System Preferences
2. Try running from a different terminal if using VS Code
3. Log out and log back in to ensure permissions are properly applied
4. Try to store the screenshots
