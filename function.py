#!/usr/bin/python

import os
import subprocess

class chdir():
    last_dir=""
    def change_dir(path):
        chdir.last_dir=os.getcwd()
        os.chdir(path)
    
    def rollback_dir():
        if chdir.last_dir:
            os.chdir(chdir.last_dir)

def search_folder(start_dir="./", search_string=""):
    repo_folders = []
    print("search path : ", start_dir)
    for root, dirs, files in os.walk(start_dir):
        if search_string in dirs:
            repo_folders.append(os.path.join(root))
    return repo_folders

def search_filename(start_dir="./", search_string=""):
    find_files = []
    print("search path : ", start_dir)
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            # print(os.path.join(root, file))
            if file == search_string:
                find_files.append(os.path.join(root, file))
    return find_files

def search_filename_extension(start_dir="./", search_string=""):
    find_files = []
    print("search path : ", start_dir)
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            # print(os.path.join(root, file))
            if file.endswith(search_string):
                find_files.append(os.path.join(root, file))
    return find_files


def open_xml_root(file):
    import xml.etree.ElementTree as ET
    print("Parse xml file : ", file)
    tree = ET.parse(file)
    root = tree.getroot()
    return root



# Search all repositories
def search_git_repo(path="./"):
    return search_folder(path,".git")
        
# Search all IFC
def search_ifc(path="./"):
    return search_filename_extension(path,"ifc")

# Search PFC
def search_pfc(path="./"):
    return search_filename(path,"Project.pfc")

# Parse IFC
def parse_ifc():
    print("todo!")



def parse_xml_element(root_element):
    if root_element.attrib == {} :      
        for child_element in root_element:
            print("child_element : ", child_element)
            print("child_element.tag : ", child_element.tag, " = ", child_element.text)
            if child_element.attrib == {} :
                parse_xml_element(child_element)

# Parse PFC
def parse_pfc(file):
    root=open_xml_root(file)
    parse_xml_element(root)


# Get git HEAD commit hash
def get_head_commit_hash(start_dir="./"):
    try:
        chdir.change_dir(start_dir)
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        chdir.rollback_dir()
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # print(f"Error: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# Get git HEAD commit tag
def get_head_commit_tag(start_dir="./"):
    try:
        chdir.change_dir(start_dir)
        result = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        chdir.rollback_dir()
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # print(f"Error: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# List git remote URL
def list_git_remote_url(start_dir="./"):
    try:
        chdir.change_dir(start_dir)
        result = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        chdir.rollback_dir()
        if result.returncode == 0:
            remote_urls = {}
            for line in result.stdout.strip().split('\n'):
                parts = line.split()
                if len(parts) >= 2:
                    name = parts[0]
                    url = parts[1]
                if name not in remote_urls:
                    remote_urls[name] = url
                    return remote_urls
        else:
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# List all reference features in PFCM PFC
def list_all_ref_features_in_pfc(file):
    workspace={}
    features={}
    # dependency_list={}
    root=open_xml_root(file)
    for xml_feature in root.findall('Feature'):
        features["Url"] = xml_feature.find('Repository/Url').text
        features["Tag"] = xml_feature.find('Repository/Tag').text
        features["Root"] = xml_feature.find('Root').text
        features["Name"] = xml_feature.find('Name').text
        features["Version"] = xml_feature.find('Version').text
        # for xml_dependency in xml_feature.findall('Dependency'):
        #     dependency_list["Name"] = xml_dependency.find('Name').text
        #     dependency_list["Version"] = xml_dependency.find('Version').text
        workspace[xml_feature.find('Root').text]=features
    return workspace


# for feature in root.findall('Feature'):
# name = feature.find('Name').text
# if name == 'Kernel_XhciPeiBin_Rev5.6':
# url = feature.find('Repository/Url').text
# print("Extracted URL:", url)
# break


# 呼叫函數並打印所有遠端倉庫的 URL
# remote_urls = get_git_remote_urls()
# if remote_urls:
# print("Git remote URLs:")
# for name, url in remote_urls.items():
# print(f"{name}: {url}")

# Search PFCM version as HEAD commit in feature IFC
def get_pfcm_version():
    print("todo!")

# Check all repositories HEAD commit has tag and PFCM version
def check_all_repo_has_ready_for_pfcm_tag():
    print("todo!")

# Update all repositories HEAD commit hash to workspace manifest.xml
def update_manfest():
    print("todo!")

# List all untracking and modified files
def list_untracking_and_modified():
    print("todo!")

# Checkout all source code with PFC
def checkout_src_with_pfc():
    print("todo!")

# Checkout all source code with workspace manifest.xml
def checkout_src_with_mainfest():
    print("todo!")

# Sync feature cruuently PFCM version to PFC dependency
def update_feature_to_pfc():
    print("todo!")

# Check featrue has existing in PFC
def parse_ifc():
    print("todo!")


ref_pfcm_src_path="..\\bhs"

# print("Try to Search all git repositories:")
# git_folders = search_git_repo(ref_pfcm_src_path)
# if git_folders:
#     if git_folders:
#         for folder in git_folders:
#             print("find .git in ", folder)
#     else:
#         print("Not found .git in here!")
# print("\n")

# print("Try to Search all PFCM IFC:")
# ifc_files = search_ifc(ref_pfcm_src_path)
# if ifc_files:
#     for file in ifc_files:
#         print("find ", file)
# else:
#     print("Not found IFC in here!")
# print("\n")

# print("Try to Search all PFCM PFC:")
# pfc_files = search_pfc(ref_pfcm_src_path)
# if pfc_files:
#     for file in pfc_files:
#         print("find ", file)
# else:
#     print("Not found PFC in here!")
# print("\n")

# print("Try Parse IFC")
# parse_ifc()
# print("\n")

# print("Parse PFC")
# pfc_files = search_pfc(ref_pfcm_src_path)
# if pfc_files:
#     for file in pfc_files:
#         print("find ", file)
#         parse_pfc(file)
# else:
#     print("Not found PFC in here!")
# print("\n")


# for fea in list:
#     print(fea)

# for fea in list:
#     for it, contain in fea.items():
#         print(f"{it}:{contain}")


print("List all reference features in PFCM PFC:")
pfc_files = search_pfc(ref_pfcm_src_path)
if pfc_files:
    for file in pfc_files:
        print("find ", file)
        workspace=list_all_ref_features_in_pfc(file)
        if workspace :
            for Path, Feature in workspace.items():
                for element, info in Feature.items():
                    print(f"{Path}: {element} = {info}")
        else:
            print("Not found reference feature in PFC!")
    print("Not found PFC in here!")
print("\n")


# import git  # pip install gitpython
# git.Git("/your/directory/to/clone").clone("git://gitorious.org/git-python/mainline.git")

# print("Get git HEAD commit hash")
# commit_hash=get_head_commit_hash(ref_pfcm_src_path)
# if commit_hash :
#     print("commit hash : ", commit_hash)
# else:
#     print("Not found commit hash")
# print("\n")

# print("Get git HEAD commit tag")
# commit_tag=get_head_commit_tag(ref_pfcm_src_path)
# if commit_tag :
#     print("commit tag : ", commit_tag)
# else:
#     print("Not found commit tag")
# print("\n")

# print("List git remote URL")
# remotes=list_git_remote_url(ref_pfcm_src_path)
# if remotes :
#     for name, url in remotes.items():
#         print(f"{name}: {url}")
# else:
#     print("Not found git remote")
# print("\n")

# print("Search PFCM version as HEAD commit in feature IFC")
# get_pfcm_version()
# print("\n")

# print("Check all repositories HEAD commit has tag and PFCM version")
# check_all_repo_has_ready_for_pfcm_tag()
# print("\n")

# print("Update all repositories HEAD commit hash to workspace manifest.xml")
# update_manfest()
# print("\n")

# print("List all untracking and modified files")
# list_untracking_and_modified()
# print("\n")

# print("Checkout all source code with PFC")
# checkout_src_with_pfc()
# print("\n")

# print("Checkout all source code with workspace manifest.xml")
# checkout_src_with_mainfest()
# print("\n")

# print("Sync feature cruuently PFCM version to PFC dependency")
# update_feature_to_pfc()
# print("\n")

# print("Check featrue has existing in PFC")
# parse_ifc()
# print("\n")

