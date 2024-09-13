#!/usr/bin/python

import re
import os
import git
import subprocess

ref_pfcm_src_path="..\\bhs_pfcm"
ref_pfcm_chipset_src_path="..\\bhs\\Intel"
ref_pfcm_kernel_base_src_path="..\\bhs\\Insyde"
ref_pfcm_pfc="ref\\Project.pfc"
checkout_src_path="Intel_BHS/"


class chdir():
    last_dir=[]
    def change_dir(path="./"):
        if os.path.isdir(path):
            # print(f"orig path : {path}")
            path=re.sub(r"\/",r"\\",path)
            # print(f"new path : {path}")
            path=re.sub(r"\\",r"\\\\",path)
            # print(f"new path : {path}")
            path=re.sub(r"\\\\\\\\",r"\\\\",path)
            # print(f"final path : {path}")
            chdir.last_dir.append(os.getcwd())
            # print("store path:", os.getcwd())
            os.chdir(path)
            # print("pwd:", os.getcwd())
            return True
        else:
            return False
    
    def rollback_dir():
        if chdir.last_dir:
            os.chdir(chdir.last_dir.pop())
            # print("restore:", os.getcwd())

def search_folder(start_dir="./", search_string=""):
    repo_folders = []
    print("    search path : ", start_dir)
    for root, dirs, files in os.walk(start_dir):
        if search_string in dirs:
            repo_folders.append(os.path.join(root))
    return repo_folders

def search_filename(start_dir="./", search_string=""):
    find_files = []
    print("    search path : ", start_dir)
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            # print(os.path.join(root, file))
            if file == search_string:
                find_files.append(os.path.join(root, file))
    return find_files

def search_filename_extension(start_dir="./", search_string=""):
    find_files = []
    print("    search path : ", start_dir)
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            # print(os.path.join(root, file))
            if file.endswith(search_string):
                find_files.append(os.path.join(root, file))
    return find_files


def search_filename_extension_without_sub_folder(start_dir="./", search_string=""):
    find_files = []
    for item in os.listdir(start_dir):
        if os.path.isfile(os.path.join(start_dir, item)) and item.endswith(search_string):
            find_files.append(item)
    return find_files


def open_xml_root(file):
    xml_file_node={}
    import xml.etree.ElementTree as ET
    print("                Parse xml file : ", file)
    tree = ET.parse(file)
    root = tree.getroot()
    xml_file_node[tree]=root
    return xml_file_node



# Search all repositories
def search_git_repo(path="./"):
    return search_folder(path,".git")
        
# Search all IFC
def search_ifc(path="./"):
    return search_filename_extension(path,"ifc")

# Search all IFC
def search_ifc_without_sub_folder(path="./"):
    return search_filename_extension_without_sub_folder(path,"ifc")


# Search PFC
def search_pfc(path="./"):
    return search_filename(path,"Project.pfc")

# Parse IFC
def parse_ifc():
    print("    todo!")



def parse_xml_element(root_element):
    if root_element.attrib == {} :      
        for child_element in root_element:
            # print("    child_element : ", child_element)
            # print("    child_element.tag : ", child_element.tag, " = ", child_element.text)
            if child_element.attrib == {} :
                parse_xml_element(child_element)

# Parse PFC
def parse_pfc(file):
    xml_file_node=open_xml_root(file)
    for tree, root in xml_file_node.items():
        parse_xml_element(root)


# Clone git source code
def clone_git_repository(url, path):
    try:
        result = subprocess.run(['git', 'clone', url, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"    Error: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"    Exception occurred: {e}")
        return None

# Checkout git tag source code
def checkout_git_tag(start_dir="./", tag_name="HEAD"):
    try:
        result = subprocess.run(['git', 'checkout', '-f', tag_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"    Error: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"    Exception occurred: {e}")
        return None

# Get git HEAD commit hash
def get_head_commit_hash(start_dir="./"):
    try:
        chdir.change_dir(start_dir)
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        chdir.rollback_dir()
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # print(f"    Error: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"    Exception occurred: {e}")
        return None

# Get git HEAD commit tag
def get_head_commit_tag(start_dir="./"):
    try:
        chdir.change_dir(start_dir)
        result = subprocess.run(['git', 'tag', '--points-at', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        chdir.rollback_dir()
        # print(result.stdout)
        if result.returncode == 0:
            tag_list=[]
            for line in result.stdout.split("\n"):
                if line:
                    tag_list.append(line)
            return tag_list
        else:
            print(f"    Error: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"    Exception occurred: {e}")
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
            print(f"    Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"    Exception occurred: {e}")
        return None

# List all reference features in PFCM PFC
def list_all_ref_features_in_pfc(file):
    print("    Target PFC : ", file)
    # workspace=[]
    # features={}
    feature_Url={}
    feature_Tag={}
    feature_Root={}
    feature_Name={}
    feature_Version={}
    workspace={'Url':feature_Url, 'Tag':feature_Tag, 'Root':feature_Root, 'Name':feature_Name, 'Version':feature_Version}
    # dependency_list={}
    xml_file_node=open_xml_root(file)
    for tree, root in xml_file_node.items():
        for xml_feature in root.findall('Feature'):
            feature_Url[xml_feature.find('Root').text] = xml_feature.find('Repository/Url').text
            feature_Tag[xml_feature.find('Root').text] = xml_feature.find('Repository/Tag').text
            feature_Root[xml_feature.find('Root').text] = xml_feature.find('Root').text
            feature_Name[xml_feature.find('Root').text] = xml_feature.find('Name').text
            feature_Version[xml_feature.find('Root').text] = xml_feature.find('Version').text
            # for xml_dependency in xml_feature.findall('Dependency'):
            #     dependency_list["Name"] = xml_dependency.find('Name').text
            #     dependency_list["Version"] = xml_dependency.find('Version').text
            # workspace[xml_feature.find('Root').text]=features
        return workspace

# List all reference features in PFCM PFC
def find_ifc_version_with_tag(file, git_tag="git_tag"):
    print(f"                Search tag({git_tag}) in {file}")
    xml_file_node=open_xml_root(file)
    for tree, root in xml_file_node.items():
        for xml_feature in root.findall('Feature'):
            # print(xml_feature)
            # print(xml_feature.find('Repository/Tag').text)
            if xml_feature.find('Repository/Tag').text == git_tag:
                print("                    git tag matched : ", git_tag, ", it mappoing PFCM version : ", xml_feature.find('Version').text)
                return xml_feature.find('Version').text
            else:
                print("                    not matched next ...")
        return None

# Search PFCM version and tag as HEAD commit in feature IFC
def get_ifc_version_with_current_commit(start_dir="."):
    # print(f"    chdir to {start_dir}")
    ifc_version=None
    chdir.change_dir(start_dir)
    all_tags=get_head_commit_tag()

    print("            List all tags on this commit:")
    if all_tags :
        for tag in all_tags:
            print("                currently commit tag : ", tag)
    else:
        print("                Not found any tag at this commit!")

    print("            Find feature IFC file:")
    ifc_files = search_ifc_without_sub_folder()
    if ifc_files:
        for ifc in ifc_files:
            print("                IFC file : ", ifc)
            for tag in all_tags:
                ifc_version=find_ifc_version_with_tag(ifc, tag)
    else:
        print("                Not found any IFC!")

    chdir.rollback_dir()

    if ifc_version == None:
        print("            Not found matched PFCM version in feature IFC!")
        print("            If you want to make PFCM tag release on this commit, you need to append a PFCM feature version description in feature IFC.")
        return None
    else:
        ret={'tag':tag, 'ifc_ver':ifc_version}
        return ret
        

# Check all repositories HEAD commit has tag and PFCM version
def check_all_repo_has_ready_for_pfcm_tag():
    print("    todo!")

# Update all repositories HEAD commit hash to workspace manifest.xml
def update_manfest():
    print("    todo!")

# List all untracking and modified files
def list_untracking_and_modified():
    print("    todo!")


def clone_repository(bare, path, replace_source=None):
    print(f"    git clone {bare} {path}")
    if replace_source != None:
        print("    Try to replace clone source code interface!")
        # bare = re.sub(r"^((\w*://[^/]*)|(.*repo))/", f"ssh://vic.ho@192.168.31.200:/home/vic.ho/proj/repo/", bare)
        bare = re.sub(r"^((\w*://[^/]*)|(.*repo))/", replace_source, bare)
        print("    New repository URL : ", bare)

    clone_git_repository(bare, path)


# Checkout all source code with PFC
def checkout_src_with_pfc(pfc_file, dist_src_path="./"):
    clone_url=""
    clone_path=""
    workspace_features=list_all_ref_features_in_pfc(pfc_file)
    if workspace_features :
        feature_Url={}
        feature_Tag={}
        feature_Root={}
        feature_Name={}
        feature_Version={}

        for informations, element in workspace_features.items():
            # print(f"    {informations}")
            if informations == "Url":
                feature_Url=element
            elif informations == "Tag":
                feature_Tag=element
            elif informations == "Root":
                feature_Root=element
            elif informations == "Name":
                feature_Name=element
            elif informations == "Version":
                feature_Version=element
            # for element, info in elements.items():
            #     print(f"        {element}:{info}")

        for feature, value in feature_Root.items():
            # print(f"    {value}:")
            # print(f"    git clone {feature_Url[value]} {feature_Root[value]}")
            final_src_dist_path=f"{dist_src_path}{feature_Root[value]}"
            clone_repository(feature_Url[value], final_src_dist_path, "../../repo/")
            # clone_repository(feature_Url[value], final_src_dist_path, "ssh://vic.ho@192.168.31.200:/home/vic.ho/proj/repo/")
            # clone_repository(feature_Url[value], final_src_dist_path, None)
            if chdir.change_dir(final_src_dist_path):
                # print(f"    chdir to {final_src_dist_path} and checkout to tag({feature_Tag[value]}) or commit")
                # git_checkout("./", feature_Tag[value])
                checkout_git_tag("./", feature_Tag[value])
                chdir.rollback_dir()
            else:
                print(f"      Not found path: {feature_Root[value]}")
    else:
        print("    Not found reference feature in PFC!")

def find_newest_versions(version1, version2):  
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 < v2:
            return version2
        elif v1 > v2:
            return version1
        else :
            return version1
    return version1

# List all feature dependency of PFC
def list_feature_dependency_wit_pfc(pfcm_pfc):
    dependency_list={}
    xml_file_node=open_xml_root(pfcm_pfc)
    for tree, root in xml_file_node.items():
        for xml_feature in root.findall('Feature/Dependency'):
            if dependency_list.get(xml_feature.find('Name').text) == None:
                dependency_list[xml_feature.find('Name').text]=xml_feature.find('Version').text
            else:
                dependency_list[xml_feature.find('Name').text]=find_newest_versions(dependency_list.get(xml_feature.find('Name').text), xml_feature.find('Version').text)
        return dependency_list

def update_pfc_feature_dependency(pfcm_feature_name, pfcm_feature_version, pfcm_feature_tag, pfcm_pfc):

    # This way not work in our case. Because it will make the comment message lost in new PFCM PFC file.
    # So we try to replace with string replace rule not xml parser to modify it.
    #  
    # xml_file_node=open_xml_root(pfcm_pfc)
    # for tree, root in xml_file_node.items():
    #     for xml_feature in root.findall('Feature/Dependency'):
    #         if xml_feature.find('Name').text == pfcm_feature_name:
    #             xml_feature.find('Version').text=pfcm_feature_version
    #     for xml_feature in root.findall('Feature'):
    #         if xml_feature.find('Name').text == pfcm_feature_name:
    #             xml_feature.find('Version').text=pfcm_feature_version
    #     tree.write(pfcm_pfc, encoding='utf-8', xml_declaration=True)

    print(f"    Update {pfcm_feature_name} to PFCM version {pfcm_feature_version} at tag {pfcm_feature_tag} in {pfcm_pfc}")

    with open(pfcm_pfc, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(pfcm_pfc, 'w', encoding='utf-8') as file:
        feature=False
        depandency=False
        feature_name=""
        depandency_feature_name=""

        for line in lines:
            if line.strip() == f"<Feature>":
                feature=True
            elif line.strip() == f"</Feature>":
                feature=False
                feature_name=""
            elif feature and line.strip() == f"<Dependency>":
                depandency=True
            elif feature and line.strip() == f"</Dependency>":
                depandency=False
            elif feature and re.match(r"<Name>.*</Name>", line.strip()):
                if depandency:
                    depandency_feature_name = re.sub(r"</Name>.*", f"", re.sub(r".*<Name>", f"", line.strip()))
                else:
                    feature_name = re.sub(r"</Name>.*", f"", re.sub(r".*<Name>", f"", line.strip()))
            elif feature and re.match(r"<Version>.*</Version>", line.strip()):
                if depandency:
                    if depandency_feature_name == pfcm_feature_name:
                        line = re.sub(r">.*<", f">{pfcm_feature_version}<", line)
                        print("    Update feature version in dependency!")
                else:
                    if feature_name == pfcm_feature_name:
                        line = re.sub(r">.*<", f">{pfcm_feature_version}<", line)
                        print("    Update feature version in feature!")
            elif feature and re.match(r"<Tag>.*</Tag>", line.strip()):
                if feature_name == pfcm_feature_name:
                    line = re.sub(r">.*<", f">{pfcm_feature_tag}<", line)
                    print("    Update feature tag in feature!")
            elif re.match(r"<!--.*-->.*", line.strip()):
                string=re.sub(r"<!-- *", "" , line.strip())
                if string.startswith(f"{pfcm_feature_name} "):
                    line=re.sub(r"<!--.*-->", f"<!-- {pfcm_feature_name} {pfcm_feature_version} -->" , line)
                    print("    Update feature comment!")
            
            file.write(line)

# Checkout all source code with workspace manifest.xml
def checkout_src_with_mainfest():
    print("    todo!")

# Sync feature cruuently PFCM version to PFC dependency
def update_feature_to_pfc():
    print("    todo!")

# Check featrue has existing in PFC
def parse_ifc():
    print("    todo!")

def update_pfc_feature_dependency_in_workspace(workspace):
    # Found PFC in workspace
    pfc_files=search_pfc(workspace)
    for pfc_file in pfc_files:
        print("    Found ", pfc_file, "in ", workspace, "\n")

    # List all features from PFC
    workspace_features=list_all_ref_features_in_pfc(pfc_file)
    if workspace_features :
        # feature_Url={}
        # feature_Tag={}
        # feature_Root={}
        # feature_Name={}
        # feature_Version={}

        for informations, element in workspace_features.items():
            # print(f"    {informations}")
            if informations == "Url":
                feature_Url=element
            elif informations == "Tag":
                feature_Tag=element
            elif informations == "Root":
                feature_Root=element
            elif informations == "Name":
                feature_Name=element
            elif informations == "Version":
                feature_Version=element

        for feature, feature_path in feature_Root.items():
            # print(f"        Todo update version and tag from real feature status")
            print(f"    Update [ {feature_path} ] to Project.pfc:")
            print(f"        [ From PFC ] : {feature_Version[feature_path]} ({feature_Tag[feature_path]})")
            version_info=get_ifc_version_with_current_commit(f"{workspace}/{feature_Root[feature_path]}")
            print(f"        [ From current status ] : {version_info}")
            if version_info:
                print(f"        [ From current status ] : {version_info}")
                # update_pfc_feature_dependency(feature_path, version_info['ifc_ver'], version_info['tag'], pfc_file)
            print(f"        !!!! Next !!!!\n")
    else:
        print("    Not found reference feature in PFC!")

####################################################################################################
####################################################################################################
#                                                                                                  #
# Test cases                                                                                       #
#                                                                                                  #
####################################################################################################
####################################################################################################

print("Try to Search all git repositories:")
git_folders = search_git_repo(ref_pfcm_src_path)
if git_folders:
    if git_folders:
        for folder in git_folders:
            print("    find .git in ", folder)
    else:
        print("    Not found .git in here!")
print("\n")

# test case
print("[ Try to Search all PFCM IFC ]:")
ifc_files = search_ifc(ref_pfcm_src_path)
if ifc_files:
    for file in ifc_files:
        print("    find ", file)
else:
    print("    Not found IFC in here!")
print("\n")

# test case
print("[ Try to Search all PFCM PFC ]:")
pfc_files = search_pfc(ref_pfcm_src_path)
if pfc_files:
    for file in pfc_files:
        print("    find ", file)
else:
    print("    Not found PFC in here!")
print("\n")

# test case
print("[ Try Parse IFC ]")
parse_ifc()
print("\n")

# test case
print("[ Parse PFC ]")
pfc_files = search_pfc(ref_pfcm_src_path)
if pfc_files:
    for file in pfc_files:
        print("    find ", file)
        parse_pfc(file)
else:
    print("    Not found PFC in here!")
print("\n")

# test case
print("[ List all reference features in PFCM PFC ]:")
pfc_files = search_pfc(ref_pfcm_src_path)
if pfc_files:
    for file in pfc_files:
        print("    find ", file)
        workspace=list_all_ref_features_in_pfc(file)
        if workspace :
            for informations, elements in workspace.items():
                print(f"    {informations}")
                for element, info in elements.items():
                    print(f"        {element}:{info}")
        else:
            print("    Not found reference feature in PFC!")
    print("    Not found PFC in here!")
print("\n")

# test case
print("[ Get git HEAD commit hash ]")
commit_hash=get_head_commit_hash(ref_pfcm_src_path)
if commit_hash :
    print("    commit hash : ", commit_hash)
else:
    print("    Not found commit hash")
print("\n")

# test case
print("[ Get git HEAD commit tag ]")
commit_tag=get_head_commit_tag(ref_pfcm_src_path)
if commit_tag :
    print("    commit tag : ", commit_tag)
else:
    print("    Not found commit tag")
print("\n")

# test case
print("[ List git remote URL ]")
remotes=list_git_remote_url(ref_pfcm_src_path)
if remotes :
    for name, url in remotes.items():
        print(f"    {name}: {url}")
else:
    print("    Not found git remote")
print("\n")

# test case
print("[ Check all repositories HEAD commit has tag and PFCM version ]")
check_all_repo_has_ready_for_pfcm_tag()
print("\n")

# test case
print("[ Update all repositories HEAD commit hash to workspace manifest.xml ]")
update_manfest()
print("\n")

# test case
print("[ List all untracking and modified files ]")
list_untracking_and_modified()
print("\n")

# test case
print("[ Checkout all source code with workspace manifest.xml ]")
checkout_src_with_mainfest()
print("\n")

# test case
print("[ Sync feature cruuently PFCM version to PFC dependency ]")
update_feature_to_pfc()
print("\n")

# test case
print("[ Check featrue has existing in PFC ]")
parse_ifc()
print("\n")

# test case
print("[ Search PFCM version as HEAD commit in feature IFC ]")
print("    Match IFC version : ", get_ifc_version_with_current_commit(ref_pfcm_chipset_src_path))
print("    Match IFC version : ", get_ifc_version_with_current_commit(ref_pfcm_kernel_base_src_path))
print("\n")

# test case
print("[ Parse all dependency description with PFC ]")
dependency_list=list_feature_dependency_wit_pfc(ref_pfcm_pfc)
for feature_name, feature_version in dependency_list.items():
    print(f"    {feature_name}: {feature_version}")
print("\n")

# test case
print("[ Sync all feature version to PFC with workspace ]")
update_pfc_feature_dependency_in_workspace(ref_pfcm_src_path)
print("\n")

# test case
print("[ Checkout all source code with PFC ]")
checkout_src_with_pfc(ref_pfcm_pfc, checkout_src_path)
print("\n")

# test case
print("[ Update PFC feature dependency ]")
pfcm_feature_name="Intel_BirchStreamEDK2"
pfcm_feature_version="99.99.99.9999"
pfcm_feature_tag="test_tag"
pfcm_pfc=ref_pfcm_pfc
update_pfc_feature_dependency(pfcm_feature_name, pfcm_feature_version, pfcm_feature_tag, pfcm_pfc)
print("\n")

exit()