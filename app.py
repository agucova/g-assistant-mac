import subprocess
import rumps
import wrapper
import thread
class Assistant(rumps.App):
    @rumps.clicked("Assistant")
    def prefs(self, _):
        print("Starting wrapper.main()...")
        thread.start_new_thread(wrapper.main, ())
        subprocess.call(["afplay", "/System/Library/Sounds/Blow.aiff"])



if __name__ == "__main__":
    Assistant(name="Assistant", icon="icon.png", quit_button='Quit').run()
