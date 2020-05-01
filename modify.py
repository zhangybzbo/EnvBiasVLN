import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--CODE_ROOT", type=str, default="tasks/R2R")
parser.add_argument("--ORIG_FEAT", type=str, default="ResNet-152-imagenet")
parser.add_argument("--ORIG_DIM", type=int, default=2048)
parser.add_argument("--REPLACE_FEAT", type=str, default="Learned-Seg")

args = parser.parse_args()

if args.REPLACE_FEAT == 'ImageNet':
    args.REPLACE_DIM = 1000
elif args.REPLACE_FEAT == 'Detection':
    args.REPLACE_DIM = 152
elif args.REPLACE_FEAT == 'GT-Seg' or args.REPLACE_FEAT == 'Learned-Seg':
    args.REPLACE_DIM = 42
else:
    raise ValueError("unsupported feature type")

print("Get ORIG files:")
orig_py_files = []
for fname in os.listdir(args.CODE_ROOT):
    stem, ext = os.path.splitext(fname)
    full_path = os.path.join(args.CODE_ROOT, fname)
    if ext == '.py':
        if 'ORIG' in stem:
            print('Ignore %s' % full_path)
            orig_py_files.append(full_path)
        else:
            new_full_path = os.path.join(args.CODE_ROOT, stem + "_ORIG" + ".py")
            if os.path.exists(new_full_path):
                pass
            else:
                print("Move %s to %s" % (full_path, new_full_path))
                shutil.copy(full_path, new_full_path)
                orig_py_files.append(new_full_path)

print("\nModify ORIG files:")
for path in orig_py_files:
    stem, ext = os.path.splitext(path)
    new_stem = stem.replace("_ORIG", '')
    new_path = new_stem + ext

    print("Making %s from %s" % (new_path, path))
    lines = open(path).readlines()
    new_lines = []
    for line in lines:
        new_line = (line.replace(str(args.ORIG_DIM), str(args.REPLACE_DIM))
                        .replace(args.ORIG_FEAT, args.REPLACE_FEAT))
        if new_line != line:
            print("OLD: %s" % line[:-1])
            print("NEW: %s" % new_line[:-1])
        new_lines.append(new_line)
    
    with open(new_path, 'w') as f:
        f.writelines(new_lines)

