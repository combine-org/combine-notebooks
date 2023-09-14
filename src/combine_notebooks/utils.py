import os
from pathlib import Path


def determine_environment():
    # determine if we're running on Google Colab
    try:
        import google.colab

        exec_env = "colab"  # we seem to be on colab
        print("Assuming this notebook is running on Google Colab")
    except:
        exec_env = "binder"  # assume it's binder

    if exec_env == "colab":
        working_dir = f"{Path.cwd()}/combine-notebooks/notebooks/results"
        os.system("git clone https://github.com/combine-org/combine-notebooks")
        os.chdir("combine-notebooks")
        os.system("pip install .")

    else:
        # binder starts off in the notebook's folder
        working_dir = f"{Path.cwd()}/results"

    os.chdir(working_dir)

    print("Current directory is: %s" % working_dir)
    return working_dir
