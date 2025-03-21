from fastai.vision.all import *

path = untar_data(URLs.PETS) / "images"


def is_cat(x):
    return x[0].isupper()


def main():
    # dls = get_dls(size=192)
    dls = ImageDataLoaders.from_name_func(
        ".",
        get_image_files(path),
        valid_pct=0.2,
        seed=42,
        label_func=is_cat,
        item_tfms=Resize(192),
    )
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(3)
    learn.save("model")


if __name__ == "__main__":
    main()
