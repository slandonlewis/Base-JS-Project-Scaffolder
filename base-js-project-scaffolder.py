import os
import argparse


def main(workspaceName, projectName):
    # get home directory
    home = os.path.expanduser("~")

    # make main code directory where all project directories live
    workspace = os.path.join(home, workspaceName)
    if not os.path.isdir(workspace):
        os.makedirs(workspace)
    # print(workspace)

    # make projectName folder
    project = os.path.join(workspace, projectName)
    if not os.path.isdir(project):
        os.makedirs(project)
    # print(project)

    # make subdirectories for html, css, js in projectName folder
    subdirectories = ["html", "css", "js"]
    for directory in subdirectories:
        subdir = os.path.join(project, directory)
        os.makedirs(subdir)
        print(subdir)
        with open("{}\\index.{}".format(project, directory), "x") as file:
            file.write("Create file")
        with open("{}\\home.{}".format(subdir, directory), "x") as file:
            file.write("Create file")

    # maybe add boilerplate code to each home file


    # cli args
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workspace', type=str)
parser.add_argument('-p', '--project', type=str)
args = parser.parse_args()

main(args.workspace, args.project)
