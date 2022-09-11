import sys
from shutil import unpack_archive
from pathlib import Path
import folder_sorter as parser
from name_normalizer import normalize


def handle_files(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    normalized_name = normalize(normalize(file_name.stem)) + file_name.suffix
    print(f'...replacing {file_name.name}')
    file_name.replace(target_folder / normalized_name)


def handle_archives(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    name = normalize(file_name.stem)
    normalized_name = name + file_name.suffix
    full_name = target_folder / normalized_name
    file_name.replace(full_name)
    target_folder.mkdir(exist_ok=True, parents=True)
    new_dir = target_folder / name
    new_dir.mkdir(exist_ok=True, parents=True)
    print(f'...unpacking archive {file_name.name}')
    unpack_archive(full_name, new_dir)


def handle_folder(file_name: Path):
    print(f'...deleting {file_name.name}')
    file_name.rmdir()


def sorter(folder: Path):
    parser.scan_folder(folder)
    for file in parser.IMAGES:
        handle_files(file, folder / 'images')
    for file in parser.VIDEO:
        handle_files(file, folder / 'video')
    for file in parser.AUDIO:
        handle_files(file, folder / 'audio')
    for file in parser.DOCUMENTS:
        handle_files(file, folder / 'documents')
    for file in parser.OTHERS:
        handle_files(file, folder / 'others')
    for file in parser.ARCHIVES:
        handle_archives(file, folder / 'archives')
    for file in parser.FOLDERS:
        handle_folder(file)
    parser.print_lst()


def main_func(target):
    if target:
        folder_for_scan = Path(target)
        print(f'Work with "{folder_for_scan}" folder...')
        sorter(folder_for_scan.resolve())
    else:
        print('Write correct path')