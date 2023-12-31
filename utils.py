import os
import glob
from random import randint


def get_labels_directory() -> str:
    return os.path.join(os.getcwd(), "data", "labels")


def get_images_directory() -> str:
    return os.path.join(os.getcwd(), "data", "images")


def __create_file_paths_for_images_and_labels(img_directory: str, label_directory: str) -> tuple[list[str], list[str]]:
    img_paths = sorted(glob.glob(img_directory + '/*.tif'))
    label_paths = sorted(glob.glob(label_directory + '/*.tif'))
    return img_paths, label_paths


def __get_count_number_of_images_and_labels(images: list, labels: list) -> tuple[int, int]:
    return len(images), len(labels)


def get_number_of_images_and_labels() -> tuple[int, int]:
    labels_directory = get_labels_directory()
    images_directory = get_images_directory()
    image_paths, label_paths = __create_file_paths_for_images_and_labels(images_directory, labels_directory)
    return __get_count_number_of_images_and_labels(image_paths, label_paths)


def get_file_paths_for_images_and_labels() -> tuple[list[str], list[str]]:
    labels_directory = get_labels_directory()
    images_directory = get_images_directory()
    image_paths, label_paths = __create_file_paths_for_images_and_labels(images_directory, labels_directory)
    number_of_images, number_of_labels = __get_count_number_of_images_and_labels(image_paths, label_paths)

    print(f"There are {number_of_images} images and {number_of_labels} labels in our dataset")
    print(f"An example of an image path is: \n {randint(0, number_of_images)}")
    print(f"An example of a mask path is: \n {randint(0, number_of_images)}")
    return image_paths, label_paths


