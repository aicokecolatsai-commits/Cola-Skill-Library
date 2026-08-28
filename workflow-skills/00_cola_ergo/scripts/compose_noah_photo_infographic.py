"""Compose Noah-style photo infographics with non-destructive versioning."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WHITE = (255, 255, 255, 255)
INK = (36, 40, 43, 255)
GREEN = (47, 116, 85, 255)
RED = (164, 70, 64, 255)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--correct-base", required=True)
    parser.add_argument("--incorrect-base", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--slug", default="noah")
    parser.add_argument("--logo", default="input/new2.png")
    parser.add_argument("--font-dir", default="fonts")
    parser.add_argument("--main-title", required=True)
    parser.add_argument("--ig-topic", default="")
    parser.add_argument("--correct-title", required=True)
    parser.add_argument("--incorrect-title", required=True)
    parser.add_argument("--correct-label", required=True)
    parser.add_argument("--incorrect-label", required=True)
    parser.add_argument("--correct-subtitle", required=True)
    parser.add_argument("--incorrect-subtitle", required=True)
    parser.add_argument("--correct-bullet", action="append", default=[])
    parser.add_argument("--incorrect-bullet", action="append", default=[])
    parser.add_argument("--fb-correct-line", action="append", default=[])
    parser.add_argument("--fb-incorrect-line", action="append", default=[])
    parser.add_argument(
        "--dual-correct",
        action="store_true",
        help="Treat both left and right images as correct sequential steps or methods (both green labels).",
    )
    parser.add_argument(
        "--transparent-output",
        action="store_true",
        help="Preserve alpha in PNG outputs for Antigravity transparent-background workflows.",
    )
    return parser.parse_args()


def next_versioned(out_dir: Path, name: str) -> Path:
    base = out_dir / name
    if not base.exists():
        return base
    stem = base.stem
    suffix = base.suffix
    for version in range(2, 100):
        path = out_dir / f"{stem}_v{version}{suffix}"
        if not path.exists():
            return path
    raise RuntimeError(f"Too many versions for {name}")


def paired_thread_path(out_dir: Path, ig_path: Path) -> Path:
    proposed = out_dir / ig_path.name.replace("ig_", "threads_", 1)
    if not proposed.exists():
        return proposed
    base_name = re.sub(r"_v\d+\.png$", ".png", proposed.name)
    stem = Path(base_name).stem
    match = re.search(r"_v(\d+)\.png$", ig_path.name)
    start = int(match.group(1)) if match else 2
    for version in range(start, 100):
        path = out_dir / f"{stem}_v{version}.png"
        if not path.exists():
            return path
    raise RuntimeError(f"Too many versions for {proposed.name}")


def load_font(font_dir: Path, filename: str, size: int) -> ImageFont.FreeTypeFont:
    path = font_dir / filename
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.truetype("arial.ttf", size)


def cover(
    img: Image.Image,
    size: tuple[int, int],
    focus=(0.5, 0.5),
    preserve_alpha: bool = False,
) -> Image.Image:
    img = img.convert("RGBA" if preserve_alpha else "RGB")
    source_w, source_h = img.size
    target_w, target_h = size
    scale = max(target_w / source_w, target_h / source_h)
    resized = img.resize(
        (int(source_w * scale), int(source_h * scale)),
        Image.Resampling.LANCZOS,
    )
    new_w, new_h = resized.size
    focus_x, focus_y = focus
    left = min(max(int(new_w * focus_x - target_w * focus_x), 0), new_w - target_w)
    top = min(max(int(new_h * focus_y - target_h * focus_y), 0), new_h - target_h)
    return resized.crop((left, top, left + target_w, top + target_h)).convert("RGBA")


def save_png(img: Image.Image, path: Path, preserve_alpha: bool):
    if preserve_alpha:
        img.save(path)
    else:
        img.convert("RGB").save(path, quality=95)


def gradient_overlay(
    size: tuple[int, int],
    top_alpha: int,
    bottom_alpha: int,
    height: int,
    from_top: bool = True,
) -> Image.Image:
    width, canvas_h = size
    overlay = Image.new("RGBA", (width, canvas_h), (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(min(height, canvas_h)):
        ratio = y / max(height - 1, 1)
        alpha = int(top_alpha * (1 - ratio) + bottom_alpha * ratio)
        target_y = y if from_top else canvas_h - 1 - y
        for x in range(width):
            pixels[x, target_y] = (0, 0, 0, alpha)
    return overlay


def side_gradient(
    size: tuple[int, int],
    alpha: int,
    gradient_w: int,
    left: bool = True,
) -> Image.Image:
    width, height = size
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = overlay.load()
    for x in range(min(gradient_w, width)):
        ratio = x / max(gradient_w - 1, 1)
        current_alpha = int(alpha * (1 - ratio))
        target_x = x if left else width - 1 - x
        for y in range(height):
            pixels[target_x, y] = (0, 0, 0, current_alpha)
    return overlay


def text_size(draw: ImageDraw.ImageDraw, text: str, font_obj) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font_obj)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw, y: int, text: str, font_obj, fill, canvas_w: int) -> int:
    width, height = text_size(draw, text, font_obj)
    draw.text(((canvas_w - width) // 2, y), text, font=font_obj, fill=fill)
    return y + height


def draw_lines(draw, x: int, y: int, lines: list[str], font_obj, fill, gap: int = 8):
def draw_lines(draw, x: int, y: int, lines: list[str], fonts, color, gap: int = 14):
    for index, line in enumerate(lines, start=1):
        r = 17
        cx = x + r
        cy = y + r + 2
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)
        bbox_n = draw.textbbox((0, 0), str(index), font=fonts["fb_circle"])
        nw, nh = bbox_n[2] - bbox_n[0], bbox_n[3] - bbox_n[1]
        draw.text((cx - nw // 2, cy - nh // 2 - 2), str(index), font=fonts["fb_circle"], fill=WHITE)
        
        clean_text = re.sub(r'^[•\-\d\.\s]+', '', line)
        draw.text(
            (x + 48, y),
            clean_text,
            font=fonts["fb_body_title"],
            fill=WHITE,
            stroke_width=1,
            stroke_fill=(0, 0, 0, 140),
        )
        y += text_size(draw, clean_text, fonts["fb_body_title"])[1] + gap
    return y


def draw_photo_label(draw, xy, text: str, font_obj, color):
    x, y = xy
    draw.rounded_rectangle((x, y + 4, x + 12, y + 56), radius=6, fill=color)
    draw.text(
        (x + 24, y),
        text,
        font=font_obj,
        fill=WHITE,
        stroke_width=2,
        stroke_fill=(0, 0, 0, 120),
    )


def paste_logo(base: Image.Image, logo_path: Path, size: tuple[int, int], pos):
    logo = Image.open(logo_path).convert("RGBA").resize(size, Image.Resampling.LANCZOS)
    base.alpha_composite(logo, pos)


def make_fb(args, fonts, paths):
    width, height = 2142, 1169
    left = cover(
        Image.open(paths["correct"]),
        (width // 2, height),
        focus=(0.55, 0.58),
        preserve_alpha=args.transparent_output,
    )
    right = cover(
        Image.open(paths["incorrect"]),
        (width - width // 2, height),
        focus=(0.47, 0.58),
        preserve_alpha=args.transparent_output,
    )
    bg = (0, 0, 0, 0) if args.transparent_output else (24, 24, 24, 255)
    canvas = Image.new("RGBA", (width, height), bg)
    canvas.alpha_composite(left, (0, 0))
    canvas.alpha_composite(right, (width // 2, 0))
    canvas.alpha_composite(gradient_overlay((width, height), 205, 0, 520, True), (0, 0))
    canvas.alpha_composite(gradient_overlay((width, height), 195, 0, 480, False), (0, 0))
    canvas.alpha_composite(side_gradient((width // 2, height), 110, 390, True), (0, 0))
    canvas.alpha_composite(
        side_gradient((width - width // 2, height), 110, 390, False),
        (width // 2, 0),
    )
    draw = ImageDraw.Draw(canvas)
    draw.line((width // 2, 0, width // 2, height), fill=(255, 255, 255, 110), width=4)
    draw_center(draw, 42, args.main_title, fonts["fb_title"], WHITE, width)
    draw_photo_label(draw, (72, 178), args.correct_label, fonts["fb_tag"], GREEN)
    draw_photo_label(
        draw,
        (width // 2 + 72, 178),
        args.incorrect_label,
        fonts["fb_tag"],
        RED,
    )
    draw_lines(draw, 76, 830, args.fb_correct_line, fonts, GREEN, 14)
    draw_lines(
        draw,
        width // 2 + 76,
        830,
        args.fb_incorrect_line,
        fonts,
        RED,
        14,
    )
    if args.fb_note:
        draw.text(
            (80, 1015),
            args.fb_note,
            font=fonts["fb_body"],
            fill=(255, 255, 255, 232),
        )
    paste_logo(canvas, paths["logo"], (450, 300), (width // 2 - 225, height // 2 - 150))
    save_png(canvas, paths["fb"], args.transparent_output)


def make_ig(args, fonts, paths, mode: str):
    width = height = 1080
    if mode == "correct":
        src = paths["correct"]
        title = args.correct_title
        subtitle = args.correct_subtitle
        bullets = args.correct_bullet
        color = GREEN
        focus = (0.54, 0.58)
        out = paths["ig_correct"]
    else:
        src = paths["incorrect"]
        title = args.incorrect_title
        subtitle = args.incorrect_subtitle
        bullets = args.incorrect_bullet
        color = RED
        focus = (0.46, 0.56)
        out = paths["ig_incorrect"]

    canvas = cover(
        Image.open(src),
        (width, height),
        focus=focus,
        preserve_alpha=args.transparent_output,
    )
    canvas.alpha_composite(gradient_overlay((width, height), 205, 0, 520, True), (0, 0))
    canvas.alpha_composite(gradient_overlay((width, height), 175, 0, 480, False), (0, 0))
    canvas.alpha_composite(side_gradient((width, height), 120, 600, True), (0, 0))
    draw = ImageDraw.Draw(canvas)
    topic = args.ig_topic or re.sub(r"｜.*$", "", args.main_title)
    draw.text(
        (48, 42),
        topic,
        font=fonts["ig_tag"],
        fill=color,
        stroke_width=2,
        stroke_fill=(0, 0, 0, 130),
    )
    draw.text((44, 112), title, font=fonts["ig_title"], fill=WHITE)
    draw.text((48, 192), subtitle, font=fonts["ig_body_title"], fill=(255, 255, 255, 238))

    y = 758
    for index, line in enumerate(bullets[:4], start=1):
        center_x, center_y = 62, y + 20
        draw.ellipse(
            (center_x - 17, center_y - 17, center_x + 17, center_y + 17),
            fill=(255, 255, 255, 210),
        )
        draw.text((center_x - 8, center_y - 19), str(index), font=fonts["ig_body"], fill=INK)
        draw.text(
            (96, y),
            line,
            font=fonts["ig_body_title"],
            fill=WHITE,
            stroke_width=1,
            stroke_fill=(0, 0, 0, 140),
        )
        y += 58

    paste_logo(canvas, paths["logo"], (270, 180), (width - 292, height - 196))
    save_png(canvas, out, args.transparent_output)


def main():
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    font_dir = Path(args.font_dir)
    paths = {
        "correct": Path(args.correct_base),
        "incorrect": Path(args.incorrect_base),
        "logo": Path(args.logo),
        "fb": next_versioned(out_dir, f"fb_{args.slug}_photo.png"),
        "ig_correct": next_versioned(out_dir, f"ig_{args.slug}_correct.png"),
        "ig_incorrect": next_versioned(out_dir, f"ig_{args.slug}_incorrect.png"),
    }
    paths["threads_correct"] = paired_thread_path(out_dir, paths["ig_correct"])
    paths["threads_incorrect"] = paired_thread_path(out_dir, paths["ig_incorrect"])
    fonts = {
        "fb_title": load_font(font_dir, "GenSenRounded2-H.ttc", 80),
        "fb_tag": load_font(font_dir, "GenSenRounded2-B.ttc", 40),
        "fb_body_title": load_font(font_dir, "GenSenRounded2-B.ttc", 36),
        "fb_body": load_font(font_dir, "GenSenRounded2-M.ttc", 28),
        "fb_circle": load_font(font_dir, "GenSenRounded2-H.ttc", 24),
        "ig_title": load_font(font_dir, "GenSenRounded2-H.ttc", 60),
        "ig_tag": load_font(font_dir, "GenSenRounded2-B.ttc", 34),
        "ig_body_title": load_font(font_dir, "GenSenRounded2-B.ttc", 34),
        "ig_body": load_font(font_dir, "GenSenRounded2-M.ttc", 26),
    }

    make_fb(args, fonts, paths)
    make_ig(args, fonts, paths, "correct")
    make_ig(args, fonts, paths, "incorrect")
    shutil.copy2(paths["ig_correct"], paths["threads_correct"])
    shutil.copy2(paths["ig_incorrect"], paths["threads_incorrect"])

    for key in ["fb", "ig_correct", "ig_incorrect", "threads_correct", "threads_incorrect"]:
        print(paths[key])


if __name__ == "__main__":
    main()
