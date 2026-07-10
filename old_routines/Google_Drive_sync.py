import time
import subprocess
import sys

def is_google_drive_installed():
    """Check if Google Drive is installed in /Applications or ~/Applications."""
    try:
        # Search for "Google Drive" or "GoogleDrive" in all locations
        result = subprocess.run(
            ['mdfind', 'kind==application AND (name=="Google Drive" OR name=="GoogleDrive")'],
            capture_output=True,
            text=True
        )
        if result.stdout.strip():
            return True
        return False
    except Exception as e:
        print(f"Error checking installation: {e}")
        return False

def is_google_drive_running():
    """Check if Google Drive is running using the process name."""
    try:
        result = subprocess.run(
            ['ps', '-axc', '--no-headers', '-o', 'command='],
            capture_output=True,
            text=True
        )
        if "GoogleDrive" in result.stdout or "Google Drive" in result.stdout:
            return True
        return False
    except Exception as e:
        print(f"Error checking process: {e}")
        return False

def start_google_drive():
    """Start Google Drive using AppleScript, with error handling."""
    try:
        # Use the correct application name based on your system
        # Change to "GoogleDrive" if your app is named without a space
        script = 'tell application "Google Drive" to activate'
        subprocess.run(['osascript', '-e', script], check=True)

        # Wait for the app to start
        print("Waiting for Google Drive to start...")
        timeout = 30  # seconds
        start_time = time.time()
        while time.time() - start_time < timeout:
            if is_google_drive_running():
                print("Google Drive is running.")
                return True
            time.sleep(1)
        print("Timeout: Google Drive did not start.")
        return False
    except Exception as e:
        print(f"Failed to start Google Drive: {e}")
        return False

def main():
    if not is_google_drive_installed():
        print("Google Drive is not installed. Please install it from the official website.")
        sys.exit(1)

    if not start_google_drive():
        print("Could not start Google Drive. Exiting.")
        sys.exit(1)

    # Check syncing status
    try:
        script = 'tell application "Google Drive" to is syncing'
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True
        )
        syncing = result.stdout.strip().lower() == "true"
        if syncing:
            print("Google Drive is currently syncing.")
        else:
            print("Google Drive is not syncing.")
    except Exception as e:
        print(f"Error checking syncing status: {e}")
        print("Could not determine syncing status.")

if __name__ == "__main__":
    main()

