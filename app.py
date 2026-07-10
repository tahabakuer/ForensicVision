from core.pipeline.pipeline import Pipeline


def main():

    Pipeline().run(
        video_path="input/video.mp4",
        start=23,
        end=25
    )


if __name__ == "__main__":
    main()