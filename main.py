import os
import reflux

root = "themes"
publish_key = os.environ["PUBLISH_KEY"]

print("Starting ~~Reflux Theme Manager!!~~\n\n")

for project in os.listdir(root):
    project = f"{root}/{project}"
    
    print(f"Building project: {project}")
    theme = reflux.Theme(f"{project}/theme.yaml")

    print("  + Uploading theme...")
    theme.upload(publish_key)

    print("  + Creating build directory...")
    if not os.path.exists(f"{project}/build"):
        os.mkdir(f"{project}/build")

    for f in ["engine.js", "style.css", "_referral"]:
        open(f"{project}/build/{f}", "w+").close()
        open(f"{project}/build/_referral", "w+").close()
    
    print("  + Building theme sources...")
    open(f"{project}/build/_referral", "w+").write(theme.referral())
    theme.engine(file=f"{project}/build/engine.js")
    theme.to_stylesheet(file=f"{project}/build/style.css")

    print("  ~ Done!\n", "-~" * 10, "\n\n")