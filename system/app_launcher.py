import subprocess
from system.app_database import load_apps


def launch(app):

    apps = load_apps()

    if app not in apps:
        return None

    try:

        subprocess.Popen(apps[app], shell=True)

        return f"Opening {app.title()}."

    except Exception:

        return None