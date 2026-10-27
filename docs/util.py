"""
Automate useful outputs for documentation.
"""

import argparse
import re
from subprocess import check_output

CMD = "ifi"


def get_help(cmd=[], hmap=None):
    args = [CMD] + cmd + ["--help"]
    output = check_output(args)
    lines = [s.strip() for s in str(output).split("\\n")]
    lines = [s for s in lines if len(s) > 1 and not s.startswith("-h")]
    if not lines:
        print
        return
    flag = False
    next_level = []
    for line in lines:
        if flag:
            m = re.search(r"\{(.*)\}", line)
            next_level = m.group(1).split(",")
            break
        elif line.strip() == "positional arguments:":
            flag = True
    if next_level:
        for name in next_level:
            get_help(cmd + [name], hmap=hmap)
    else:
        flag = False
        help_lines = []
        for line in lines:
            if flag:
                help_lines.append(line)
            elif line.startswith("options:"):
                flag = True
            elif line and not re.match(r"^(b|\[)", line):
                help_lines.append(line)
        if help_lines:
            cur = hmap
            for tok in cmd[:-1]:
                if not tok in cur:
                    cur[tok] = {}
                cur = cur[tok]
            cur[cmd[-1]] = help_lines


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["help"])
    args = p.parse_args()
    if args.mode == "help":
        hmap = {}
        get_help(hmap=hmap)

        def print_help(key, val, path):
            if isinstance(val, dict):
                # print(f"{indent}* {key}")
                for k, v in val.items():
                    print_help(k, v, path + [k])
            else:
                label = " ".join(path)
                desc = val[0]
                print(f"* **{label}**: {desc}")
                indent = "    "
                print(f"{indent}```")
                for line in val[1:]:
                    print(f"{indent}{line}")
                print(f"{indent}```")

        print_help("ifi", hmap, ["ifi"])
        # for key, val in hmap.items():
        #     val_lines = "\n".join(val)
        #     print(f"{key}:")
        #     print(f"```\n{val_lines}\n```")
