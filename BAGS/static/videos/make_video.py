import imageio
import os
from glob import glob
import cv2
import numpy as np

def split_video(vid_path, start_frame=0, end_frame=None, interval=1):
    """
    Split a video into frames between start_frame and end_frame with a given interval.

    Args:
        vid_path (str): Path to the input video file.
        start_frame (int): The starting frame index (inclusive).
        end_frame (int): The ending frame index (inclusive).
        interval (int): The interval between frames to be included.

    Returns:
        List of frames (numpy arrays) between start_frame and end_frame with the given interval.
    """
    end_frame = int(imageio.get_reader(vid_path).count_frames()) if end_frame is None else end_frame
    print(f'Clip video {vid_path} from {start_frame} to {end_frame} with interval {interval}')

    frames = []
    vid = imageio.get_reader(vid_path, 'ffmpeg')
    for i, frame in enumerate(vid):
        if i < start_frame:
            continue
        if i > end_frame:
            break
        if i % interval == 0:
            frames.append(frame)
    return frames


for vid in glob("*_ref.mp4"):
    print(vid)
    input_file1 = vid.replace("_ref.mp4", "_ours.mp4")
    input_file2 = vid.replace("_ref.mp4", "_banmo.mp4")

    output_file = vid.replace("_ref.mp4", "_merged.mp4")

    input_path1 = os.path.join(os.getcwd(), input_file1)
    input_path2 = os.path.join(os.getcwd(), input_file2)
    input_video1 = imageio.get_reader(input_path1)
    input_video2 = imageio.get_reader(input_path2)

    width1, height1 = input_video1.get_meta_data()['size']
    width2, height2 = input_video2.get_meta_data()['size']

    output_path = os.path.join(os.getcwd(), output_file)

    output_video = []
    for frame1, frame2 in zip(split_video(input_path1, interval=3), split_video(input_path2)):
        frame1 = frame1[:height1, :width1, :]
        frame2 = frame2[:height2, :width2, :]
        
        frame1 = cv2.resize(frame1, (480, 272))
        frame2 = cv2.resize(frame2, (480, 272))

        merged_frame = np.concatenate((frame1, frame2), axis=1)
        output_video.append(merged_frame)

    input_video1.close()
    input_video2.close()
    imageio.mimsave(output_path, output_video, fps=10)
