# batchwords

This program operates on batches of audio/video files, listing all audio files with the format ##_##.wav (ex. 01_06.wav) or all video files with the format ##_##_video.mp4 (ex. 01_06_video.mp4). The matches can then be exported (i.e. copied) to a new folder, which should be an external drive. 

The main use for this script is mass-copying video and audio files within a child's Subject Files directory into an external drive. The data is for use by subjects after their involvement is complete in the study.

You can exclude audio or video files, or choose to include both of them in the final export.

##running

```bash
$ python batchexport.py
```

##issues

Please report any bugs to the Github issue tracker.