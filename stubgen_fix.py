"""
Fix to stubgen
stubgen replaces NewType to Incomplete.
We discover files with NewType and
replace them in stubgen generated files back to NewType
"""
from pathlib import Path

pathlist = Path(".").rglob('*.pyi')
for path in pathlist:
    path_in_str = str(path)
    if ".venv" in path_in_str:
        continue

    with open(path_in_str, "r") as file:
        pyi_file = file.readlines()
    with open(path_in_str.replace("-stubs","").replace(".pyi", ".py"), "r") as file:
        py_file = file.readlines()

    has_new_types = False

    # replace in pyi files NewType back to original code line
    for py_line in py_file:
        if "NewType" in py_line:
            varname: str = py_line.split(" ")[0]
            has_new_types = True
            
            for pyi_i, pyi_line in enumerate(pyi_file):
                if f"{varname}: Incomplete\n" == pyi_line:
                    pyi_file[pyi_i] = py_line

    if has_new_types:
        # replace from typing import back because
        # stubgen autoremoved some of it
        for py_line in py_file:
            if "from typing" in py_line:
                for pyi_i, pyi_line in enumerate(pyi_file):
                    if f"from typing" in pyi_line:
                        pyi_file[pyi_i] = py_line

    with open(path_in_str, "w") as file:
        file.writelines(pyi_file)
