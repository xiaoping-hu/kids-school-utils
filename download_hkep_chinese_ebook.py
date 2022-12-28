from PIL import Image

from urllib_utils import recu_down


def download_ebook(base_url: str, total_pages: int):
    img_list = []

    for i in range(total_pages):
        page_num: str = str(i+1)
        image_name = f"page-{page_num}.jpg"
        recu_down(f"{base_url}/{image_name}", image_name)
        img_list.append(Image.open(image_name).convert('RGB'))

    img_list[0].save(r'images.pdf', save_all=True, append_images=img_list[1:])


download_ebook(
    'https://ireader.hkep.com/ebook_package/book/99/100/page-image', 24)
