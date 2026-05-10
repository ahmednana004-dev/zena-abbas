from moviepy.editor import ImageClip, concatenate_videoclips, vfx
from PIL import Image
import numpy as np

img_path = "/mnt/data/a_clean_well_lit_product_photography_video_stor.png"
output_path = "/mnt/data/final_wedding_invitation_video.mp4"

# Load full storyboard image
img = Image.open(img_path)
img_np = np.array(img)

w, h = img.size
cols, rows = 2, 3
frame_w = w // cols
frame_h = h // rows

clips = []

# Create 6 animated scenes from storyboard panels
for r in range(rows):
    for c in range(cols):
        crop = img.crop((c * frame_w, r * frame_h, (c + 1) * frame_w, (r + 1) * frame_h))
        temp_path = f"/mnt/data/frame_{r}_{c}.png"
        crop.save(temp_path)

        clip = (
            ImageClip(temp_path)
            .set_duration(1.2)
            .resize(lambda t: 1 + 0.03 * t)
            .fx(vfx.fadein, 0.2)
            .fx(vfx.fadeout, 0.2)
        )

        clips.append(clip)

final_video = concatenate_videoclips(clips, method="compose")
final_video.write_videofile(output_path, fps=24, codec="libx264", audio=False)

print("DONE:", output_path)
